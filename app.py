from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():

    return """

<h1>CI/CD Pipeline Working!</h1>

<h2>Application deployed automatically using Jenkins.</h2>
<h3> Very basic level of CICD with docker+Jenkins!</h3>

"""

app.run(host="0.0.0.0",port=5000)
