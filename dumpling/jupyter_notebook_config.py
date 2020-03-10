import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# TODO: change IP
s.connect(('8.8.8.8', 1))
local_ip = s.getsockname()[0]

c.NotebookApp.ip = local_ip
c.NotebookApp.open_browser = False
