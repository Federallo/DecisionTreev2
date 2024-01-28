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
        # checks if there are no examples left
        if examples.features.empty or self.depth == self.max_depth or len(examples.features) < self.min_examples:
            return self.plurality_value(parent_examples.targets)
        # checks if the current examples have the same outcome
        elif examples.targets.value_counts() == 1:
            return list(examples.targets.value_counts())[0] # gives the only target in common between the examples
        # checks if there are no attributes left in the examples
        elif attributes is empty:
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
        most_name = none
        for i in range (0, len(list(exaples.value_counts()))): # list(examples.value_counts()) gives the list of amount per value 
            if list(examples.value_counts())[i] > most_count:
                most_count = list(examples.value_counts())[i]
                most_name = list(example[list(examples)[0]].drop_duplicates())[i]
        return most_name

    # defining the most important attribute among the other by using information gain
    def max_importance(self, examples):
        entropy_set = entropy(examples.targets) # computing the entropy of the entire set
        current_attribute = list(examples.features)[0]
        information_gain = entropy_set - entropy(current_attribute) # information gain of the first attribute
        # determing the attribute with highest information gain
        for attribute in list(examples.features):
            current = entropy_set - entropy(example.features[attribute]) # computing the entropy of single attributes
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

    # defining a function that returns the examples that has that attribute's value
    def update_examples(self, examples, attribute, attribute_value):
        # getting the ids of the examples with attribute_value
        ids = list(examples.features[example.features[list(attribute)[0] == attribute_value]].index)
        # creating the dataframe which has only the examples with attribute_value
        filtered_examples = pd.concat([examples.features.loc[ids], examples.targets.loc[ids]], keys = ['features', 'targets'])
        filtered_examples.features = filtered_examples['features']
        filtered_examples.targets = filtered_examples['targets']


# TODO add this part into another file. Tree class definitions must be in a separate file and every test for dataset must be done in a different file
iris = fetch_ucirepo(id=53)
x = iris.data.features
y = iris.data.targets
#tmp = list(x)
#print(x[tmp[1]].value_counts())

#print("attributes names list", list(iris.data.features))
#print("check if dataset is empty ", iris.data.features.empty)
#print("length examples (row counts) ", len(iris.data.features))
#print("only target name in common ", list(y[list(y)[0]].drop_duplicates())[0])
#print("attribute name ", list(y)[0])
#print("attribute values", list(y[list(y)[0]].drop_duplicates()))
#print("list of attributes which have that exact value", x[x['petal length']==4.9])
#print("filtering examples by attribute's value (gives the ids)")
#print(list(iris.data.features[x['petal length']==4.9].index))
#print(list(x[x['petal length'] == 4.9].value_counts()))

#print(list(x['petal length'].value_counts()))
#total = 0
#for values in list(y.value_counts()):
                                      #    total += values
#print(total)
