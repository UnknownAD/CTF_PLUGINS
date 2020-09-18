print("""
d888888b d8b   db d8888b. d88888b db    db 
  `88'   888o  88 88  `8D 88'     `8b  d8' 
   88    88V8o 88 88   88 88ooooo  `8bd8'  
   88    88 V8o88 88   88 88~~~~~  .dPYb.  
  .88.   88  V888 88  .8D 88.     .8P  Y8. 
Y888888P VP   V8P Y8888D' Y88888P YP    YP 
                                           
                                           
.88b  d88.  .d8b.   d888b  d8b   db d888888b d88888b db    db 
88'YbdP`88 d8' `8b 88' Y8b 888o  88   `88'   88'     `8b  d8' 
88  88  88 88ooo88 88      88V8o 88    88    88ooo    `8bd8'  
88  88  88 88~~~88 88  ooo 88 V8o88    88    88~~~      88    
88  88  88 88   88 88. ~8~ 88  V888   .88.   88         88    
YP  YP  YP YP   YP  Y888P  VP   V8P Y888888P YP         YP    
                                                    By : UnknownAD -_-
                           
""")
import socket
class socks:
    def __init__(self,host,index):
         self.host=host
         self.client=socket.socket()
         self.index=index
    def bruteforce(self):
         self.client.connect((self.host,80))
         self.r="GET "+self.index+" HTTP/1.1\r\nHost: "+self.host+"\r\n\r\n"
         self.client.send(bytes(self.r,"utf-8"))
         if self.client.recv(1024).decode("utf-8").split("\r\n")[0]=="HTTP/1.1 200 OK":
             return f"\033[1;31;40m [+] Found : {self.index} \033[0m 1;31;40m"
         else:
             return f"[+] Failed : {self.index}"
requirements=__import__('sys').argv
print(requirements)
indexlist=open(requirements[2],'r')
host=requirements[1]
print("[+] Start Bruteforcing...")
for x in indexlist.read().split('\n'):    
    Myobject=socks(host,x)
    print(Myobject.bruteforce())
