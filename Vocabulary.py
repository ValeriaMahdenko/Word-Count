from Validation import Validation
from tabulate import tabulate


class Vocabulary:

    def __init__(self):
        self.words = list()
        self.search_history = {}

    def __setitem__(self, floor_number, data):
        self.words[floor_number] = data

    def __getitem__(self, key):
        return self.words[key]

    def __str__(self):
        x = ""
        for i in self.words:
            x += str(i) + ", "
        return x

    def count(self):
        return len(self.words)

    def print_vocabulary(self, offset=None, limit=None):
        print(self.words[offset:(limit + offset)])

    def print_search_history(self):
        print(tabulate([(k, v) for (k, v) in self.search_history.items()],
        headers=['Input', 'Result']))

    @Validation.decorator_string
    def add(self, word):
        if word in [var for var in self.words]:
            print("This word is in your vocabulary.")
        else:
            self.words.append(word)

    def find(self, letters_for_search, show_list=False, ):
        counter = 0
        search_list = []
        for word in self.words:
            if letters_for_search in word:
                search_list.append(word)
                counter += 1
        if(counter > 0):
            self.search_history[letters_for_search] = counter
            print("{} : {}".format(letters_for_search, counter))
            if show_list is True:
                return search_list
        else:
            print("There are no more words in the searched "
            "results in your vocabulary!")

    def clear_vocabulary(self):
        self.words.clear()
        print("Vocabulary is empty and ready to use!")

    def clear_search_history(self):
        self.search_history.clear()
        print("Search history is empty!")

    def sort(self, check=True):
        if check is False:
            self.words.sort(reverse=True)
        else:
            self.words.sort()
        print("Success! You can print vocabulary to watch result")
