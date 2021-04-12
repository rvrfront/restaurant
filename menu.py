'''En este ejercicios debes crear una interfaz gráfica con tkinter (menu.py) que muestre de forma elegante el menú del restaurante.

Tú eliges el nombre del restaurante y el precio del menú, así como las tipografías, colores, adornos y tamaño de la ventana.

El único requisito es que el programa se conectará a la base de datos para buscar la lista categorías y platos.
'''

import restaurante
import tkinter as tk
import time
status = False

#Se crea una función callToCreateBd para hacer una llamada a la función crear_bd del módulo restaurante
def callToCreateBd():
    restaurante.crear_bd(createBd)

#Se crea una función callToShowMenu para invocar a la función mostrar_menu del módulo restaurante
def callToShowMenu():
    restaurante.mostrar_menu(showPlatesFrame)

#Se crea una función callToAddCategory para llamar a la fubnción crear_categoria del módulo restaurante
def callToAddCategory():
    categoryName = categoryInput.get()
    restaurante.crear_categoria(addCategoryFrame, categoryName)

#Se crea una función callToAddNewPlate para llamar a la función agregar_plato del módulo restaurante
def callToAddNewPlate():
    ref = int(newPlateInputCat.get())
    plateName = newPlateInput.get()
    restaurante.agregar_plato(addPlateFrame, ref, plateName)

#Se crea el frame root
root = tk.Tk()
root.title("Python Restaurant by Raul Vergel Romero")
#Dentro del frame root, se define un frame para poder poner el título de la app
titleFrame = tk.Frame(root)
titleFrame.pack(side="top", anchor="n", fill="x")
titleFrame.config(width=800, height=45, bg="#5E9BD8", padx=10, pady=10, bd=5, relief="sunken")
#Dentro del frame anterior se define un label para mostrar el título de la app
titleText = tk.Label(titleFrame, text="Welcome to Python Restaurant...", fg="#FAFAFB")
titleText.pack(side="top", anchor="n", fill="x")
titleText.config(font=("Consolas", 18), bg="#5E9BD8", padx=10, pady=10)

#Se define otro frame, para tener accesible el botón para crear la BD
createBd = tk.Frame(root)
createBd.pack(side="top", anchor="n", fill="x")
createBd.config(width=800, height=45, bg="#5E9BD8", padx=10, pady=10, bd=5, relief="sunken")
#Se define el botón para disparar la función callToCreateBd cuando se pulse el botón
createBdButton = tk.Button(createBd, text="create restaurante.db", command=callToCreateBd)
createBdButton.pack(side="top", anchor="n")
createBdButton.config(width=25, height=2, padx=10, pady=10)

#Se define otro frame para definir el layout de la parte de la app para crear una nueva categoria
addCategoryFrame = tk.Frame(root)
addCategoryFrame.pack(side="top", anchor="n", fill="x")
addCategoryFrame.config(bg="#5E9BD8", padx=10, pady=10, bd=5, relief="sunken")

#Se define un label dentro del frame, para informar al usuario que de debe introducir una nueva categoria
categoryLabel = tk.Label(addCategoryFrame, text="Please, insert a new category", fg="#FAFAFB")
categoryLabel.pack(sid="top", anchor="n", fill="x")
categoryLabel.config(font=("Consolas", 12), padx=10, pady=10, bg="#5E9BD8")

#Se define un entry para capturar la información por parte del usuario
categoryInput = tk.Entry(addCategoryFrame)
categoryInput.pack(padx=10, pady=10)
categoryInput.config()

#Se define el botón para disparar la función callToAddCategory cuando se pulse el botón
categoryButton = tk.Button(addCategoryFrame, text="click to add", command=callToAddCategory)
categoryButton.pack(side="top", anchor="n")
categoryButton.config(width=25, height=2, padx=10, pady=10)

#Se define otro frame para la parte del layout relativa a poder añadir un nuevo plato
addPlateFrame = tk.Frame(root)
addPlateFrame.pack(side="top", anchor="n", fill="x")
addPlateFrame.config(bg="#5E9BD8", padx=10, pady=10, bd=5, relief="sunken")

#Se crea un label para informar al usuario que se debe introducir una nueva categoria
newPlateCat = tk.Label(addPlateFrame, text="Please, insert the category", fg="#FAFAFB")
newPlateCat.pack(sid="top", anchor="n", fill="x")
newPlateCat.config(font=("Consolas", 12), padx=10, pady=10, bg="#5E9BD8")

#Se define un entry para capturar la nueva categoruia introducida por el usuario
newPlateInputCat = tk.Entry(addPlateFrame)
newPlateInputCat.pack(padx=10, pady=10)
newPlateInputCat.config()

#Se define otro label para informar al usuario que se debe introducir el nombre del nuevo plato
newPlateLabel = tk.Label(addPlateFrame, text="Please, insert the plate name", fg="#FAFAFB")
newPlateLabel.pack(sid="top", anchor="n", fill="x")
newPlateLabel.config(font=("Consolas", 12), padx=10, pady=10, bg="#5E9BD8")

#Se define otro entry para capturar el nombre del nuevo plato por parte del usuario
newPlateInput = tk.Entry(addPlateFrame)
newPlateInput.pack(padx=10, pady=10)
newPlateInput.config()

#Se define un botón para disparar la función callToAddNew Plate cuando el usuario pulse el botón
newPlateButton = tk.Button(addPlateFrame, text="click to add plate", command=callToAddNewPlate)
newPlateButton.pack(side="top", anchor="center")
newPlateButton.config(width=25, height=2, padx=10, pady=10)

#Se define un nuevo frame para mostrar toda la información que se tiene en restaurante.bd
showPlatesFrame = tk.Frame(root)
showPlatesFrame.pack(side="top", anchor="n", fill="x")
showPlatesFrame.config(width=45, height= 55, bg="#5E9BD8", padx=10, pady=10, bd=5, relief="sunken")
showButton = tk.Button(showPlatesFrame, text="click to show menu", command=callToShowMenu)
showButton.pack(side="top", anchor="center")
showButton.config(width=25, height=2, padx=10, pady=10)


root.mainloop()