"""
You can do it either with networkx ('cause tree is a graph)
or with dicts (smth like {'key': 0, value: 123, 'left': {...}, 'right':{...}})
"""

from typing import Any, Optional, Tuple
# import networkx as nx


class BinarySearchTree:
    def __init__(self):
        self.tree = {'node': {}}

    def insert(self, key: int, value: Any) -> None:
        """
        Insert (key, value) pair to binary search tree
        :param key: key from pair (key is used for positioning node in the tree)
        :param value: value associated with key
        :return: None
        """
        print(key, value)
        current_node = self.tree['node']

        while current_node:
            key_node = current_node['key']
            if key == key_node:
                return None
            elif key < key_node:
                current_node = current_node['left']['node']
            else:
                current_node = current_node['right']['node']

        current_node.update({'key': key, 'value': value, 'left': {'node': {}}, 'right': {'node': {}}})
        return None

    def remove(self, key: int) -> Optional[Tuple[int, Any]]:
        """
        Remove key and associated value from the BST if exists

        :param key: key to be removed
        :return: deleted (key, value) pair or None
        """
        print(key)

        if self.tree['node']:
            current_node = self.tree['node']
            prev_node = self.tree['node']
            prev_side = None
        else:
            return None

        while current_node:
            key_node = current_node['key']
            if key == key_node:
                del_data = (current_node['key'], current_node['value'])

                if current_node['right']['node'] and current_node['left']['node']:
                    min_node = self._find_min_node(current_node['right']['node'])
                    prev_node['key'], prev_node['value'] = min_node['key'], min_node['value']
                    min_node.clear()
                    return del_data

                if current_node['left']['node'] and not current_node['right']['node']:
                    prev_node[prev_side] = current_node['left']['node']
                    return del_data

                if current_node['right']['node'] and not current_node['left']['node']:
                    prev_node[prev_side] = current_node['right']['node']
                    return del_data

                current_node.clear()
                return del_data

            elif key < key_node:
                prev_node = current_node
                prev_side = 'left'
                current_node = current_node['left']['node']
            else:
                prev_node = current_node
                prev_side = 'right'
                current_node = current_node['right']['node']

        return None

    def _find_min_node(self, node: dict) -> dict:

        current_node = node
        while current_node['left']['node']:
            current_node = current_node['left']['node']

        return current_node

    def find(self, key: int) -> Optional[Any]:
        """
        Find value by given key in the BST

        :param key: key for search in the BST
        :return: value associated with the corresponding key
        """
        print(key)
        if self.tree['node']:
            current_node = self.tree['node']
        else:
            raise KeyError('несуществующий ключ')

        while current_node:
            key_node = current_node['key']
            if key == key_node:
                return current_node['value']
            elif key < key_node:
                current_node = current_node['left']['node']
            else:
                current_node = current_node['right']['node']

        raise KeyError('несуществующий ключ')

    def clear(self) -> None:
        """
        Clear the tree

        :return: None
        """
        self.tree.clear()
        self.tree['node'] = {}
        return None


if __name__ == '__main__':
    c = BinarySearchTree()
    c.insert(8, 'val_8')
    c.insert(3, 'val_3')
    c.insert(10, 'val_10')
    c.insert(10, 'dublicat')
    c.insert(9, 'val_9')
    c.insert(14, 'val_14')
    c.insert(11, 'val_11')
    print(c.find(9))
    c.remove(11)
    # c.insert(15, 'val_11')
    # c.remove(14)
    print(c.find(1))
    print(1)
