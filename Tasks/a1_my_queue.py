"""
My little Queue
"""
from typing import Any


class Queue:
    def __init__(self):
        ...  # todo для очереди можно использовать python list
        self.data = []
    def enqueue(self, elem: Any) -> None:
        """
        Operation that add element to the end of the queue

        :param elem: element to be added
        :return: Nothing
        """
        print(elem)
        self.data.append(elem)

    def dequeue(self) -> Any:
        """
        Return element from the beginning of the queue. Should return None if no elements.

        :return: dequeued element
        """
        if self.data:
            return self.data.pop(0)
        return None

    def peek(self, ind: int = 0) -> Any:
        """
        Allow you to see at the element in the queue without dequeuing it

        :param ind: index of element (count from the beginning)
        :return: peeked element
        """
        print(ind)
        if ind < 0 or ind > len(self.data):
            return None
        return self.data[ind]

    def clear(self) -> None:
        """
        Clear my queue

        :return: None
        """
        self.data.clear()
        return None
