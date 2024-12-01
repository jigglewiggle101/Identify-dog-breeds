def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the program run using the classifier's model 
    architecture to classifying pet images.

    Parameters:
      results_dic (dict): Results of image classification.

    Returns:
      results_stats_dic (dict): Dictionary with the calculated statistics.
    """

    # Initialize statistics dictionary
    results_stats_dic = dict()

    # Initialize counters for various categories
    results_stats_dic['n_dogs_img'] = 0
    results_stats_dic['n_match'] = 0
    results_stats_dic['n_correct_dogs'] = 0
    results_stats_dic['n_correct_notdogs'] = 0
    results_stats_dic['n_correct_breed'] = 0

    # Process results
    for key in results_dic:
        # Check if the labels match
        if results_dic[key][2] == 1:
            results_stats_dic['n_match'] += 1
            if results_dic[key][3] == 1:  # Correct breed classification
                results_stats_dic['n_correct_breed'] += 1

        # Check for dog images
        if results_dic[key][3] == 1:
            results_stats_dic['n_dogs_img'] += 1
            if results_dic[key][4] == 1:  # Correct dog classification
                results_stats_dic['n_correct_dogs'] += 1
        else:
            if results_dic[key][4] == 0:  # Correct non-dog classification
                results_stats_dic['n_correct_notdogs'] += 1

    # Calculate percentages
    results_stats_dic['n_images'] = len(results_dic)
    results_stats_dic['n_notdogs_img'] = results_stats_dic['n_images'] - results_stats_dic['n_dogs_img']
    results_stats_dic['pct_match'] = (results_stats_dic['n_match'] / results_stats_dic['n_images']) * 100.0

    if results_stats_dic['n_dogs_img'] > 0:
        results_stats_dic['pct_correct_dogs'] = (results_stats_dic['n_correct_dogs'] / results_stats_dic['n_dogs_img']) * 100.0
        results_stats_dic['pct_correct_breed'] = (results_stats_dic['n_correct_breed'] / results_stats_dic['n_dogs_img']) * 100.0
    else:
        results_stats_dic['pct_correct_dogs'] = 0.0
        results_stats_dic['pct_correct_breed'] = 0.0

    if results_stats_dic['n_notdogs_img'] > 0:
        results_stats_dic['pct_correct_notdogs'] = (results_stats_dic['n_correct_notdogs'] / results_stats_dic['n_notdogs_img']) * 100.0
    else:
        results_stats_dic['pct_correct_notdogs'] = 0.0

    return results_stats_dic
