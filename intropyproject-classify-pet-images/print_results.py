def print_results(results, results_stats, model, print_incorrect=False, print_summary=True):
    """
    Print results of the classification, including accuracy and misclassified cases.
    """
    if print_summary:
        print(f"\nModel Architecture: {model.upper()}")
        print(f"Total images: {results_stats['n_images']}")
        print(f"Dog Images: {results_stats['n_dogs_img']}, "
              f"Correctly Classified: {results_stats['pct_correct_dogs']:.2f}%")
        print(f"Non-Dog Images: {results_stats['n_notdogs_img']}, "
              f"Correctly Classified: {results_stats['pct_correct_notdogs']:.2f}%")
        print(f"Correct Breed Classification: {results_stats['pct_correct_breed']:.2f}%")

    if print_incorrect:
        print("\nIncorrect Classifications:")
        for filename, label in results.items():
            # Misclassification logic: check if labels match
            if label[2] == 0:
                print(f"{filename}: Real={label[0]}, Predicted={label[1]}")
