import os

from boards.image_utils import get_image_names
from boards.file_utils import create_html_file, create_css_file, create_js_file, create_index_file, create_master_index_file
from boards.dir_utils import getDirList

import yaml

def load_config(yml_path="config.yml"):
    with open(yml_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

config = load_config()
masterDir = config["masterDir"]


# choice = input("which csvs to choose?\n1. misc\n2. SSD files\n3. pinterest\n4. All\n")
# add more options to include more combinations of csv files. 
choice = 4 # for test puposes

try:
    choice = int(choice)
except ValueError:
    print("Invalid input. Enter a number from 1 to 4.")
    exit(1)

csvList = []

match choice:
    case 1:
        csvList = ["fileLists/misc.csv"]
    case 2:
        csvList = ["fileLists/onSsd.csv"]
    case 3:
        csvList = ["fileLists/pinterest.csv"]
    case 4:
        csvList = ["fileLists/misc.csv", "fileLists/onSsd.csv", "fileLists/pinterest.csv"]
        

directories = getDirList(csvList, masterDir)

for directory_info in directories:
    source_directory = directory_info["source_directory"]
    target_directory = directory_info["target_directory"]

    subfolders = {}

    # Walk through all subfolders
    for root, _, files in os.walk(source_directory):
        rel_path = os.path.relpath(root, source_directory)
        if rel_path == ".":
            continue  # Skip the base folder itself

        subfolders[rel_path] = sorted(files)

    os.makedirs(target_directory, exist_ok=True)

    # Create HTML files for each subfolder
    for subfolder, files in subfolders.items():
        subfolder_path = os.path.join(source_directory, subfolder)
        subfolder_file = f"{subfolder.replace(os.sep, '_')}.html"  # Replace slashes with underscores
        output_file = os.path.join(target_directory, subfolder_file)

        os.makedirs(os.path.dirname(output_file), exist_ok=True)  #  Ensure parent directory exists

        create_html_file(files, output_file, subfolder_path, subfolder)


    # Create main index file linking to all subfolder pages
    create_index_file(subfolders.keys(), target_directory)
    # After all individual target directory processing
    create_master_index_file(directories, masterDir)


    # Generate CSS & JS (only needed once)
    create_css_file(target_directory)
    create_js_file(target_directory)
    create_css_file(masterDir)
    create_js_file(masterDir)