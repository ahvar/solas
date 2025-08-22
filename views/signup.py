from __main__ import app
from flask import render_template, request, Response
from model.candidates import AdminUser, CounselorUser, PatientUser
from repository.signup import select_all_signup
from urllib.parse import parse_qsl

@app.route('/signup/approve', methods=['POST'])
@app.route('/signup/approve/<int:utype>', methods=['GET'])
def signup_approve(utype:int=None):
    if (request.method == 'GET'):
        id = request.args['id']
        user = select_single_signup(id)
    else:
        utype = int(utype)
        if utype == 1:
            adm = request.get_data()
            adm_dict = dict(parse_qsl(adm.decode('utf-8')))
            adm_model = AdminUser(**adm_dict)
            user_approval_service(utype, adm_model)
        elif utype == 2:
            cnsl = request.get_data()
            cnsl_dict = dict(parse_qsl(cnsl.decode('utf-8')))
            cnsl_model = CounselorUser(**cnsl_dict)
            user_approval_service(utype, cnsl_model)
        elif utype == 3:
            pat = request.get_data()
            pat_dict = dict(parse_qsl(pat.decode('utf-8')))
            pat_model = PatientUser(**pat_dict)
            user_approval_service(utype, pat_model)
        return render_template('approved_user.html', message='approved'), 200
    
@app.route('/signup/form', methods=['GET'])
def signup_users_form():
    resp = Response( response=render_template('add_signup.html'), status=200, content_type='text/html')
    return resp

@app.route('/signup/list', methods=['GET'])
def signup_list_users():
    candidates = select_all_signup()
    return render_template('reports/list_candidates.html', records=candidates), 200 
