import sys

def main():

    line_count = int(input())

    for i in range(line_count):
        word = str(input())
        if len(word) > 10:
            new_word = word[0] + str(len(word) - 2) + word[len(word) - 1]
            print(new_word)
        else:
            print(word)

    return


main()
