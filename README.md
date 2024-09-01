## Deleting Old Files Script
Script for deleting old recordings from CCTV cameras

This script is designed to automatically delete old daily records from surveillance cameras on a network-attached storage (NAS). It provides regular cleaning of the directory to free up space and ensure reliable operation of the surveillance system.

### Features

- **Automatic deletion of old records**: The script checks the directory on the network-attached storage for the number of days since the files were created and deletes files that are older than the specified period.

- **Waiting and rechecking**: After cleaning the directory, the script waits for 24 hours and then repeats the check in an infinite loop, ensuring regular cleaning of the directory.

- **Written in Python 3.9.6**: The script is written in the Python programming language version 3.9.6, providing cross-platform compatibility and ease of use.

- **Uses standard Python modules**: To work with files, the script uses standard modules `os` and `shutil`, making it easy to understand and modify.

- **Uses a separate thread and error handling**: For efficient operation, the script uses a separate thread to not block the main process. Error handling is also provided to ensure stable operation.

- **Dockerfile for containerization**: The project includes a Dockerfile, which allows you to create a separate container for running the script, providing isolation and deployment convenience.

### Usage

1. **Install dependencies**: Make sure Docker is installed on your computer.

2. **Build Docker image**: In the root directory of the project, execute the command `docker build -t delete-old-files .` to build the Docker image.

3. **Run the container**: After successfully building the Docker image, execute the command `docker run -v -d /path/to/local/directory1:/data/directory1 -v /path/to/local/directory1:/data/directory2 delete-old-files` to run the container in the background.

### Example Usage


```bash
docker build -t delete-old-files .
docker run -v /path/to/local/directory1:/data/directory1 -v /path/to/local/directory1:/data/directory2 delete-old-files
