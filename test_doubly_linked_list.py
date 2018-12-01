from doubly_linked_list import *

def test_append():
    dll = DoublyLinkedList()

    assert dll.head.next == None, "LinkedList empty, so head should point to None"

    item = 5
    dll.append(item)

    assert dll.head.next == item, "head should point to the first node"

    second_item = 8
    dll.append(second_item)

    assert dll.head.next == item, "head should point to the first node"

    first_node = dll.head.next
    second_node = first_node.next

    assert first_node.next.data == second_item, "first_node should point to the second_node"

    assert second_node.prev.data == item, "previous_node of second_node should be the first_node"

    assert str(dll) == "5,8", "string reprensentation of dll should match 5,8"



def test_prepend():
    dll = DoublyLinkedList()

    assert dll.head.next == None, "LinkedList empty, so head should point to None"


    item = 5
    dll.prepend(item)

    assert dll.head.next == item, "head should point to the first node"

    new_item = 10
    dll.prepend(new_item)

    assert dll.head.next.data == new_item, "head should point to the new node"

    new_node = dll.head.next
    old_node = new_node.next

    assert new_node.prev == None, "previous_node of new_node should be None"

    assert old_node.prev == new_node,"previous_node of old_node should be new_node"

    assert old_node.data == item, "checking the data of old node"

    assert str(dll) == "10,5", "string reprensentation of dll should match 10,5"



def insert():
    dll = DoublyLinkedList()

    item = 5
    dll.insert(10,item)

    assert dll == None, "on empty linked list, insert method can't insert item"

    dll.append(item)

    dll.insert(7,9)

    assert dll == 5, "can't find 7"

    second_item == 10
    dll.prepend(second_item)
    dll.insert(5,8)
    dll.insert(10,7)

    assert str(dll) == "10,7,5,8", "string reprensentation of dll should match 10,7,5,8"





def test_search():
    dll = DoublyLinkedList()

    item = 5

    assert dll.search(item) == None, "item shouldn't be found in an empty list"

    dll.append(item)
    node = dll.search(item)

    assert node.data == item, "item should be found in the list"

    dll.append(10)
    dll.append(15)
    node = dll.search(10)

    assert node == 10, "10 should be found in the list"

    node = dll.search(20)

    assert node == None, "20 shouldn't be found in the list"





def test_remove_node():
    dll = DoublyLinkedList()
    dll.append(5)
    node = dll.search(5)

    assert dll.head.next == node, "head should point to node"

    dll.remove_node(node)

    assert dll.head.next == None, "head should point to None, as list is empty"




def test_remove():
    dll = DoublyLinkedList()
    dll.append(5)
    dll.append(10)
    dll.append(15)
    dll.append(20)

    node_5 = dll.search(5)
    node_10 = dll.search(10)
    node_15 = dll.search(15)
    node_20 = dll.search(20)

    assert node_10.next == node_15

    assert node_15.prev == node_10

    dll.remove(15)

    assert node_10.next == node_20, "now next of 10 should be 20"

    assert node_20.prev == node_10, "now prev of 20 should be 10"

    assert str(dll) == "5,10,20", "15 shouldn't be in list anymore"

    dll.remove(20)

    assert node_10.next == None, "now next of 10 should be None"

    assert str(dll) == "5,10", "20 shouldn't be in list anymore"

    dll.remove(5)

    assert dll.head.next == node_10, "now head should be point to 10"

    assert node_10.prev == None, "10 is the 1st node, so prev should be none"

    assert str(dll) == "10", "dll should only contain 10"
