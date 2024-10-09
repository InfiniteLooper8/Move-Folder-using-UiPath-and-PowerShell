import os

def get_folder_size(folder_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size / (1024 * 1024)  # size in MB

# Test the function by printing the folder size
folder_path = "C:\\GeneratedFiles\\Files"
size_in_mb = get_folder_size(folder_path)
print(f"Folder size: {size_in_mb} MB")