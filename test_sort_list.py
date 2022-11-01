import unittest
from sort_list import Solution, ListNode


class Test791(unittest.TestCase):

    def setUp(self):
        self.function = Solution()

    def to_list(self, puntero):
        list_return = []
        temp = puntero
        while (temp != None):
            list_return.append(temp.val)
            temp = temp.next
        return list_return

    def test_1(self):
        list_nodes = ListNode(4, ListNode(1, ListNode(2, ListNode(3, None))))
        resultado = self.to_list(self.function.sortList(list_nodes))
        self.assertEqual(resultado, [1, 2, 3, 4])

    def test_2(self):
        list_nodes = ListNode(8, ListNode(3, ListNode(12, ListNode(10, None))))
        resultado = self.to_list(self.function.sortList(list_nodes))
        self.assertEqual(resultado, [3, 8, 10, 12])


if __name__ == '__main__':
    unittest.main()
