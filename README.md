# Aplicación de Gestión de Tareas - Proyecto SIS-123

![Flask](https://img.shields.io/badge/Flask-v2.3.2-orange)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![SQLite](https://img.shields.io/badge/SQLite-Lightgrey)

---

## Descripción

Aplicación web sencilla desarrollada con Flask y SQLite para la materia **Ingeniería de Sistemas (SIS-123)**.  
Permite crear, editar, listar y gestionar tareas con título, descripción, fecha, hora y estado (completada o pendiente).

---

## Funcionalidades

- Crear nuevas tareas con detalles completos.  
- Visualizar tareas ordenadas por fecha y hora.  
- Editar tareas existentes.  
- Marcar tareas como completadas o pendientes.  
- Eliminar tareas.

---

## Tecnologías usadas

- Python 3.x  
- Flask  
- Flask-SQLAlchemy  
- SQLite  

---
## Estructura del proyecto
```
├── app.py # Archivo principal con la lógica de Flask
├── requirements.txt # Archivo con las dependencias del proyecto
├── todo.db # Base de datos SQLite (se crea automáticamente)
└── templates/ # Carpeta que contiene las plantillas HTML
├── index.html # Vista principal que lista las tareas
└── form.html # Formulario para agregar o editar tareas
```
---




