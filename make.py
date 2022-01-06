# Load libraries
import os
import datetime

nb_path = 'notebooks/'

def main():

    all_ipynb_files = [os.path.join(root, name)
                    for root, dirs, files in os.walk(nb_path)
                        for name in files
                            if name.endswith((".ipynb"))]

    ipynb_files = [ x for x in all_ipynb_files if ".ipynb_checkpoints" not in x ]

    md_files = [ x.replace(".ipynb", ".md") for x in ipynb_files]

    md_files = [ x.replace("notebooks", "content") for x in md_files ]

    md_temp_files = [ "./" + x for x in md_files ]

    # print(md_files)

    # [ process_folder(x) for x in md_files ]

    for nb_file, md_file in zip(ipynb_files, md_temp_files):

        print(nb_file, md_file)

        os.system(f"jupyter nbconvert --to markdown {nb_file} --output-dir {'/'.join(md_file.split('/')[:-1])}")

    author = "Altair"

    for single_file in md_files:

        title = single_file.split('/')[-1].split('.')[0]

        template_metadata = f"""---
title: "{title}"
author: "{author}"
type: article
draft: false
--- \n
"""

        with open(single_file, 'r') as f:
            content = f.read()
            new_content = template_metadata + content
            with open(single_file, "w") as f:
                f.write(new_content)
        
if __name__ == "__main__":

    main()


