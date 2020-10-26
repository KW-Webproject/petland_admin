import mariadb
from flask import request


def get_conn():
    conn = mariadb.connect(user="root",
                           password="000000",
                           host="193.123.233.236",
                           port=3306,
                           database="testPetland")
    return conn


def show_res():
    result = ""
    sql = get_sql()
    try:
        conn = get_conn()
        cur = conn.cursor()

        if sql[:6] == 'DELETE':
            cur.execute(sql)
            conn.commit()

        sql_all = sql
        cur.execute(sql_all)
        for r_num, u_name, r_date, r_time, pet, service, r_p_id in cur:
            result += "<tr>"
            result += "<td>" + str(r_num) + "</td>"
            result += "<td>" + u_name + "</td>"
            result += "<td>" + str(r_date) + "</td>"
            result += "<td>" + r_time + "</td>"
            result += "<td>" + pet + "</td>"
            result += "<td>" + service + "</td>"
            result += "<td>" + str(r_p_id) + "</td>"
            result += """<td><a href="/form?cmd=delete&r_num={}">삭제</a></td>""".format(
                str(r_num))
            result += "</tr>"

        # print(result)
    except mariadb.Error as e:
        print("ERR: {}".format(e))
    finally:
        if conn:
            conn.close()
    return result


def show_cus():
    result = ""
    sql = "SELECT * FROM user_info"
    try:
        conn = get_conn()
        cur = conn.cursor()

        cur.execute(sql)
        for u_id, u_name, u_phone, u_address in cur:
            result += "<tr>"
            result += "<td>" + str(u_id) + "</td>"
            result += "<td>" + u_name + "</td>"
            result += "<td>" + u_phone + "</td>"
            result += "<td>" + u_address + "</td>"
            result += """<td><a href="/customer?cmd=delete&u_id={}">삭제</a></td>""".format(
                str(u_id))
            result += "</tr>"
    except mariadb.Error as e:
        print("ERR: {}".format(e))
    finally:
        if conn:
            conn.close()
    return result


def show_staff():
    result = ""
    sql = "SELECT * FROM pet_sitter"
    try:
        conn = get_conn()
        cur = conn.cursor()

        cur.execute(sql)
        for p_id, p_name, p_phone, p_local in cur:
            result += "<tr>"
            result += "<td>" + str(p_id) + "</td>"
            result += "<td>" + p_name + "</td>"
            result += "<td>" + p_phone + "</td>"
            result += "<td>" + p_local + "</td>"
            result += """<td><a href="/staff?cmd=delete&p_id={}">삭제</a></td>""".format(
                str(p_id))
            result += "</tr>"
        # print(result)
    except mariadb.Error as e:
        print("ERR: {}".format(e))
    finally:
        if conn:
            conn.close()
    return result


def get_sql():
    cmd = request.args.get('cmd')

    if cmd == 'delete':
        r_num = request.args.get('r_num')
        sql = """DELETE FROM reservation WHERE r_num={}
        """.format(int(r_num))
    elif cmd == 'search':
        name = request.args.get('name')
        sql = """SELECT r.r_num, u.u_name, r.r_date, r.r_time, r.pet, r.service, r.r_p_id 
            FROM testPetland.reservation r
            LEFT JOIN testPetland.user_info u ON u.u_id = r.r_u_id
            WHERE u.u_name="{}"
        """.format(name)
    else:
        sql = """SELECT r.r_num, u.u_name, r.r_date, r.r_time, r.pet, r.service, r.r_p_id 
        FROM reservation r
        LEFT JOIN user_info u ON u.u_id = r.r_u_id
        ORDER BY r.r_num
    """

    return sql
