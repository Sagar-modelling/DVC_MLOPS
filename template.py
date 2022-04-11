import os


dirs = [
    os.path.join("data","raw"), #to create multiple folders
    os.path.join("data","processed"),
    "notebooks", #creating single folder
    "saved_models",
    "src" #source folder where we do development
]

for dir_ in dirs: #createing the directory structure
    os.makedirs(dir_, exist_ok=True)
#The purpose of the . gitkeep file is to solve problem of Git not pushing empty folders to remote DVCS repos like GitHub or GitLab.
    with open(os.path.join(dir_, ".gitkeep"), "w") as f: 
        pass

files = [                   #files
        "dvc.yaml",
        "params.yaml",
        ".gitignore",
        os.path.join("src","__init__.py") #To treat src as a package
]

for file_ in files: #creating the files
    with open(file_, "w") as f:
        pass