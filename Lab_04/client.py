"""client_start.py
   start script to create send message to a listening server socket
   Owen Lo Nov 2016; expanded Gaye Cleary Nov 2017
   PEP8 Nov 2018; function annotations & pylint Feb 2021

   For documentation on socket library, see....
   https://docs.python.org/3/library/socket.html
"""
import socket

BUFFER_SIZE = 1024  # Packet size, 1024 is standard


def client_socket(tcp_ip: str, tcp_port: int) -> None:
    """create_client socket, send message and close"""
    # enter your code here to....
    # 1) create a local socket and
    # 2) connect it to the server socket
    print(f"#<INFO> Connected to server {tcp_ip}:{tcp_port}")
    message = input("Enter a message to send to the server: ")
    # enter your code here to....
    # 3) encode the message and send to the server
    # 4) receive and decode the server's reply
    decoded_data = ''
    print(f"#<INFO> Reply Received: {decoded_data}")

    # 5) remember to close the socket unless you've used with


def main():
    """ runs if script is run.
        Calls client_socket function with test parameters"""
    tcp_ip = "127.0.0.1"  # IP address of server to connect to
    tcp_port = 5005     # Port of server to connect to
    client_socket(tcp_ip, int(tcp_port))

    print("#<INFO> exiting...")


if __name__ == "__main__":
    main()
