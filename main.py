from tree_creation import create_tree

def main():
    # dataset: 53 for iris, 109 for wine, 519 for heart failure clinical records 
    # sizes: 150 for iris, 178 for wine, 299 for heart failure clinical records
    dataset_id = 10
    test_amount_examples = 34
    tree_max_depth = 3 # P
    examples_lower_bound = 0 # M
    create_tree(dataset_id, test_amount_examples, tree_max_depth, examples_lower_bound)

if __name__ == '__main__':
    main()
