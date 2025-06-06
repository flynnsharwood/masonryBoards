import os
import yaml
import argparse

from boards.image_utils import get_image_names
from boards.file_utils import create_html_file, create_css_file, create_js_file, create_index_file, create_master_index_file
from boards.dir_utils import getDirList



def load_config(yml_path="config.yml"):
    with open(yml_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)
    

parser = argparse.ArgumentParser()
parser.add_argument('--csvs', nargs='+', help='List of CSV files to use')
args = parser.parse_args()

config = load_config()
masterDir = config["masterDir"]


# choice = input("which csvs to choose?\n1. misc\n2. SSD files\n3. pinterest\n4. All\n")
# add more options to include more combinations of csv files. 
# choice = 4 # for test puposes

# Determine CSV list
csvList = args.csvs if args.csvs else config.get("csvList", [])

if not csvList:
    print("No CSV files provided. Set them in config.yml or pass using --csvs.")
    exit(1)

# Build directory list from CSVs
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