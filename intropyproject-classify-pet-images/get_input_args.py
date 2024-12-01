#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_input_args.py
#                                                                             
# PROGRAMMER: Jesmine Goh
# DATE CREATED:  30/11/2024                                 
# REVISED DATE:  01/12/2024
# PURPOSE: Create a function that retrieves the following 3 command line inputs 
#          from the user using the Argparse Python module. If the user fails to 
#          provide some or all of the 3 inputs, then the default values are
#          used for the missing inputs. Command Line Arguments:
#     1. Image Folder as --dir with default value 'pet_images'
#     2. CNN Model Architecture as --arch with default value 'vgg'
#     3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
#
## Imports python modules
import argparse

def get_input_args():
    """
    Retrieves and parses the command line arguments.

    Returns:
      Namespace: Contains the three arguments parsed from the command line.
    """
    # Create the parser object
    parser = argparse.ArgumentParser(description="Classify pet images using CNN models.")
    
    # Add arguments for the image folder, model architecture, and dog names file
    parser.add_argument('--dir', type=str, default='pet_images', 
                        help='Directory path to the folder of images to be classified (default is "pet_images")')
    parser.add_argument('--arch', type=str, default='vgg', choices=['vgg', 'alexnet', 'resnet'], 
                        help='CNN model architecture to use for classification (choices: vgg, alexnet, resnet; default is "vgg")')
    parser.add_argument('--dogfile', type=str, default='dognames.txt', 
                        help='Text file containing dog names (default is "dognames.txt")')
    
    # Parse arguments from the command line
    return parser.parse_args()
