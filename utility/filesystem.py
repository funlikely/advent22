class Folder:

    def __init__(self, name, path):
        self.name = name
        """:files: list of dict {name, size} files"""
        self.files = []
        """:sub_folders: list of dict {name, Folder(name)}"""
        self.sub_folders = []
        """:path: list of sub folders from the root to this folder; may not be needed if recursion and things work."""
        self.path = path

    def add_sub_folder(self, folder_name):
        """Add a dict {name: Folder(name)} to the set of sub_folders."""
        self.sub_folders.append({folder_name: Folder(folder_name, self.path.append(self.name))})

    def add_file(self, file_name, file_size):
        """Add a file represented by a dict {name: size} to the set of files"""
        self.files.append({file_name: file_size})

    def sub_folder(self, sub_folder_path):
        """Return the Folder object represented by the sub folder path."""
        # root case
        if not sub_folder_path:
            return self
        # recursive case
        else:
            return self.sub_folders[sub_folder_path[0]].sub_folder(sub_folder_path[1:])

    def get_all_folder_sizes(self):
        if not self.sub_folders:
            # base case
            return {self.path: self.local_files_size_total()}
        else:
            # recursive case
            local_files_size = self.local_files_size_total()
            child_folder_sizes_list = []
            child_folder_sizes_total = sum([list(x.values())[0] for x in child_folder_sizes_list.values()])
            return [{self.path: local_files_size + child_folder_sizes_total}] + child_folder_sizes_list

    def local_files_size_total(self):
        return sum([list(file.values())[0] for file in self.files])


