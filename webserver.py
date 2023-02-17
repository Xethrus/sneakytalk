from flask import Flask, request, render_template

app = Flask(__name__)

# dictionary to store messages
messages = {}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send():
    sender = request.form["sender"]
    recipient = request.form["recipient"]
    message = request.form["message"]
    
    # check if recipient exists
    if recipient not in messages:
        messages[recipient] = []
    
    # add message to recipient's inbox
    messages[recipient].append((sender, message))
    
    return "Message sent successfully!"

@app.route("/inbox", methods=["GET"])
def inbox():
    recipient = request.args.get("recipient")
    
    # check if recipient exists
    if recipient not in messages:
        messages[recipient] = []
    
    return render_template("inbox.html", recipient=recipient, messages=messages[recipient])

if __name__ == "__main__":
    app.run(debug=True)

