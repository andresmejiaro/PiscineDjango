def read_and_print():
    with  open("/home/andres/Django_Piscine/day2/ex01/numbers.txt") as file:
        text = file.read()
    text2 = text.split(",")
    list(map(lambda number: print(number), text2))


if __name__ == "__main__":
    read_and_print()


