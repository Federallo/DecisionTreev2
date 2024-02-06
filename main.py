from tree_creation import create_tree

def main():
    dataset_id = 53
    test_amount_examples = 30
    tree_max_depth = 100 # P
    examples_lower_bound = 0 # M
    create_tree(dataset_id, test_amount_examples, tree_max_depth, examples_lower_bound)

if __name__ == '__main__':
    main()
