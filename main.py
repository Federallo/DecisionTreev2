from tree_creation import create_tree
from enum import Enum

# Enumerating the datasets
class Dataset(Enum):
    IRIS = 53
    WINE = 109
    HEART_FAILURE = 519

def main():

    # Asking  P and M
    tree_max_depth = int(input("Enter the maximum depth of the tree (P): "))
    examples_lower_bound = int(input("Enter the minimum number of examples in a node (M): "))
    test_amount_examples = int(input("Enter the amount of examples to test the tree: "))
    # dataset: 53 for iris, 109 for wine, 519 for heart failure clinical records 
    # sizes: 150 for iris, 178 for wine, 299 for heart failure clinical records
    valid_datasets = [c.name.lower() for c in Dataset]
    dataset_id = input(f"Enter the dataset id: ({', '.join(valid_datasets)})\n").upper()
    try:
        dataset_id = Dataset[dataset_id].value
    except KeyError:
        print(f"Invalid dataset id. Please enter a valid dataset id from the list: {', '.join(valid_datasets)}")
        exit()



    test_amount_examples = 30
    create_tree(dataset_id, test_amount_examples, tree_max_depth, examples_lower_bound)

if __name__ == '__main__':
    main()
