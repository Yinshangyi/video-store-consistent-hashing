# Distributed Video Storage System API

## Introduction
This project provides an API for administering a distributed storage system. It's designed to manage and interact with a distributed environment where data is stored and retrieved efficiently. The system is primarily focused on video data management.

## Architecture

### Persistence Layer
- **VideoRepository Class**: This class serves as the in-memory storage component, implemented using a Python dictionary. It's designed for simplicity and quick access. However, the implementation can be extended or modified to connect to actual storage servers for a more persistent and robust storage solution.

### Server Manager
- **Consistent Hashing**: The server manager uses a consistent hashing algorithm to distribute video storage across various servers. This method provides a scalable and efficient way to add or remove servers with minimal reshuffling of data. 
- **How Consistent Hashing Works**: Consistent hashing maps data to physical servers. When a server is added or removed, only a small portion of the data is re-mapped, significantly reducing the overhead compared to traditional hashing methods.

### API Layers
- **Web/Controller Layer**: This layer handles HTTP requests and responses, providing the interface through which users interact with the storage system.
- **Service Layer**: It encapsulates the business logic of the application, interacting with the persistence layer to perform data operations.
- **Repository Layer**: This layer is responsible for data storage and retrieval, abstracted in the `VideoRepository` class.

## Testing
- **Unit Tests**: Comprehensive unit tests have been implemented for both the service and web layers to ensure reliability and stability of the API. These tests cover various scenarios and edge cases to maintain high-quality code standards.

## Getting Started
A Dockerfile is provided if you wish to run the application with Docker (which is recommended to avoid version issues).
```bash
docker build -t <IMAGE_NAME> .
```
```bash
docker run -p 5000:5000 --name <CONTAINER_NAME> <IMAGE_NAME>
```

A script is also provided to build the Docker image if it doesn't exist yet and to run the container:
```bash
./run_app.sh
```



