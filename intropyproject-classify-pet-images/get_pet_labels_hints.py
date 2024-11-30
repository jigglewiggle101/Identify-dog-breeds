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
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Creates list of files in directory
    in_files = listdir(image_dir)
    
    # Creates empty dictionary for the results (pet labels, etc.)
    results_dic = dict()
   
    # Processes through each file in the directory
    for idx in range(len(in_files)):
       
        # Skips file if starts with . (like .DS_Store of Mac OSX) because it 
        # isn't a pet image file
        if in_files[idx][0] != ".":
            # Extract pet label from the filename
            filename = in_files[idx]
            
            # Process the filename to remove extensions and underscores
            pet_label = "".join([char if char.isalpha() or char == " " else " " for char in filename.split('.')[0]])
            pet_label = pet_label.replace("_", " ").strip().lower()
            
            # If filename doesn't already exist in dictionary, add it
            if filename not in results_dic:
                results_dic[filename] = [pet_label]
            else:
                print("** Warning: Duplicate files exist in directory:", filename)
 
    return results_dic
