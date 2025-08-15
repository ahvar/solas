from __main__ import app
from flask import render_template, request, Response

@app.route('/admin/users/list')
def generate_admin_users():
    users = select_admin_join_user()
    user_list = [list(rec) for rec in users]
    content = '''
        <html>
          <head>
            <title>User List</title>
          </head>
          <body>
            <h1>List of Users</h1>
            <p>{}
          </body>
        </html>
    '''.format(user_list)
    resp = Response(response=content, status=200, content_type='text/html')
    return resp
