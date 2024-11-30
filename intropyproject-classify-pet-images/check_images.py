#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/check_images.py
#
# PROGRAMMER: [Your Name]
# DATE CREATED: [Date]
# REVISED DATE: [Date]
# PURPOSE: Classifies pet images using a pretrained CNN model, compares these
#          classifications to the true identity of the pets in the images, and
#          summarizes how well the CNN performed on the image classification task.
#
# Use argparse Expected Call with <> indicating expected user input:
#      python check_images.py --dir <directory with images> --arch <model>
#             --dogfile <file that contains dognames>
#   Example call:
#    python check_images_solution.py --dir pet_images/ --arch vgg --dogfile dognames.txt
##

# Imports python modules
from time import time
from print_functions_for_lab_checks import *
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results

# Main program function defined below
def main():
    # Measures total program runtime by collecting start time
    start_time = time()
    
    # Retrieves Command Line Arguments from user input
    in_arg = get_input_args()
    
    # Function that checks command line arguments using in_arg
    check_command_line_arguments(in_arg)
    
    # Creates pet labels dictionary using get_pet_labels function
    results = get_pet_labels(in_arg.dir)
    
    # Function that checks Pet Images in the results Dictionary
    check_creating_pet_image_labels(results)
    
    # Creates Classifier Labels with classifier function and compares them
    classify_images(in_arg.dir, results, in_arg.arch)
    
    # Function that checks Results Dictionary for classification
    check_classifying_images(results)
    
    # Adjusts results to determine if image labels are correctly classified as dogs
    adjust_results4_isadog(results, in_arg.dogfile)
    
    # Function that checks Results Dictionary for 'is-a-dog' adjustment
    check_classifying_labels_as_dogs(results)
    
    # Calculates results statistics and creates results_stats dictionary
    results_stats = calculates_results_stats(results)
    
    # Function that checks Results Statistics Dictionary
    check_calculating_results(results, results_stats)
    
    # Prints summary results, incorrect classifications of dogs, and incorrect breeds
    print_results(results, results_stats, in_arg.arch, True, True)
    
    # Measures total program runtime by collecting end time
    end_time = time()
    
    # Computes overall runtime and prints it in hh:mm:ss format
    tot_time = end_time - start_time
    print("\n** Total Elapsed Runtime:",
          str(int((tot_time/3600)))+":"+str(int((tot_time%3600)/60))+":"
          +str(int((tot_time%3600)%60)))


# Call to main function to run the program
if __name__ == "__main__":
    main()
