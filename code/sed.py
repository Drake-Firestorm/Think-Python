def sed(pattern, replacement, filename_1, filename_2):
    # f1 = open(filename_1, encoding="utf-8")
    try:
        f1 = open(filename_1, encoding="utf-8")
        f2 = open(filename_2, "w", encoding="utf-8")
    except:
        print("Error opening file")
        raise

    try:
        f1_read = f1.readlines()
    except:
        print("Error reading file")
        raise

    try:
        for line in f1_read:
            # print(line.lower(), pattern.lower(), replacement.lower())
            line = line.replace(pattern.lower(), replacement.lower()).capitalize()
            # print(line)
            f2.write(line)
    except:
        print("Error writing file")
        raise

    try:
        f1.close()
        f2.close()
    except:
        print("Error closing file")
        raise


if __name__ == "__main__":
    sed("Bee", "Cat", "Bee.txt", "Cat.txt")
