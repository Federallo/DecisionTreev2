# importing datasets repos
from ucimlrepo import fetch_ucirepo
import pandas as pd

# other libraries
import math
import networkx
import matplotlib.pyplot as plt

# defining branch data class in order to contain the branch's label and it subtree
class Branch:
    def __init__(self):
        self.label = []
        self.subtree = []

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
        self.root = self.decision_tree_learning(examples, list(examples)[:-1], {}) # parents_examples is empty because we are starting from an empty tree

    # defining recursive decision tree learning algorithm
    def decision_tree_learning(self, examples, attributes, parent_examples):
        # checking if there are no examples left or the tree have reached a certain depth or there are an amount of examples are less than a specific value
        if examples.empty or self.depth == self.max_depth or len(examples) < self.min_examples:
            return self.plurality_value(parent_examples[[list(examples)[-1]]])
        # checking if the current examples have the same outcome
        elif len(list(examples.value_counts())) == 1:
            return list(examples[list(examples)[-1]])[0] # gives the only target in common between the examples
        # checking if there are no attributes left in the examples
        elif not attributes:
            return self.plurality_value(examples[[list(examples)[-1]]])
        # defining the most important attribute and adding it to the tree as a node
        else:
            A = self.max_importance(examples) # here we choose the most important attribute among the others
            tree = Node(list(A)[0]) # list(A)[0] gives the attribute name
            attributes.remove(list(A)[0]) # remoivng the attribut with highest information gain from the list
            for value in list(A[list(A)[0]].drop_duplicates()): # gives the set of attribute values
                exs = self.update_examples(examples, A, value) # selects the examples which have the attribute's value 'value'
                subtree = self.decision_tree_learning(exs, attributes, examples)
                # FIXME maybe this one can be done better
                tree.branch.label.append(value)
                tree.branch.subtree.append(subtree)
                self.depth += 1 # TODO check if the position is correct
        return tree
                
    # defining the function that selects the most common output value
    def plurality_value(self, examples):
        most_count = 0
        most_name = None
        for i in range(len(list(examples.value_counts()))): # list(examples.value_counts()) gives the list of amount per value
            if list(examples.value_counts())[i] > most_count:
                most_count = list(examples.value_counts())[i]
                most_name = list(examples[list(examples)[0]].drop_duplicates())[i]
        return most_name

    # defining the most important attribute among the other by using information gain
    def max_importance(self, examples):
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
            if current > information_gain:
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
        # FIXME maybe it needs to be fixed
        filtered_examples = pd.DataFrame(examples.loc[ids])
        return filtered_examples


#plotting tree
T = networkx.Graph()
# defining plotting tree function
def plot_tree(decision_tree, target): # where target is the list of the possible dataset's targets
    T.add_node(decision_tree.attribute_name)
    for i in range (0, len(decision_tree.branch.subtree)-1):
        # add directly target name if the are no subtrees
        if decision_tree.branch.subtree[i] in target: # FIXME maybe it doesn't see the value in attributes.subtree[i]
            T.add_node(decision_tree.branch.subtree[i])
            T.add_edge(decision_tree.attribute_name, decision_tree.branch.subtree[i], weight = decision_tree.branch.label[i])
        # recursive call for the subtrees
        else:
            T.add_node(decision_tree.branch.subtree[i].attribute_name) # attribute_name because there is an attribute connected to the node
            T.add_edge(decision_tree.attribute_name, decision_tree.branch.subtree[i].attribute_name)
            plot_tree(decision_tree.branch.subtree[i], target)

        
    



# TODO add this part into another file. Tree class definitions must be in a separate file and every test for dataset must be done in a different file
iris = fetch_ucirepo(id=53)
dataset = iris.data.original

decision_tree = DecisionTree(dataset, 100, 0)
# creating tree
plot_tree(decision_tree.root, list(dataset[list(dataset)[-1]].drop_duplicates()))

# printing tree
networkx.draw(g1)
plt.show()
