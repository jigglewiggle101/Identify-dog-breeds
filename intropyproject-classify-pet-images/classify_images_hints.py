from classifier import classifier

def classify_images(images_dir, results_dic, model):
    """
    Processes pet image labels with classifier labels, compares them, 
    and updates the results dictionary with the classifier label and 
    a match indicator (1/0).
    """
    for key in results_dic:
        # Construct the full image path
        full_path = f"{images_dir}/{key}"

        # 3a: Use the classifier function to get the classifier label
        model_label = classifier(full_path, model)

        # 3b: Process the model label (lowercase and strip whitespace)
        model_label = model_label.lower().strip()

        # 3c: Compare pet image label (truth) with classifier label
        truth = results_dic[key][0]
        
        # Check for a match and update results_dic
        if truth in model_label:
            results_dic[key].extend([model_label, 1])  # Match (1)
        else:
            results_dic[key].extend([model_label, 0])  # No match (0)
