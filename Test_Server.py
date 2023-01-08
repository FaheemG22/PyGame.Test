import socket

print(socket.gethostbyname(socket.gethostname()))

def serv():
    HOST = "127.0.0.1"                                                                                                  # Standard loopback interface address (localhost)
    PORT = 65432                                                                                                        # Port to listen on (non-privileged ports are > 1023)
    colour = ['unique', 'red', 'amber', 'green', 'leave']
    all_colour = []                                                                                                     # creates list for the client to chose from and record their options
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:                                                    # does some sort of divine magic that I have no clue about
            s.bind((HOST, PORT))
            s.listen()
            conn, addr = s.accept()                                                                                     # this listens and searches for connections to this specific port and accepts it
            with conn:
                print(f"-=Connected by {addr}")                                                                         # reads out the address it was connected by

                choice = conn.recv(1024)                                                                                # receives a bit of data ie 0s 1s
                conn.close()
                chosen = int(choice.decode().strip("b"))

serv()
