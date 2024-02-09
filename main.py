
def main():
  #ggggggg
  print("fdfdbh")


if __name__ == "__main__":
  main()



import os
import datetime
import time
import threading

folder_path = "/path/to/folder"  # путь к директории, в которой нужно проверять папки
days_to_keep = 5  # количество дней, после которых папка будет удалена

def delete_old_folders():
    while True:
        for filename in os.listdir(folder_path):
            filepath = os.path.join(folder_path, filename)
            if os.path.isdir(filepath):
                folder_age = (datetime.datetime.now() - datetime.datetime.fromtimestamp(os.path.getmtime(filepath))).days
                if folder_age > days_to_keep:
                    os.rmdir(filepath)
                    print(f"Folder {filepath} has been deleted.")
        time.sleep(86400)  # задержка в 24 часа

# запуск программы в отдельном потоке
thread = threading.Thread(target=delete_old_folders)
thread.start()



import os
import datetime
import time
import threading

days_to_keep = 1  # количество дней, после которых папка будет удалена

def delete_old_folders(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            folder_age = (datetime.datetime.now() - datetime.datetime.fromtimestamp(os.path.getmtime(dir_path))).days
            if folder_age > days_to_keep:
                os.rmdir(dir_path)
                print(f"Folder {dir_path} has been deleted.")
        for file in files:
            file_path = os.path.join(root, file)
            file_age = (datetime.datetime.now() - datetime.datetime.fromtimestamp(os.path.getmtime(file_path))).days
            if file_age > days_to_keep:
                os.remove(file_path)
                print(f"File {file_path} has been deleted.")

folder_paths = ["path/to/folder1", "path/to/folder2", "path/to/folder3"]  # список путей к директориям, которые нужно проверять

def run_deletion():
    while True:
        for folder_path in folder_paths:
           delete_old_folders(folder_path)
        time.sleep(86400)  # задержка в 24 часа  
# запуск программы в отдельном потоке
thread = threading.Thread(target=run_deletion)
thread.start()



import os
import datetime
import threading

days_to_keep = 5  # количество дней, после которых папка будет удалена

def delete_old_folders(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            folder_age = (datetime.datetime.now() - datetime.datetime.fromtimestamp(os.path.getmtime(dir_path))).days
            if folder_age > days_to_keep:
                os.rmdir(dir_path)
                print(f"Folder {dir_path} has been deleted.")
        for file in files:
            file_path = os.path.join(root, file)
            file_age = (datetime.datetime.now() - datetime.datetime.fromtimestamp(os.path.getmtime(file_path))).days
            if file_age > days_to_keep:
                os.remove(file_path)
                print(f"File {file_path} has been deleted.")

folder_paths = ["path/to/folder1", "path/to/folder2", "path/to/folder3"]  # список путей к директориям, которые нужно проверять

def run_deletion():
    for folder_path in folder_paths:
        delete_old_folders(folder_path)

# запуск программы в отдельном потоке
thread = threading.Thread(target=run_deletion)
thread.start()