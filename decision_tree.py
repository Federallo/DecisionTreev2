# importing datasets repos
from ucimlrepo import fetch_ucirepo
import pandas as pd

# other libraries
import math
import networkx
import matplotlib.pyplot as plt

# import custom libraries
from tree_elements import Branch, Node

# defining the decision tree data structure 
class DecisionTree:

    # initialising decision tree
    def __init__(self, examples, P, M): # note examples input must be like iris.data
        if M > len(examples):
            return print("Error: lower bound exceedes dataset dimensions")
        elif P < 1:
            return print("Error: cannot create a tree of depth that is less than 1")
        self.min_examples = M
        self.max_depth = P
        self.depth = 1
        self.root = self.decision_tree_learning(examples, list(examples)[:-1], {}) # parents_examples is empty because we are starting from an empty tree

    # defining recursive decision tree learning algorithm
    def decision_tree_learning(self, examples, attributes, parent_examples):
        # checking if there are no examples left or the number of examples are less than a lower bound         
        if examples.empty or len(examples) < self.min_examples:
            return self.plurality_value(parent_examples[[list(parent_examples)[-1]]])
        # checking if the current examples have the same outcome (i.e. the dataset is pure)or the tree have reached a certain depth 
        elif len(list(examples[list(examples)[-1]].value_counts())) == 1 or self.depth >= self.max_depth:
            return list(examples[list(examples)[-1]])[0] # gives the only target in common between the examples
        # checking if there are no attributes left in the examples
        elif not attributes:
            return self.plurality_value(examples[[list(examples)[-1]]])
        # defining the most important attribute and adding it to the tree as a node
        else:
            self.depth += 1
            A = self.max_importance(examples, attributes) # here we choose the most important attribute among the others
            tree = Node(list(A)[0]) # list(A)[0] gives the attribute name
            attributes.remove(list(A)[0]) # remoivng the attribute with highest information gain from the list
            for value in list(A[list(A)[0]].drop_duplicates()): # gives the set of attribute values
                exs = self.update_examples(examples, A, value) # selects the examples which have the attribute's value 'value'
                subtree = self.decision_tree_learning(exs, attributes, examples)
                tree.branch.label.append(value)
                tree.branch.subtree.append(subtree)

        return tree
                
    # defining the function that selects the most common output value
    def plurality_value(self, examples):
        most_common_output_count = 0
        most_common_output_name = None
        for i in range(len(list(examples.value_counts()))): # list(examples.value_counts()) gives the list of amount per value
            if list(examples.value_counts())[i] > most_common_output_count:
                most_common_output_count = list(examples.value_counts())[i]
                most_common_output_name = list(examples[list(examples)[0]].drop_duplicates())[i]

        return most_common_output_name

    # defining the most important attribute among the other by using information gain
    def max_importance(self, examples, list_attributes):
        entropy_set = self.entropy(examples[list(examples)[-1]]) # computing the entropy of the entire set note: examples[-1] gives only 
                                                                 # the class of outcomes (for example in iris is class)
        current_attribute = None
        information_gain = -1 # we set to -1 because the information gain value lise withnin the range 0-1. By doing so. We set the information gain of the first attribute
                              # in the for cycle
        # determining the attribute with highest information gain
        for attribute in list(examples[:-1]): # :-1 to indicate only features
            # computing the right member of information gain function
            right_member = 0
            for i in list(examples[attribute].drop_duplicates()):
                right_member -= len(examples[examples[attribute] == i])/len(examples[list(examples)[:-1]]) \
                    *self.entropy(examples[examples[attribute] == i])

            current = entropy_set + right_member # computing the information gain of each attribute

            if current > information_gain and attribute in list_attributes:
                information_gain = current
                current_attribute = examples[[attribute]]

        return current_attribute
    
    # defining the entropy of a set
    def entropy(self, examples_set):
        total = 0
        for i in list(examples_set.value_counts()): #the indices of values
            total -= i/len(examples_set)*math.log2(i/len(examples_set)) # where the fraction represent the distribution of datasets' values
                                                                        # (which are targets' or attributes')
        return total

    # defining a function that returns the examples that has a specific attribute's value
    def update_examples(self, examples, attribute, attribute_value):
        # getting the ids of the examples with attribute_value
        ids = list(examples[examples[list(attribute)[0]] == attribute_value].index)
        # creating the dataframe which has only the examples with attribute_value
        filtered_examples = pd.DataFrame(examples.loc[ids])

        return filtered_examples


#plotting tree
T = networkx.MultiGraph()
# defining plotting tree function
def plot_tree(decision_tree, target, counter): # where target is the list of the possible dataset's targets
    # adding unique identifiers in order to have separate nodes and branches
    root_id = f"{counter}_root"
    T.add_node(root_id, label = decision_tree.attribute_name)
    counter += 1
    for i in range(len(decision_tree.branch.subtree)):
        # add directly target name if the are no subtrees
        if decision_tree.branch.subtree[i] in target:
            target_id = f"{counter}_target"
            T.add_node(target_id, label = decision_tree.branch.subtree[i])
            #T.add_edge(decision_tree.attribute_name, decision_tree.branch.subtree[i], weight = decision_tree.branch.label[i])
            T.add_edge(root_id, target_id, label = decision_tree.branch.label[i])
            counter += 1
        # recursive call for the subtrees
        else:
            node_id, counter = plot_tree(decision_tree.branch.subtree[i], target, counter) # keeping track of counter in order to have separate nodes
            T.add_edge(root_id, node_id, label = decision_tree.branch.label[i])

    return root_id, counter


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



# TODO add this part into another file. Tree class definitions must be in a separate file and every test for dataset must be done in a different file
iris = fetch_ucirepo(id=53)

#shuffle rows of dataframe
shuffled_dataset = iris.data.original.sample(frac = 1, random_state = 42)
# extracting test data
rows_to_extract = 30# 60
test_data = shuffled_dataset.head(rows_to_extract)
dataset = shuffled_dataset.drop(test_data.index)

# creating tree
decision_tree = DecisionTree(dataset, 100, 0) # (dataset, max tree depth, lower bound of examples)

# testing tree
# with test data
print(test_tree(decision_tree.root, test_data, list(shuffled_dataset[list(shuffled_dataset)[-1]].drop_duplicates())))
# with training data
print(test_tree(decision_tree.root, dataset.head(rows_to_extract), list(shuffled_dataset[list(shuffled_dataset)[-1]].drop_duplicates())))

#checking if the tree is empty or not
if decision_tree.__dict__:
    # plotting tree
    counter_start = 0 # setting the counter to distinguish nodes and branches
    plot_tree(decision_tree.root, list(dataset[list(dataset)[-1]].drop_duplicates()), counter_start)


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
