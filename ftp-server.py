import os

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# Instantiate a dummy authorizer for managing 'virtual' users
authorizer = DummyAuthorizer()

# Define a new user having full r/w permissions and a read-only
# anonymous user
authorizer.add_user('hacker', '12345', '.', perm='elradfmwMT')
authorizer.add_anonymous(os.getcwd())

 # Instantiate FTP handler clas
handler = FTPHandler
handler.authorizer = authorizer
FTPHandler.permit_foreign_addresses = True

# Define a customized banner (string returned when client connects)
handler.banner = "FTP server ready"

# Instantiate FTP server class and listen on the given IP address and port
PRIVATE_IP = "192.168.0.121"
address = (PRIVATE_IP, 1026)
server = FTPServer(address, handler)

# set a limit for connections and start the FTP server
server.max_cons = 256
server.max_cons_per_ip = 5
server.serve_forever()
