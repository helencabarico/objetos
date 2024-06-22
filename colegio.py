import tkinter as tk
from tkinter import messagebox, ttk

# Datos simulados para el colegio
cursos_disponibles = [
    {"nombre": "Matemáticas Avanzadas", "profesor": "Juan Pérez", "horarios": ["08:00 - 10:00", "14:00 - 16:00"], "asignaturas": ["Álgebra Lineal", "Cálculo Avanzado", "Geometría Analítica"]},
    {"nombre": "Literatura Universal", "profesor": "María Gómez", "horarios": ["10:00 - 12:00", "16:00 - 18:00"], "asignaturas": ["Shakespeare", "Cervantes", "García Márquez"]},
    {"nombre": "Programación en Python", "profesor": "Luis Ramírez", "horarios": ["09:00 - 11:00", "13:00 - 15:00"], "asignaturas": ["Introducción a Python", "Programación Orientada a Objetos", "Aplicaciones Web con Flask"]},
    {"nombre": "Historia Contemporánea", "profesor": "Ana Martínez", "horarios": ["11:00 - 13:00", "15:00 - 17:00"], "asignaturas": ["Primera y Segunda Guerra Mundial", "Guerra Fría", "Movimientos Sociales del Siglo XX"]}
]

profesores = [
    {"nombre": "Juan Pérez", "curso": "Matemáticas Avanzadas", "asignaturas": ["Álgebra Lineal", "Cálculo Avanzado", "Geometría Analítica"]},
    {"nombre": "María Gómez", "curso": "Literatura Universal", "asignaturas": ["Shakespeare", "Cervantes", "García Márquez"]},
    {"nombre": "Luis Ramírez", "curso": "Programación en Python", "asignaturas": ["Introducción a Python", "Programación Orientada a Objetos", "Aplicaciones Web con Flask"]},
    {"nombre": "Ana Martínez", "curso": "Historia Contemporánea", "asignaturas": ["Primera y Segunda Guerra Mundial", "Guerra Fría", "Movimientos Sociales del Siglo XX"]}
]

asignaturas = [
    {"nombre": "Álgebra Lineal", "curso": "Matemáticas Avanzadas", "profesor": "Juan Pérez"},
    {"nombre": "Cálculo Avanzado", "curso": "Matemáticas Avanzadas", "profesor": "Juan Pérez"},
    {"nombre": "Geometría Analítica", "curso": "Matemáticas Avanzadas", "profesor": "Juan Pérez"},
    {"nombre": "Shakespeare", "curso": "Literatura Universal", "profesor": "María Gómez"},
    {"nombre": "Cervantes", "curso": "Literatura Universal", "profesor": "María Gómez"},
    {"nombre": "García Márquez", "curso": "Literatura Universal", "profesor": "María Gómez"},
    {"nombre": "Introducción a Python", "curso": "Programación en Python", "profesor": "Luis Ramírez"},
    {"nombre": "Programación Orientada a Objetos", "curso": "Programación en Python", "profesor": "Luis Ramírez"},
    {"nombre": "Aplicaciones Web con Flask", "curso": "Programación en Python", "profesor": "Luis Ramírez"},
    {"nombre": "Primera y Segunda Guerra Mundial", "curso": "Historia Contemporánea", "profesor": "Ana Martínez"},
    {"nombre": "Guerra Fría", "curso": "Historia Contemporánea", "profesor": "Ana Martínez"},
    {"nombre": "Movimientos Sociales del Siglo XX", "curso": "Historia Contemporánea", "profesor": "Ana Martínez"}
]

COLOR_BARRA_SUPERIOR = "#2b1d1e"
COLOR_MENU_LATERAL = "#543f41"
COLOR_CUERPO_PRINCIPAL = "#FFFFFF"
COLOR_MENU_CURSOR_ENCIMA = "#7b6265"
COLOR_SELECCIONADO = "#7b6265"

opcion_seleccionada = None
matriculas = []

def iniciar_sesion():
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    user_id = entry_id.get()
    if nombre and apellido and user_id:
        messagebox.showinfo("Iniciar Sesión", f"Bienvenido {nombre} {apellido} con ID: {user_id}")
        abrir_ventana_principal(nombre)
        root.destroy()  # Cierra la ventana de inicio de sesión
    else:
        messagebox.showwarning("Datos faltantes", "Por favor, ingrese todos los datos.")

def mostrar_cursos():
    global opcion_seleccionada
    opcion_seleccionada = "Cursos"
    limpiar_cuerpo_principal()

    cursos_texto = "Cursos disponibles:\n\n"
    for curso in cursos_disponibles:
        cursos_texto += f"{curso['nombre']} - Profesor: {curso['profesor']}\n"
        cursos_texto += f"Asignaturas: {', '.join(curso['asignaturas'])}\n"
        cursos_texto += f"Horarios: {', '.join(curso['horarios'])}\n\n"

    label_cursos = tk.Label(cuerpo_principal, text=cursos_texto, font=("Helvetica", 11), justify="left", padx=20, pady=20, bg=COLOR_CUERPO_PRINCIPAL)
    label_cursos.pack(anchor="w")

def mostrar_profesores():
    global opcion_seleccionada
    opcion_seleccionada = "Profesores"
    limpiar_cuerpo_principal()

    profesores_texto = "Profesores disponibles:\n\n"
    for profesor in profesores:
        profesores_texto += f"{profesor['nombre']} - Curso: {profesor['curso']}\n"
        profesores_texto += f"Asignaturas: {', '.join(profesor['asignaturas'])}\n\n"

    label_profesores = tk.Label(cuerpo_principal, text=profesores_texto, font=("Helvetica", 11), justify="left", padx=20, pady=20, bg=COLOR_CUERPO_PRINCIPAL)
    label_profesores.pack(anchor="w")

def mostrar_asignaturas():
    global opcion_seleccionada
    opcion_seleccionada = "Asignaturas"
    limpiar_cuerpo_principal()

    # Crear un Text para mostrar las asignaturas
    text_asignaturas = tk.Text(cuerpo_principal, wrap="word", font=("Helvetica", 11), padx=20, pady=20, bg=COLOR_CUERPO_PRINCIPAL)
    text_asignaturas.pack(fill="both", expand=True)

    # Crear un Scrollbar y vincularlo al Text
    scrollbar = tk.Scrollbar(cuerpo_principal, command=text_asignaturas.yview)
    scrollbar.pack(side="right", fill="y")
    text_asignaturas.config(yscrollcommand=scrollbar.set)

    asignaturas_texto = "Asignaturas disponibles:\n\n"
    for asignatura in asignaturas:
        asignaturas_texto += f"{asignatura['nombre']} - Curso: {asignatura['curso']}\n"
        asignaturas_texto += f"Profesor: {asignatura['profesor']}\n\n"

    # Insertar el texto en el widget Text
    text_asignaturas.insert("1.0", asignaturas_texto)

    # Deshabilitar la edición del Text (solo lectura)
    text_asignaturas.config(state="disabled")

def mostrar_matriculas():
    global opcion_seleccionada
    opcion_seleccionada = "Matricular Curso"
    limpiar_cuerpo_principal()

    matriculas_texto = "Cursos matriculados:\n\n"
    for matricula in matriculas:
        matriculas_texto += f"{matricula}\n"

    label_matriculas = tk.Label(cuerpo_principal, text=matriculas_texto, font=("Helvetica", 11), justify="left", padx=20, pady=20, bg=COLOR_CUERPO_PRINCIPAL)
    label_matriculas.pack(anchor="w")

    matricular_frame = tk.Frame(cuerpo_principal, bg=COLOR_CUERPO_PRINCIPAL)
    matricular_frame.pack(pady=20)

    label_curso = tk.Label(matricular_frame, text="Curso:", font=("Helvetica", 12), bg=COLOR_CUERPO_PRINCIPAL)
    label_curso.grid(row=0, column=0, padx=10, pady=5, sticky="w")

    curso_var = tk.StringVar()
    cursos_combo = ttk.Combobox(matricular_frame, textvariable=curso_var, font=("Helvetica", 12))
    cursos_combo['values'] = [curso["nombre"] for curso in cursos_disponibles]
    cursos_combo.grid(row=0, column=1, padx=10, pady=5)

    label_profesor = tk.Label(matricular_frame, text="Profesor:", font=("Helvetica", 12), bg=COLOR_CUERPO_PRINCIPAL)
    label_profesor.grid(row=1, column=0, padx=10, pady=5, sticky="w")

    profesor_var = tk.StringVar()
    profesores_combo = ttk.Combobox(matricular_frame, textvariable=profesor_var, font=("Helvetica", 12))
    profesores_combo['values'] = [profesor["nombre"] for profesor in profesores]
    profesores_combo.grid(row=1, column=1, padx=10, pady=5)

    label_horario = tk.Label(matricular_frame, text="Horario:", font=("Helvetica", 12), bg=COLOR_CUERPO_PRINCIPAL)
    label_horario.grid(row=2, column=0, padx=10, pady=5, sticky="w")

    horario_var = tk.StringVar()
    horarios_combo = ttk.Combobox(matricular_frame, textvariable=horario_var, font=("Helvetica", 12))
    horarios_combo['values'] = [horario for curso in cursos_disponibles for horario in curso["horarios"]]
    horarios_combo.grid(row=2, column=1, padx=10, pady=5)

    def matricular_curso():
        curso = curso_var.get()
        profesor = profesor_var.get()
        horario = horario_var.get()

        # Verificar que los campos no estén vacíos
        if curso and profesor and horario:
            matricula = f"Curso: {curso}, Profesor: {profesor}, Horario: {horario}"
            matriculas.append(matricula)
            mostrar_matriculas()  # Actualizar la vista de las matrículas
            messagebox.showinfo("Matriculación Exitosa", "El curso ha sido matriculado exitosamente.")
        else:
            # Mostrar un mensaje de advertencia si faltan datos (opcional)
            messagebox.showinfo("Matrícula Exitosa", "El curso ha sido matriculado exitosamente")

    boton_matricular = tk.Button(matricular_frame, text="Matricular", font=("Helvetica", 14), bg="#4CAF50", fg="white", relief="flat", command=matricular_curso)
    boton_matricular.grid(row=3, columnspan=2, pady=10)

    # Inicializar los Combobox con valores predeterminados si se desea
    cursos_combo.current(0)
    profesores_combo.current(0)
    horarios_combo.current(0)


def limpiar_cuerpo_principal():
    for widget in cuerpo_principal.winfo_children():
        widget.destroy()

def abrir_ventana_principal(nombre):
    ventana_principal = tk.Tk()
    ventana_principal.title("Menú Principal")
    ventana_principal.geometry("1024x600")

    barra_superior = tk.Frame(ventana_principal, bg=COLOR_BARRA_SUPERIOR, height=50)
    barra_superior.pack(side=tk.TOP, fill='both')

    menu_lateral = tk.Frame(ventana_principal, bg=COLOR_MENU_LATERAL, width=200)
    menu_lateral.pack(side=tk.LEFT, fill='both', expand=False)

    global cuerpo_principal
    cuerpo_principal = tk.Frame(ventana_principal, bg=COLOR_CUERPO_PRINCIPAL)
    cuerpo_principal.pack(side=tk.RIGHT, fill='both', expand=True)

    label_titulo = tk.Label(barra_superior, text="Gestión Escolar", fg="#fff", font=("Roboto", 15), bg=COLOR_BARRA_SUPERIOR, pady=10, width=16)
    label_titulo.pack(side=tk.LEFT)

    label_nombre_usuario = tk.Label(barra_superior, text=f"Bienvenido, {nombre}", fg="#fff", font=("Roboto", 12), bg=COLOR_BARRA_SUPERIOR, padx=10, width=20)
    label_nombre_usuario.pack(side=tk.RIGHT)

    opciones_menu = [("Cursos", mostrar_cursos),
                     ("Profesores", mostrar_profesores),
                     ("Asignaturas", mostrar_asignaturas),
                     ("Matricular Curso", mostrar_matriculas),
                     ("Salir", ventana_principal.destroy)]

    for opcion, comando in opciones_menu:
        button = tk.Button(menu_lateral, text=opcion, font=("Helvetica", 14), bg=COLOR_MENU_LATERAL, fg="white", command=comando, relief="flat")
        button.pack(fill="x", pady=5)

    ventana_principal.mainloop()

root = tk.Tk()
root.title("Gestión Escolar")
root.geometry("500x500")

# Configuración de la ventana de inicio de sesión
frame_inicio_sesion = tk.Frame(root, bg=COLOR_CUERPO_PRINCIPAL)
frame_inicio_sesion.pack(expand=True)

label_titulo_inicio = tk.Label(frame_inicio_sesion, text="Inicio de Sesión", font=("Helvetica", 16))
label_titulo_inicio.pack(pady=10)

# Campos de entrada para el inicio de sesión
frame_campos = tk.Frame(frame_inicio_sesion, bg=COLOR_CUERPO_PRINCIPAL)
frame_campos.pack(pady=10)

label_nombre = tk.Label(frame_campos, text="Nombre:", font=("Helvetica", 12), bg=COLOR_CUERPO_PRINCIPAL)
label_nombre.grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_nombre = tk.Entry(frame_campos, font=("Helvetica", 12))
entry_nombre.grid(row=0, column=1, padx=10, pady=5)

label_apellido = tk.Label(frame_campos, text="Apellido:", font=("Helvetica", 12), bg=COLOR_CUERPO_PRINCIPAL)
label_apellido.grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_apellido = tk.Entry(frame_campos, font=("Helvetica", 12))
entry_apellido.grid(row=1, column=1, padx=10, pady=5)

label_id = tk.Label(frame_campos, text="ID:", font=("Helvetica", 12), bg=COLOR_CUERPO_PRINCIPAL)
label_id.grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_id = tk.Entry(frame_campos, font=("Helvetica", 12))
entry_id.grid(row=2, column=1, padx=10, pady=5)

# Botón para iniciar sesión
boton_iniciar_sesion = tk.Button(frame_inicio_sesion, text="Iniciar Sesión", font=("Helvetica", 14), bg="#4CAF50", fg="white", relief="flat", command=iniciar_sesion)
boton_iniciar_sesion.pack(pady=10)

# Función principal para iniciar la aplicación
root.mainloop()
