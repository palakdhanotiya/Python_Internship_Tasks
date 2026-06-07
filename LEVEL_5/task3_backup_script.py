import os
import shutil

source = "source_folder"
backup = "backup_folder"

if not os.path.exists(backup):
    os.mkdir(backup)

files = os.listdir(source)

for file in files:

    source_path = os.path.join(source, file)
    backup_path = os.path.join(backup, file)

    if os.path.isfile(source_path):
        shutil.copy(source_path, backup_path)

print("Backup completed successfully!")