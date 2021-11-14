from Vocabulary import Vocabulary
from Validation import Validation


def menu():
    print("\n1 - read new vocabulary from file")
    print("2 - print vocabulary")
    print("3 - add element to vocabulary ")
    print("4 - sort list")
    print("5 - search")
    print("6 - show search history")
    print("7 - create new vocabulary")
    print("8 - clear search history")
    print("0 - EXIT")


@Validation.decorator_filename
def read_txt(lst, file_name):
    read_list = []
    try:
        with open(file_name) as file:
            read_list = file.read().split("\n")
            for i in read_list:
                try:
                    lst.add(i)
                except ValueError as a:
                    print("Element '{}' : {}".format(i, str(a)))
                    continue
        file.close()
    except ValueError and FileNotFoundError as e:
        print(str(e))


@Validation.decorator_filename
def write_txt(lst, file_name):
    try:
        f = open(file_name, "w")
        f.writelines(str(i) + "\n" for i in lst)
        f.close()
    except ValueError or FileNotFoundError:
        print("File not exit")


def limited_list(lst, count, offset=0, limit=5):
    choice = "yes"
    print("For your convenience, the page displays 5 words "
    "from your vocabulary")
    while True:
        if choice.lower() == "yes":
            print(lst[offset:(limit + offset)])
        else:
            break

        offset += limit
        if offset >= count:
            break
        choice = input("Next page: (Yes/No)\t")
        continue


def main():
    words = Vocabulary()
    while True:
        menu()
        response = input("Your choice: ")
        if response == "0":
            print("Thank you for attention! Goodbay!")
            break
        elif response == "1":
            try:
                read_txt(words, input("Enter filename (only .txt): "))
            except Exception as e:
                print(str(e))

        elif response == "2":
            limited_list(words, words.count())

        elif response == "3":
            print("~~~~~~~~~~~~~~~~ADD~~~~~~~~~~~~~~~~~~~~")
            word = input("Enter word: ")
            try:
                words.add(word)
            except ValueError as e:
                print("{}:  {}".format(word, str(e)))

        elif response == "4":
            print("~~~~~~~~~~~~~Sort~~~~~~~~~~~~~~~~~~")
            word = input("Enter asc/decs:\t")
            if word.lower() == "decs":
                words.sort(False)
            else:
                words.sort()

        elif response == "5":
            print("~~~~~~~~~~~~~~~~~~~~~Search~~~~~~~~~~~~~~~~~~~~~")
            key = input("Enter key:")
            show = input("You want to show words that contain provided "
                "letters?(Yes/No)\t")
            if show.lower() == "yes":
                search_list = words.find(key, True)
                print(len(search_list))
                limited_list(search_list, len(search_list))
            else:
                words.find(key)

        elif response == "6":
            print("~~~~~~~~~~~~~~~Show search history~~~~~~~~~~~~~~~")
            words.print_search_history()

        elif response == "7":
            print("~~~~~~~~~~~~~~Create new vocabulary~~~~~~~~~~~")
            for_write = input("Maybe You want to save your vocabulary "
                "before clear it? (Yes/No)\t")
            if for_write.lower() == "yes":
                try:
                    write_txt(words, input("Enter filename: "))
                except Exception as e:
                    print(str(e))
            words.clear_vocabulary()

        elif response == "8":
            print("~~~~~~~~~~~~~~~~~~~~~~Clean search history~~~~~~~~~~~~~~~~")
            words.clear_search_history()

        else:
            print("The value is incorrect! Please, try again")


if __name__ == "__main__":
    main()
