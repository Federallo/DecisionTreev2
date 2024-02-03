# testing data # must be done on training set and test set
def test_tree(decision_tree, test_data, target):
    counter = 0
    total_test_length = len(test_data)
    for i in test_data.index: # gives the ids of the dataset rows
        extracted_row = test_data.head(1)
        test_data = test_data.drop(index = [i]) # removing tested rows from dataset
        if tree_precision(decision_tree, extracted_row, target):
            counter += 1
    return counter/total_test_length

# calculating tree precision on a single row
def tree_precision(tree, row, target):
    
    # checking if the root attribute value in case we chose a tree of depth 1 (i.e. the tree is only a leaf)
    if tree == list(row[list(row)[-1]])[0] and tree in target:
        return True
    elif tree in target:
        return False

    # confronting the tree outcome with the training/test example
    for i in range(0, len(tree.branch.label)):
        if list(row[tree.attribute_name])[0] == tree.branch.label[i]:
            # checking if the branch is connected to a leaf
            if tree.branch.subtree[i] in target:
                # checking if test data target is equal to decision tree one
                if list(row[list(row)[-1]])[0] == tree.branch.subtree[i]:
                    return True
                else:
                    return False
            # ... or to a node
            else:
                tree_precision(tree.branch.subtree[i], row, target)
