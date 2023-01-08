
import socket
print(socket.gethostbyname(socket.gethostname()))

def server():                                                                                                     
    HOST = socket.gethostbyname(socket.gethostname())
    PORT = 3730
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()  # this listens and searches for connections to this specific port and accepts it
        with conn:
            s.sendall(str([1,5]).encode())
            s.close()

server()

"""
def serv():
    HOST = "127.0.0.1"                                                                                                  # Standard loopback interface address (localhost)
    PORT = 65432                                                                                                        # Port to listen on (non-privileged ports are > 1023)
    colour = ['unique', 'red', 'amber', 'green', 'leave']
    all_colour = []                                                                                                     # creates list for the client to chose from and record their options
    try:
        while True:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:                                                # does some sort of divine magic that I have no clue about
                s.bind((HOST, PORT))
                s.listen()
                conn, addr = s.accept()                                                                                 # this listens and searches for connections to this specific port and accepts it
                with conn:
                    print(f"-=Connected by {addr}")                                                                     # reads out the address it was connected by

                    choice = conn.recv(1024)                                                                            # receives a bit of data ie 0s 1s
                    conn.close()
                    chosen = int(
                        choice.decode())                                                                                # this decodes the 0s and 1s into a string then gets turned into an integer

                    selected = (colour[chosen]).strip("b")                                                              # this checks what they chose
                                                                                                                        # this records their option
    except Exception as e:
        print(e)
"""
