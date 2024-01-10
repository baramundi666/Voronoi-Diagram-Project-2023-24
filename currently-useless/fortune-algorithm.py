from AVLTREE import *
from dcel import * 
from queue import PriorityQueue

def Fortune(P):
    Q = PriorityQueue()
    for p in P:
        Q.put(p)

    Beach = AVLTree()


# Wyświetlenie drzewa lub jego fragmentu (można dostosować do własnych potrzeb)
def print_tree(node, level=0, prefix="Root: "):
    if node is not None:
        print(" " * (level * 4) + prefix + str(node.value))
        if node.left or node.right:
            print_tree(node.left, level + 1, "L--- ")
            print_tree(node.right, level + 1, "R--- ")

# Inicjalizacja drzewa AVL
avl_tree = AVLTree()

# Dodanie elementów do drzewa
values_to_insert = [10, 15, 2, 7, 12, 17]
for value in values_to_insert:
    avl_tree.insert(value)

# Wyszukanie elementu w drzewie
search_value = 7
found_node = avl_tree.find(search_value)
print(f"Node with value {search_value}: {found_node}")

# Znalezienie następnika i poprzednika dla określonego węzła
node_value = 10
node_to_find = avl_tree.find(node_value)
successor_node = avl_tree.successor_by_node(node_to_find)
predecessor_node = avl_tree.predecessor_by_node(node_to_find)
print(f"Successor of {node_value}: {successor_node}")
print(f"Predecessor of {node_value}: {predecessor_node}")

# Znalezienie największego i najmniejszego liścia dla określonego węzła
max_leaf = avl_tree.predecessor_leaf_by_node(node_to_find)
min_leaf = avl_tree.successor_leaf_by_node(node_to_find)
print(f"Max leaf of {node_value}: {max_leaf}")
print(f"Min leaf of {node_value}: {min_leaf}")

print("AVL Tree:")
print_tree(avl_tree.root)

# Zamiana liścia na poddrzewo
sub_tree = Node(20)
sub_tree.insert(Node(18)) 
sub_tree.insert(Node(25))
sub_tree.insert(Node(30))
sub_tree.insert(Node(40))
node_to_find = avl_tree.find(17)
avl_tree.replace_leaf(node_to_find, sub_tree)
avl_tree.rebalance(avl_tree.root)
print("AVL Tree:")
print_tree(avl_tree.root)




