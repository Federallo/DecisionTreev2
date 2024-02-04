# Decision Tree
Decision tree algorithm based on R&N 2020: 19.3, with the base step that returns PLURALITY-VALUE if three-depth > P or # example < M. \
Dataset for learning procedures are provided by Fisher,R. A.. (1988). Iris. UCI Machine Learning Repository. https://doi.org/10.24432/C56C76. \
Before running the code, please install dataset's repo and the other dependencies by running
```
pip install pandas ucimlrepo networkx PyQt5
```
All dataset are made by Dataframes from pandas.

Here is a little description of single py files:
- tree_elements.py: defines the nodes and the branches of the tree
- decision_tree.py: defines the creation of the decision tree from the dataset
- plot_tree.py: draws the tree
- tree_creation: creates the tree and plots it
- main: calls tree_creation and lets changes parameters of the tree like the dataset type, the max depth, the test/training split, ...
