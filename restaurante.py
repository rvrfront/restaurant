''' Crea un pequeño sistema para gestionar los platos del menú de un restaurante.
Por ahora debes empezar creando un script llamado restaurante.py y dentro una función crear_bd()
que creará una pequeña base de datos restaurante.db con las siguientes dos tablas:

CREATE TABLE categoria(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(100) UNIQUE NOT NULL)

CREATE TABLE plato(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(100) UNIQUE NOT NULL,
                categoria_id INTEGER NOT NULL,
                FOREIGN KEY(categoria_id) REFERENCES categoria(id))

Nota: La línea FOREIGN KEY(categoria_id) REFERENCES categoria(id) indica un tipo de clave especial (foránea),
por la cual se crea una relación entre la categoría de un plato con el registro de categorías.

Llama a la función y comprueba que la base de datos se crea correctamente.

Crea una función llamada agregar_categoria() que pida al usuario un nombre de categoría y se encargue de crear
la categoría en la base de datos (ten en cuenta que si ya existe dará un error, por que el nombre es UNIQUE).

Ahora, crea un pequeño menú de opciones dentro del script, que te de la bienvenida al sistema y te permita
crear una categoría o Salir. Añade las siguientes tres categorías utilizando este menú de opciones:

- Primeros
- Segundos
- Postres

Crea una función llamada agregar_plato() que muestre al usuario las categorías disponibles y le permita escoger una
(escribiendo un número).

Luego le pedirá introducir el nombre del plato y lo añadirá a la base de datos, teniendo en cuenta que
la categoria del plato concuerde con el id de la categoría y que el nombre del plato no puede repetirse
(no es necesario comprobar si la categoría realmente existe, en ese caso simplemente no se insertará el plato).

Agrega la nueva opción al menú de opciones y añade los siguientes platos:

Primeros: Ensalada del tiempo / Zumo de tomate
Segundos: Estofado de pescado / Pollo con patatas
Postres: Flan con nata / Fruta del tiempo

Crea una función llamada mostrar_menu() que muestre el menú con todos los platos de forma ordenada:
los primeros, los segundos y los postres. Optativamente puedes adornar la forma en que muestras el menú por pantalla
'''
import sqlite3
import tkinter as tk
from tkinter import messagebox

#La función crear_bd se encarga de crear la base de datos llamada reataurante.bd
def crear_bd():
    connection = sqlite3.connect("restaurante.db")
    cursor = connection.cursor()
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS categoria (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre VARCHAR(100) UNIQUE NOT NULL
                    )
                    ''')

    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS plato (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre VARCHAR(100) UNIQUE NOT NULL,
                    categoria_id INTEGER NOT NULL,
                    FOREIGN KEY(categoria_id) REFERENCES categoria(id) 
                    )
                    ''')
    connection.commit()
    connection.close()
    #En este momento se lanza  un nuevo mensaje en el layout de la app, para informar que la bbdd se ha creado correctamente
    messagebox.showinfo(message="DB created successfully", title="Create DB")

#La función crear:_categoria se encarga de crwear una nueva categoría, siempre que ésta no exista ya en la base de datos
#a la función se le pasa como parámetro la ruta del padre donde va a crear el mensaje y la nueva categoria
#introducida por el usuario
def crear_categoria(newCat):
            #Se hace un try para intentar introducir esa nueva categoria en la base de datos
            if newCat != "":
                try:
                    connection = sqlite3.connect("restaurante.db")
                    cursor = connection.cursor()
                    cursor.execute("INSERT INTO categoria VALUES (null,?)", (newCat,))
                    connection.commit()
                    connection.close()
                except sqlite3.IntegrityError:
                    #En caso que se lance un error se captura aquí y se muestra un mensaje por pantalla para informar al
                    #respecto
                    print(f"La categoria {newCat} no se puede introducir. | No se puede repetir categorias")
                    expression = f"The category {newCat} can not be added. | Categories can not be repeated"
                    messagebox.showerror(message=expression, title="Add a new category")

                else:
                    #En caso que se haya podido añadir la categoría se lanza un mensaje para informar al respecto
                    print(f"La categoria {newCat} se ha añadido satisfactoriamente.")
                    expression = f"The category {newCat} has been added successfully."
                    messagebox.showinfo(message=expression, title="Add a new category")
            else:
                messagebox.showwarning(message="You did not type any new category", title="Add a new category")


#Se define la función agregar_plato, para agregar un nuevo plato, se le pasa como parámetro a la función la ruta del padre donde se va a crear el nuevo
#mensaje informando del proceso, así como dle valor de la categoría ref y el nombre del plato newPlate
def agregar_plato(ref, newPlate):
        if newPlate != "" and ref != None:
            try:
                connection = sqlite3.connect("restaurante.db")
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM plato")
                plates = cursor.fetchall()
                cursor.execute("SELECT * FROM categoria")
                categories = cursor.fetchall()
                print(categories)
                categoriesIndex = [item[0] for item in categories]
                #Se hace uso de una comprenhension-list para capturar en una lista todoas las categorias que se tiene
                #Si la categoria introducida por el usuario está en la lista se crea el nuevo plato
                if ref in categoriesIndex:
                    cursor.execute("INSERT INTO plato VALUES (null,?,?)", (newPlate, ref))
                    expression = f"The plate: {newPlate} has been added into {ref} category"
                    #Y se lanza un nuevo mensaje en el layout informando al respecto
                    messagebox.showinfo(message=expression, title="Add a new plate")
                else:
                    #Si la categoria no existe en la base de datos se informa al usuario
                    print("You have just selected a wrong category, please try again...")
                    expression = "You have just selected a wrong category, please try again..."
                    #Se lanza otro nuevo mensaje en el layout para informar al respecto
                    messagebox.showwarning(message=expression, title="Add a new plate")
                connection.commit()
                connection.close()
            except sqlite3.IntegrityError:
                #En caso que se intente introducir un plato repetido se captura el error
                print(f"{newPlate} can not be added because it is in the menu...")
                expression = f"{newPlate} can not be added because it is in the menu..."
                #Y se lanza un nuevo mensaje para informar al respecto
                messagebox.showerror(message=expression, title="Add a new plate")
                connection.commit()
                connection.close()
        else:
            messagebox.showwarning(message="You did not type any new plate", title="Add a new plate")

#Se define al función mostrar_menu para mostrar por pantalla todos los platos que se tiene en la base de datos
def mostrar_menu(path):
    connection = sqlite3.connect("restaurante.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM plato")
    plates = cursor.fetchall()
    for plate in plates:
        print(f"Id: {plate[0]} | category: {plate[2]} | name: {plate[1]}")
        expression = f"Id: {plate[0]} | category: {plate[2]} | name: {plate[1]}"
        tk.Label(path, text= expression).pack(side="top", anchor="n", padx=10, pady=10)
    connection.commit()
    connection.close()
