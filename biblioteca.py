import tkinter as tk
from tkinter import font, messagebox
from tkinter import ttk 

COLOR_BARRA_SUPERIOR = "#2b1d1e"
COLOR_MENU_LATERAL = "#543f41"
COLOR_CUERPO_PRINCIPAL = "#FFFFFF"
COLOR_MENU_CURSOR_ENCIMA = "#7b6265"
COLOR_SELECCIONADO = "#7b6265"

lista_prestamos = []


libros_disponibles = [
    "El principito",
    "Harry Potter y la piedra filosofal",
    "Cien años de soledad",
    "Don Quijote de la Mancha",
    "Orgullo y prejuicio",
    "Crimen y castigo"
]

opcion_seleccionada = None

def iniciar_sesion():
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    user_id = entry_id.get()
    if nombre and apellido and user_id:
        messagebox.showinfo("Iniciar Sesión", f"Bienvenido {nombre} {apellido} con ID: {user_id}")
        abrir_ventana_principal(nombre)
        root.destroy() 
    else:
        messagebox.showwarning("Datos faltantes", "Por favor, ingrese todos los datos.")

def crear_usuario():
    ventana_registro = tk.Toplevel(root)
    ventana_registro.title("Registro de Usuario")
    ventana_registro.geometry("400x300")

    label_titulo_registro = tk.Label(ventana_registro, text="Registro Nuevo Usuario", font=("Helvetica", 14))
    label_titulo_registro.pack(pady=10)

    label_nombre_registro = tk.Label(ventana_registro, text="Nombre:")
    label_nombre_registro.pack(pady=5)
    entry_nombre_registro = tk.Entry(ventana_registro)
    entry_nombre_registro.pack(pady=5)

    label_apellido_registro = tk.Label(ventana_registro, text="Apellido:")
    label_apellido_registro.pack(pady=5)
    entry_apellido_registro = tk.Entry(ventana_registro)
    entry_apellido_registro.pack(pady=5)

    label_id_registro = tk.Label(ventana_registro, text="ID:")
    label_id_registro.pack(pady=5)
    entry_id_registro = tk.Entry(ventana_registro, validate="key", validatecommand=(ventana_registro.register(validar_id), '%P'))
    entry_id_registro.pack(pady=5)

    def registrar():
        nombre_registro = entry_nombre_registro.get()
        apellido_registro = entry_apellido_registro.get()
        id_registro = entry_id_registro.get()
        if nombre_registro and apellido_registro and id_registro:
            messagebox.showinfo("Registro Exitoso", f"Usuario {nombre_registro} {apellido_registro} con ID: {id_registro} ha sido registrado exitosamente.")
            ventana_registro.destroy()
        else:
            messagebox.showwarning("Datos faltantes", "Por favor, ingrese todos los datos.")

    boton_registrar = tk.Button(ventana_registro, text="Registrarse", command=registrar, bg="#009e2a")
    boton_registrar.pack(pady=20)

def validar_id(nuevo_id):
    return nuevo_id.isdigit() or nuevo_id == ""

def salir():
    root.destroy()

def mostrar_libros():
    global opcion_seleccionada
    opcion_seleccionada = "Libros"
    actualizar_menu()
    limpiar_cuerpo_principal()

    libros_texto = """
    Libros disponibles:
    
    1. "El principito"\n   ISBN: 978-84-9104-348-1\n   Autor: Antoine de Saint-Exupéry\n   Categoría: Literatura infantil\n
    2. "Harry Potter y la piedra filosofal"\n   ISBN: 978-84-9838-455-2\n   Autor: J.K. Rowling\n   Categoría: Fantasía\n
    3. "Cien años de soledad" \n   ISBN: 978-84-376-0157-6\n   Autor: Gabriel García Márquez\n   Categoría: Realismo mágico\n
    4. "Don Quijote de la Mancha" \n   ISBN: 978-84-670-0000-0\n   Autor: Miguel de Cervantes\n   Categoría: Novela\n
    5. "Orgullo y prejuicio"\n   ISBN: 978-84-376-0007-4\n   Autor: Jane Austen\n   Categoría: Novela romántica\n
    6. "Crimen y castigo"\n   ISBN: 978-84-609-8835-5\n   Autor: Fyodor Dostoevsky\n   Categoría: Novela psicológica\n
    """

    label_libros = tk.Label(cuerpo_principal, text=libros_texto, font=("Helvetica", 11), justify="left", padx=20, pady=20, bg=COLOR_CUERPO_PRINCIPAL)
    label_libros.pack(anchor="w")

def realizar_prestamo():
    global opcion_seleccionada
    opcion_seleccionada = "Realizar Préstamo"
    actualizar_menu()
    limpiar_cuerpo_principal()

    label_prestamo = tk.Label(cuerpo_principal, text="Realizar Préstamo", font=("Helvetica", 16, "bold"), bg=COLOR_CUERPO_PRINCIPAL)
    label_prestamo.pack(pady=10)

    label_id_usuario = tk.Label(cuerpo_principal, text="ID del Usuario:")
    label_id_usuario.pack(pady=5)
    entry_id_usuario = tk.Entry(cuerpo_principal, validate="key", validatecommand=(cuerpo_principal.register(validar_id), '%P'))
    entry_id_usuario.pack(pady=5)

    label_titulo_libro = tk.Label(cuerpo_principal, text="Título del Libro:")
    label_titulo_libro.pack(pady=5)
    
    combobox_titulo_libro = ttk.Combobox(cuerpo_principal, values=libros_disponibles)
    combobox_titulo_libro.pack(pady=5)

    def confirmar_prestamo():
        id_usuario = entry_id_usuario.get()
        titulo_libro = combobox_titulo_libro.get()
        if id_usuario and titulo_libro:
            
            prestamos_usuario = [prestamo for prestamo in lista_prestamos if prestamo["ID Usuario"] == id_usuario and prestamo["Título del Libro"] == titulo_libro]
            if len(prestamos_usuario) < 1:
                prestamo = {"ID Usuario": id_usuario, "Título del Libro": titulo_libro}
                lista_prestamos.append(prestamo)
                mostrar_prestamo_confirmado(id_usuario, titulo_libro)
                actualizar_prestamos()
            else:
                messagebox.showwarning("Préstamo Excedido", f"El usuario con ID: {id_usuario} ya ha prestado el libro '{titulo_libro}'.")
        else:
            messagebox.showwarning("Datos faltantes", "Por favor, ingrese el ID del usuario y seleccione el título del libro.")

    boton_confirmar = tk.Button(cuerpo_principal, text="Confirmar Préstamo", command=confirmar_prestamo, bg="#009e2a")
    boton_confirmar.pack(pady=20)

def mostrar_prestamo_confirmado(id_usuario, titulo_libro):
    texto_prestamo = f"ID Usuario: {id_usuario}\nTítulo del Libro: {titulo_libro}"
    label_prestamo_confirmado = tk.Label(cuerpo_principal, text=texto_prestamo, font=("Helvetica", 12), justify="left", padx=20, pady=20, bg=COLOR_CUERPO_PRINCIPAL)
    label_prestamo_confirmado.pack(anchor="w")

def actualizar_prestamos():
    global opcion_seleccionada
    opcion_seleccionada = "Préstamos"
    actualizar_menu()
    limpiar_cuerpo_principal()

    if lista_prestamos:
        texto_prestamos = "Préstamos Realizados:\n\n"
        for prestamo in lista_prestamos:
            texto_prestamos += f"ID Usuario: {prestamo['ID Usuario']}\nTítulo del Libro: {prestamo['Título del Libro']}\n\n"
    else:
        texto_prestamos = "No hay préstamos realizados."

    label_prestamos = tk.Label(cuerpo_principal, text=texto_prestamos, font=("Helvetica", 12), justify="left", padx=20, pady=20, bg=COLOR_CUERPO_PRINCIPAL)
    label_prestamos.pack(anchor="w")

def devolucion_libro():
    global opcion_seleccionada
    opcion_seleccionada = "Devolución"
    actualizar_menu()
    limpiar_cuerpo_principal()

    label_devolucion = tk.Label(cuerpo_principal, text="Devolución de Libro", font=("Helvetica", 16, "bold"), bg=COLOR_CUERPO_PRINCIPAL)
    label_devolucion.pack(pady=10)

    label_id_usuario = tk.Label(cuerpo_principal, text="ID del Usuario:")
    label_id_usuario.pack(pady=5)
    entry_id_usuario = tk.Entry(cuerpo_principal, validate="key", validatecommand=(cuerpo_principal.register(validar_id), '%P'))
    entry_id_usuario.pack(pady=5)

    label_titulo_libro = tk.Label(cuerpo_principal, text="Título del Libro:")
    label_titulo_libro.pack(pady=5)
    
    
    combobox_titulo_libro = ttk.Combobox(cuerpo_principal)
    combobox_titulo_libro.pack(pady=5)
    
    def actualizar_libros_prestados(event):
        id_usuario = entry_id_usuario.get()
        libros_prestados = [prestamo["Título del Libro"] for prestamo in lista_prestamos if prestamo["ID Usuario"] == id_usuario]
        combobox_titulo_libro['values'] = libros_prestados

    entry_id_usuario.bind("<FocusOut>", actualizar_libros_prestados)

    def confirmar_devolucion():
        id_usuario = entry_id_usuario.get()
        titulo_libro = combobox_titulo_libro.get()
        if id_usuario and titulo_libro:
            prestamo_encontrado = None
            for prestamo in lista_prestamos:
                if prestamo["ID Usuario"] == id_usuario and prestamo["Título del Libro"] == titulo_libro:
                    prestamo_encontrado = prestamo
                    break
            if prestamo_encontrado:
                lista_prestamos.remove(prestamo_encontrado)
                messagebox.showinfo("Devolución Exitosa", f"El libro '{titulo_libro}' ha sido devuelto por el usuario con ID: {id_usuario}.")
                actualizar_prestamos()
            else:
                messagebox.showwarning("Préstamo No Encontrado", "No se encontró un préstamo con los datos ingresados.")
        else:
            messagebox.showwarning("Datos faltantes", "Por favor, ingrese el ID del usuario y seleccione el título del libro.")

    boton_confirmar = tk.Button(cuerpo_principal, text="Confirmar Devolución", command=confirmar_devolucion, bg="#009e2a")
    boton_confirmar.pack(pady=20)

def limpiar_cuerpo_principal():
    for widget in cuerpo_principal.winfo_children():
        widget.destroy()

def actualizar_menu():
    for button in menu_lateral.winfo_children():
        button.config(bg=COLOR_MENU_LATERAL, font=("Helvetica", 14))

    if opcion_seleccionada == "Libros":
        boton_libros.config(bg=COLOR_SELECCIONADO)
    elif opcion_seleccionada == "Préstamos":
        boton_prestamos.config(bg=COLOR_SELECCIONADO)
    elif opcion_seleccionada == "Realizar Préstamo":
        boton_realizar_prestamo.config(bg=COLOR_SELECCIONADO)
    elif opcion_seleccionada == "Devolución":
        boton_devolucion.config(bg=COLOR_SELECCIONADO)
    elif opcion_seleccionada == "Salir":
        boton_salir.config(bg=COLOR_SELECCIONADO)

def abrir_ventana_principal(nombre):
    global menu_lateral, cuerpo_principal, boton_libros, boton_prestamos, boton_realizar_prestamo, boton_devolucion, boton_salir

    ventana_principal = tk.Tk()
    ventana_principal.title("Menú Principal")
    ventana_principal.geometry("1024x600")
    
    barra_superior = tk.Frame(ventana_principal, bg=COLOR_BARRA_SUPERIOR, height=50)
    barra_superior.pack(side=tk.TOP, fill='both')

    menu_lateral = tk.Frame(ventana_principal, bg=COLOR_MENU_LATERAL, width=200)
    menu_lateral.pack(side=tk.LEFT, fill='both', expand=False)

    cuerpo_principal = tk.Frame(ventana_principal, bg=COLOR_CUERPO_PRINCIPAL)
    cuerpo_principal.pack(side=tk.RIGHT, fill='both', expand=True)

    label_titulo = tk.Label(barra_superior, text="Biblioteca Nacional", fg="#fff", font=("Roboto", 15), bg=COLOR_BARRA_SUPERIOR, pady=10, width=16)
    label_titulo.pack(side=tk.LEFT)

    label_nombre_usuario = tk.Label(barra_superior, text=f"Bienvenido, {nombre}", fg="#fff", font=("Roboto", 12), bg=COLOR_BARRA_SUPERIOR, padx=10, width=20)
    label_nombre_usuario.pack(side=tk.RIGHT)

    opciones_menu = [("Libros", mostrar_libros),
                     ("Préstamos", actualizar_prestamos),
                     ("Realizar Préstamo", realizar_prestamo),
                     ("Devolución", devolucion_libro),
                     ("Salir", ventana_principal.destroy)]

    for opcion, comando in opciones_menu:
        button = tk.Button(menu_lateral, text=opcion, font=("Helvetica", 14), bg=COLOR_MENU_LATERAL, fg="white", command=comando, relief="flat")
        button.pack(fill="x", pady=5)

        if opcion == "Libros":
            boton_libros = button
        elif opcion == "Préstamos":
            boton_prestamos = button
        elif opcion == "Realizar Préstamo":
            boton_realizar_prestamo = button
        elif opcion == "Devolución":
            boton_devolucion = button
        elif opcion == "Salir":
            boton_salir = button

root = tk.Tk()
root.title("Biblioteca Nacional")
root.geometry("500x500")

label_titulo = tk.Label(root, text="Bienvenido a la Biblioteca Nacional", font=("Helvetica", 16))
label_titulo.pack(pady=10)

label_nombre = tk.Label(root, text="Nombre:")
label_nombre.pack(pady=5)
entry_nombre = tk.Entry(root)
entry_nombre.pack(pady=5)

label_apellido = tk.Label(root, text="Apellido:")
label_apellido.pack(pady=5)
entry_apellido = tk.Entry(root)
entry_apellido.pack(pady=5)

label_id = tk.Label(root, text="ID:")
label_id.pack(pady=5)
entry_id = tk.Entry(root, validate="key", validatecommand=(root.register(validar_id), '%P'))
entry_id.pack(pady=5)

boton_iniciar = tk.Button(root, text="Iniciar Sesión", command=iniciar_sesion, bg="#009e2a")
boton_iniciar.pack(pady=20)

label_crear_usuario = tk.Label(root, text="Regístrate aquí: ")
label_crear_usuario.pack(pady=10)
boton_crear_usuario = tk.Button(root, text="Crear Usuario", command=crear_usuario, bg="#b9fff7")
boton_crear_usuario.pack(pady=5)

boton_salir = tk.Button(root, text="Salir", command=salir, bg="#ff7780")
boton_salir.pack(pady=20)

root.mainloop()
