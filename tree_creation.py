# importing datasets repos
from ucimlrepo import fetch_ucirepo
import pandas as pd

from decision_tree import DecisionTree
from plot_tree import plot_tree
from tree_testing import test_tree

import networkx
import matplotlib.pyplot as plt

def create_tree(dataset_id, test_amount_examples, tree_max_depth, examples_lower_bound):
    iris = fetch_ucirepo(id=dataset_id)

    #shuffle rows of dataframe
    shuffled_dataset = iris.data.original.sample(frac = 1, random_state = 42)
    # extracting test data
    test_data = shuffled_dataset.head(test_amount_examples)
    dataset = shuffled_dataset.drop(test_data.index)

    # creating tree
    decision_tree = DecisionTree(dataset, tree_max_depth, examples_lower_bound) # (dataset, max tree depth, lower bound of examples)

    # testing tree
    # with test data
    print(test_tree(decision_tree.root, test_data, list(shuffled_dataset[list(shuffled_dataset)[-1]].drop_duplicates())))
    # with training data
    print(test_tree(decision_tree.root, dataset.head(test_amount_examples), list(shuffled_dataset[list(shuffled_dataset)[-1]].drop_duplicates())))

    #checking if the tree is empty or not
    if decision_tree.__dict__:
        # plotting tree
        T = networkx.MultiGraph()
        # plotting tree
        counter_start = 0 # setting the counter to distinguish nodes and branches
        plot_tree(decision_tree.root, list(dataset[list(dataset)[-1]].drop_duplicates()), counter_start, T)


        # printing tree
        pos = networkx.fruchterman_reingold_layout(T) # choosing the layout for displaying the tree
        labels = networkx.get_node_attributes(T, 'label') # getting the branch labels from multigraph T
        edge_labels = {(u,v): d['label'] for u, v, d in T.edges(data = True)} # adding the labels in a new variable
        node_size = 2000
        font_size = 8
        networkx.draw(T, pos, with_labels = True, labels = labels, node_size = node_size, font_size = font_size) # setting the draw
        networkx.draw_networkx_edge_labels(T, pos, edge_labels = edge_labels)
        plt.show()
    else:
        print("Error: cannot plot an empty tree")
