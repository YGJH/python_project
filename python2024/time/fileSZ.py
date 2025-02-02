import os

def list_file_by_size(directory, n):
    for root, dirs, files in os.walk(directory):
        for file in files:
            full_file_name = os.path.join(root, file)
            filesize = os.path.getsize(full_file_name)
            if filesize >= n:
                yield (full_file_name, filesize) 


