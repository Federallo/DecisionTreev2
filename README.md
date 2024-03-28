# Decision Tree
Decision tree algorithm based on R&N 2020: chapter 19.3, with the base step that returns PLURALITY-VALUE if three-depth > P or # example < M. \
Dataset for learning procedures are provided by [Fisher,R. A.. (1988). Iris. UCI Machine Learning Repository](https://doi.org/10.24432/C56C76). \
Before running the code, please install dataset's repo and the other dependencies by running
```
pip install pandas ucimlrepo networkx PyQt5
```
All dataset are made by Dataframes from pandas library.

Here is a little description of single py files:
- tree_elements.py: defines the nodes and the branches of the tree
- decision_tree.py: defines the methods that creates the decision tree from the dataset
- plot_tree.py: draws the tree
- tree_creation: creates the actual tree and plots it
- main: calls tree_creation and and asks the user for the parameters in input

To make the application work, please run main.py. The program will ask P, M, the training/test split and the dataset.
In order to have the same results as the ones in the report, please use the following parameters:
- for Iris
    - P = 3, M = 0, split = 30
    - P = 2, M = 0, split = 30
    - P = 1, M = 0, split = 30
    - P = 3, M = 50, split = 30
    - P = 3, M = 3, split = 30
    - P = 3, M = 2, split = 30
    - P = 2, M = 2, split = 30
- for Heart disease
    - P = 3, M = 0, split = 76
    - P = 2, M = 0, split = 76
    - P = 1, M = 0, split = 76
    - P = 3, M = 50, split = 76
    - P = 3, M = 3, split = 76
    - P = 3, M = 2, split = 76
- for Wine
    - P = 3, M = 0, split = 34
    - P = 2, M = 0, split = 34
    - P = 1, M = 0, split = 34
