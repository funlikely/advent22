class Folder:

    def __init__(self, name, path):
        self.name = name
        self.files = []
        """:sub_folders: set of dict {name, Folder(name)}"""
        self.sub_folders = {}
        """:path: list of subfolders from the root to this folder --- may not be needed if recursion and things work."""
        self.path = path

    def add_sub_folder(self, folder_name):
        """Add a dict {name, Folder(name)} to the set of sub_folders."""
        self.sub_folders.append({folder_name: Folder(folder_name, self.path.append(self.name))})

    def add_file(self, file_name, file_size):
        self.files.append({file_name: file_size})

    def sub_folder(self, sub_folder_path):
        """Return the Folder object represented by the sub folder path."""
        # root case
        if not sub_folder_path:
            return self
        # recursive case
        else:
            return self.sub_folders[sub_folder_path[0]].sub_folder(sub_folder_path[1:])
