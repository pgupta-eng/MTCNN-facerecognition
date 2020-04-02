from fire import firebase

firebase = firebase.FirebaseApplication('https://collapp-2605.firebaseio.com', None)

while True:

    #rollno =(input('Enter no here...'))
    teacher=input('Enter teacher here...')
    #ACLASS = input('Enter attended classes here...')
    #date = input('Enter date here...')
    LAST_ATT = firebase.get('/Attendance' + teacher, None)
    data = {
        'rollno': rollno
    }

    #result = firebase.post('Attendance',{'gjh':data})

    resultput = firebase.put('Attendance'+teacher,rollno,{"teacher":teacher,'total class':'26','attended classes':ACLASS,'last class':date})

    print(LAST_ATT)
    print(resultput)
