import smtplib
from flask import Flask, jsonify, request
from random import *
from flask_cors import CORS

app = Flask(__name__,
            static_folder = "./dist/static",
            template_folder = "./dist")
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})



@app.route('/api/submitToken', methods=('POST',))
def submitCoinToken():
    #Bitcoin stuff
    pass


@app.route('/api/getData', methods=('POST',))
def getdata():
    request_dict = request.get_json()
    if(request_dict['name']=='tylerquast'):
        returnData = getTylerData()
    elif(request_dict['name']=='rileymiller'):
        returnData = getRileyData()
    else:
        print('Name not found')
        returnData = {}
    return jsonify(returnData)
    

@app.route('/api/random', methods=('POST',))
def random_number():
    request_dict = request.get_json()


    gmail_user = 'tylerquast68@gmail.com'  
    gmail_password = '5635Quast'

    sent_from = gmail_user  
    to = ['tylerquast68@gmail.com', 'tylerquast@mymail.mines.edu']  
    subject = 'Accedemic Certificate'  
    body = 'Hi, ' + request_dict['Name'] + '\n\nThank you for requesting your accedemic certificate. Please follow the link below to complete your request\n\n\n\n http://localhost:8080/process?name='+ request_dict['Name']

    email_text = """  
    From: %s  
    To: %s  
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:  
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print ('Email sent!')
    except:  
        print ('Something went wrong...')




    response = {
        'randomNumber': randint(1, 100)
    }
    return jsonify(response)



@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")


def getTylerData():
    return {
            'Name': 'Tyler Quast',
            'email': 'tylerquast68@gmail.com',
            'Degree': 'Computer Science',
            'University': 'Colorado School of Mines',
            'GPA': '3.2',
            'Standing': 'Great',
            'Gender': 'Male',
            'Graudation Year': '2019',
            'Enrollment Start': '2015'
           }

def getRileyData():
    return {
            'Name': 'Tyler Quast',
            'email': 'tylerquast68@gmail.com',
            'Degree': 'Computer Science',
            'University': 'Colorado School of Mines',
            'GPA': '3.2',
            'Standing': 'Great',
            'Gender': 'Male',
            'Graudation Year': '2019',
            'Enrollment Start': '2015'
           }
