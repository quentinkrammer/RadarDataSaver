from datetime import datetime
import socket
import collections

# def writeToFile(txt):
#     f = open(filename, "a")
#     f.write(txt)
#     f.close()    
#
filename = datetime.now()
filename = filename.replace(microsecond=0)
filename = str(filename)
filename = filename.replace(":", "-")
filename = filename.replace(" ", "_")
filename = filename+".txt"
f = open(filename, "w")
f.close()

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 13377   

print("data dump active...: ")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while(True):
        #data = s.recv(int(2**10))
        deque = collections.deque([], 6)
        data = ""
        while True:
            char = s.recv(1).decode()            
            data += char
            deque.append(char)
            terminator = str().join(deque)            
            if terminator == "</DGM>":
                break
        timestamp = str(datetime.now())
        with open(filename, "a") as f:
            f.write(timestamp+"\n")
            f.write(data)            
        
#         writeToFile(timestamp+"\n")
#         writeToFile(data.decode())