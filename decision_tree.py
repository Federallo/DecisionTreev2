# importing datasets repos
from ucimlrepo import fetch_ucirepo
import pandas as pd

# other libraries
import math

# defining tree nodes data structure
class Node:
    def __init__(self, name, branch, type_name):
        self.attribute_name = name # attribute name for the node
        self.branch = branch  # list of node's branches (attribute's possible values)
        #self.parent = none # node's parent TODO maybe not needed because tree doesnt need to backtrack
        self.type = type_name # to distinguish between node and leafs


# defining the decision tree data structure 
class DecisionTree:

    # initialising decision tree
    def __init__(self, examples):
        self.depth = 0
        self.root = self.decision_tree_learning(examples, attributes, {}) # parents_examples is empty because we are starting from an empty tree

    # defining recursive decision tree learning algorithm
    def decision_tree_learning(examples, attributes, parent_examples):
        # checks if there are no examples left
        if examples.empty:
            return self.plurality_value(parent_examples.targets)
        # checks if all examples have the same outcome
        else if examples.targets.value_counts() == 1:
            return examples.targets.value_counts() # TODO must be changed to the effective outcome name
        # checks if there are no attributes left in the examples
        if examples.features.value_counts() is empty:
            return self.plurality_value(examples.targets)
        # defining the most important attribute and adding it to the tree as a node
        else:
            A = max_importance(examples)# here we choose the most important attribute among the others
            tree = Node(#A.name, A.branch, node)
            for values in A:
                # exs = e must belong to examples and e.A=v # TODO find the meaning of this line
                subtree = self.decision_tree_learning(exs, attributes-A, examples)# FIXME
                # TODO add a branch to tree with label (A=v) and as subtree 'subtree'
    return tree
                
    # defining the function that selects the most common output value
    # FIXME must count only the most common outcome among the examples
    def plurality_value(examples):
        most_common = 0
        for unique_value in exaples.value_counts():
            if unique_value > most_common:
                most_common = unique_value
        return most_common

    # defining the most important attribute among the other by using information gain
    def max_importance(examples):
        entropy_set = entropy(examples.targets) # computing the entropy of the entire set
        current_attribute = examples.features[0]
        information_gain = entropy_set - entropy(current_attribute) # information gain of the first attribute
        # determing the attribute with highest information gain
        for attribute in examples.features:
            current = entropy_set - entropy(attribute) # computing the entropy of single attributes
            if current > information_gain:
                information_gain = current
                current_attribute = attribute
        return current_attribute
    
    # defining the entropy of a set
    def entropy(set):
        total = 0
        for i = 0 to len(set.value_counts())-1 #the indices of values
            total -= len(set[i])/len(set)*math.log2(len(set[i])/len(set)) # where the fraction represent the distribution of datasets' values
                                                                          # (which are targets' or attributes')
        return total

# TODO add this part into another file. Tree class definitions must be in a separate file and every test for dataset must be done in a different file
iris = fetch_ucirepo(id=53)
x = iris.data.features
y = iris.data.targets
print(y)

#print(len(x))
#print(iris.data.features)
#print(iris.data.targets)

