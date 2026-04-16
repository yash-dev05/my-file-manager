import os
import shutil

def list_files(path):
    try:
        files = os.listdir(path)   # Gets all files and folders inside given path
        print("\nContents of folder:\n")
        for file in files:
            print(file)  #print each file/folder name
    except Exception as e:
        print("Error:",e)

#function to create a new folder
def create_folder(path,folder_name):
    try:
        #combine the path and folder
        full_path = os.path.join(path,folder_name)
        os.mkdir(full_path)#creates the folder
        print("Folder created successfully.")
    
    except Exception as e:
        print("Error:",e)

#function to delete file or folder
def delete_item(path):
    try:
        if os.path.isfile(path):
            os.remove(path)
            print("File deleted successfully.")

        elif os.path.isdir(path):
            shutil.rmtree(path)
            print("File deleted successfully.")

        else:
            print("File/Folder not found.")
    
    except Exception as e:
        print("Error:", e)

#function to rename the file or folder
def rename_item(old_name,new_name):
    try:
        os.rename(old_name, new_name) 
        print("Renamed successfully.")

    except Exception as e:
        print("Error:", e)

#function to copy file
def copy_file(source,destination):
    try:
        shutil.copy(source,destination)
        print("File copied successfully.")

    except Exception as e:
        print("Error:", e)

# Function to move file
def move_file(source, destination):
    try:
        shutil.move(source, destination)   # Move file from source to destination
        print("File moved successfully.")

    except Exception as e:
        print("Error:", e)