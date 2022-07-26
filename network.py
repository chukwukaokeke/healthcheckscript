#!/usr/bin/env python3

import requests
import socket



def check_localhost():
        localhost = socket.gethostbyname('localhost')
        return localhost == "127.0.0.1"

def check_connectivity():
        r = requests.get("http://www.google.com")
        return r.status_code == 200 
        

