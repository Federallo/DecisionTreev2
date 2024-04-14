import pandas as pd

# other libraries
import math

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
        self.root = self.decision_tree_learning(examples, list(examples)[:-1], {}, 1) # parents_examples is empty because we are starting from an empty tree

    # defining recursive decision tree learning algorithm
    def decision_tree_learning(self, examples, attributes, parent_examples, current_depth):
        # checking if there are no examples left or the number of examples are less than a lower bound        
        if examples.empty or len(examples) < self.min_examples:
            return self.plurality_value(parent_examples[[list(parent_examples)[-1]]])
        # checking if the tree have reached a certain depth
        elif current_depth >= self.max_depth:
            return self.plurality_value(examples[[list(examples)[-1]]])
        # checking if the current examples have the same outcome (i.e. the dataset is pure)
        elif len(list(examples[list(examples)[-1]].value_counts())) == 1:
            return list(examples[list(examples)[-1]])[0] # gives the only target in common between the examples
        # checking if there are no attributes left in the examples
        elif not attributes:
            return self.plurality_value(examples[[list(examples)[-1]]])
        # defining the most important attribute and adding it to the tree as a node
        else:
            A = self.max_importance(examples, attributes) # here we choose the most important attribute among the others
            tree = Node(list(A)[0]) # list(A)[0] gives the attribute name
            attributes.remove(list(A)[0]) # remoivng the attribute with highest information gain from the list
            for value in list(A[list(A)[0]].drop_duplicates()): # gives the set of attribute values
                exs = self.update_examples(examples, A, value) # selects the examples which have the attribute's value 'value'
                subtree = self.decision_tree_learning(exs, attributes, examples, current_depth + 1)
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
        for attribute in list(examples)[:-1]: # :-1 to indicate only features
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

