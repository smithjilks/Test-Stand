from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def uploadToDrive(filename):
    gauth = GoogleAuth() 
    gauth.LocalWebserverAuth()          
    drive = GoogleDrive(gauth)  

    gfile = drive.CreateFile({'parents': [{'id': '1YVdiiRn29I9b-xMm9GWAKmapi-gn7jY9'}]})
    # Read file and set it as the content of this instance.
    gfile.SetContentFile(filename)
    gfile.Upload() # Upload the file.
