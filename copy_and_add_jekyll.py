import os
import shutil
import sys

def copy_and_add_jekyll(source_dir, destination_dir):
    for filename in os.listdir(source_dir):
        if filename.endswith('.html'):
           if os.path.isfile(os.path.join(source_dir, filename)):
            try:
                name, extension = os.path.splitext(filename)
                character = name.split('.')[0] 
                title = name.split('.')[1]
                title.replace('-out.html', '')
                with open(os.path.join(source_dir, filename), 'r') as file:
                    content = file.read()
                link = '''
---
layout: page
title: %s
permalink: /l%s
---
Leetcode Question: %s
                '''%(title, character, character)
                new_content = link + content
                with open(os.path.join(destination_dir, filename), 'w') as file:
                    file.write(new_content)
            except Exception as e:
                print(e)
                print("Error processing file: ", filename)

if __name__ == "__main__":
    # if len(sys.argv) < 3:
    #     print("Usage: python copy_and_add_jekyll.py <source_dir> <destination_dir>")
    #     sys.exit(1)

    # source_dir = sys.argv[1]
    # destination_dir = sys.argv[2]
    copy_and_add_jekyll("/home/darulebreaker/repos/Leetcode-Questions-Scraper/", "/home/darulebreaker/repos/algoadvance/problems/")