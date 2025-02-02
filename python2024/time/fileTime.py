import os
import datetime

def list_file_by_time(directory, d):
    today = datetime.datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
    for root, dirs, files in os.walk(directory):
        for file in files:
            full_file_name = os.path.join(root, file)
            if os.path.exists(full_file_name):
                modification_time = os.path.getmtime(full_file_name)
                file_datetime = datetime.datetime.fromtimestamp(modification_time).replace(hour=0, minute=0, second=0, microsecond=0)
                delta_days = (today - file_datetime).days
                if delta_days <= d:
                    yield (full_file_name, file_datetime)


for f in list_file_by_time("c:\\users",10):
    print(f)