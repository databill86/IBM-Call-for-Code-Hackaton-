import json
from watson_developer_cloud import VisualRecognitionV3
import csv
import os 
import tarfile
import shutil




def zip(dirName):

	with tarfile.open( dirName + ".tgz", "w:gz" ) as tar:
		for name in os.listdir(dirName):
			tar.add(dirName)


	shutil.rmtree(dirName, ignore_errors=True)



	arch = dirName+".tgz"

	print arch # zip name


	uplo(arch)



def uplo(arch):

	credentials = {
    'IBM_API_KEY_ID': 'Your API',
    'IAM_SERVICE_ID': 'Your service ID',
    #'ENDPOINT': 'https://s3-api.us-geo.objectstorage.service.networklayer.com', # BAD
    'ENDPOINT': 'https://s3-api.us-geo.objectstorage.softlayer.net', # GOOD
    'IBM_AUTH_ENDPOINT': 'https://iam.ng.bluemix.net/oidc/token',
    'BUCKET': 'Your Bucket',
    'FILE': 'arch'
	}

	from ibm_botocore.client import Config
	import ibm_boto3

	cos = ibm_boto3.client(service_name='s3',
    	ibm_api_key_id=credentials['IBM_API_KEY_ID'],
    	ibm_service_instance_id=credentials['IAM_SERVICE_ID'],
    	ibm_auth_endpoint=credentials['IBM_AUTH_ENDPOINT'],
    	config=Config(signature_version='oauth'),
    	endpoint_url=credentials['ENDPOINT'])

	cos.upload_file(Filename=arch, Bucket=credentials['BUCKET'],Key=arch)

	print "File upload to Cloud"
	


def VisualR(ruta,dirName):

	visual_recognition = VisualRecognitionV3(
    version='2018-03-19',
    iam_apikey='Your API',
    url='https://gateway.watsonplatform.net/visual-recognition/api'
	)

	with open(ruta, 'rb') as images_file:

		classes = visual_recognition.classify(
			images_file,
			threshold='0.23',
			classifier_ids='Modelodesastres_910018447')

		Result = (classes.result['images'][0]['classifiers'][0]['classes'])


	


		file = open(str(dirName)+"/score.txt", "w")

		file.write(str(Result))
		file.close()

		zip(dirName)



path = "Data"

 
# Set the directory you want to start from
rootDir = '.'
for dirName, subdirList, fileList in os.walk(path):
    print(dirName)
    for fname in fileList:
        print('\t%s' % fname)

        if os.path.isfile(dirName+"/image1.jpeg"):

        	ruta = dirName+"/image1.jpeg"

        	VisualR(ruta,dirName)
        else:

        	pass # work in this part
 



