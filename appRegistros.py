import tkinter as tk
from tkinter import ttk, messagebox
import requests

# Función para obtener los últimos 10 registros del Mckapi
def get_last_records():
    try:
        # Hacer la solicitud GET al Mockapi
        response = requests.get("https://66eb019a55ad32cda47b4cc5.mockapi.io/IoTCarStatus")
        response.raise_for_status()

        # Obtener los últimos 10 registros
        data = response.json()
        return data[-10:]  # Retorna los últimos 10 elementos
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"No se pudieron obtener los datos: {e}")
        return []

# Función para llenar la tabla con los datos obtenidos
def populate_table():
    records = get_last_records()
    table.delete(*table.get_children())  # Limpia la tabla antes de llenarla
    for record in records:
        print(record)  # Para verificar qué hay en cada registro
        # Insertar los valores de los campos correctos
        table.insert("", "end",
                     values=(record["id"], record["status"], record["date"], record["ipClient"], record["name"], record["direccion"]))

# Ventana principal
root = tk.Tk()
root.title("Últimos 10 registros de IoTCarStatus")
root.geometry("800x400")

# Crea la tabla
columns = ("ID", "Status", "Date", "IP Client", "Name", "Direction")
table = ttk.Treeview(root, columns=columns, show="headings")
table.heading("ID", text="ID")
table.heading("Status", text="Status")
table.heading("Date", text="Date")
table.heading("IP Client", text="IP Client")
table.heading("Name", text="Name")
table.heading("Direction", text="Direction")

# Ajustar el tamaño de las columnas
table.column("ID", anchor="center", width=50)
table.column("Status", anchor="center", width=100)
table.column("Date", anchor="center", width=150)
table.column("IP Client", anchor="center", width=150)
table.column("Name", anchor="center", width=200)
table.column("Direction", anchor="center", width=150)

# Crear el botón para refrescar la tabla
refresh_button = tk.Button(root, text="Refrescar", command=populate_table)
refresh_button.pack(pady=10)

# Ubicar la tabla en la ventana
table.pack(padx=10, pady=10, expand=True, fill="both")

# Ejecutar la aplicación
root.mainloop()
