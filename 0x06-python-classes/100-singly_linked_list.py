#!/usr/bin/python3

"""creating sorted singlylinkedlist"""


class Node:
    """node class for singlylinkedlist"""
    def __init__(self, data, next_node=None):
        """node intialization"""
        if type(data) is not int:
            raise TypeError("data must be an integer")
        self.__data = data
        if type(next_node) is not Node and next_node is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node

    @property
    def data(self):
        """data getter"""
        return self.__data

    @data.setter
    def data(self, value):
        """data setter"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """next_node getter"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """next_node setter"""
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList():
    """class for singlylinkedlist"""
    def __init__(self):
        """ initialization of linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """ inserted a node in a sorted way"""
        new = Node(value)
        tmp = self.__head
        new_list = []

        if not self.__head:
            self.__head = new
            new.next_node = None
        else:
            while tmp.next_node is not None:
                tmp = tmp.next_node
            tmp.next_node = new
            tmp = self.__head
            while tmp is not None:
                new_list.append(tmp.data)
                tmp = tmp.next_node
            new_list.sort()
            tmp = self.__head
            for i in new_list:
                tmp.data = i
                tmp = tmp.next_node

    def __str__(self):
        """str reperesentation of objects"""
        new_str = ""
        while self.__head:
            new_str += (str(self.__head.data) +
                        ("\n" if self.__head.next_node is not None else ""))
            self.__head = self.__head.next_node
        return new_str
