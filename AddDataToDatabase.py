import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceattendacerealtime-aab78-default-rtdb.firebaseio.com/"
})
ref = db.reference('Students')

data = {
    "852741":
        {
            "name": "Emly Blunt",
            "major": "Economics",
            "starting_year": 2024,
            "total_attendance": 12,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2024-01-01 00:05:00"
        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2024,
            "total_attendance": 0,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2024-01-01 00:05:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)