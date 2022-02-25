import io
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/drive']

def download_gdrive_doc(file_id, dest_file):
	try:
		'''
		How to get service-account.json:
			1- Go to https://console.cloud.google.com/apis/credentials
			2- On the top left there is a blue "create credentials" button click it and select "service account key." 
			3- Choose the service account you want, and select "JSON" as the key type.
			4- It should allow give you a json to download.
		'''

		PASS_CREDENTIALS = service_account.Credentials.from_service_account_file('service-account.json')
		service = build('drive', 'v3', credentials=PASS_CREDENTIALS)
		
		'''
		This function can download any GDrive document: HTML, Word, Excelsheets, and Presentations
		Google Workspace documents and corresponding export MIME types:
			https://developers.google.com/drive/api/v3/ref-export-formats
			
			PDF: application/pdf
			MS PowerPoint:	application/vnd.openxmlformats-officedocument.presentationml.presentation
			Open Office presentation:	application/vnd.oasis.opendocument.presentation
		'''
		request = service.files().export_media(fileId=file_id, mimeType='application/pdf')
		
		fh = io.BytesIO()
		downloader = MediaIoBaseDownload(fd=fh, request=request)
		done = False
		while done is False:
			status, done = downloader.next_chunk()
			print("Download {percent}%".format(percent=int(status.progress() * 100)))

		fh.seek(0)
		
		with open(dest_file, 'wb') as f:
			f.write(fh.read())
			f.close()
		
		print('Presentation downloaded successfully!')

	except HttpError as error:
		print('An error occurred: {error}'.format(error=error))

file_id = '1lRuc_70GJ5iT7A26_MRMgfwEYjRIO5mGpykjtycE6Pw'
dest_file = 'test.pdf'
download_gdrive_doc(file_id, dest_file)