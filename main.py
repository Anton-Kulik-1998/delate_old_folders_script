import threading
from app.delete_old_folders_script import check_old_files
from config.settings import FOLDERS_PATH
from config.settings import DAYS_TO_KEEP
from config.settings import TIME_TO_SLEEP

def main(directory_path, days_to_keep, time_to_sleep):
    # Создаем поток для выполнения функции в отдельном потоке
    thread = threading.Thread(target=check_old_files, args=(directory_path, days_to_keep, time_to_sleep))
    # thread.daemon = True  # Поток завершится, если основной поток завершится
    thread.start()

if __name__ == "__main__":
    main(FOLDERS_PATH, DAYS_TO_KEEP, TIME_TO_SLEEP)
