import socket
import json


def start_server(host='localhost', port=12345):
    """
    Start a server

    Args:
        host (str): The host to bind the server to
        port (int): The port to listen on
    """
    try:
        # Create a socket object
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Allow reuse of address
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # Bind the socket to the host and port
        server_socket.bind((host, port))

        # Listen for incoming connections
        server_socket.listen(1)
        print(f"Server listening on {host}:{port}")

        while True:
            # Accept a connection
            client_socket, client_address = server_socket.accept()
            print(f"Connection from {client_address}")

            try:
                # Receive data from client
                data = b""
                while True:
                    chunk = client_socket.recv(1024)
                    if not chunk:
                        break
                    data += chunk

                # Deserialize the JSON data
                if data:
                    received_dict = json.loads(data.decode('utf-8'))
                    print("Received Dictionary from Client:")
                    print(received_dict)

            except Exception as e:
                print(f"Error handling client: {e}")
            finally:
                # Close the client connection
                client_socket.close()
                break  # Exit after handling one connection for this example

    except Exception as e:
        print(f"Server error: {e}")
    finally:
        # Close the server socket
        if 'server_socket' in locals():
            server_socket.close()


def send_data(dictionary, host='localhost', port=12345):
    """
    Send a dictionary as JSON data to a server.

    Args:
        dictionary (dict): The dictionary to send
        host (str): The server host
        port (int): The server port
    """
    try:
        # Create a socket object
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the server
        client_socket.connect((host, port))

        # Serialize the dictionary to JSON
        json_data = json.dumps(dictionary)

        # Send the JSON data
        client_socket.sendall(json_data.encode('utf-8'))

        print("Data sent successfully")

    except Exception as e:
        print(f"Client error: {e}")
    finally:
        if 'client_socket' in locals():
            client_socket.close()
