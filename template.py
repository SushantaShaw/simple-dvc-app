import os
dirs = [
    os.path.join("Data","Raw"),
    os.path.join("Data","Processed"),
    "notebooks",
    "saved_mdoels",
    "src"
]

for dir_ in dirs:
    os.makedirs(dir_,exist_ok=True)
    with open(os.path.join(dir_,".gitkeep"),"w"):
        pass


files = [
    "dvc.yaml",
    "params.yaml",
    ".gitignore",
    os.path.join("src","__init__.py")
]

for file_ in files:
    with open(file_,"w") as f:
        pass
