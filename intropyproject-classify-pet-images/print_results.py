def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs=False, print_incorrect_breed=False):
    """
    Prints summary results on the classification and then prints incorrectly 
    classified dogs and incorrectly classified dog breeds if user indicates 
    they want those printouts (use non-default values).
    
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
                    (index)idx 0 = pet image label (string)
                           idx 1 = classifier label (string)
                           idx 2 = 1/0 (int) where 1 = match between pet image and 
                                  classifier labels and 0 = no match between labels
                           idx 3 = 1/0 (int) where 1 = pet image 'is-a' dog and 
                                  0 = pet Image 'is-NOT-a' dog. 
                           idx 4 = 1/0 (int) where 1 = Classifier classifies image 
                                  'as-a' dog and 0 = Classifier classifies image 
                                  'as-NOT-a' dog.
      results_stats_dic - Dictionary containing the results statistics (either
                          a percentage or a count) where the key is the statistic's 
                          name (starting with 'pct' for percentage or 'n' for count)
                          and the value is the statistic's value.
      model - Indicates which CNN model architecture was used by the classifier function 
              to classify the pet images (values must be either: resnet, alexnet, vgg).
      print_incorrect_dogs - True prints incorrectly classified dog images, False doesn't print anything (default).
      print_incorrect_breed - True prints incorrectly classified dog breeds, False doesn't print anything (default).
    
    Returns:
           None - simply prints results.
    """
    # Print the summary statistics
    print("\n\n*** Results Summary for CNN Model Architecture", model.upper(), "***")
    print("{:20}: {:3d}".format('N Images', results_stats_dic['n_images']))
    print("{:20}: {:3d}".format('N Dog Images', results_stats_dic['n_dogs_img']))
    
    # Print the number of NOT-dog images
    print("{:20}: {:3d}".format('N Not-Dog Images', results_stats_dic['n_notdogs_img']))

    # Print percentage statistics
    print(" ")
    for key in results_stats_dic:
        if key.startswith('pct'):  # Check for percentage keys
            print("{:20}: {:.2f}%".format(key, results_stats_dic[key]))

    # If print_incorrect_dogs is True, print incorrect dog classifications
    if print_incorrect_dogs and \
        ( (results_stats_dic['n_correct_dogs'] + results_stats_dic['n_correct_notdogs']) 
          != results_stats_dic['n_images'] ):
        print("\nINCORRECT Dog/NOT Dog Assignments:")
        
        # Process results to print misclassified dogs and not-dogs
        for key in results_dic:
            pet_label, classifier_label, match, pet_is_dog, classifier_is_dog = results_dic[key]

            # If the pet image label is a dog but classified as not a dog OR vice versa
            if (pet_is_dog == 1 and classifier_is_dog == 0) or (pet_is_dog == 0 and classifier_is_dog == 1):
                print("Pet Image: {:>26}   Classifier: {:>30}".format(pet_label, classifier_label))

    # If print_incorrect_breed is True, print incorrect breed classifications
    if print_incorrect_breed and \
        (results_stats_dic['n_correct_dogs'] != results_stats_dic['n_correct_breed']):
        print("\nINCORRECT Dog Breed Assignment:")
        
        # Process results to print misclassified breeds
        for key in results_dic:
            pet_label, classifier_label, match, pet_is_dog, classifier_is_dog = results_dic[key]

            # Only consider dogs (pet_is_dog == 1) and misclassified breed (match == 0)
            if pet_is_dog == 1 and classifier_is_dog == 1 and match == 0:
                print("Real: {:>26}   Classifier: {:>30}".format(pet_label, classifier_label))
