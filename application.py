from flask import render_template, session, request, redirect, Flask
from queue import Queue
import sys, os, encrypt
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

def clean_text(text):
    regex = re.compile("[^a-zA-Z]")
    punc_free = regex.sub("", text)
    space_free = punc_free.replace(" ", "")
    return space_free.upper()

@app.route("/", methods=["GET"])
def welcome():
    if request.method == "POST":
        req = request.form
        print(req)
        result = iexStocks.getFinancials(req["symbol"].upper(), req["pe"])
        print(result)
        session["result"] = result
        return render_template("index.html")
    else:
        return render_template("index.html")


@app.route("/encode", methods=["POST"])
def result():
    req = request.form
    print(req)
    rotors = f"{req['r1']} {req['r2']} {req['r3']}"
    result = encrypt.encryptMessage(f"Sept Fourth {req['text']}", rotors)
    intercepts.put({"intercept": result, "plaintext":clean_text(f"Sept Fourth {req['text']}")})
    # encrypt.encryptMessage()
    # result = "test"

    print(rotors)
    print(result)
    return render_template(
        "encode.html", result=result, submitted=f"Sept Fourth {req['text']}"
    )


@app.route("/api/get-message", methods=["get"])
def lookup():
    if intercepts.empty() == True:
        return json.dumps(False)
    else:
        return json.dumps(intercepts.get())


if __name__ == "__main__":
    application.run(debug=True)
