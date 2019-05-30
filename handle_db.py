import pymysql


def retrieve_all():
    conn = pymysql.connect(user="utente", password="piru",
                           host="localhost", database="tasklist")

    query = "select * from task order by todo"
    cursor = conn.cursor()
    cursor.execute(query)
    ris = cursor.fetchall()
    cursor.close()
    conn.close()
    tasks = []

    for row in ris:
        tasks.append({'id': row[0], 'todo': row[1], 'urgency': row[2]})

    return tasks


def insert(task, urgency):
    conn = pymysql.connect(user="utente", password="piru",
                            host="localhost", database="tasklist")

    insert_t = "insert into task(todo, urgency) values(%s, %s);"
    cursor = conn.cursor()
    cursor.execute(insert_t, (task, urgency))
    conn.commit()
    cursor.close()
    conn.close()


def retrieve_one(id):
    conn = pymysql.connect(user="utente", password="piru",
                           host="localhost", database="tasklist")

    query = "select * from task where id_task=%s order by todo"
    cursor = conn.cursor()
    cursor.execute(query, (id, ))
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    tasks = []

    tasks.append({'id': row[0], 'todo': row[1], 'urgency': row[2]})

    return tasks


def remove(id):
    conn = pymysql.connect(user="utente", password="piru",
                            host="localhost", database="tasklist")

    delete_one = "delete from task where id_task=%s;"
    print(id)
    cursor = conn.cursor()
    cursor.execute(delete_one, (id,))
    conn.commit()
    cursor.close()
    conn.close()


def update_urgency(id, urgency):
    conn = pymysql.connect(user="utente", password="piru",
                            host="localhost", database="tasklist")

    update_urg = "update task set urgency=%s where id_task=%s;"
    cursor = conn.cursor()
    cursor.execute(update_urg, (urgency, id))
    conn.commit()
    cursor.close()
    conn.close()


def update_todo(id, todo):
    conn = pymysql.connect(user="utente", password="piru",
                            host="localhost", database="tasklist")

    update_urg = "update task set todo=%s where id_task=%s;"
    cursor = conn.cursor()
    cursor.execute(update_urg, (todo, id))
    conn.commit()
    cursor.close()
    conn.close()