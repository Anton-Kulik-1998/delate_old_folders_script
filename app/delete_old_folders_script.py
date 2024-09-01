import os
import datetime
import time
import shutil

def delete_old_folders(directory_path, days_to_keep):
    try:
        for root, dirs, files in os.walk(directory_path):
          for dir in dirs:
            dir_path = os.path.join(root, dir)
            folder_age = age_in_days(dir_path)
            if folder_age > days_to_keep:
                remove_this_dir_recursive(dir_path)
        #   for file in files:
        #     file_path = os.path.join(root, file)
        #     file_age = age_in_days(file_path)
        #     if file_age > days_to_keep:
        #         remove_this_file(file_path)
    except Exception as e:
        print(f"Ошибка при удалении файлов: {e}")


def age_in_days(path):
    return (datetime.datetime.now() - datetime.datetime.fromtimestamp(os.path.getmtime(path))).days

        
def remove_this_dir_recursive(dir_path):
    shutil.rmtree(dir_path)
    print(f"Folder: {dir_path} has been deleted.")


def remove_this_file(file_path):
    os.remove(file_path)
    print(f"File {file_path} has been deleted.")


def check_old_files(directory_path, days_to_keep, time_to_sleep):
    while True:
        try:
            for dir in directory_path:
                print(f"Проверка на наличие старых файлов в {dir}")
                delete_old_folders(dir, days_to_keep)
            # Получение текущей даты и времени
            current_datetime = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            print(f"Проверка завершена! Дата проверки: {current_datetime}\nОжидание перед следующей проверкой... ({time_to_sleep} часа)")
            time.sleep(time_to_sleep * 60 * 60) # задержка в 24 часа (24 * 60 * 60 = 86400)
        except Exception as e:
            current_datetime = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            print(f"Ошибка при выполнении проверки: {e}\nДата ошибки: {current_datetime}")


