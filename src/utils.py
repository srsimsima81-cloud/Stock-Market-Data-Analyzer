import os

def create_project_folders():
    folders = [
        "data",
        "docs",
        "images",
        "outputs",
        "reports"
    ]

    for folder in folders:
        os.makedirs(folder, exist_ok=True)

    print("✅ Project folders ready.")