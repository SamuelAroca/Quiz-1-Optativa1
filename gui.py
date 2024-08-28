import tkinter as tk
from tkinter import ttk

# Suponiendo que 'generar_recomendacion' esté definido en tu módulo 'destinos_perfectos'
from destinos_perfectos import generar_recomendacion

def recomendar_destinos():
    preferencias = preferencias_var.get() if preferencias_var.get() else None
    tipo_viaje = tipo_viaje_var.get() if tipo_viaje_var.get() else None
    presupuesto = presupuesto_var.get() if presupuesto_var.get() else None

    recomendaciones = generar_recomendacion(preferencias, tipo_viaje, presupuesto)

    resultado_var.set(", ".join(recomendaciones) if recomendaciones else "No hay recomendaciones disponibles")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Destinos Perfectos")
ventana.geometry("400x300")

# Variables para almacenar las selecciones del usuario
preferencias_var = tk.StringVar()
tipo_viaje_var = tk.StringVar()
presupuesto_var = tk.StringVar()
resultado_var = tk.StringVar()

# Crear un marco para organizar los widgets
frame = ttk.Frame(ventana, padding="20 20 20 20")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Ajustar el tamaño de las columnas y filas para que se expandan según el contenido
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_rowconfigure(0, weight=1)

# Etiquetas y Comboboxes
ttk.Label(frame, text="Preferencias:").grid(column=1, row=1, sticky=tk.W, pady=5)
preferencias_menu = ttk.Combobox(frame, textvariable=preferencias_var)
preferencias_menu['values'] = ("aventura", "playa", "ciudad", "naturaleza", "cultura")
preferencias_menu.grid(column=2, row=1, sticky=tk.EW, pady=5)

ttk.Label(frame, text="Tipo de viaje:").grid(column=1, row=2, sticky=tk.W, pady=5)
tipo_viaje_menu = ttk.Combobox(frame, textvariable=tipo_viaje_var)
tipo_viaje_menu['values'] = ("individual", "familiar", "grupal")
tipo_viaje_menu.grid(column=2, row=2, sticky=tk.EW, pady=5)

ttk.Label(frame, text="Presupuesto:").grid(column=1, row=3, sticky=tk.W, pady=5)
presupuesto_menu = ttk.Combobox(frame, textvariable=presupuesto_var)
presupuesto_menu['values'] = ("bajo", "medio", "alto")
presupuesto_menu.grid(column=2, row=3, sticky=tk.EW, pady=5)

# Botón para recomendar destinos
ttk.Button(frame, text="Recomendar Destino", command=recomendar_destinos).grid(column=2, row=4, pady=10)

# Etiqueta para mostrar las recomendaciones
ttk.Label(frame, text="Recomendaciones:").grid(column=1, row=5, sticky=tk.W, pady=5)
ttk.Label(frame, textvariable=resultado_var, wraplength=300).grid(column=2, row=5, sticky=tk.W, pady=5)

# Añadir un poco de espacio alrededor de los elementos
for child in frame.winfo_children():
    child.grid_configure(padx=10, pady=5)

# Ejecutar la aplicación
ventana.mainloop()
