import unittest
from Vocabulary import Vocabulary


class Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.vocabulary = Vocabulary()
        self.vocabulary.add("one")
        self.vocabulary.add("two")
        self.vocabulary.add("three")

        return super().setUp()

    def test_add(self):
        self.vocabulary.add("four")
        self.vocabulary.add("five")

        self.assertEqual(self.vocabulary.count(), 5)
        self.assertEqual(self.vocabulary[3], "four")
        self.assertNotEqual(self.vocabulary.count(), 3)

    def test_add_notvalid(self):
        try:
            self.vocabulary.add("one")
            self.vocabulary.add("no4444")
        except Exception as e:
            print(e)
        self.assertEqual(self.vocabulary.count(), 3)
        self.assertNotEqual(self.vocabulary.count(), 4)
        self.assertNotEqual(self.vocabulary.count(), 5)

    def test_sort(self):
        self.vocabulary.sort()
        self.assertEqual(self.vocabulary[0], "one")
        self.assertEqual(self.vocabulary[-1], "two")

        self.vocabulary.sort(False)
        self.assertEqual(self.vocabulary[0], "two")
        self.assertEqual(self.vocabulary[-1], "one")

    def test_find(self):
        self.vocabulary.find("ee")
        self.vocabulary.find("e")
        self.vocabulary.find("o")

        self.assertEqual(self.vocabulary.search_history["ee"], 1)
        self.assertEqual(self.vocabulary.search_history["e"], 2)
        self.assertEqual(self.vocabulary.search_history["o"], 2)

    def test_clear_vocabulary(self):
        self.vocabulary.clear_vocabulary()

        self.assertEqual(self.vocabulary.count(), 0)
        self.assertNotEqual(self.vocabulary.count(), 3)

    def test_clear_search(self):
        self.vocabulary.clear_search_history()

        self.assertEqual(len(self.vocabulary.search_history), 0)


unittest.main()
