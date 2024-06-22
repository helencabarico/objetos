import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime

# Colores utilizados en la interfaz
COLOR_BARRA_SUPERIOR = "#492945"
COLOR_MENU_LATERAL = "#6a3d5c"
COLOR_CUERPO_PRINCIPAL = "#FFFFFF"
COLOR_MENU_CURSOR_ENCIMA = "#9f5880"
COLOR_SELECCIONADO = "#db7ea8"

# Datos de productos por categoría
productos = {
    "Bebidas": {
        "Coca-Cola (355 ml)": {"precio": 6.375, "cantidad": 100},
        "Pepsi (500 ml)": {"precio": 7.875, "cantidad": 80},
        "Agua mineral (1 litro)": {"precio": 4.131, "cantidad": 50},
        "Jugo de naranja (250 ml)": {"precio": 10.125, "cantidad": 60},
        "Té helado (330 ml)": {"precio": 7.920, "cantidad": 70}
    },
    "Panadería": {
        "Pan de molde": {"precio": 2.000, "cantidad": 120},
        "Croissant": {"precio": 1.800, "cantidad": 90},
        "Dona": {"precio": 1.500, "cantidad": 110},
        "Baguette": {"precio": 2.500, "cantidad": 80},
        "Bollo de canela": {"precio": 2.200, "cantidad": 100}
    },
    "Lácteos": {
        "Leche (1 litro)": {"precio": 3.500, "cantidad": 70},
        "Queso fresco": {"precio": 4.000, "cantidad": 50},
        "Yogur natural": {"precio": 1.200, "cantidad": 60},
        "Mantequilla": {"precio": 2.800, "cantidad": 90},
        "Huevo (unidad)": {"precio": 0.500, "cantidad": 200}
    },
    "Frutas y verduras": {
        "Piña (kg)": {"precio": 4.000, "cantidad": 150},
        "Duraznos (kg)": {"precio": 6.000, "cantidad": 100},
        "Peras (kg)": {"precio": 5.000, "cantidad": 120},
        "Manzanas (kg)": {"precio": 4.500, "cantidad": 130},
        "Uvas (kg)": {"precio": 7.000, "cantidad": 80},
        "Maíz (kg)": {"precio": 1.500, "cantidad": 110},
        "Guisantes (kg)": {"precio": 4.000, "cantidad": 95},
        "Judías verdes (kg)": {"precio": 3.500, "cantidad": 105},
        "Zanahorias (kg)": {"precio": 2.000, "cantidad": 125},
        "Espinacas (kg)": {"precio": 3.000, "cantidad": 85}
    },
    "Productos de limpieza": {
        "Limpiador genérico (1L)": {"precio": 8.000, "cantidad": 60},
        "Limpiador de suelos (1L)": {"precio": 10.000, "cantidad": 40},
        "Desincrustante para baños (1L)": {"precio": 12.000, "cantidad": 30},
        "Limpiacristales (1L)": {"precio": 9.000, "cantidad": 50},
        "Desengrasante (1L)": {"precio": 11.000, "cantidad": 35}
    }
}

# Variables globales
opcion_seleccionada = None
clientes_registrados = []
ventas_realizadas = []

def abrir_ventana_principal():
    global menu_lateral, cuerpo_principal, ventana_principal

    usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()

    # Verificar las credenciales
    if usuario == "admin" and contraseña == "12345":
        ventana_login.destroy()  # Cerrar ventana de inicio de sesión

        ventana_principal = tk.Tk()
        ventana_principal.title("Sistema de Tienda")
        ventana_principal.geometry("1024x600")

        # Barra superior
        barra_superior = tk.Frame(ventana_principal, bg=COLOR_BARRA_SUPERIOR, height=50)
        barra_superior.pack(side=tk.TOP, fill='x')

        label_titulo = tk.Label(barra_superior, text="Sistema de Tienda", fg="#fff", font=("Roboto", 15), bg=COLOR_BARRA_SUPERIOR, pady=10, width=16)
        label_titulo.pack(side=tk.LEFT)

        # Menú lateral
        menu_lateral = tk.Frame(ventana_principal, bg=COLOR_MENU_LATERAL, width=200)
        menu_lateral.pack(side=tk.LEFT, fill='y')

        opciones_menu = [
            ("Inventario", mostrar_inventario),
            ("Realizar Venta", realizar_venta),
            ("Registrar Clientes", registrar_clientes),
            ("Ventas Realizadas", mostrar_ventas),
            ("Salir", salir_sistema)
        ]

        # Crear botones del menú lateral
        for opcion, comando in opciones_menu:
            button = tk.Button(menu_lateral, text=opcion, font=("Helvetica", 14), bg=COLOR_MENU_LATERAL, fg="white",
                               command=comando, relief="flat")
            button.pack(fill="x", pady=5)

        # Cuerpo principal
        cuerpo_principal = tk.Frame(ventana_principal, bg=COLOR_CUERPO_PRINCIPAL)
        cuerpo_principal.pack(side=tk.RIGHT, fill='both', expand=True)

        ventana_principal.mainloop()
    else:
        messagebox.showerror("Error de autenticación", "Usuario o contraseña incorrectos.")

def mostrar_inventario():
    limpiar_cuerpo_principal()

    label_titulo = tk.Label(cuerpo_principal, text="Inventario", font=("Helvetica", 16, "bold"), bg=COLOR_CUERPO_PRINCIPAL)
    label_titulo.pack(pady=10)

    # Crear un canvas con una barra de desplazamiento vertical
    canvas = tk.Canvas(cuerpo_principal, bg=COLOR_CUERPO_PRINCIPAL)
    canvas.pack(side=tk.LEFT, fill='both', expand=True)

    scrollbar = tk.Scrollbar(cuerpo_principal, orient="vertical", command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill='y')

    canvas.configure(yscrollcommand=scrollbar.set)

    # Frame interior dentro del canvas
    frame_interior = tk.Frame(canvas, bg=COLOR_CUERPO_PRINCIPAL)
    canvas.create_window((0, 0), window=frame_interior, anchor="nw")

    # Mostrar todas las categorías de productos y sus productos
    for categoria, productos_categoria in productos.items():
        frame_categoria = tk.Frame(frame_interior, bg=COLOR_CUERPO_PRINCIPAL)
        frame_categoria.pack(fill='both', expand=True, padx=20, pady=10, anchor="w")

        label_categoria = tk.Label(frame_categoria, text=categoria, font=("Helvetica", 14, "underline"), bg=COLOR_CUERPO_PRINCIPAL)
        label_categoria.pack(anchor="w", pady=5, fill='x')

        for producto, detalles in productos_categoria.items():
            label_producto = tk.Label(frame_categoria, text=f"{producto} - ${detalles['precio']:.2f} - Cantidad: {detalles['cantidad']}", font=("Helvetica", 12), bg=COLOR_CUERPO_PRINCIPAL)
            label_producto.pack(anchor="w", padx=20, pady=2, fill='x')

    # Configurar el canvas para que se desplace correctamente
    frame_interior.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))

def realizar_venta():
    limpiar_cuerpo_principal()

    label_titulo = tk.Label(cuerpo_principal, text="Realizar Venta", font=("Helvetica", 16, "bold"), bg=COLOR_CUERPO_PRINCIPAL)
    label_titulo.pack(pady=10)

    # Variables para la venta
    productos_seleccionados = {}
    total_venta = tk.DoubleVar()
    total_venta.set(0.0)

    def calcular_total():
        total = sum(producto["precio"] * producto["cantidad"] for producto in productos_seleccionados.values())
        total_venta.set(total)

    def agregar_producto():
        nonlocal productos_seleccionados

        if opcion_seleccionada.get() and cantidad.get() > 0:
            categoria, producto = opcion_seleccionada.get().split(" - ")
            cantidad_producto = cantidad.get()

            # Verificar disponibilidad del producto
            if cantidad_producto > productos[categoria][producto]["cantidad"]:
                messagebox.showwarning("Stock Insuficiente", f"No hay suficientes unidades de {producto} en stock.")
                return

            # Actualizar cantidad en stock
            productos[categoria][producto]["cantidad"] -= cantidad_producto

            # Agregar producto al carrito
            if producto in productos_seleccionados:
                productos_seleccionados[producto]["cantidad"] += cantidad_producto
            else:
                productos_seleccionados[producto] = {
                    "precio": productos[categoria][producto]["precio"],
                    "cantidad": cantidad_producto
                }

            calcular_total()
            actualizar_carrito()

    def actualizar_carrito():
        for widget in frame_carrito.winfo_children():
            widget.destroy()

        for producto, detalles in productos_seleccionados.items():
            label_producto = tk.Label(frame_carrito, text=f"{producto} - {detalles['cantidad']} x ${detalles['precio']:.2f}", font=("Helvetica", 12), bg=COLOR_CUERPO_PRINCIPAL)
            label_producto.pack(anchor="w", padx=10, pady=2, fill='x')

        label_total = tk.Label(frame_carrito, text=f"Total: ${total_venta.get():.2f}", font=("Helvetica", 14, "bold"), bg=COLOR_CUERPO_PRINCIPAL)
        label_total.pack(anchor="e", padx=10, pady=10, fill='x')

    def finalizar_venta():
        if not productos_seleccionados:
            messagebox.showwarning("Carrito Vacío", "No hay productos en el carrito para realizar la venta.")
            return

        venta = {
            "productos": productos_seleccionados.copy(),
            "total": total_venta.get(),
            "fecha": datetime.now()
        }
        ventas_realizadas.append(venta)

        messagebox.showinfo("Venta Realizada", f"La venta por ${total_venta.get():.2f} ha sido realizada con éxito.")

        # Limpiar carrito
        productos_seleccionados.clear()
        total_venta.set(0.0)
        actualizar_carrito()

    # Selección de productos
    frame_seleccion = tk.Frame(cuerpo_principal, bg=COLOR_CUERPO_PRINCIPAL)
    frame_seleccion.pack(pady=10, fill='x', expand=True)

    tk.Label(frame_seleccion, text="Producto:", font=("Helvetica", 12), bg=COLOR_CUERPO_PRINCIPAL).pack(side=tk.LEFT, padx=5)

    # Crear una lista de productos con sus categorías
    opciones_productos = [f"{categoria} - {producto}" for categoria, productos_categoria in productos.items() for producto in productos_categoria.keys()]
    opcion_seleccionada = tk.StringVar()
    combobox_productos = ttk.Combobox(frame_seleccion, textvariable=opcion_seleccionada, values=opciones_productos, state="readonly")
    combobox_productos.pack(side=tk.LEFT, padx=5)

    tk.Label(frame_seleccion, text="Cantidad:", font=("Helvetica", 12), bg=COLOR_CUERPO_PRINCIPAL).pack(side=tk.LEFT, padx=5)

    cantidad = tk.IntVar()
    spinbox_cantidad = tk.Spinbox(frame_seleccion, from_=1, to=100, textvariable=cantidad, width=5)
    spinbox_cantidad.pack(side=tk.LEFT, padx=5)

    button_agregar = tk.Button(frame_seleccion, text="Agregar", command=agregar_producto)
    button_agregar.pack(side=tk.LEFT, padx=10)

    # Carrito de compras
    frame_carrito = tk.Frame(cuerpo_principal, bg=COLOR_CUERPO_PRINCIPAL)
    frame_carrito.pack(pady=10, fill='both', expand=True)

    button_finalizar = tk.Button(cuerpo_principal, text="Finalizar Venta", command=finalizar_venta)
    button_finalizar.pack(pady=10)

def registrar_clientes():
    limpiar_cuerpo_principal()

    label_titulo = tk.Label(cuerpo_principal, text="Registrar Clientes", font=("Helvetica", 16, "bold"), bg=COLOR_CUERPO_PRINCIPAL)
    label_titulo.pack(pady=10)

    frame_formulario = tk.Frame(cuerpo_principal, bg=COLOR_CUERPO_PRINCIPAL)
    frame_formulario.pack(pady=10)

    tk.Label(frame_formulario, text="Nombre:", font=("Helvetica", 12), bg=COLOR_CUERPO_PRINCIPAL).grid(row=0, column=0, padx=5, pady=5)
    entry_nombre = tk.Entry(frame_formulario)
    entry_nombre.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(frame_formulario, text="ID:", font=("Helvetica", 12), bg=COLOR_CUERPO_PRINCIPAL).grid(row=1, column=0, padx=5, pady=5)
    entry_correo = tk.Entry(frame_formulario)
    entry_correo.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(frame_formulario, text="Teléfono:", font=("Helvetica", 12), bg=COLOR_CUERPO_PRINCIPAL).grid(row=2, column=0, padx=5, pady=5)
    entry_telefono = tk.Entry(frame_formulario)
    entry_telefono.grid(row=2, column=1, padx=5, pady=5)

    def registrar_cliente():
        nombre = entry_nombre.get()
        correo = entry_correo.get()
        telefono = entry_telefono.get()

        if nombre and correo and telefono:
            cliente = {
                "nombre": nombre,
                "correo": correo,
                "telefono": telefono
            }
            clientes_registrados.append(cliente)
            messagebox.showinfo("Registro Exitoso", f"Cliente {nombre} registrado correctamente.")
            entry_nombre.delete(0, tk.END)
            entry_correo.delete(0, tk.END)
            entry_telefono.delete(0, tk.END)
        else:
            messagebox.showwarning("Campos Vacíos", "Por favor, complete todos los campos.")

    button_registrar = tk.Button(cuerpo_principal, text="Registrar", command=registrar_cliente)
    button_registrar.pack(pady=10)

def mostrar_ventas():
    limpiar_cuerpo_principal()

    label_titulo = tk.Label(cuerpo_principal, text="Ventas Realizadas", font=("Helvetica", 16, "bold"), bg=COLOR_CUERPO_PRINCIPAL)
    label_titulo.pack(pady=10)

    # Crear un canvas con una barra de desplazamiento vertical
    canvas = tk.Canvas(cuerpo_principal, bg=COLOR_CUERPO_PRINCIPAL)
    canvas.pack(side=tk.LEFT, fill='both', expand=True)

    scrollbar = tk.Scrollbar(cuerpo_principal, orient="vertical", command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill='y')

    canvas.configure(yscrollcommand=scrollbar.set)

    # Frame interior dentro del canvas
    frame_interior = tk.Frame(canvas, bg=COLOR_CUERPO_PRINCIPAL)
    canvas.create_window((0, 0), window=frame_interior, anchor="nw")

    # Mostrar todas las ventas realizadas
    for venta in ventas_realizadas:
        frame_venta = tk.Frame(frame_interior, bg=COLOR_CUERPO_PRINCIPAL, bd=1, relief="solid")
        frame_venta.pack(fill='both', expand=True, padx=20, pady=10, anchor="w")

        label_fecha = tk.Label(frame_venta, text=f"Fecha: {venta['fecha'].strftime('%Y-%m-%d %H:%M:%S')}", font=("Helvetica", 12, "bold"), bg=COLOR_CUERPO_PRINCIPAL)
        label_fecha.pack(anchor="w", pady=5, fill='x')

        for producto, detalles in venta["productos"].items():
            label_producto = tk.Label(frame_venta, text=f"{producto} - {detalles['cantidad']} x ${detalles['precio']:.2f}", font=("Helvetica", 12), bg=COLOR_CUERPO_PRINCIPAL)
            label_producto.pack(anchor="w", padx=20, pady=2, fill='x')

        label_total = tk.Label(frame_venta, text=f"Total: ${venta['total']:.2f}", font=("Helvetica", 12, "bold"), bg=COLOR_CUERPO_PRINCIPAL)
        label_total.pack(anchor="e", padx=20, pady=5, fill='x')

    # Configurar el canvas para que se desplace correctamente
    frame_interior.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))

def salir_sistema():
    ventana_principal.destroy()

def limpiar_cuerpo_principal():
    for widget in cuerpo_principal.winfo_children():
        widget.destroy()

# Ventana de inicio de sesión
ventana_login = tk.Tk()
ventana_login.title("Inicio de Sesión")
ventana_login.geometry("300x200")

frame_login = tk.Frame(ventana_login, padx=20, pady=20)
frame_login.pack(expand=True)

label_usuario = tk.Label(frame_login, text="Usuario:", font=("Helvetica", 12))
label_usuario.grid(row=0, column=0, pady=10, sticky="e")
entry_usuario = tk.Entry(frame_login)
entry_usuario.grid(row=0, column=1, pady=10)

label_contraseña = tk.Label(frame_login, text="Contraseña:", font=("Helvetica", 12))
label_contraseña.grid(row=1, column=0, pady=10, sticky="e")
entry_contraseña = tk.Entry(frame_login, show="*")
entry_contraseña.grid(row=1, column=1, pady=10)

button_login = tk.Button(frame_login, text="Iniciar Sesión", command=abrir_ventana_principal)
button_login.grid(row=2, column=0, columnspan=2, pady=20)

ventana_login.mainloop()
