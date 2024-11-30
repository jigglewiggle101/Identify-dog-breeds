import argparse

def get_input_args():
    """
    Retrieves and parses the 3 command line arguments provided by the user when
    they run the program from a terminal window. This function uses Python's 
    argparse module to create and define these 3 command line arguments. If 
    the user fails to provide some or all of the 3 arguments, then the default 
    values are used for the missing arguments. 
    Command Line Arguments:
      1. Image Folder as --dir with default value 'pet_images/'
      2. CNN Model Architecture as --arch with default value 'vgg'
      3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
    This function returns these arguments as an ArgumentParser object.
    
    Parameters:
     None - simply using argparse module to create & store command line arguments
    Returns:
     parse_args() - data structure that stores the command line arguments object  
    """
    # Create ArgumentParser object
    parser = argparse.ArgumentParser(description="Process command line arguments for image classification.")

    # Add argument for the directory of images
    parser.add_argument('--dir', type=str, default='pet_images/', 
                        help='Path to the folder of pet images (default: pet_images/)')

    # Add argument for the CNN model architecture
    parser.add_argument('--arch', type=str, default='vgg', 
                        help='CNN model architecture to use (default: vgg)')

    # Add argument for the text file containing dog names
    parser.add_argument('--dogfile', type=str, default='dognames.txt', 
                        help='Path to the file containing dog names (default: dognames.txt)')

    # Parse and return the arguments
    return parser.parse_args()
