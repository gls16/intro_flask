from flask import Flask, request, url_for, redirect, abort, render_template
app = Flask(__name__)

import mysql.connector

midb = mysql.connector.connect(
    host='localhost',
    user='outs1der',
    password='Theadminishere1',
    database='Prueva'
)

cursor = midb.cursor(dictionary= True)
    # - dictionary trus: cambia el iden de los datos y los combierte en secciones por columna
@app.route('/')
def index():
    return 'hola mundo'

# GET, POST, PUT, PATCH, DELETE
@app.route('/post/<post_id>',methods=['GET','POST'])
def lala(post_id):
    if request.method == 'GET':
        return 'El id del post es: ' + post_id
    else:
        return 'Este es el otro metodo y no es GET'

"""
@app.route('/post/<post_id>',methods=['POST'])
def lili(post_id):
    return 'El id del post es: ' + post_id
"""

@app.route('/lele',methods=['POST','GET'])
def lele():
    #base de datos
    cursor.execute('select * from Usuario')
    usuarios = cursor.fetchall()
    print(usuarios)
    # abort
    #abort(401) #abort(|# numero del error|)

    #return
    #return redirect(url_for('lala',post_id=2)) #url_for(|funcion del url|, argumento)
    
    # contrccion de url 
    #print(url_for('lala',post_id=2))  #url_for(|funcion del url|, argumento)
    
    # enviar datos de formulario  a travez de flask
    #print(request.form)
    
    # devolver datos
    #print(request.form['llave1'])
    #print(request.form['llave1'])

    # redireccionando  plantillas
    #return render_template('lele.html') #busca en la capeta templates un archivo html
    
    # devolver JSON
    #return{
    #    "username": 'Chanchito',
    #    "email" : 'chantito@das.com'
    #}   #los .json son amigables con las API rest por eso pueden ser enviados en un return

    return render_template('lele.html', usuarios=usuarios)

@app.route('/home',methods=['GET'])
def home():
    return render_template('home.html',mensaje='Hola mundo')

@app.route('/crear', methods=['GET','POST'])
def crear():
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        edad = request.form['edad']
        sql = "insert into Usuario (username, email, edad) values (%s, %s, %s)"
        values = (username, email, edad)
        cursor.execute(sql, values)
        midb.commit()

        return redirect(url_for('lele'))
    
    return render_template('crear.html')


# curl:
# Metodos http > curl -X (metodo) http://localhost:5000/
# 
# DAtos de formulario > 
# opcion |.json| :  curl -d "{|json|}" -X (metodo) http://localhost:5000/
# opcion formulario :  curl -d " llave# = dato# & -- " -X (metodo) http://localhost:5000/
