from firebase import firebase


firebase = firebase.FirebaseApplication("https://pythondbtest-f7d3d.firebaseio.com/",None)
data = {
    'Name': 'Prerna Gupta',
    'Email' : 'prernaajigupta@gmail.com',
    'contact number': 6353420534,

}

result = firebase.post('pythondbtest-f7d3d/student',data)
print(result)