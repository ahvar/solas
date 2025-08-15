

@connect_db
def validate_user(conn, user, passwd)->bool:
    try:
        cur = conn.cursor() 
        sql = "SELECT * FROM all_user where username = '{}' and password = '{}'".format(user, passwd)
        cur.execute(sql)
        users = cur.fetchall()
        cur.close()
        if len(users) > 0:
            return True
    except Exception as e:
        print(e)
    return False