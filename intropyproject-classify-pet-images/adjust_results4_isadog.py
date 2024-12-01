def adjust_results4_isadog(results_dic, dogfile):
    """
    Adjust the results dictionary to indicate whether or not the pet image label is a dog, 
    and whether or not the classifier label is a dog.

    Parameters:
      results_dic (dict): Dictionary with image filenames and classification results.
      dogfile (str): Path to a text file containing dog names.

    Modifies the results_dic in place to include information about whether each label corresponds to a dog.
    """

    # Read the dog names from the file and store them in a dictionary for fast lookup
    dog_names = {}
    with open(dogfile, 'r') as f:
        for line in f:
            dog_name = line.strip().lower()  # Convert dog name to lowercase for uniform comparison
            dog_names[dog_name] = 1  # Value is irrelevant; the key indicates a dog

    # Adjust the results_dic to mark whether the labels are of dogs or not
    for key in results_dic:
        pet_label = results_dic[key][0].lower()  # Pet image label (lowercase)
        classifier_label = results_dic[key][1].lower()  # Classifier label (lowercase)

        # Ensure the list has at least 5 elements (if not, extend it with default values)
        if len(results_dic[key]) < 5:
            results_dic[key].extend([None] * (5 - len(results_dic[key])))  # Add None for missing elements
        
        # Check if the pet label corresponds to a dog
        if pet_label in dog_names:
            results_dic[key][3] = 1  # Pet image is a dog
        else:
            results_dic[key][3] = 0  # Pet image is not a dog

        # Check if the classifier label corresponds to a dog
        if classifier_label in dog_names:
            results_dic[key][4] = 1  # Classifier label is a dog
        else:
            results_dic[key][4] = 0  # Classifier label is not a dog
