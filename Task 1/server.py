import time
import zmq
"""
Creating Class Server
"""
class Server:

    def __init__(self, port):
        """
        Initialize the Server class.

        Args:
            port (int): The port number on which the server will listen for incoming connections.
        """
        self.context = zmq.Context()  # Create a ZeroMQ context
        self.socket = self.context.socket(zmq.REP)  # Create a REP (reply) socket
        self.socket.bind(f"tcp://*:{port}")  # Bind the socket to the specified port

    def run(self):
        """
        The server enters an infinite loop, where it receives messages from clients.
        If the message is "TIME", it sends the current time back to the client.
        Otherwise, it sends back the same message as recieved.
        """
        while True:
            message = self.socket.recv_string()  # Receive a message from a client
            if message == "TIME":
                current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # Get the current time
                self.socket.send_string(current_time)  # Send the current time back to the client
            else:
                self.socket.send_string(f"Received: {message}")  # Send an acknowledgment message back to the client

if __name__ == "__main__":
    server = Server(5555)  # Create a Server instance with port 5555
    server.run()  # Run the server