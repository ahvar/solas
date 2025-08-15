from __main__ import app
from flask import make_response, render_template
@app.route('/exam/details/list')
def report_exam_list():
    exams = list_exam_details()
    response = make_response( render_template('exam/list_exams.html', exams=exams), 200)
    headers = dict()
    headers['Content-Type'] = 'application/vnd.ms-excel'
    headers['Content-Disposition'] = 'attachment;filename=questions.xls'
    response.headers = headers
    return response