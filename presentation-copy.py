
import io
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload
from google.oauth2 import service_account
# Install API lib:
# pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

SCOPES = ['https://www.googleapis.com/auth/drive']
PASS_CREDENTIALS = service_account.Credentials.from_service_account_file('service-account.json')
service = build('drive', 'v3', credentials=PASS_CREDENTIALS)

def get_info(file_id):
	try:
		res = service.files().get(fileId=file_id).execute()	
		print(res)

	except HttpError as error:
		print('An error occurred: {error}'.format(error=error))



def copy_presetnation(file_id, dest_folder_id):
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
        
        Drive API:
            files API: 	https://developers.google.com/drive/api/v3/reference/files/copy
						https://developers.google.com/resources/api-libraries/documentation/drive/v2/python/latest/drive_v2.files.html
						https://www.youtube.com/watch?v=q2RQ8DXYzrE

            All:		https://developers.google.com/drive/api/v3/reference
		'''

		service.files().copy(fileId=file_id, body={"parents": ['ParentFolderID'], 'name': 'NewFileName'} ).execute()	

	except HttpError as error:
		print('An error occurred: {error}'.format(error=error))



file_id = '1eTE9rkbCFpghSW28OC_Ud4eD-jtub527JTaj9S7GhUU'
dest_path = '1Egwlos9M4mU4nHwx3XRhoyhPTpL51kos'  # gdrive/.../v2.5-Curriculum/1-Lesson-Plans/01-cybersecurity-101/1
#dest_path = '1MCUdrpJdwuKihhOGKta9VI-F99MQY6xn'  # gdrive/.../v2.5-Curriculum/1-Lesson-Plans
#copy_presetnation(file_id, dest_path)
get_info(file_id)
