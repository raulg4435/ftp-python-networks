# import FP class, which implements client side of FTP
from ftplib import FTP

IP = '67.48.137.212'

# connect to server and login
ftp = FTP('')
ftp.connect(IP, 1026)                       # connect to host, port
#ftp.login()                                # login (anonymous)
ftp.login(user='hacker', passwd='12345')    # login with full access
ftp.cwd('books')                            # change working directory
ftp.retrlines('LIST')                       # FTP command to list directory contents

def uploadFile():
    filename = 'hunger_games.txt'
    # store file in binary transfer mode, opening in 'rb' mode: "read-binary"
    ftp.storbinary('STOR '+ filename, open(filename, 'rb')) 
    ftp.quit()

def downloadFile():
    filename = 'odyssey.txt'
    localfile = open(filename, 'wb')                            # open in 'wb' mode: "write-binary"
    ftp.retrbinary('RETR ' + filename, localfile.write, 1024)   # retrieve file, use port
    ftp.quit()
    localfile.close()

# Un-comment the function you'd like to execute
#uploadFile()
downloadFile()
