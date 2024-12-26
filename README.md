# 🚀 **Gestor de Proyectos**

### **Descripción General**
**Gestor de Proyectos** es una aplicación web desarrollada con **Django** que permite a usuarios crear y administrar espacios de trabajo, proyectos, tareas y colaboradores de manera eficiente. Diseñada para equipos que buscan optimizar la gestión de proyectos y tareas, ofreciendo una experiencia clara, intuitiva y colaborativa.

## Inicio sin necesidad de iniciar sesión
Puedes ver sin necesidad de loguearte, la página de **Inicio**, **Sobre la aplicación** y **Sobre mí**. En un **dropdown**, tendrás la posibilidad de iniciar sesión o registrarte.

---

## 📚 **Características Principales**
1. **Espacios de Trabajo**  
   - Crear y gestionar espacios de trabajo.  
   - Administrador único por espacio.  
   - Agregar colaboradores manualmente mediante su nombre de usuario.

2. **Proyectos**  
   - Crear proyectos dentro de un espacio de trabajo.  
   - Editar y eliminar proyectos.  
   - Acceso limitado a administradores y colaboradores.

3. **Tareas**  
   - Crear tareas dentro de un proyecto.  
   - Asignar tareas a colaboradores específicos.  
   - Editar y eliminar tareas (solo para administradores y asignados).  
   - Comentar tareas.

4. **Colaboradores**  
   - Administrador puede agregar colaboradores manualmente por nombre de usuario.  
   - Visualización clara de roles y permisos.

5. **Autenticación**  
   - Sistema de registro e inicio de sesión seguro.  
   - Edición de perfil y cambio de contraseña.  
   - Subida de avatar personal.

6. **Panel de Administración**  
   - Vista exclusiva para superusuarios que permite listar todos los usuarios registrados en el sistema.

---

## 🛠️ **Tecnologías Utilizadas**
- **Backend:** Django 4.2  
- **Frontend:** HTML5, CSS3, Bootstrap  
- **Base de Datos:** SQLite  
- **Autenticación:** Sistema de autenticación de Django  
- **Despliegue:** Preparado para entornos de producción  

---

## 📂 **Estructura del Proyecto**
```
gestor_proyectos/
├── App/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   │   ├── App/
│   │   │   ├── base.html
│   │   │   ├── dashboard.html
│   │   │   ├── crear_espacio.html
│   │   │   ├── espacio_detalle.html
│   │   │   ├── proyecto_detalle.html
│   │   │   ├── editar_proyecto.html
│   │   │   ├── eliminar_proyecto.html
│   │   │   ├── editar_tarea.html
│   │   │   ├── eliminar_tarea.html
│   │   │   ├── agregar_colaborador_manual.html
│   │   │   ├── 403.html
|   |   |   ├── crear_proyecto.html
│   │   │   ├── crear_tarea.html
|   |   |   ├── editar_espacio.html
│   │   │   ├── eliminar_espacio.html
│   │   │   ├── index.html
│   │   │   ├── lista_usuarios.html
│   │   │   ├── sobre_aplicacion.html
│   │   │   ├── sobre_mi.html
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│
├── usuarios/
│   ├── migrations/
│   ├── templates/
│   │   ├── usuarios/
│   │   │   ├── agregar_avatar.html
│   │   │   ├── cambiar_contrasenia.html
│   │   │   ├── editar_usuario.html
│   │   │   ├── login.html
│   │   │   ├── registro.html
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│
├── configuracion/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── media/ (Avatares y archivos subidos por usuarios)
├── manage.py
└── README.md
```

---

## ⚙️ **Instalación y Configuración**
1. **Clonar el repositorio:**  
   ```bash
   git clone https://github.com/LautaroPetersen/Proyecto_final.git
   cd gestor-proyectos
   ```

2. **Crear un entorno virtual:**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instalar dependencias:**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Realizar migraciones:**  
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Crear un superusuario:**  
   ```bash
   python manage.py createsuperuser
   ```

6. **Iniciar el servidor de desarrollo:**  
   ```bash
   python manage.py runserver
   ```

7. **Acceder a la aplicación:**  
   - Usuario: `http://127.0.0.1:8000/`  
   - Admin: `http://127.0.0.1:8000/admin/`

---

## 🔒 **Permisos y Roles**
- **Superusuario:** Acceso total, incluido el panel de administración y la lista de usuarios.  
- **Administrador del Espacio:** Puede crear, editar y eliminar proyectos, tareas y colaboradores.  
- **Colaborador:** Puede visualizar, editar y comentar tareas asignadas.  

---

## 📈 **Futuras Mejoras**
1. Sistema de notificaciones por correo electrónico.  
2. Integración con herramientas externas (e.g., Slack, Trello).  
3. Reportes automáticos y gráficos de progreso.  
4. Funcionalidad de archivos adjuntos en tareas.  

---

## 📧 **Contacto**
- **Desarrollador:** Lautaro Petersen  


---

## 📝 **Licencia**
Este proyecto está bajo la licencia **MIT**. Puedes ver más detalles en el archivo `LICENSE`.

---

¡Gracias por usar **Gestor de Proyectos**! 🚀✨
