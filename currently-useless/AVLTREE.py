class Node:
    """The class defining a node."""

    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None
        self.height = 1

    def __repr__(self):
        return str(self.value)

    def insert(self, node):
        if node is None:
            return
        if node.value < self.value:
            if self.left is None:
                node.parent = self
                self.left = node
            else:
                self.left.insert(node)
        else:
            if self.right is None:
                node.parent = self
                self.right = node
            else:
                self.right.insert(node)

    def find(self, value):
        if value == self.value:
            return self
        elif value < self.value:
            if self.left is None:
                return None
            else:
                return self.left.find(value)
        else:
            if self.right is None:
                return None
            else:
                return self.right.find(value)

    def find_min(self):
        current = self
        while current.left:
            current = current.left
        return current

    def find_max(self):
        current = self
        while current.right:
            current = current.right
        return current

    def successor(self):
        if self.right:
            return self.right.find_min()
        current = self
        while current.parent and current is current.parent.right:
            current = current.parent
        return current.parent

    def predecessor(self):
        if self.left:
            return self.left.find_max()
        current = self
        while current.parent and current is current.parent.left:
            current = current.parent
        return current.parent


def height(node):
    if node:
        return node.height
    else:
        return 0


def update_height(node):
    node.height = max(height(node.left), height(node.right)) + 1


class AVLTree:
    """The class defining an AVL tree."""

    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)
        if self.root:
            self.root.insert(node)
        else:
            self.root = node
        self.rebalance(node)

    def find(self, value):
        return self.root and self.root.find(value)

    def delete(self, value):
        node = self.find(value)
        if node:
            if not (node.left or node.right): # no children
                self._delete_leaf(node)
            elif not (node.left and node.right): # one child
                self._delete_leaf_parent(node)
            else:
                self._delete_node(node)

    remove = delete

    def _delete_leaf(self, node):
        parent_node = node.parent
        if parent_node:
            if parent_node.left == node:
                parent_node.left = None
            else:
                parent_node.right = None
            self.rebalance(parent_node)
        else:
            self.root = None

    def _delete_leaf_parent(self, node):
        parent_node = node.parent
        if node.value == self.root.value:
            assert parent_node is None
            if node.right:
                self.root = node.right
                node.right = None
                self.root.parent = None
            else:
                self.root = node.left
                node.left = None
                self.root.parent = None
        else:
            if parent_node.right == node:
                if node.right:
                    parent_node.right = node.right
                    parent_node.right.parent = parent_node
                    node.right = None
                else:
                    parent_node.right = node.left
                    parent_node.right.parent = parent_node
                    node.left = None
            else:
                if node.right:
                    parent_node.left = node.right
                    parent_node.left.parent = parent_node
                    node.right = None
                else:
                    parent_node.left = node.left
                    parent_node.left.parent = parent_node
                    node.left = None
        self.rebalance(parent_node)

    def _switch_nodes(self, node1, node2):
        switch1 = node1
        switch2 = node2
        temp_value = switch1.value

        if switch1.value == self.root.value:
            self.root.value = node2.value
            switch2.value = temp_value
        elif switch2.value == self.root.value:
            switch1.value = self.root.value
            self.root.value = temp_value
        else:
            switch1.value = node2.value
            switch2.value = temp_value

    def _delete_node(self, node):
        if height(node.left) > height(node.right):
            to_switch = node.predecessor()
            self._switch_nodes(node, to_switch)

            if not (to_switch.right or to_switch.left):
                to_delete = node.predecessor()
                self._delete_leaf(to_delete)
            else:
                to_delete = node.predecessor()
                self._delete_leaf_parent(to_delete)
        else:
            to_switch = node.successor()
            self._switch_nodes(node, to_switch)

            if not (to_switch.right or to_switch.left):
                to_delete = node.successor()
                self._delete_leaf(to_delete)
            else:
                to_delete = node.successor()
                self._delete_leaf_parent(to_delete)

    def successor(self, value):
        node = self.find(value)
        return node and node.successor()

    def predecessor(self, value):
        node = self.find(value)
        return node and node.predecessor()

    def rebalance(self, node):
        while node:
            update_height(node)
            if height(node.left) >= 2 + height(node.right):
                if height(node.left.left) >= height(node.left.right):
                    self.right_rotate(node)
                else:
                    self.left_rotate(node.left)
                    self.right_rotate(node)
            elif height(node.right) >= 2 + height(node.left):
                if height(node.right.right) >= height(node.right.left):
                    self.left_rotate(node)
                else:
                    self.right_rotate(node.right)
                    self.left_rotate(node)
            node = node.parent

    def left_rotate(self, x):
        y = x.right
        y.parent = x.parent
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left is x:
                y.parent.left = y
            elif y.parent.right is x:
                y.parent.right = y
        x.right = y.left
        if x.right:
            x.right.parent = x
        y.left = x
        x.parent = y
        update_height(x)
        update_height(y)

    def right_rotate(self, x):
        y = x.left
        y.parent = x.parent
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left is x:
                y.parent.left = y
            elif y.parent.right is x:
                y.parent.right = y
        x.left = y.right
        if x.left:
            x.left.parent = x
        y.right = x
        x.parent = y
        update_height(x)
        update_height(y)

    def predecessor_by_node(self, node):
        return node and node.predecessor()

    def successor_by_node(self, node):
        return node and node.successor()

    def predecessor_leaf_by_node(self, node):
        if node.left:
            return node.left.find_max()

        current = node
        while current.parent and current is current.parent.left:
            current = current.parent

        if current.parent is None or current.parent.left is None:
            return None

        return current.parent.left.find_max()

    def successor_leaf_by_node(self, node):
        if node.right:
            return node.right.find_min()

        current = node
        while current.parent and current is current.parent.right:
            current = current.parent

        if current.parent is None or current.parent.right is None:
            return None

        return current.parent.right.find_min()
    
    def update_heights(self, node):
        while node:
            update_height(node)
            node = node.parent
    
    def replace_leaf(self, node, sub_tree):
        if node.left is not None or node.right is not None:
            raise Exception("Not a leaf")

        if node.parent is None:
            self.root = sub_tree
        elif node.parent.left == node:
            parent = node.parent
            parent.left = sub_tree
            sub_tree.parent = parent
        elif node.parent.right == node:
            parent = node.parent
            parent.right = sub_tree
            sub_tree.parent = parent
   

class Arc:
    def __init__(self, point, circle_event=None):
        self.point = point
        self.circle_event = circle_event

    def __str__(self):
        return "Arc({}, {})".format(self.point, self.circle_event)

    def __hash__(self):
        return hash((self.point.x, self.point.y))

class Breakpoint:
    def __init__(self, pair, half_edge=None):
        self.data = pair
        self.half_edge = half_edge

    def __str__(self):
        return "Breakpoint({})".format(self.data)

    def __lt__(self, other):
        return self.data[0].x < other.data[0].x

    def __le__(self, other):
        return self.data[0].x <= other.data[0].x

    def __gt__(self, other):
        return self.data[0].x > other.data[0].x

    def __ge__(self, other):
        return self.data[0].x >= other.data[0].x

    def __eq__(self, other):
        return (
            self.data[0].x == other.data[0].x
            and self.data[0].y == other.data[0].y
            and self.data[1].x == other.data[1].x
            and self.data[1].y == other.data[1].y
        )

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        return hash(self.data)
class Event:
    SITE = 7  # For tune
    CIRCLE = 8  # For tune

    def __init__(self, point, event_type, *sequence):
        self.point = point
        self.type = event_type
        if self.type == Event.SITE:
            pass
        elif self.type == Event.CIRCLE:
            self.center = sequence[0]
            self.leaf_pointer = sequence[1]
            self.is_valid = sequence[2]

    def __str__(self):
        return "Event ({}, {})".format(self.point, self.type)

    # Reverse comparisons because PriorityQueue is a minimum priority queue,
    # while sweep line goes from top to bottom
    def __lt__(self, other):
        return (-self.point.y, self.point.x) < (-other.point.y, other.point.x)

    def __le__(self, other):
        return (-self.point.y, self.point.x) <= (-other.point.y, other.point.x)

    def __gt__(self, other):
        return (-self.point.y, self.point.x) > (-other.point.y, other.point.x)

    def __ge__(self, other):
        return (-self.point.y, self.point.x) >= (-other.point.y, other.point.x)

    def __eq__(self, other):
        # Equal check must distinguish events because priority queue
        # deletes duplicates
        if self.type == other.type:
            if self.type == Event.CIRCLE:
                return (
                    self.point == other.point
                    and self.center == other.center
                    and self.leaf_pointer == other.leaf_pointer
                    and self.is_valid == other.is_valid
                )
            else:  # Event.SITE
                return self.point == other.point
        else:
            return False

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        return hash((self.point.x, self.point.y, self.type))
