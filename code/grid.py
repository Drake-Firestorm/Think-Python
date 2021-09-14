def do_twice(f):
    f()
    f()


def do_four(f):
    do_twice(f)
    do_twice(f)


def print_border():
    print("+ - - - -", end=" ")


def print_borders():
    do_twice(print_border)
    print("+")


def print_column():
    print("|" + " "*8, end=" ")


def print_columns():
    do_twice(print_column)
    print("|")


def frame():
    print_borders()
    do_four(print_columns)


# 2x2 grid
def two_by_two():
    do_twice(frame)
    print_borders()


two_by_two()


# 4x4 grid
def print_columns_2():
    do_twice(print_column)
    print_columns()


def frame2():
    do_twice(print_border)
    print_borders()
    do_four(print_columns_2)


def four_by_four():
    do_four(frame2)
    do_twice(print_border)
    print_borders()


four_by_four()


# The manual way of creating the grids
def two_by_two_explicit():
    print("+", end=" ")
    print("- " * 4, end=" ")
    print("+", end=" ")
    print("- " * 4, end=" ")
    print("+")
    print("|", end=" ")
    print(" " * 8, end=" ")
    print("|", end=" ")
    print(" " * 8, end=" ")
    print("|")
    print("|", end=" ")
    print(" " * 8, end=" ")
    print("|", end=" ")
    print(" " * 8, end=" ")
    print("|")
    print("|", end=" ")
    print(" " * 8, end=" ")
    print("|", end=" ")
    print(" " * 8, end=" ")
    print("|")
    print("|", end=" ")
    print(" " * 8, end=" ")
    print("|", end=" ")
    print(" " * 8, end=" ")
    print("|")
    print("+", end=" ")
    print("- " * 4, end=" ")
    print("+", end=" ")
    print("- " * 4, end=" ")
    print("+")
    print("|", end=" ")
    print(" " * 8, end=" ")
    print("|", end=" ")
    print(" " * 8, end=" ")
    print("|")
    print("|", end=" ")
    print(" " * 8, end=" ")
    print("|", end=" ")
    print(" " * 8, end=" ")
    print("|")
    print("|", end=" ")
    print(" " * 8, end=" ")
    print("|", end=" ")
    print(" " * 8, end=" ")
    print("|")
    print("|", end=" ")
    print(" " * 8, end=" ")
    print("|", end=" ")
    print(" " * 8, end=" ")
    print("|")
    print("+", end=" ")
    print("- " * 4, end=" ")
    print("+", end=" ")
    print("- " * 4, end=" ")
    print("+")


def four_by_four_explicit():
    print("+ " + "- "*4 + "+ " + "- "*4 + "+ " + "- "*4 + "+ " + "- "*4 + "+ ")
    print("|" + " " * 9 + "|" + " " * 9 + "|" + " " * 9 + "|" + " " * 9 + "|")
    print("|" + " " * 9 + "|" + " " * 9 + "|" + " " * 9 + "|" + " " * 9 + "|")
    print("|" + " " * 9 + "|" + " " * 9 + "|" + " " * 9 + "|" + " " * 9 + "|")
    print("|" + " " * 9 + "|" + " " * 9 + "|" + " " * 9 + "|" + " " * 9 + "|")
    print("+ " + "- "*4 + "+ " + "- "*4 + "+" + "- "*4 + "+ " + "- "*4 + "+ ")
    print("|" + " " * 9 + "|" + " " * 9 + "|" + " " * 9 + "|" + " " * 9 + "|")
    print("|" + " " * 9 + "|" + " " * 9 + "|" + " " * 9 + "|" + " " * 9 + "|")
    print("|" + " " * 9 + "|" + " " * 9 + "|" + " " * 9 + "|" + " " * 9 + "|")
    print("|" + " " * 9 + "|" + " " * 9 + "|" + " " * 9 + "|" + " " * 9 + "|")
    print("+ " + "- " * 4 + "+ " + "- " * 4 + "+" + "- " * 4 + "+ " + "- " * 4 + "+ ")
    print("|" + " " * 9 + "|" + " " * 9 + "|" + " " * 9 + "|" + " " * 9 + "|")
    print("|" + " " * 9 + "|" + " " * 9 + "|" + " " * 9 + "|" + " " * 9 + "|")
    print("|" + " " * 9 + "|" + " " * 9 + "|" + " " * 9 + "|" + " " * 9 + "|")
    print("|" + " " * 9 + "|" + " " * 9 + "|" + " " * 9 + "|" + " " * 9 + "|")
    print("+ " + "- "*4 + "+ " + "- "*4 + "+" + "- "*4 + "+ " + "- "*4 + "+ ")
    print("|" + " " * 9 + "|" + " " * 9 + "|" + " " * 9 + "|" + " " * 9 + "|")
    print("|" + " " * 9 + "|" + " " * 9 + "|" + " " * 9 + "|" + " " * 9 + "|")
    print("|" + " " * 9 + "|" + " " * 9 + "|" + " " * 9 + "|" + " " * 9 + "|")
    print("|" + " " * 9 + "|" + " " * 9 + "|" + " " * 9 + "|" + " " * 9 + "|")
    print("+ " + "- " * 4 + "+ " + "- " * 4 + "+ " + "- " * 4 + "+ " + "- " * 4 + "+ ")


# two_by_two_explicit()
# print(" ")
# four_by_four_explicit()
