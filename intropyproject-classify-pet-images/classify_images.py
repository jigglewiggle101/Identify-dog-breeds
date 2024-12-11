#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#
# PROGRAMMER: Jesmine Goh
# DATE CREATED:  30/11/2024
# REVISED DATE:  01/12/2024
# PURPOSE: Create a function classify_images that uses the classifier function
#          to create the classifier labels and then compares the classifier
#          labels to the pet image labels. This function inputs:
#            - The Image Folder as image_dir within classify_images and function
#              and as in_arg.dir for function call within main.
#            - The results dictionary as results_dic within classify_images
#              function and results for the function call within main.
#            - The CNN model architecture as model within classify_images function
#              and in_arg.arch for the function call within main.
#           This function uses the extend function to add items to the list
#           that's the 'value' of the results dictionary. You will be adding the
#           classifier label as the item at index 1 of the list and the comparison
#           of the pet and classifier labels as the item at index 2 of the list.
#
##
# Imports
from classifier import classifier
import os

def classify_images(images_dir, results_dic, model):
    """
    Creates classifier labels with classifier function, compares pet labels to 
    the classifier labels, and adds the classifier label and the comparison of 
    the labels to the results dictionary using the extend function.
    Parameters: 
      images_dir - Path to the folder of images (string).
      results_dic - Results dictionary where key is image filename and value 
                    is a list: 
                      index 0 = pet image label (string)
                      index 1 = classifier label (string, added by this function)
                      index 2 = match (1/0, added by this function).
      model - CNN model architecture to use (string).
    Returns:
           None - results_dic is mutable, so no return is needed.         
    """
    for key, value in results_dic.items():
        # Get classifier label using the classifier function
        image_path = os.path.join(images_dir, key)
        model_label = classifier(image_path, model).strip().lower()
        
        # Get true pet label from the dictionary
        truth = value[0]
        
        # Check if pet label matches any term in classifier label
        if truth in model_label:
            value.extend((model_label, 1))
        else:
            value.extend((model_label, 0))
