from __main__ import app
from flask import render_template, request
from model.candidates import AdminUser, CounselorUser, PatientUser
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
