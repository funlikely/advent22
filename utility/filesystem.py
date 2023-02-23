import itertools

class Folder:

    def __init__(self, name, path, parent):
        self.name = name
        """:files: list of dict {name, size} files"""
        self.files = []
        """:sub_folders: list of dict {name, Folder(name)}"""
        self.sub_folders = []
        """:path: list of sub folders from the root to this folder; may not be needed if recursion and things work."""
        self.path = path
        self.size = 0
        self.parent = parent

    def add_sub_folder(self, folder_name):
        """Add a dict {name: Folder(name)} to the set of sub_folders."""
        self.sub_folders.append({folder_name: Folder(folder_name, self.path + [folder_name], self)})

    def add_file(self, file_name, file_size):
        """Add a file represented by a dict {name: size} to the set of files"""
        self.files.append({file_name: file_size})
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
            return self.get_specific_sub_folder(sub_folder_path)
        # recursive case
        else:
            return self.sub_folder(sub_folder_path[0]).sub_folder(sub_folder_path[1:])

    def get_all_folder_sizes(self):
        """
        :return: List of Dicts of {(Str)path : (Int)size}
        """

        if not self.sub_folders:
            # base case
            return {'/'.join(self.path): self.size}
        else:
            # recursive case
            list_of_lists_of_sf_sizes = [sf.get_all_folder_sizes() for sf in self.sub_folder_list()]
            child_folder_sizes_list = list(itertools.chain.from_iterable(list_of_lists_of_sf_sizes))
            return [{'/'.join(self.path): self.size}] + child_folder_sizes_list

    def sub_folder_list(self):
        return [list(x.values())[0] for x in self.sub_folders]

    def local_files_size_total(self):
        return sum([list(file.values())[0] for file in self.files])

    def get_list_of_sub_folders(self, path):
        """Returns list of the names of the immediate sub folders (non-recursive)"""
        return [list(x.keys())[0] for x in self.sub_folder(path).sub_folders]

    def get_list_of_file_names(self, path):
        """Returns list of the names of the immediate sub folders (non-recursive)"""
        return [list(x.keys())[0] for x in self.sub_folder(path).files]

    def get_specific_sub_folder(self, name):
        return [folder for folder in self.sub_folders if list(folder.keys())[0] == name][0][name]

