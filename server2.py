from flask import render_template, session, request, redirect, Flask
from queue import Queue
import sys, os, server_decrypt
import simplejson as json

intercepts = Queue()

if getattr(sys, "frozen", False):
    template_folder = os.path.join(sys._MEIPASS, "templates")
    application = Flask(__name__, template_folder=template_folder)
else:
    application = Flask(__name__)

# application.config['SECRET_KEY'] = os.environ['SECRET_KEY']
application.config["SECRET_KEY"] = "1023912038109823aljksdflkajds"
app = application

# intercepts.put({"intercept":"ELCSDBAJDEIHYIJGSBBNGURMSKZPLFDHJIDQRQSQNTUGHJFCXKIPAUXYFVPIYEHHIVGAE"})

@app.route("/", methods=["GET"])
def welcome():
    return render_template("index.html")


@app.route("/api/decode", methods=["POST"])
def lookup():
    req = request.form
    print(req['intercept'])
    intercepts.put(req['intercept'] )
    result = server_decrypt.solveText(req['intercept'])
    return json.dumps(result)

    # if intercepts.empty() == True:
    #     return json.dumps(False)
    # else:
    #     return json.dumps(intercepts.get())

if __name__ == "__main__":
    application.run(debug=True)
