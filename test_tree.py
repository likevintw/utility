import unittest
import utility

# python3 -m unittest -v <.py>

ROOT = utility.TreeNode(27)
utility.TreeNode.insert(ROOT, 14)
utility.TreeNode.insert(ROOT, 35)
utility.TreeNode.insert(ROOT, 10)
utility.TreeNode.insert(ROOT, 19)
utility.TreeNode.insert(ROOT, 31)
utility.TreeNode.insert(ROOT, 42)


class TestTree(unittest.TestCase):
    def test_preorder_traversal(self):
        class TestFormat:
            def __init__(self, args, wants) -> None:
                self.args = args
                self.wants = wants
        cases = []
        cases.append(TestFormat(ROOT, [27, 14, 10, 19, 35, 31, 42]))

        for case in cases:
            result = utility.TreeNode.show_preorder_traversal(case.args)
            self.assertEqual(result, case.wants)

    def test_inorder_traversal(self):
        class TestFormat:
            def __init__(self, args, wants) -> None:
                self.args = args
                self.wants = wants
        cases = []
        cases.append(TestFormat(ROOT, [10, 14, 19, 27, 31, 35, 42]))

        for case in cases:
            result = utility.TreeNode.show_inorder_traversal(case.args)
            self.assertEqual(result, case.wants)

    def test_postorder_traversal(self):
        class TestFormat:
            def __init__(self, args, wants) -> None:
                self.args = args
                self.wants = wants
        cases = []
        cases.append(TestFormat(ROOT, [10, 19, 14, 31, 42, 35, 27]))

        for case in cases:
            result = utility.TreeNode.show_postorder_traversal(case.args)
            self.assertEqual(result, case.wants)

    def test_traversal_BFS(self):
        class TestFormat:
            def __init__(self, args, wants) -> None:
                self.args = args
                self.wants = wants
        cases = []
        cases.append(TestFormat(ROOT,  [27, 14, 35, 10, 19, 31, 42]))

        for case in cases:
            result = utility.TreeNode.traversal_BFS(case.args)
            self.assertEqual(result, case.wants)


if __name__ == '__main__':
    unittest.main()
