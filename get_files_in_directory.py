import os

class get_files():

	def __init__(self, path=0, subfolders=False, ftype="All", incl_ext=[], excl_ext=[]):
		'''
		A collection of helpful methods for handling file directories
		@Params:
			► path (str) = Path to the directory
			► subfolders (Bool) = True/False whether to look within sub-folders
			► ftype (str) = String file extension filter (Unsused)
			► incl_ext (List) = List of file extensions to include in search
			► excl_ext (List) = List of file extensions to exclude in search

		@Methods:
			► get_all_in_folder() -> Get the list of file names in the folder
			► get_files_in_folder() -> Get the list of file names in the folder
			► get_folders_in_folder() -> Get the list of file names in the folder
			► get_all_in_subfolders() -> Walk through all subdirectories and files and return list of items
			► get_files_in_subfolders) -> Same as get_all_in_subfolders() but with file extension filters
		'''
		
		if path != 0:
			self.path = path
		else:
			self.path = self.get_path()

		print(self.path)

		self.subfolders = subfolders
		self.ftype = ftype
		self.incl = incl_ext
		self.excl = excl_ext

		self.files = self.get_folders_in_folder()

	@staticmethod
	def get_path():
    from tkinter.filedialog import askdirectory
		return askdirectory()

	def get_all_in_folder(self):
		# Get the list of file names in the folder
		return os.listdir(self.path)

	def get_files_in_folder(self):
		# Get the list of file names in the folder
		return [f for f in os.listdir(self.path) if os.path.isfile(os.path.join(self.path, f))]

	def get_folders_in_folder(self):
		# Get the list of file names in the folder
		return [item for item in os.listdir(self.path) if os.path.isdir(os.path.join(self.path, item))]

	def get_all_in_subfolders(self):
		items = []
		# Walk through all subdirectories and files
		for root, dirs, files in os.walk(self.path):
			for file in files:
				# Print the full path of each file
				items.append(os.path.join(root, file))
		return items

	def get_files_in_subfolders(self):
		items = []
		# Walk through all subdirectories and files
		for root, dirs, files in os.walk(self.path):
			for file in files:
				# Only include files (not directories) in the list
				if os.path.isfile(os.path.join(root, file)):

					if len(self.incl) > 0:
						if os.path.splitext(file)[1] in self.incl:
							# Print the full path of each file
							items.append(file)

					if len(self.excl) > 0:
						if os.path.splitext(file)[1] not in self.excl:
							# Print the full path of each file
							items.append(file)
		return items
