# defining branch data class in order to contain the branch's label and it subtree
class Branch:
    def __init__(self):
        self.label = []
        self.subtree = []
        self.weight = []

# defining tree nodes data structure
class Node:
    def __init__(self, name):
        self.attribute_name = name # attribute name for the node
        self.branch = Branch() # list of node's branches (attribute's possible values)
