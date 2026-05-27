# Python Socket Chat

A real-time, terminal-based chat application built using Python’s native `socket` library. This project serves as a practical implementation of client-server architecture, demonstrating how to handle multiple concurrent connections and broadcast messages over a TCP network.

## Features

* **Multi-Client Support:** The server utilizes multithreading to manage several connected users simultaneously.
* **Real-time Broadcasting:** Messages sent by one client are instantly relayed to all other connected participants.
* **Lightweight:** Built entirely using Python’s built-in libraries—no external dependencies required.
* **Terminal-Ready:** Designed for a clean CLI experience.

## How to Get Started

### Prerequisites
* [Python 3.x](https://www.python.org/downloads/) installed on your machine.

### Running the Application

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Nirushanth-07/Python-Socket-Chat.git](https://github.com/Nirushanth-07/Python-Socket-Chat.git)
   ```
   ```bash
   cd python-socket-chat
   ```

2. **Start the Server:**
   ```bash
   python server.py
   ```
3. **Start the CLients:**
   ```bash
   python client.py
   ```

## Technical Overview
* Networking: Uses the **socket** module for TCP connections.
* Concurrency: Implements the **threading** module to ensure the server can listen for new connections while simultaneously handling incoming messages from existing ones.
* I/O: Uses **sendall()** to ensure reliable data delivery across the network.

### License
This project is open-source and available under the MIT License.
