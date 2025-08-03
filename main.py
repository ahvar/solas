from flask import Flask
app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    return "Solas is an personal online counseling system (POCS)"


@app.route('/introduction')
@app.route('/information')
@app.route('/home')
def home():
    return '''
        <html>
            <head><title>Solas - An Online Personal Counseling System</title></head>
            <body>
                <h1>Solas</h1>
                <p>This is a template of a web-based counseling application where counselors can....</em>
            </body>
        </html>


'''




if __name__ == "__main__":
    app.run(debug=True)