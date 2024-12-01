#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/check_images.py
#
# PROGRAMMER: Jesmine Goh
# DATE CREATED: 30/11/2024
# REVISED DATE: 01/12/2024
# PURPOSE: Classifies pet images using a pretrained CNN model, compares these
#          classifications to the true identity of the pets in the images, 
#          and summarizes the model's performance. The program compares 3 CNN 
#          architectures to find the best model.
#
# Use argparse for user input:
#      python check_images.py --dir <directory with images> --arch <model>
#             --dogfile <file that contains dognames>
#   Example call:
#    python check_images_solution.py --dir pet_images/ --arch vgg --dogfile dognames.txt
##

# Imports
from time import time
from print_functions_for_lab_checks import *
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results

# Main program function
def main():
    start_time = time()
    in_arg = get_input_args()
    
    # Check command line arguments
    check_command_line_arguments(in_arg)
    
    # Create pet labels dictionary
    results = get_pet_labels(in_arg.dir)
    check_creating_pet_image_labels(results)
    
    # Classify images and compare labels
    classify_images(in_arg.dir, results, in_arg.arch)
    check_classifying_images(results)
    
    # Adjust results for dog classification
    adjust_results4_isadog(results, in_arg.dogfile)
    check_classifying_labels_as_dogs(results)
    
    # Calculate and check results statistics
    results_stats = calculates_results_stats(results)
    check_calculating_results(results, results_stats)
    
    # Print results
    print_results(results, results_stats, in_arg.arch, True, True)
    
    # Measure total program runtime
    end_time = time()
    tot_time = end_time - start_time
    print("\n** Total Elapsed Runtime:",
          str(int((tot_time / 3600))) + ":" + str(int((tot_time % 3600) / 60)) + ":"
          + str(int((tot_time % 3600) % 60)))


# Call main function
if __name__ == "__main__":
    main()
