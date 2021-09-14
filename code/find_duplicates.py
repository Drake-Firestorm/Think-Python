import hashlib
import os


def file_paths(directory, suffix):
    suffix = "." + suffix
    paths = list()
    for root, subdir, files in os.walk(directory):
        for file in files:
            root2, ext = os.path.splitext(file)
            if ext == suffix:
                paths.append(os.path.join(root, root2 + ext))
    return paths


def is_duplicate(file_list, file):
    file = open(file, encoding="utf-8")
    file_data = file.read()
    file_md5 = hashlib.md5(file_data.encode("utf-8")).hexdigest()
    for f in file_list:
        f = open(f, encoding="utf-8")
        f_data = f.read()
        if f != file and file_md5 == hashlib.md5(f_data.encode("utf-8")).hexdigest():
            return True
    file.close()
    f.close()
    return False


def duplicate_files(directory, suffix):
    paths = file_paths(directory, suffix)
    duplicates = list()
    for file in paths:
        if is_duplicate(paths, file):
            duplicates.append(file)
    return duplicates


if __name__ == "__main__":
    path = "D:\\Codes\\Python\\code"
    print(duplicate_files(path, "txt"))
