from v1.node import Node


class GameBoard:
    def __init__(self, size: int = 100):
        self.size = size

        self.start_node = self.__create_start_node()
        # self.__create_nodes()
        self.last_node = self.__create_nodes(self.start_node, self.size)
        # self.last_node.next = self.__create_end_node()

    def __str__(self):
        return "GameBoard: [size = {}, start_node = [{}]]".format(self.size, self.start_node)

    def __create_start_node(self) -> None:
        node = Node()
        node.value = str("START")

        return node

    def __create_end_node(self) -> None:
        node = Node()
        node.value = str("END")

        return node

    def __create_nodes(self, start_node: Node, size: int) -> Node:
        '''
        creates intermediate node, and return last node

        :return: last node
        :rtype: Node
        '''
        previous_node = start_node
        for i in range(1, size + 1):
            node = Node()
            node.value = str(i)
            previous_node.next = node

            previous_node = node

        return previous_node

    def is_last_node(self, node: Node) -> bool:
        return node == self.last_node
