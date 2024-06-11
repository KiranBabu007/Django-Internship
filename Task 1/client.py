import zmq
# creating a class Client
class Client:
    def __init__(self, server_address):
        """
        Initialize the Client class.

        Args:
            server_address (str): The address of the server to connect to.
        """
        self.context = zmq.Context()  # Create a ZeroMQ context
        self.socket = self.context.socket(zmq.REQ)  # Create a REQ (request) socket
        self.socket.connect(server_address)  # Connect the socket to the server address

    def send_message(self, message):
        """
        Send a message to the server and print the server's response.

        Args:
            message (str): The message to send to the server.
        """
        self.socket.send_string(message)  # Send the message to the server
        response = self.socket.recv_string()  # Receive the server's response
        print(f"Server response: {response}")  # Print the server's response

if __name__ == "__main__":
    # Create a Client instance connected to the server at "tcp://localhost:5555"
    client = Client("tcp://localhost:5555")
    while True:
        # Send the message to the server and print the response
        client.send_message(input("Enter a message (or 'TIME' for current time): "))