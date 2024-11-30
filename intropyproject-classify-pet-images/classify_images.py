from classifier import classifier

def classify_images(images_dir, results_dic, model):
    """
    Creates classifier labels with the classifier function, compares pet labels to 
    the classifier labels, and adds the classifier label and the comparison of 
    the labels to the results dictionary using the extend function.
    
    Parameters: 
      images_dir - The path to the folder of images that are to be
                   classified by the classifier function (string)
      results_dic - Results Dictionary with 'key' as image filename and 'value'
                    as a List:
                      index 0 = pet image label (string)
                      index 1 = classifier label (string) [added by this function]
                      index 2 = 1/0 (int)  where 1 = match, 0 = no match [added by this function]
      model - CNN model architecture used by the classifier function to classify the pet images.
              Values must be either: resnet, alexnet, or vgg (string).
    Returns:
           None - results_dic is mutable data type so no return needed.
    """
    for key in results_dic:
        # Create the full file path for the image
        image_path = f"{images_dir}/{key}"

        # Use the classifier function to classify the image
        model_label = classifier(image_path, model)

        # Process the classifier label: make lowercase and strip whitespace
        model_label = model_label.lower().strip()

        # Get the true label (pet label) from the dictionary
        truth = results_dic[key][0]

        # Compare pet label (truth) and classifier label
        if truth in model_label:
            # Add classifier label and match indicator (1) to the results dictionary
            results_dic[key].extend([model_label, 1])
        else:
            # Add classifier label and no-match indicator (0) to the results dictionary
            results_dic[key].extend([model_label, 0])
