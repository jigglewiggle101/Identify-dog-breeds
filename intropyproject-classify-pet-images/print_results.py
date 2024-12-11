def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs=False, print_incorrect_breed=False):
    """
    Prints summary results on the classification and then prints incorrectly 
    classified dogs and incorrectly classified dog breeds if user indicates 
    they want those printouts (use non-default values).
    """
    # Print the model architecture
    print(f"\n*** Results Summary for CNN Model Architecture {model.upper()} ***\n")
    
    # Print summary statistics
    print(f"N Images               : {results_stats_dic['n_images']}")
    print(f"N Dog Images           : {results_stats_dic['n_dogs_img']}")
    print(f"N Not-a-Dog Images     : {results_stats_dic['n_notdogs_img']}")
    print(f"pct_match              : {results_stats_dic.get('pct_match', 0):.6f}")
    print(f"pct_correct_dogs       : {results_stats_dic['pct_correct_dogs']:.6f}")
    print(f"pct_correct_breed      : {results_stats_dic['pct_correct_breed']:.6f}")
    print(f"pct_correct_notdogs    : {results_stats_dic['pct_correct_notdogs']:.6f}\n")

    # Print misclassified dogs if requested
    if print_incorrect_dogs:
     print("\nINCORRECT Dog/NOT Dog Assignment:")
    for filename, result in results_dic.items():
        if sum(result[3:]) == 1:  # Misclassified as dog/not-a-dog
            print(f"Real: {result[0]:<22} Classifier: {result[1]}")

   # Print misclassified breeds if requested
    if print_incorrect_breed:
     print("\nINCORRECT Dog Breed Assignment:")
    for filename, result in results_dic.items():
        if sum(result[3:]) == 2 and result[2] == 0:  # Correctly classified as dog, wrong breed
            print(f"Real: {result[0]:<22} Classifier: {result[1]}")

