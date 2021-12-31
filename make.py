# Load libraries
import os
import re
import fileinput
import sys
from glob import glob
import shutil
import datetime

path = 'content/'

# Find all jupyter notebooks in all content folders
all_ipynb_files = [os.path.join(root, name)
                   for root, dirs, files in os.walk(path)
                       for name in files
                           if name.endswith((".ipynb"))]

# Remove all notebooks from checkpoint folders
ipynb_files = [ x for x in all_ipynb_files if ".ipynb_checkpoints" not in x ]

# For each file
for file in ipynb_files:
    # Convert into markdown
    os.system('jupyter nbconvert --to markdown {file}'.format(file=file))

date_time = datetime.datetime.now()
author = "Altair"

md_files = [ x.replace(".ipynb", ".md") for x in ipynb_files]


for single_file in md_files:

    title = single_file.split('/')[-1].split('.')[0]

    template_metadata = f"""---
title: "{title}"
author: "{author}"
date: 2021-07-07T00:00:00-07:00
type: article
draft: false
--- \n
"""

    # Read the file
    with open(single_file, 'r') as f:
        content = f.read()
        new_content = template_metadata + content
        with open(single_file, "w") as f:
            f.write(new_content)
        


