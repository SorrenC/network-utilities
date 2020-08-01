# Author: Sorren Chandra
# Date: 08/01/2020
# Function: Create's a group of simple network functions

import socket

class network_util():

    def __init__(self,targetip):
        
        self.targetip = targetip 

    def pscan(self,x,y): # Local port scan
        
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        for port in range(x,y):
            response = sock.connect((self.targetip,port))
            if response == 0:
                print("OPEN:",port)
            else:
                print("CLOSED",port)
