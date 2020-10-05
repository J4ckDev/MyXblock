# :scroll: MyXBlock <!-- omit in toc -->

El objetivo de la guía es orientar como crear XBlock, para la plataforma de OpenEDX, desarrollando a lo largo de esta guía el siguiente XBlock: 

<p align="center">
  <img width="200px" height="280px" alt="Ejemplo" src="https://i.pinimg.com/originals/ae/42/1e/ae421e54a839cff4f0ce6cc89940a7db.jpg">
</p>

## :clipboard: Contenido <!-- omit in toc -->

- [1. Introducción a los XBlock](#1-introducción-a-los-xblock)
  - [1.1. ¿Qué son los XBlocks?](#11-qué-son-los-xblocks)
  - [1.2. Estructura de un XBlock](#12-estructura-de-un-xblock)
- [2. Entorno de trabajo](#2-entorno-de-trabajo)
  - [2.1. Requisitos](#21-requisitos)
  - [2.2. Configuración del Entorno](#22-configuración-del-entorno)
- [3. Construcción del XBlock](#3-construcción-del-xblock)
  - [3.1. Creación del prototipo base](#31-creación-del-prototipo-base)
  - [3.2. Construir el XBlock](#32-construir-el-xblock)
  - [3.3 Probar el XBlock](#33-probar-el-xblock)

## 1. Introducción a los XBlock

### 1.1. ¿Qué son los XBlocks?

Los XBlocks son componentes que permiten aumentar las funcionalidades de aplicaciones web basadas en la plataforma OpenEDX, proporcionando flexibilidad en la creación de cursos en línea más atractivos, ya que los XBlocks en conjunto pueden brindar solución a problemas individuales, mostrar textos y videos en formato web, simulaciones interactivas, laboratorios o nuevas experiencias de aprendizaje colaborativo. Además, los XBlocks son componibles, permitiendo a los desarrolladores de XBlock controlar lo que muestren otros XBlock para componer lecciones, secciones y cursos completos.

### 1.2. Estructura de un XBlock

Un XBlock funciona de tal forma que mantiene su estado en una capa de almacenamiento, se representan así mismos a través de vistas y procesan las acciones del usuario a través de controladores, por esa razón se compone de 4 elementos, el **HTML** para su estructura, el **CSS** para su diseño, el **Javascript** para obtener las acciones del usuario y un **script de Python** para procesar dichas acciones.

## 2. Entorno de trabajo

### 2.1. Requisitos

Es importante contar con una versión de Ubuntu o Debian, contar con **Python 3.5 o mayor** e instalar las siguientes librerías mediante el *terminal*:

Librería|Comando de Instalación
:---|:---
GNOME XML library  | `sudo apt-get install libxml2-dev`
XSLT 1.0 processing library | `sudo apt-get install libxslt-dev`
Compression library 32-bit development | `sudo apt-get install lib32z1-dev`
IJG JPEG library | `sudo apt-get install libjpeg62-dev`
Virtualenv | `pip install virtualenv` 

### 2.2. Configuración del Entorno

Con las librerias necesarias instaladas, es momento de configurar el entorno de trabajo de la siguiente forma:

1. Crear una carpeta con el nombre que deseen, en mi caso la llamé *mi directorio* con el comando `mkdir midirectorio`.
2. Ingresar a la carpeta creada y ejecutar el comando `virtualenv venv`.
3. Iniciar el entorno virtual con el comando `source venv/bin/activate`. En mi caso luego de ejecutar el comando, en el terminal me apareció `(venv) jackdev@J4ckDev:~/midirectorio$`, el `(venv)` me indica que estoy trabajando en mi entorno virtual.
4. Obtener el XBlock SDK mediante el comando `git clone https://github.com/edx/xblock-sdk`.
5. por último, abrir la carpeta del proyecto clonado con `cd xblock-sdk` y ejecutar el comando `pip install -r requirements/base.txt` 

## 3. Construcción del XBlock   

### 3.1. Creación del prototipo base

Con el entorno virtual ejecutándose y el XBlock SDK configurado, se procede a crear la base para nuestro XBlock de la siguiente manera:

1. Asegurese de encontrarse en la carpeta padre, creada en el **paso 1** de la [sección 2.2](#22-configuración-del-entorno). En mi caso en el terminal aparece `(venv) jackdev@J4ckDev:~/midirectorio$` o si ejecuto el comando `pwd` obtengo `/home/J4ckDev/Documentos/midirectorio`.
2. Ejecutar el comando `xblock-sdk/bin/workbench-make-xblock` para crear un nuevo XBlock. Este comando desplegará 2 campos que se deben llenar, **Short Name** y **Class Name**, donde el primero debe ser un nombre corto y todo en minúsculas, mientras que para el segundo, se recomienda que tenga el mismo nombre corto pero obligatoriamente al final debe ir la palabra XBlock. En mi caso el **Short name** quedó como *myxblock* y el **Class name** quedó como *MyXBlock*.

<p align="center">
  <img width="350px" height="200px" alt="Short Name y Class Name" src="https://i.pinimg.com/originals/48/8d/a1/488da1dfe778135bdcf44fe667bfa30c.png">
</p>

3. Instalar el bloque en el XBlock SDK mediante el comando `pip install -e myxblock`.
4. Escribir el comando `mkdir ./xblock-sdk/var`, después  `cd xblock-sdk` y por último escribir el comando `make install`, este último comando se encargará de instalar todos los módulos, librerías y dependencias requeridas por el proyecto, finalmente realizará la migración de la base de datos. Este comando a su vez permite ver todos los XBlock instalados cuando se corra el servidor. 
5. Escribir el comando `python manage.py migrate`.
6. Por último, ejecutar el comando `python manage.py runserver` y en el navegador abrir la dirección `http://127.0.0.1:8000/`. Si todo está bien se debe ver nuestro XBlock creado, en mi caso aparece MyXBlock.

<p align="center">
  <img width="250px" height="250px" alt="Resultado Final" src="https://i.pinimg.com/originals/43/eb/52/43eb52bc444bd86ceeacd16f277a1a3c.png">
</p>

### 3.2. Construir el XBlock
Con lo desarrollado en la subsección anterior, creamos la estructura para el XBlock y en mi caso al llamarse myxblock, se generó el siguiente arbol de carpetas:

<p align="center">
  <img alt="Resultado Final" src="https://i.pinimg.com/originals/30/1a/ef/301aef5bbac7e4e4e1a5b7b53e59a146.png">
</p>

La carpeta de interés será **static**, ya que dentro encontraremos las carpetas contenedoras para los archivos *HTML, CSS* y *Javascript*; para el caso del *script de Python* que controlará esos archivos, lo encontramos por fuera de la carpeta static por el nombre, en mi caso, de `myxblock.py`. 

Ahora conociendo donde se encuentran los archivos, reemplazaremos con los siguientes fragmentos de código, el contenido del archivo que corresponda.

- Para el HTML, en mi caso `myxblock.html`:

```html
<div class="myxblock_block">
  <h3>Formulario de registro</h3>
  <form id="form">
    <div class="form-group">
      <label class="form-label" for="name">
        <i class="fa fa-id-card-o"></i> Nombres
      </label>
      <input id="name" name="name" type="text" placeholder="John" title="Sus Nombres" required />
    </div>
    <div class="form-group">
      <label class="form-label" for="lastname">
        <i class="fa fa-id-card-o"></i> Apellidos
      </label>
      <input id="lastname" name="lastname" type="text" placeholder="Doe" title="Sus Apellidos" required />
    </div>
    <div class="form-group">
      <label class="form-label" for="email">
        <i class="fa fa-envelope-o"></i> Correo
      </label>
      <input id="email" name="email" type="email" placeholder="email@email.com" title="Su Correo" required  />
    </div>
    <div class="form-button">
      <button id="Send">
        Enviar <i class="fa fa-send-o"></i>
      </button>
    </div>
  </form>  
</div>
<p id="data"></p>
```

Como se observa en el código, la estructura se compone por un formulario y una etiqueta `<p id="data"></p>`, la estructura se define así para que en el formulario se llenen los datos y en la etiqueta se reciban los datos procesados por el script de Python y sean mostrados.

- Para el CSS, en mi caso `myxblock.css`:

```css
/* CSS for MyXBlock */
@import url("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css");

.myxblock_block {
  display: flex;
  margin: 0.5em;
  text-align: center;
  justify-content: center;
  flex-wrap: wrap;
  width: 100%;
  border-radius: 15px;
  border: 1px black solid;
}

.myxblock_block h3 {
  text-align: center;
  padding: 0.5em 0;
  margin: 0%;
  width: 100%;
  border-radius: 15px 15px 0 0;
  background-color: rgba(206, 206, 206, 0.5);
}

#form {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
  box-sizing: border-box;
  margin: 0.2em;
  padding: 0.2em;
  width: 100%;
}

.form-group {
  margin: 0em;
  padding: 0em 1em;
  display: flex;
  justify-content: center;
  align-items: baseline;
  text-align: right;
  width: 30%;
}

.form-label {
  margin: 0.5em;
  padding: 0.5em;
  width: 30%;
}

#name,
#lastname,
#email {
  margin: 0.2em;
  outline-color: #065683;
  width: 60%;
}

.form-button {
  width: 100%;
  display: flex;
  padding: 0.5em;
  justify-content: center;
}

#Send {
  background-color: #0075b4;
  border: 2px solid #0075b4;
  border-radius: 5px;
  font-size: 1em;
  color: white;
  margin: 0px;
  padding: 5px 30px;
  cursor: pointer;
  transition: all 0.4s linear;
}

#Send:hover {
  background-color: #065683;
  border-color: #065683;
}

@media only screen and (max-width: 1370px) {
  .form-group {
    width: 40%;
  }
}

@media only screen and (max-width: 1060px) {
  #name,
  #lastname,
  #email {
    width: 50%;
  }
}
@media only screen and (max-width: 910px) {
  .form-group {
    text-align: left;
    width: 60%;
  }
  #name,
  #lastname,
  #email {
    width: 70%;
  }
}

@media only screen and (max-width: 740px) {
  .form-group {
    width: 100%;
  }
}

@media only screen and (max-width: 520px) {
  .form-group {
    flex-wrap: wrap;
  }
  .form-label {
    padding-left: 0em;
    margin-left: 0.2em;
    width: 100%;
  }
  #name,
  #lastname,
  #email {
    width: 100%;
  }
}

```

- Para el JS, en mi caso `myxblock.js`:

```javascript
/* Javascript for MyXBlock. */
function MyXBlock(runtime, element) {
    
    function updateData(result) {
        var sectionData = document.getElementById("data");
        sectionData.innerHTML = result.resultado;
	    document.getElementById("name").value = "";
        document.getElementById("lastname").value = "";
        document.getElementById("email").value = "";
    }

    var handlerUrl = runtime.handlerUrl(element, 'get_formdata');

    $('#Send', element).click(function (eventObject) {
        var name = document.getElementById("name").value;
        var lastname = document.getElementById("lastname").value;
        var email = document.getElementById("email").value;

        $.ajax({
	        type: "POST",
            url: handlerUrl,            
            data: JSON.stringify({ "name": name, "lastname": lastname, "email": email }),
            success: updateData
        });
    });

    $(function ($) {
        /* Here's where you'd do things on page load. */
    });
}
```

Este código Javascript hace uso de AJAX para generar la consulta por POST al servidor, cuando en el formulario la persona de click en el botón de enviar, y si se procesan correctamente los datos, los muestra en la etiqueta `<p id="data"></p>`

- Para el script de Python, en mi caso `myxblock.py`, solo hay que reemplazar la función que está debajo de `@XBlock.json_handler` por la siguiente:

```python
def get_formdata(self, data, suffix=''):
        formData = 'Los datos del usuario son:' + \
            "<br> Nombres: " + data['name'] + \
            "<br> Apellidos: " + data['lastname'] + \
            "<br> Email: " + data['email'] 
        return{"resultado":formData}
```

Está función es la que procesa la solicitud por POST generada en el archivo Javascript, lo que hace es recibir los datos del formulario, procesarlos y retornarlos en formato JSON para mostrarlos como:

```
Los datos del usuario son:
Nombres: NombresDelFormulario
Apellidos: ApellidosDelFormulario
Email: CorreoDelFormulario
```

### 3.3 Probar el XBlock

Con todo construido, es momento de abrir en el navegador la dirección `http://127.0.0.1:8000/`, seleccionar nuestro XBlock y ya deberíamos tener nuestro formulario listo para funcionar. En mi caso se obtuvo el siguiente resultado:

<p align="center">
  <img alt="Resultado con el formulario" src="https://i.pinimg.com/originals/67/2c/3b/672c3b83e50ec532b187eed3a47e539c.png">
</p>
