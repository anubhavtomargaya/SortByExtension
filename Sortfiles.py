import os
import shutil

# path directory to be sorted
path = '/Users/anubhav/Downloads/'
# ls of path
list_of_file = os.listdir(path)
new_folder = []
# loop through files extract name and extension separately
for i in list_of_file:
    name, exta = os.path.splitext(i)
    exta = exta[1:] #removes the period from extension

    if exta == '': # skip folders
        continue
    else:

        curr_dir = path #join makes the path with right slashes
        fin_path = os.path.join(curr_dir, exta) # makes the path for the new extension folder
        file_path = os.path.join(curr_dir, i) # makes path of current file

        if os.path.exists(fin_path): # if extension folder exists, move
            shutil.move(file_path, fin_path + '/' + i)
        else:
            os.makedirs(fin_path) #if it doesnt exits, make it then move
            new_folder.append(exta)
            shutil.move(file_path, fin_path + '/' + i)
print(f"folders are sorted by extension: {list_of_file}")

# # print(os.getcwd()) #get current working directory to check
