import os
import random
import string

def create_random_files(folder_path, num_files, min_size_kb, max_size_kb):
    if not os.path.exists(folder_path): #create folder, if does not exist
        os.makedirs(folder_path, exist_ok=True)  # Create folder for generated files if it doesn't exist
    for i in range(num_files):
        file_name = f"random_file_{i}.txt"
        file_path = os.path.join(folder_path, file_name)

        # Randomize file size between min_size_kb and max_size_kb
        file_size_kb = random.randint(min_size_kb, max_size_kb)

        with open(file_path, 'w') as f:
            f.write(''.join(random.choices(string.ascii_letters + string.digits, k=file_size_kb * 1024)))
        
        print(f"Created {file_name} with size {file_size_kb} KB")

# Example: Create 10 random files of 100 to 1000KB each
create_random_files("C:\\GeneratedFiles\\Files", num_files=10, min_size_kb=100, max_size_kb=1000)

print("Random files successully generated.")