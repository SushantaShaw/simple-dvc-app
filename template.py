import os

dirs = [
    os.path.join("Data", "Raw"),
    os.path.join("Data", "Processed"),
    os.path.join("prediction_service", "model"),
    "notebooks",
    "saved_mdoels",
    "src",
    "reports",
]

for dir_ in dirs:
    os.makedirs(dir_, exist_ok=True)
    with open(os.path.join(dir_, ".gitkeep"), "w"):
        pass


files = [
    "dvc.yaml",
    "params.yaml",
    ".gitignore",
    os.path.join("src", "__init__.py"),
    os.path.join("reports", "score.json"),
    os.path.join("reports", "params.json"),
]

for file_ in files:
    with open(file_, "a+") as f:
        pass
