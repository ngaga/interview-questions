import unittest

# Move elements from the end of one array to another
def move_elements(source, target, num_elements):
    if num_elements > len(source):  # Corrected typo from 'numelements' to 'num_elements'
        num_elements = len(source)
    target.extend(source[-num_elements:])
    del source[-num_elements:]

class TestMoveElements(unittest.TestCase):
    def test_move_elements(self):
        source = [1, 2, 3, 4, 5]
        target = [10, 20, 30]
        move_elements(source, target, 3)
        self.assertEqual(source, [1, 2])
        self.assertEqual(target, [10, 20, 30, 3, 4, 5])

    def test_move_more_than_exists(self):
        source = [1, 2]
        target = [10, 20, 30]
        move_elements(source, target, 5)
        self.assertEqual(source, [])
        self.assertEqual(target, [10, 20, 30, 1, 2])

    def test_move_zero_elements(self):
        source = [1, 2, 3, 4, 5]
        target = [10, 20, 30]
        move_elements(source, target, 0)
        self.assertEqual(source, [1, 2, 3, 4, 5])
        self.assertEqual(target, [10, 20, 30])
