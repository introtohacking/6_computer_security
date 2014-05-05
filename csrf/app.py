import datetime
from flask import Flask, request, session, render_template, make_response
app = Flask(__name__)

@app.route("/reset")
def reset():

    if 'transactions' in session:
        del session['transactions']

    return "Session reset complete"


@app.route("/")
def hello():

    # create the transactions cookie if it doesn't exist already
    if 'transactions' in session:
        transactions = session['transactions']
    else:
        transactions = [
                (datetime.datetime.strptime("2014 04 22","%Y %m %d"),"DEPOSIT", 500.0),
                (datetime.datetime.strptime("2014 04 27","%Y %m %d"),"WITHDRAW", 20.0),
                (datetime.datetime.strptime("2014 05 01","%Y %m %d"),"DEPOSIT", 37.0),
                ]

    if 'amount' in request.args:
        transactions.append((datetime.datetime.now(), request.args['type'], request.args['amount']))

    session['transactions'] = transactions

    return render_template('index.html', transactions=transactions)

if __name__ == "__main__":
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.run(debug=True)