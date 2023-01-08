import socket
from options import p1,p2

HOST="127.0.0.1"
PORT=65432

def server(choice):                                                                                                     #The function called when clicking the button
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:                                                    # don't fully understand this line
            print(f"-=Connected to {HOST} ({PORT})")                                                                    # just displays in command line if successfully connected
            s.connect((HOST, PORT))                                                                                     # connects to port
            s.sendall(choice.encode())                                                                                  # Sends encoded data ie 0s and 1s depending on what button clicked
            s.close()                                                                                                   # updates app logo
    except Exception as e:
        print(e)

server('10')

