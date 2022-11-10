from array import *
import sqlite3
from flask import Flask, render_template


app = Flask(__name__)
con = sqlite3.connect("sitio.db", check_same_thread=False)
cursor = con.cursor()

# Un ejemplo es probar con endpoint /proyecto/Anapoima


@app.route('/proyecto/<id_proyecto>')
def consultarProyectos(id_proyecto):
    print("id proyecto", id_proyecto)
    param = [(id_proyecto)]
    res = cursor.execute(
        "SELECT * FROM project WHERE project_name=?", param)
    data = res.fetchall()
    proyectos = list(data)

    #
    res = cursor.execute(
        "SELECT * FROM user JOIN user_role_association_table AS urat ON user.id=urat.user_id JOIN role ON role.id=urat.role_id")
    data = res.fetchall()
    usuarios = list(data)

    query = {
        "projects": proyectos,
        "users": usuarios
    }
    # nombre del proyecto
    name = query['projects'][0][len(query['projects'][0])-2]
    return render_template('index.html', **query, name=name)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
