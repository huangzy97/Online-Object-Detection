# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 19:09:48 2020

@author: sbtithzy
"""

import numpy as np
import os
import six.moves.urllib as urllib
import sys
import tarfile
import tensorflow as tf
from collections import defaultdict
from io import StringIO
from matplotlib import pyplot as plt
from PIL import Image
from media.research.object_detection.utils import label_map_util
from media.research.object_detection.utils import visualization_utils as vis_util
NUM_CLASSES = 90
IMAGE_SIZE = (12, 8)

def Model():
    MODEL_NAME = 'media/research/object_detection/ssd_mobilenet_v1_coco_11_06_2017'
    MODEL_FILE = MODEL_NAME + '.tar.gz'
    PATH_TO_CKPT = MODEL_NAME + '/frozen_inference_graph.pb'
    PATH_TO_LABELS = os.path.join('media/research/object_detection/data', 'mscoco_label_map.pbtxt')
    return MODEL_FILE,PATH_TO_LABELS,PATH_TO_CKPT

def load_image_into_numpy_array(image):
  (im_width, im_height) = image.size
  return np.array(image.getdata()).reshape(
      (im_height, im_width, 3)).astype(np.uint8)
def Picture_process(model_file,path_to_ckpt,test_image_path,category_index):
    tar_file = tarfile.open(model_file)
    for file in tar_file.getmembers():
        file_name = os.path.basename(file.name)
        if 'frozen_inference_graph.pb' in file_name:
            tar_file.extract(file, os.getcwd())   
    detection_graph = tf.Graph()
    with detection_graph.as_default():
        od_graph_def = tf.GraphDef()
        with tf.gfile.GFile(path_to_ckpt, 'rb') as fid:
            serialized_graph = fid.read()
            od_graph_def.ParseFromString(serialized_graph)
            tf.import_graph_def(od_graph_def, name='')
        
    with detection_graph.as_default():
        with tf.Session(graph=detection_graph) as sess:
            # Definite input and output Tensors for detection_graph
            image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
			# Each box represents a part of the image where a particular object was detected.
            detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
			# Each score represent how level of confidence for each of the objects.
			# Score is shown on the result image, together with the class label.
            detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
            detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')
            num_detections = detection_graph.get_tensor_by_name('num_detections:0')
            for image_path in test_image_path:
                image = Image.open(image_path)
                image_np = load_image_into_numpy_array(image)
                image_np_expanded = np.expand_dims(image_np, axis=0)
                (boxes, scores, classes, num) = sess.run([detection_boxes, detection_scores, 
                detection_classes, num_detections],feed_dict={image_tensor: image_np_expanded})
                vis_util.visualize_boxes_and_labels_on_image_array(image_np,np.squeeze(boxes),
                                                                   np.squeeze(classes).astype(np.int32),
                                                                   np.squeeze(scores),category_index,
                                                                   use_normalized_coordinates=True,line_thickness=4)
    return image_np,classes,category_index

def main(image_name):
    TEST_IMAGE_PATHS = [ os.path.join('media/research/object_detection/test_images',image_name)]
    MODEL_FILE,PATH_TO_LABELS,PATH_TO_CKPT = Model()
    label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
    categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
    category_index = label_map_util.create_category_index(categories)
    image_np,label,category_index = Picture_process(MODEL_FILE,PATH_TO_CKPT,TEST_IMAGE_PATHS,category_index)
    plt.figure(figsize=IMAGE_SIZE)
    plt.imshow(image_np)
    image_np = Image.fromarray(np.uint8(image_np))
    ext = os.path.splitext(image_name)[1]
    name_result = os.path.splitext(image_name)[0]
    image_np.save('media/research/object_detection/test_images/'+name_result+'_result'+ext)
    #return category_index[label[0][0]]['name']
if __name__ == '__main__':
    main()