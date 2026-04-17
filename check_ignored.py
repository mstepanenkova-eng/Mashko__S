
import os
import re
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--project_dir', required=True)
params = parser.parse_args()
folder = params.project_dir
git_file = os.path.join(folder, '.gitignore')
list = []

try:
    f = open(git_file, 'r')
    for line in f:
        line = line.strip()
        if line == '' or line[0] == '#':
            continue
        list.append(line)
    f.close()
except:
    print('Ниче нет')
    sys.exit(1)

all_files = []
for current_folder, subfolders, filenames in os.walk(folder):
    for name in filenames:
        full_name = os.path.join(current_folder, name)
        rel_name = full_name[len(folder) + 1:]
        all_files.append(rel_name)


ignored_list = []
for file_path in all_files:
    for thing in list:
        regex_pattern = '^' + re.escape(thing).replace('\\*', '.*') + '$'
        if re.match(regex_pattern, file_path):
            ignored_list.append([file_path, thing])
            break

        if thing[0] == '*':
            just_name = file_path.split('/')[-1]
            if re.match(regex_pattern, just_name):
                ignored_list.append([file_path, thing])
                break

if len(ignored_list) == 0:
    print('ниче нет')
else:
    print('Ignored files:')
    for item in ignored_list:
        print(item[0], '->', item[1])