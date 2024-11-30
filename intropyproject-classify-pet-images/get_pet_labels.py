from os import listdir

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains the following item:
         index 0 = pet image label (string)
    """
    # Creates list of files in directory
    in_files = listdir(image_dir)
    
    # Creates empty dictionary for the results (pet labels, etc.)
    results_dic = {}
    
    # Processes each file in the directory
    for filename in in_files:
        # Skips files starting with a '.' (e.g., system files like .DS_Store)
        if filename[0] != ".":
            # Extracts the label from the filename
            pet_label = filename.split('.')[0]  # Remove file extension
            pet_label = pet_label.replace("_", " ").strip().lower()  # Replace underscores and format
            
            # Adds filename as key and pet_label as value in a list
            if filename not in results_dic:
                results_dic[filename] = [pet_label]
            else:
                print(f"** Warning: Duplicate file exists in directory: {filename}")
    
    return results_dic
