# TASK-1
import os
import shutil


example_dir = "Example"
if not os.path.exists(example_dir):
    os.mkdir(example_dir)
    print(f"'{example_dir}' directory created.")


subdirect_dir = os.path.join(example_dir, "subdirect")
if not os.path.exists(subdirect_dir):
    os.mkdir(subdirect_dir)
    print(f"'{subdirect_dir}' subdirectory created.")
    
image_file = "images.jpg"
text_file = "file.txt"


shutil.move(image_file, subdirect_dir)
print(f"'{image_file}' moved to '{subdirect_dir}'.")
shutil.move(text_file, subdirect_dir)
print(f"'{text_file}' moved to '{subdirect_dir}'.")

for filename in os.listdir(subdirect_dir):
    if filename.endswith(".txt"):
        source = os.path.join(subdirect_dir, filename)
        destination = os.path.join(example_dir, filename)
        shutil.move(source, destination)
        print(f"'{filename}' moved from '{subdirect_dir}' to '{example_dir}'.")
