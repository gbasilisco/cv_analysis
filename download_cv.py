from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload
import shutil

import io

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive']


def main():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token_.json'):
        creds = Credentials.from_authorized_user_file('token_.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret_560342406312-8i0tv3kojidffep9sgioshchsdd7rs17_.apps.googleusercontent.com.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token_.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('drive', 'v3', credentials=creds)

        # ID della cartella da cui vuoi scaricare i file
        folder_id = '1YTdWcHYNZoX21ta4o7TsEkmuCf8zc6-B'

        # Ottieni la lista dei file nella cartella
        results = service.files().list(supportsAllDrives=True, includeItemsFromAllDrives=True, q=f"'{folder_id}' in parents",
                                   fields='files(id, name)').execute()
        
        #results = service.files().list(
        #    pageSize=10, fields="nextPageToken, files(id, name)").execute()
        
        #results = service.files().list(q="'" + folder_id + "' in parents", pageSize=1000, fields="nextPageToken, files(id, name)").execute()

        #print(results)
        files = results.get('files', [])

        folder_path = "CV/"

        # Loop attraverso i file nella cartella e cancellali
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f'Errore durante la cancellazione di {file_path}: {e}')

        print("Cancellazione completata.")


        # Loop attraverso i file e scaricali
        for file in files:
            file_id = file['id']
            file_name = file['name']
            print(file_name)
            
            # Apri un flusso di output per il file locale
            local_file = open(folder_path + file_name, 'wb')
            
            # Crea una richiesta per il download del file
            request = service.files().get_media(fileId=file_id)
            
            # Esegui il download del contenuto del file
            downloader = MediaIoBaseDownload(local_file, request)
            
            done = False
            while not done:
                status, done = downloader.next_chunk()
            
            # Chiudi il file locale
            local_file.close()

        print("Download completato.")

        
    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f'An error occurred: {error}')


if __name__ == '__main__':
    main()