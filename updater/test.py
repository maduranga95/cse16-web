import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use the application default credentials
cred = credentials.Certificate('serviceAccount.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

# students_ref = db.collection(u'students')
# modules_ref = db.collection(u'modules').order_by(u'semester')

student_ref = db.collection(u'students').document(u'haritha@cse.mrt.ac.lk')
student_doc = student_ref.get()
student = student_doc.to_dict()

data = {
    u'cgpa': student['cgpa'],
    u'crank': student['crank'],
    u'email': u'haritha.16@cse.mrt.ac.lk',
    u'field': student['field'],
    u'id': student['id'],
    u'mobile': student['mobile'],
    u'name': student['name'],
    u'results': student['results'],
    u'sgpa': student['sgpa'],
    u'srank': student['srank'],
}
print(data)
db.collection(u'students').document(u'haritha.16@cse.mrt.ac.lk').set(data)
