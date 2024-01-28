# importing datasets repos
from ucimlrepo import fetch_ucirepo
import pandas as pd

# other libraries
import math

# defining branch data class in order to contain the branch's label and it subtree
class Branch:
    def __init__(self):
        self.label = none
        self.subtree = none

# defining tree nodes data structure
class Node:
    def __init__(self, name):
        self.attribute_name = name # attribute name for the node
        self.branch = Branch() # list of node's branches (attribute's possible values)

# defining the decision tree data structure 
class DecisionTree:

    # initialising decision tree
    def __init__(self, examples, P, M): # note examples input must be like iris.data
        self.min_examples = M
        self.max_depth = P
        self.depth = 0 # TODO find where to increase tree depth
        self.root = self.decision_tree_learning(examples, list(examples.features), {}) # parents_examples is empty because we are starting from an empty tree

    # defining recursive decision tree learning algorithm
    def decision_tree_learning(self, examples, attributes, parent_examples):
        # checking if there are no examples left or the tree have reached a certain depth or there are an amount of examples are less than a specific value
        if examples.features.empty or self.depth == self.max_depth or len(examples.features) < self.min_examples:
            return self.plurality_value(parent_examples.targets)
        # checking if the current examples have the same outcome
        elif len(list(examples.targets.value_counts())) == 1:
            return list(examples.targets.value_counts())[0] # gives the only target in common between the examples
        # checking if there are no attributes left in the examples
        elif attributes:
            return self.plurality_value(examples.targets)
        # defining the most important attribute and adding it to the tree as a node
        else:
            A = max_importance(examples) # here we choose the most important attribute among the others
            tree = Node(list(A)[0]) # list(A)[0] gives the attribute name
            for value in list(A[list(A)[0]].drop_duplicates()): # gives the set of attribute values
                exs = update_examples(examples, A, value) # selects the examples which have the attribute's value 'value'
                subtree = self.decision_tree_learning(exs, attributes.remove(list(A)[0]), examples)
                # FIXME maybe this one can be done better
                tree.branch.label.append(values)
                tree.branch.subtree.append(subtree)
                self.depth += 1 # TODO check if the position is correct
        return tree
                
    # defining the function that selects the most common output value
    def plurality_value(self, examples):
        most_count = 0
        most_name = None
        for i in range (0, len(list(examples.value_counts()))-1): # list(examples.value_counts()) gives the list of amount per value 
            if list(examples.value_counts())[i] > most_count:
                most_count = list(examples.value_counts())[i]
                most_name = list(examples[list(examples)[0]].drop_duplicates())[i]
        return most_name

    # defining the most important attribute among the other by using information gain
    def max_importance(self, examples):
        entropy_set = entropy(examples.targets) # computing the entropy of the entire set
        current_attribute = None
        information_gain = -1 # we set to -1 because the information gain value lise withnin the range 0-1. By doing so. We set the information gain of the first attribute
                              # in the for cycle
        # determining the attribute with highest information gain
        for attribute in list(examples.features):
            # computing the right member of information gain function
            right_member = 0
            for i in list(examples.features[attribute].drop_duplicates()):
                right_member -= len(examples.features[example.features[attribute] == i])/len(example.features) \
                    *entropy(examples.features[example.features[attribute] == i])
            current = entropy_set + right_member # computing the information gain of each attribute
            if current > information_gain:
                information_gain = current
                current_attribute = attribute
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
        ids = list(examples.features[example.features[list(attribute)[0] == attribute_value]].index)
        # creating the dataframe which has only the examples with attribute_value
        filtered_examples = pd.concat([examples.features.loc[ids], examples.targets.loc[ids]], keys = ['features', 'targets'])
        filtered_examples.features = filtered_examples['features']
        filtered_examples.targets = filtered_examples['targets']
        return filtered_examples


# TODO add this part into another file. Tree class definitions must be in a separate file and every test for dataset must be done in a different file
iris = fetch_ucirepo(id=53)
dataset = iris.data

decision_tree = DecisionTree(dataset, 100, 0)
