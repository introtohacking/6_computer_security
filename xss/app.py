import datetime
from flask import Flask, request, session, render_template, make_response
app = Flask(__name__)

@app.route("/reset")
def reset():

    if 'entries' in session:
        del session['entries']

    return "Session reset complete"


@app.route("/", methods=["GET","POST"])
def hello():

    # create the entries cookie if it doesn't exist already
    if 'entries' in session:
        entries = session['entries']
    else:
        entries = [
                (datetime.datetime.strptime("2014 04 22","%Y %m %d"),"You're awesome, keep up this web site"),
                (datetime.datetime.strptime("2014 04 27","%Y %m %d"),"Free the whales"),
                (datetime.datetime.strptime("2014 05 01","%Y %m %d"),"Hey! I love this web site. Can you give me a call sometime? 8675309"),
                ]

    if request.method == "POST":
        entries.append((datetime.datetime.now(), request.form['submission-content']))

    session['entries'] = entries

    return render_template('index.html', entries=entries)

if __name__ == "__main__":
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.run(debug=True)