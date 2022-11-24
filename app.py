# Download the helper library from https://www.twilio.com/docs/python/install
import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from twilio.rest import Client


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


# Define Verify_otp() function
@app.route('/login' , methods=['POST'])
def verify_otp():
    username = request.form['username']
    password = request.form['password']
    mobile_number = request.form['number']

    if username == 'verify' and password == '12345':   
        account_sid = 'AC1f7d7d782260ae0c57deb7b3a8e81255'
        auth_token = '5f7e373a1873fb06948b51fc9a5a205f'
        client = Client(account_sid, auth_token)

        verification = client.verify \
            .services('VAe5789b88fdc8eb399946d078ca47ae70') \
            .verifications \
            .create(to="+91"+mobile_number, channel='sms')

        print(verification.status)
        return render_template('otp_verify.html')
    else:
        return render_template('user_error.html')



@app.route('/otp', methods=['POST'])
def get_otp():
    print('processing')

    received_otp = request.form['recieved_otp']
    mobile_number = request.form['number']

    account_sid = 'AC1f7d7d782260ae0c57deb7b3a8e81255'
    auth_token = '5f7e373a1873fb06948b51fc9a5a205f'
    client = Client(account_sid, auth_token)
                                            
    verification_check = client.verify \
        .services('VAe5789b88fdc8eb399946d078ca47ae70') \
        .verification_checks \
        .create(to="+91"+mobile_number, code=received_otp)
    print(verification_check.status)

    if verification_check.status == "pending":
        return render_template("otp_error.html")    # Write code here
    else:
        return redirect("https://collaborative-notepad.herokuapp.com/")


if __name__ == "__main__":
    app.run()

