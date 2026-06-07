#Task 1: Organize files automatically based on file types.

import os
import shutil

source_folder = r"C:\Users\Lenovo\Python_Internship_Tasks\LEVEL_4\test_files"

files = os.listdir(source_folder)

for file in files:

    file_path = os.path.join(source_folder, file)

    if os.path.isfile(file_path):

        extension = file.split(".")[-1]

        folder_name = extension.upper() + "_Files"

        destination_folder = os.path.join(source_folder, folder_name)

        if not os.path.exists(destination_folder):
            os.mkdir(destination_folder)

        shutil.move(file_path, os.path.join(destination_folder, file))

print("Files organized successfully!")