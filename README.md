# gdoc-downloader
Download any GDrive document: HTML, Word, Excelsheet, Presentation.

This function can download any GDrive document: HTML, Word, Excelsheets, and Presentations

Google Workspace documents and corresponding export MIME types:
https://developers.google.com/drive/api/v3/ref-export-formats
			
- PDF: application/pdf
- MS PowerPoint:	application/vnd.openxmlformats-officedocument.presentationml.presentation
- Open Office presentation:	application/vnd.oasis.opendocument.presentation
- MS Excel:	application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
- MS Word document:	application/vnd.openxmlformats-officedocument.wordprocessingml.document

## How to get service-account.json:
	1- Go to https://console.cloud.google.com/apis/credentials
	2- On the top left there is a blue "create credentials" button click it and select "service account key." 
	3- Choose the service account you want, and select "JSON" as the key type.
	4- It should allow give you a json to download.