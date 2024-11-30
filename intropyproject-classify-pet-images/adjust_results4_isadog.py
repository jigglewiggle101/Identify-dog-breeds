def adjust_results4_isadog(results_dic, dogfile):
    """
    Adjusts the results dictionary to determine if classifier correctly 
    classified images 'as a dog' or 'not a dog' especially when not a match. 
    Demonstrates if model architecture correctly classifies dog images even if
    it gets dog breed wrong (not a match).
    Parameters:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
                    List. Where the list will contain the following items: 
                  index 0 = pet image label (string)
                  index 1 = classifier label (string)
                  index 2 = 1/0 (int)  where 1 = match between pet image
                    and classifer labels and 0 = no match between labels
                ------ where index 3 & index 4 are added by this function -----
                 NEW - index 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                 NEW - index 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
     dogfile - A text file that contains names of all dogs from the classifier
               function and dog names from the pet image files. This file has 
               one dog name per line dog names are all in lowercase with 
               spaces separating the distinct words of the dog name. Dog names
               from the classifier function can be a string of dog names separated
               by commas when a particular breed of dog has multiple dog names 
               associated with that breed (ex. maltese dog, maltese terrier, 
               maltese) (string - indicates text file's filename)
    Returns:
           None - results_dic is mutable data type so no return needed.
    """
    # Read dog names into a set for efficient lookup
    dog_names = set()
    with open(dogfile, "r") as f:
        for line in f:
            dog_names.add(line.strip().lower())
    
    # Update the results dictionary
    for key, value in results_dic.items():
        # Check if pet image label is a dog
        is_pet_dog = 1 if value[0] in dog_names else 0
        
        # Check if classifier label is a dog
        classifier_labels = value[1].split(", ")
        is_classifier_dog = any(label in dog_names for label in classifier_labels)
        is_classifier_dog = 1 if is_classifier_dog else 0
        
        # Add the new values to the results dictionary
        value.extend([is_pet_dog, is_classifier_dog])
