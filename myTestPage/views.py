from django.shortcuts import render

import sqlite3

def addInfo(_name, _age):
    con = sqlite3.connect('db.sqlite3')
    cur = con.cursor()

    cur.execute('SELECT COUNT(*) FROM myTestPage_mytestpagedb')
    numberOfRows = cur.fetchone()
    id = int(numberOfRows[0])
    id += 1

    cur.execute('INSERT INTO myTestPage_mytestpagedb VALUES (?, ?, ?)', (id, _name, _age))

    con.commit()
    con.close()


def IndexPage(_request):
    return render(_request, 'myTestPage/index.html')

def UploadInfo(_request):
    name = _request.POST.get('name')
    age = _request.POST.get('age')

    resultMessage = ''
    if not(1 < len(name) and len(name) <= 10):
        resultMessage = 'Length of name should be greater than 1 and less than or equal to 10'
    
    elif(age.isdigit() == False):
        resultMessage = 'Age should be a number'
    
    else:
        resultMessage = 'Hello ' + name + '(' + age + '). Welcome to TestPage'
        addInfo(name, age)

    return render(_request, 'myTestPage/result.html', {'result':resultMessage})