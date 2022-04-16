import re
from glob import glob

files = glob("files/*")


def clearing_text():
    f = (x for x in files)
    lst = []
    for i in range(len(files)):
        try:
            with open(next(f), 'r') as file:
                num = re.sub("[-a-z '. ()\n +A-Z]", "", str(file.read()))
                num = num.split(',')
                for i in num:
                    if i.isdigit():
                        lst.append(i)
                    else:
                        continue

        except FileNotFoundError:
            print('not found')
        finally:
            file.closed

    return lst


def phonebook(num):
    numb_book = []
    for el in num:
        if len(el) > 9 and len(el) < 12:
            my_num = f"+7 (812) {el[5:8]}-{el[7:]}"
            numb_book.append(my_num)

    return numb_book


if __name__ == '__main__':

    res = clearing_text()

    result = phonebook(res)
    ascending_numb = sorted(result)
    print(f"ascending {ascending_numb}")
    print(f"not sorted {result}")
    # +7 (812) 123-4567
