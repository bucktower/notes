import pytest
import linked_list


def test_empty_list():
    lst = linked_list.LinkedList()
    assert lst.length() == 0


def test_list_of_one():
    lst = linked_list.LinkedList(linked_list.LinkedNode(1))
    assert lst.length() == 1
    assert lst.root.nxt == lst.root


def test_list_insert():
    lst = linked_list.LinkedList(linked_list.LinkedNode(1))
    other_node = linked_list.LinkedNode("other")
    lst.insert(other_node)
    assert lst.length() == 2
    assert lst.root.nxt.data == "other"
    assert lst.root.prv == other_node
    assert lst.root.nxt.nxt == lst.root

def test_empty_list_insert():
    lst = linked_list.LinkedList()
    new_node = linked_list.LinkedNode("n")
    lst.insert(new_node)
    assert lst.root == new_node
    assert lst.root.prv == new_node
    assert lst.root.nxt == new_node


def test_insert_at_index():
    lst = linked_list.LinkedList()
    node_1 = linked_list.LinkedNode("o")
    node_2 = linked_list.LinkedNode("t")
    node_3 = linked_list.LinkedNode("d")
    lst.insert(node_1)
    lst.insert(node_2)
    lst.insert(node_3, 1)
    assert lst.root.nxt == node_3
    assert lst.root.prv == node_2

    # Inserting before the root
    node_4 = linked_list.LinkedNode("i")
    lst.insert(node_4, 0)
    assert lst.root == node_4
    assert lst.root.nxt.data == "o"
    assert lst.root.nxt.prv == node_4
    assert lst.root.prv == node_2
