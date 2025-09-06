import os
import shutil

class Node:
    def __init__(self, name, is_dir=False):
        self.name = name
        self.is_dir = is_dir
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def print_tree(self, level=0):
        indent = " "* level
        print(f"{indent}{self.name}")
        for child in self.children:
            child.print_tree(level + 1)

def build_tree(path):
    node = Node(os.path.basename(path), is_dir=True)
    try:
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                node.add_child(build_tree(item_path))
            else:
                node.add_child(Node(item, is_dir=False))
    except PermissionError:
        pass
    return node

def organize_by_extension(directory):
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)

        if os.path.isfile(item_path):
            ext = os.path.splitext(item)[1][1:]
            if not ext:
                ext = "others"


            folder_path = os.path.join(directory, ext)
            os.makedirs(folder_path, exist_ok=True)


            shutil.move(item_path, os.path.join(folder_path, item))

if __name__ == "__main__":
    directory = r"C:\Users\Jojo Oresanya\PycharmProjects\week2\files_to_organize"

    if not os.path.exists(directory):
        print(f"Folder does not exist: {directory}")
    else:
        root = build_tree(directory)
        root.print_tree()

