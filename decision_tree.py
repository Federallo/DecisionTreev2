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
        self.type = type_name # to distinguish between node and leafs


# defining the decision tree data structure 
class DecisionTree:

    # initialising decision tree
    def __init__(self, examples, P, M):
        self.min_examples = M
        self.max_depth = P
        self.depth = 0 # TODO find where to increase tree depth
        self.root = self.decision_tree_learning(examples, attributes, {}) # parents_examples is empty because we are starting from an empty tree

    # defining recursive decision tree learning algorithm
    def decision_tree_learning(examples, attributes, parent_examples):
        # checks if there are no examples left
        if examples.empty or self.depth == self.max_depth or len(examples) < self.min_examples:
            return self.plurality_value(parent_examples.targets)
        # checks if the current examples have the same outcome
        elif examples.targets.value_counts() == 1:
            return examples.targets.value_counts() # TODO must be changed to the effective outcome name
        # checks if there are no attributes left in the examples
        elif examples.features.value_counts() is empty:
            return self.plurality_value(examples.targets)
        # defining the most important attribute and adding it to the tree as a node
        else:
            A = max_importance(examples)# here we choose the most important attribute among the others
            #tree = Node(#A.name, A.branch, node)
            for values in A:
                # exs = e must belong to examples and e.A=v # TODO find the meaning of this line
                subtree = self.decision_tree_learning(exs, attributes-A, examples)# FIXME
                # TODO add a branch to tree with label (A=v) and as subtree 'subtree'
        return tree
                
    # defining the function that selects the most common output value
    def plurality_value(examples):
        most_common = 0
        for unique_value in list(exaples.value_counts()):
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
        for i in len(set.value_counts()): #the indices of values
            total -= len(set[i])/len(set)*math.log2(len(set[i])/len(set)) # where the fraction represent the distribution of datasets' values
                                                                          # (which are targets' or attributes')
        return total

# TODO add this part into another file. Tree class definitions must be in a separate file and every test for dataset must be done in a different file
iris = fetch_ucirepo(id=53)
x = iris.data.features
y = iris.data.targets
#tmp = list(x)
#print(x[tmp[1]].value_counts())

total = 0
for values in list(y.value_counts()):
    total += values
print(total)
