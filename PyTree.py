import os

def print_directory(path, indentation_level=0):
    total_files = 0
    total_directories = 0

    files = sorted(os.scandir(path), key=lambda f: f.name.lower())

    for idx, file in enumerate(files):
        if idx == len(files) - 1:
            if file.is_dir():
                print("│   " * indentation_level, "└──", file.name)
                subdir_files, subdir_directories = print_directory(file.path, indentation_level + 1)
                total_files += subdir_files
                total_directories += subdir_directories
                total_directories += 1
            else:
                print("│   " * indentation_level, "└──", file.name)
                total_files += 1
        else:
            if file.is_dir():
                print("│   " * indentation_level, "├──", file.name)
                subdir_files, subdir_directories = print_directory(file.path, indentation_level + 1)
                total_files += subdir_files
                total_directories += subdir_directories
                total_directories += 1
            else:
                print("│   " * indentation_level, "├──", file.name)
                total_files += 1

    return total_files, total_directories
total_files, total_directories = print_directory(".")
print(f"\n{total_directories} directories, {total_files} files")