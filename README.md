

---

# Python Names Manager with Docker Volume Persistence

This repository contains a simple Python application designed to manage a list of names. The application allows users to add and display names through a command-line interface. The key feature of this project is the persistence of data using Docker volumes, ensuring that the names you add are not lost between container runs.

## Features

- **Add Names:** Enter names via the command line, which will be stored persistently.
- **Display Names:** View the list of all added names.
- **Data Persistence:** Names are saved to a file within a Docker volume, ensuring they persist across container restarts.

## Files in This Repository

- **`a.py`:** The Python script containing the logic for adding and displaying names, along with file handling for data persistence.
- **`Dockerfile`:** The Dockerfile used to build the Docker image for this application.

## Getting Started

### Prerequisites

- Docker installed on your local machine.
- Basic knowledge of Docker commands.

### How to Use

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/repository-name.git
   cd repository-name
   ```

2. **Build the Docker Image:**

   Use the following command to build the Docker image:

   ```bash
   docker build -t my-python-app .
   ```

3. **Run the Docker Container with a Volume:**

   Run the container with a Docker volume to ensure data persistence:

   ```bash
   docker run -it -v myvolume:/python-volume my-python-app
   ```

   - The `-v` flag mounts a Docker volume named `myvolume` to the `/python-volume` directory inside the container.
   - This ensures that the names are saved in the `names.txt` file within the volume, persisting across container runs.

4. **Interacting with the Application:**

   Once the container is running, you will see a menu with the following options:

   - `1) Add name`: Add a new name to the list.
   - `2) Display names`: Display the list of added names.
   - `3) Exit`: Exit the program.

   Names added during the session will be saved to `names.txt` and will be available in future sessions.

### Example Usage

Here’s an example of how to interact with the application:

```bash
Options:
1) Add name
2) Display names
3) Exit
Choose an option: 1
Enter a name to add: John
John has been added.

Options:
1) Add name
2) Display names
3) Exit
Choose an option: 2

List of names:
1. John
```

### Inspecting the Volume (Optional)

You can inspect the contents of the volume to verify that the names are being stored:

```bash
docker run -it -v myvolume:/python-volume --rm my-python-app bash
```

### Rebuilding the Image

If you make any changes to the Python script, don’t forget to rebuild the Docker image:

```bash
docker build -t my-python-app .
```

## Contributing

If you have any suggestions or improvements, feel free to submit a pull request or open an issue.

## License

This project is open-source and available under the [MIT License](LICENSE).

---
