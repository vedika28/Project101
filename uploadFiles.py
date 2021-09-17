import dropbox,os
from dropbox.files import WriteMode

class TransferData(object):
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):        
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from,'rb') as f:
            dbx.files_upload(f.read(),file_to,mode=WriteMode("overwrite"))
        

def main():
    access_token = '8r58NdGX07kAAAAAAAAAARLv8iCWMARRc4FcEg2cm_0qDQK3IVzLuI0Aq0LpJ0-0'
    transferData = TransferData(access_token)
    
    #taking name of file from user to upload
    file_from=input("Enter file to upload: ")
    to=input("Enter name you want in dropbox: ")
    
    file_to = '/test_dropbox/'+to
    
    #Transfering data
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()
