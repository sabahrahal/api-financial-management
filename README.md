# API Financial Management

Esta es una API diseñada para la gestión financiera personal, construida utilizando **Flask**, **SQLAlchemy** y **MySQL**. Está diseñada con una arquitectura modular y buenas prácticas para facilitar su escalabilidad y mantenimiento.

## 🚀 Tecnologías Utilizadas

- **Python**: Lenguaje principal.
- **Flask**: Framework ligero para el desarrollo de aplicaciones web.
- **Flask-JWT-Extended**: Manejo de autenticación basada en tokens JWT.
- **SQLAlchemy**: ORM para interactuar con la base de datos.
- **MySQL**: Sistema de gestión de base de datos relacional.
- **python-dotenv**: Gestión de variables de entorno.

## 🛠️ Dependencias

Las principales dependencias del proyecto se encuentran en el archivo `requirements.txt`:

- `Flask==3.1.0`
- `Flask-SQLAlchemy==3.1.1`
- `Flask-JWT-Extended==4.7.1`
- `mysql-connector-python==9.1.0`
- `python-dotenv==1.0.1`
- `Werkzeug==3.1.3`
- `SQLAlchemy==2.0.36`

## ⚙️ Configuración del Proyecto

### 1. Clonar el repositorio
```bash
git clone https://github.com/sabahrahal/api-financial-management.git
cd api-financial-management
```

### Crear el entorno virtual
```bash
python -m venv venv
```

### Activar el entorno virtual
```bash
# En Windows:
.\venv\Scripts\activate

# En Linux/MacOS:
source venv/bin/activate
```

### Instalar dependencias
```bash
pip install -r requirements.txt
```
### Configurar las variables de entorno
```bash
DB_HOST=localhost
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
DB_NAME=mi_aplicacion
DB_PORT=3306
JWT_SECRET_KEY=mi_secreto_jwt_super_seguro
DEBUG=True
```
---

## 📋 Endpoints Principales

1. **Registro de Usuarios**
   - **Método**: `POST`
   - **URL**: `/auth/register`

2. **Inicio de Sesión**
   - **Método**: `POST`
   - **URL**: `/auth/login`

