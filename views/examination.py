from __main__ import app
from flask import make_response, render_template, request, redirect, url_for
from services.utility import list_cid, list_pid
from repository.question_details import insert_question_details
from uuid import uuid4
@app.route('/exam/details/list')
def report_exam_list():
    exams = list_exam_details()
    response = make_response( render_template('exam/list_exams.html', exams=exams), 200)
    headers = dict()
    headers['Content-Type'] = 'application/vnd.ms-excel'
    headers['Content-Disposition'] = 'attachment;filename=questions.xls'
    response.headers = headers
    return response


@app.route('/exam/assign', methods=['GET', 'POST'])
def assign_exam():
    if request.method == 'GET':
        cids = list_cid()
        pids = list_pid()
        response = make_response(
            render_template('exam/assign_exam_form.html', pids=pids, cids=cids), 200
        )
        response.set_cookie('exam_token', str(uuid4))
        return response, 200
    else:
        id = int(request.form['id'])
        cid = request.form['cid']
        pid = int(request.form['pid'])
        exam_date = request.form['exam_date']
        duration = int(request.form['duration'])
        result = insert_question_details(id=id,cid=cid,pid=pid, exam_date=exam_date, duration=duration)
        if result:
            task_token = request.cookies.get('exam_token')
            task = 'exam assignment (task id {})'.format(task_token)
            return redirect(url_for('redirect_success_exam', message=task))
        else:
            return redirect('/exam/task/error')
        
@app.route('/exam/success', methods=['GET'])
def redirect_success_exam():
    message = request.args['message']
    return render_template('exam/redirect_success_view.html', message=message)