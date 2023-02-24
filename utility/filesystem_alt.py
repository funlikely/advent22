class Folder:

    def __init__(self, name, path, parent):
        self.name = name
        """:files: dict {name, size} files"""
        self.files = {}
        """:sub_folders: dict {name, Folder(name)}"""
        self.sub_folders = {}
        """:path: list of sub folders from the root to this folder; may not be needed if recursion and things work."""
        self.path = path
        self.size = 0
        self.parent = parent

    def add_sub_folder(self, folder_name):
        """Add a {name: Folder(name)} to the dict of sub_folders."""
        self.sub_folders[folder_name] = Folder(folder_name, self.path + [folder_name], self)

    def add_file(self, file_name, file_size):
        """Add a file represented by a {name: size} to the dict of files"""
        self.files[file_name] = file_size
        self.size += file_size
        if self.parent is not None:
            self.parent.update_parent_size(file_size)

    def update_parent_size(self, size):
        self.size += size
        if self.parent is not None:
            self.parent.update_parent_size(size)

    def sub_folder(self, sub_folder_path):
        """Return the Folder object represented by the sub folder path."""
        # root case
        if not sub_folder_path:
            return self
        elif isinstance(sub_folder_path, str):
            return self.sub_folders[sub_folder_path]
        # recursive case
        else:
            return self.sub_folder(sub_folder_path[0]).sub_folder(sub_folder_path[1:])

    def get_all_folder_sizes(self):
        """
        :return: Dict of {(Str)path : (Int)size}
        """

        if not self.sub_folders:
            # base case
            return {'/'.join(self.path): self.size}
        else:
            # recursive case
            list_of_dict_of_sub_folder_sizes = [self.sub_folders[path].get_all_folder_sizes() for path in self.sub_folders]
            dict_of_sub_folder_sizes = {}
            while len(list_of_dict_of_sub_folder_sizes) > 1:
                dict_of_sub_folder_sizes = dict_of_sub_folder_sizes | list_of_dict_of_sub_folder_sizes[0]
                list_of_dict_of_sub_folder_sizes = list_of_dict_of_sub_folder_sizes[1:]

            return {'/'.join(self.path): self.size} | dict_of_sub_folder_sizes

    def local_files_size_total(self):
        return sum(self.files.values())

    def get_list_of_sub_folders(self, path):
        """Returns list of the names of the immediate sub folders (non-recursive)"""
        return list(self.sub_folder(path).sub_folders.keys())

    def get_list_of_file_names(self, path):
        """Returns list of the names of the immediate sub folders (non-recursive)"""
        return list(self.sub_folder(path).files.keys())
