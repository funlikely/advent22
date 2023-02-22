class Folder:

    def __init__(self, name, path):
        self.name = name
        self.files = []
        self.sub_folders = []
        self.path = path

    def add_sub_folder(self, folder_name):
        self.sub_folders.append(Folder(folder_name, self.path.append(self.name)))

    def add_file(self, file_name, file_size):
        self.files.append({file_name: file_size})

