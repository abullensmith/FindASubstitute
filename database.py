import database
import cs304dbi as dbi

dsn = dbi.cache_cnf()
dbi.use('findasubstitute_db')

#sees if an entered username already exists
def usernameAvailability(conn, username):
    curs = dbi.dict_cursor(conn)
    sql = 'select * from employee where username = %s'
    vals = [username]
    curs.execute(sql, vals)
    available = curs.fetchall()
    if (len(available) == 1):
        return True #username already exists
    else:
        return False #unique username

def emailAvailability(conn, email):
    curs = dbi.dict_cursor(conn)
    sql = 'select * from employee1 where email = %s'
    vals = [email]
    curs.execute(sql, vals)
    available = curs.fetchall()
    if (len(available) == 1):
        return True #username already exists
    else:
        return False #unique username

def insertEmployee(conn, name, username, email, password):
    curs = dbi.dict_cursor(conn)
    sql = 'insert into employee1(name, username, email, password) VALUES(%s, %s, %s, %s)'
    vals = [name, username, email, password]
    curs.execute(sql, vals)
    conn.commit()

def lookupEmployee(conn, username):
    curs = dbi.dict_cursor(conn)
    sql = 'select * from employee1 where username = %s'
    vals = [username]
    curs.execute(sql, vals)
    info = curs.fetchone()
    return info

def available(conn):
    curs = dbi.dict_cursor(conn)
    curs.execute('''select coverage.request_id, coverage.req_employee, shift1.time, shift1.day, coverage.shift 
    from coverage, shift1 
    where coverage.shift = shift1.shift_id AND coverage.covered = 0''')
    info = curs.fetchall()
    return info

def lookupShift(conn, shift_id):
    curs = dbi.dict_cursor(conn)
    sql = 'select * from shift1 where shift_id = %s'
    vals = [shift_id]
    curs.execute(sql, vals)
    info = curs.fetchone()
    return info

