from ftplib import FTP_TLS

def init_connection():
    ftps = FTP_TLS('ftp.site.com') # connect to host
    # login after securing control channel
    ftps.login('username', 'password') # 230 Anonymous user logged in
    # switch to secure data connection.. 
    # IMPORTANT! Otherwise, only the user and password is encrypted and
    # not all the file data.
    ftps.prot_p() # 200 Data protection level set to "private"
    return ftps

def change_working_directory(ftps, directory_name):
    response_message = ftps.cwd(directory_name) # change directory
    print(response_message)

def store_file(ftps, filename):
    # get binary file from Server
    '''filename = 'remote_filename.bin'
    print 'Opening local file ' + filename
    with open(filename, 'wb') as myfile:
        ftps.retrbinary('RETR %s' % filename, myfile.write)
    '''

    # write file to Server
    #filename = "testfiletosend.txt"
    file_object = open(filename, "rb") # rb read binary
    ftp_command = "STOR %s"%filename

    response_message = ftps.storbinary(ftp_command, fp=file_object)
    print(response_message)


def close_connection(ftps):
    ftps.close()

def print_files_from_current_dir(ftps):
    ftps.retrlines('LIST') # print file or directory listing (alternative: print(ftps.nlst()))

if __name__ == "__main__":
    try:
        ftp_object = init_connection()
        filename = "testfiletosend.txt"
        change_working_directory(ftp_object, 'content')
        #print_files_from_current_dir(ftp_object)
        store_file(ftp_object, filename)
    except:
        (type, value, traceback) = sys.exc_info()
        print("Type: ", type)
        print("Value: ", value)
        print("traceback: ", traceback)
    finally:
        close_connection(ftp_object)