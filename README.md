# get_files_in_directory
Collection of class methods for listing files from a directory

## Methods

* get_all_in_folder() -> Get the list of file names in the folder
* get_files_in_folder() -> Get the list of file names in the folder
* get_folders_in_folder() -> Get the list of file names in the folder
* get_all_in_subfolders() -> Walk through all subdirectories and files and return list of items
* get_files_in_subfolders) -> Same as get_all_in_subfolders() but with file extension filters

## Parameters

* path (str) = Path to the directory
* subfolders (Bool) = True/False whether to look within sub-folders
* ftype (str) = String file extension filter (Unsused)
* incl_ext (List) = List of file extensions to include in search
* excl_ext (List) = List of file extensions to exclude in search
