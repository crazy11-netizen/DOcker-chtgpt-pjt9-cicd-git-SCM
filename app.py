from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():

    return """

<h1>CI/CD Pipeline Working!</h1>

<h2>Application deployed automatically using Jenkins.</h2>
<h3> Very basic level of CICD with docker+Jenkins!</h3>
<h3> added github webhook as jenkins website-current-ec2, whenever changes are done in git jenkins will start and the finished images are sent to dockerhub via docker credentials added in jenkins credentials" </h3>

<h2> relax relax</h2>

"""

app.run(host="0.0.0.0",port=5000)
