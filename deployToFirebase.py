

import firebase_admin

cred_obj = firebase_admin.credentials.Certificate('key.json')
default_app = firebase_admin.initialize_app(cred_obj, {
	'databaseURL': "https://tech-hub-org-default-rtdb.firebaseio.com",
	})
from firebase_admin import db

ref = db.reference("/")




import json
with open("data.json", "r") as f:
	file_contents = json.load(f)

ref.set(file_contents)
