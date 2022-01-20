import dropbox
import os

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
    
    def upload_files(self, file_from, file_to):
        for root, dirs, files in os.walk(file_from):
            relative_path = os.path.relpath(local_path, file_from)
            dropbox_path = os.path.join(file_to, relative_path)

        with open(local_path, 'rb') as f:
            dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))








def main():
    access_token = "sl.BAepo2ZglFcHKRlg_5AKhd3iV1cXKd0WPDz4bq_hNcdePI1N2JCX_HbKKq2lgA-eP7kJOWzI1hqYYmwB3NZJmAjLsdiFH1Lyx-Ub7odreEQ5wQNf3BBNs6GPW6hP9Q_PLkFhrpI"
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer:- ")
    file_to = input("Enter the full path to upload to dropbox:- ")
    transferData.upload_files(file_from, file_to)
    print("File has been successfully uploaded.")







main()