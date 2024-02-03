import networkx

# defining plotting tree function
def plot_tree(decision_tree, target, counter, multigraph): # where target is the list of the possible dataset's targets
    # adding unique identifiers in order to have separate nodes and branches
    root_id = f"{counter}_root"
    multigraph.add_node(root_id, label = decision_tree.attribute_name)
    counter += 1
    for i in range(len(decision_tree.branch.subtree)):
        # add directly target name if the are no subtrees
        if decision_tree.branch.subtree[i] in target:
            target_id = f"{counter}_target"
            multigraph.add_node(target_id, label = decision_tree.branch.subtree[i])
            multigraph.add_edge(root_id, target_id, label = decision_tree.branch.label[i])
            counter += 1
        # recursive call for the subtrees
        else:
            node_id, counter = plot_tree(decision_tree.branch.subtree[i], target, counter, multigraph) # keeping track of counter in order to have separate nodes
            multigraph.add_edge(root_id, node_id, label = decision_tree.branch.label[i])

    return root_id, counter

