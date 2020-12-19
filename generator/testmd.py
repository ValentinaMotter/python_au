import unittest
from generate_md import MdMaker


class TestGenerate_md(unittest.TestCase):
    def test_md_link(self):
        example = MdMaker('142. Linked List Cycle II', 'https://leetcode.com/problems/linked-list-cycle-ii/', '    solution')
        expect = '+ [Linked List Cycle II](#linked-list-cycle-ii)'
        result = example.md_link()
        self.assertEqual(expect, result)

    def test_md_title(self):
        example = MdMaker('142. Linked List Cycle II', 'https://leetcode.com/problems/linked-list-cycle-ii/', '    solution')
        expect = '## Linked List Cycle II'
        result = example.md_title()
        self.assertEqual(expect, result)

    def test_md_code(self):
        example = MdMaker('142. Linked List Cycle II', 'https://leetcode.com/problems/linked-list-cycle-ii/', '    solution')
        expect = '```python\nsolution\n```'
        result = example.md_code()
        self.assertEqual(expect, result)

    def test_md_formatted(self):
        example = MdMaker('142. Linked List Cycle II', 'https://leetcode.com/problems/linked-list-cycle-ii/', '    solution')
        expect = ('+ [Linked List Cycle II](#linked-list-cycle-ii)',
                  '## Linked List Cycle II\n\nhttps://leetcode.com/problems/linked-list-cycle-ii/\n\n``` python\nsolution\n```')
        result = example.md_formatted()
        self.assertEqual(expect, result)


if __name__ == '__main__':
    unittest.main()