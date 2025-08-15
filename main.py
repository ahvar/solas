
from flask import Flask, render_template
from datetime import datetime
from datetime import date
from converter.date_converter import DateConverter
from views.certificates import show_honor_dissmisal
from views import ListUnpaidContractView
app = Flask(__name__)
app.url_map.converters['date'] = DateConverter
app.add_url_rule('/certificate/terminate/<string:counselor>/<date:effective_date>/<string:patient>', 'show_honor_dismissal', show_honor_dissmisal)
app.add_url_rule('/contract/unpaid/patients', view_func=ListUnpaidContractView.as_view('list-unpaid-view'))

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

@app.route('/exam/passers/list/<float:rate>/<uuid:doc>')
def report_exam_passers(rating: float, doc_id:uuid4=None):
    exams = list_passing_scores(rating)
    response = make_response(
        render_template('exam/list_exam_passers.html', exams=exams, doc_id=doc_id), 200
    )
    return response

@app.route('/certificate/accomp/<string:name>/<string:course>/<date:accomplished_date>')
def show_certificate(name:str, course:str, accomplished_date:date):
    certificate = """
        <html><head><title>Certificate of Accomplishment</title></head>
            <body>
                <h1>Certificate of Accomplishment</h1>
                <p>The participant {} is, hereby awarded this certificate of accomplishment,
                in {} course on {} date for passing all exams. He/she proved to be ready for
                any of his/her future endeavors.</em>
            </body>
        </html>
    """.format(name, course, accomplished_date)


if __name__ == "__main__":
    app.run(debug=True)