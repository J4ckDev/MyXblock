# :scroll: MyXBlock <!-- omit in toc -->

El objetivo de la guía es orientar como crear un XBlock para la plataforma de OpenEDX, desarrollando a lo largo de esta guía el siguiente XBlock: 

<p align="center">
  <img  alt="Xblock antes de resolver" src="https://i.pinimg.com/originals/b7/16/d3/b716d31519649950a97ebbe442c49d26.png">
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
  - [3.2. Construcción del XBlock](#32-construcción-del-xblock)
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

1. Crear una carpeta con el nombre que deseen, en mi caso la llamé *midirectorio* con el comando `mkdir midirectorio`.
2. Ingresar a la carpeta creada y ejecutar el comando `virtualenv venv`.
3. Iniciar el entorno virtual con el comando `source venv/bin/activate`. En mi caso luego de ejecutar el comando, en el terminal me apareció `(venv) jackdev@J4ckDev:~/midirectorio$`, el `(venv)` me indica que estoy trabajando en mi entorno virtual.
4. Obtener el XBlock SDK mediante el comando `git clone https://github.com/edx/xblock-sdk`.
5. Abrir la carpeta del proyecto clonado con `cd xblock-sdk` y ejecutar el comando `pip install -r requirements/base.txt` 
6. Escribir el comando `mkdir ./var` y el comando `make install`, este último comando se encargará de instalar todos los módulos, librerías y dependencias requeridas por el SDK. Este comando a su vez permite ver todos los XBlock instalados cuando se corra el servidor. 
7. Realizar la migración de la base de datos con el comando `python manage.py migrate`.
8. Por último, si desea ejecutar el servidor del SDK hacerlo con `python manage.py runserver`.

## 3. Construcción del XBlock   

### 3.1. Creación del prototipo base

Con el entorno virtual ejecutándose y el XBlock SDK configurado, se procede a crear la base para nuestro XBlock de la siguiente manera:

1. Asegurese de encontrarse en la carpeta padre, creada en el **paso 1** de la [sección 2.2](#22-configuración-del-entorno). En mi caso en el terminal aparece `(venv) jackdev@J4ckDev:~/midirectorio$` o si ejecuto el comando `pwd` obtengo `/home/J4ckDev/Documentos/midirectorio`.
2. Ejecutar el comando `xblock-sdk/bin/workbench-make-xblock` para crear un nuevo XBlock. Este comando desplegará 2 campos que se deben llenar, **Short Name** y **Class Name**, donde el primero debe ser un nombre corto y todo en minúsculas, mientras que para el segundo, se recomienda que tenga el mismo nombre corto pero obligatoriamente al final debe ir la palabra XBlock. En mi caso el **Short name** quedó como *myxblock* y el **Class name** quedó como *MyXBlock*.

<p align="center">
  <img width="350px" height="200px" alt="Short Name y Class Name" src="https://i.pinimg.com/originals/48/8d/a1/488da1dfe778135bdcf44fe667bfa30c.png">
</p>

3. Instalar el bloque creado, en el XBlock SDK, mediante el comando `pip install -e myxblock`.
4. Por último, ejecutar el comando `python manage.py runserver` dentro de la carpeta del XBlock SDK y en el navegador abrir la dirección `http://127.0.0.1:8000/`. Si todo está bien se debe ver nuestro XBlock creado, en mi caso aparece MyXBlock.

<p align="center">
  <img width="250px" height="250px" alt="Resultado Final" src="https://i.pinimg.com/originals/43/eb/52/43eb52bc444bd86ceeacd16f277a1a3c.png">
</p>

### 3.2. Construcción del XBlock
Con lo desarrollado en la subsección anterior, creamos la estructura para el XBlock y en mi caso al llamarse myxblock, se generó el siguiente arbol de carpetas:

<p align="center">
  <img alt="Resultado Final" src="https://i.pinimg.com/originals/30/1a/ef/301aef5bbac7e4e4e1a5b7b53e59a146.png">
</p>

La carpeta de interés será **static**, ya que dentro encontraremos las carpetas contenedoras para los archivos *HTML, CSS* y *Javascript*; para el caso del *script de Python*, que controlará esos archivos, lo podemos encontrar por fuera de la carpeta static con el nombre de `myxblock.py`. 

Para construir el XBlock propuesto se realizaron las siguientes modificaciones:

1. **Código HTML:** La vista se hizo con el concepto de las plantillas de *Django*, el cuál hace uso de etiquetas especiales donde se pueden declarar variables y/o procesos como ciclos, condicionales, etc; la sintaxis de estas etiquetas es `{{ variable }}` y `{% proceso %}`. A continuación se puede observar el fragmento del código HTML donde hago uso de las etiquetas:
   
   ```html
    <div class="myxblock_block">
    <h2>Bienvenido a {{title}}</h2>
    {% if flag %}
    <h3>Sus datos registrados</h3>
    <p id="data">
      <strong>Nombres:</strong> {{name}} <br>
      <strong>Apellidos:</strong> {{lastname}} <br>
      <strong>Email:</strong> {{email}} <br><br>
      {{total}} estudiantes han respondido a este XBlock. <br>
    </p>  
    {% else %}
    <h3>Formulario de registro</h3>
    <form id="form" method="POST">...</form>
    {% endif %}
    </div>
   ```
    Como se puede observar la vista del XBlock está dividida en 2 partes por un condicional `{% if flag %}`, esto es para mostrar el formulario si no ha sido respondido por el usuario y si fue respondido, mostrará la vista donde muestra los datos almacenados `{{ name }}, {{ lastname }}, {{ email }}` y el `{{ total }}` de estudiantes o usuarios que han llenado el formulario.  El código completo de la vista se encuentra [aquí](https://github.com/J4ckDev/MyXblock/blob/main/myxblock/static/html/myxblock.html).
2. **Código CSS:** Los estilos implementados solo fueron para mejorar la presentación del XBlock y para que fuera responsive. Como es un código largo e irrelevante para la funcionalidad, dejo el enlace para ver el código [aquí](https://github.com/J4ckDev/MyXblock/blob/main/myxblock/static/css/myxblock.css).
3. **Código Javascript:** Será el encargado de procesar la información ingresada en el formulario, hará uso de *AJAX* para construir una consulta con método **POST**, a fin de enviar los datos al servidor y si recibe una respuesta positiva, actualizar la página para mostrar la información registrada. El código es el siguiente:
   ```javascript
   function MyXBlock(runtime, element) {
    
    var handlerUrl = runtime.handlerUrl(element, 'get_formdata');

        $('#Send', element).click(function (eventObject) {
        var name = document.getElementById("name").value;
        var lastname = document.getElementById("lastname").value;
        var email = document.getElementById("email").value;
        $.ajax({
            type: "POST",
            url: handlerUrl,                     
            data: JSON.stringify({ "name": name, "lastname": lastname, "email": email }),
            success: location.reload
        });
    });

    $(function ($) {
        /* Here's where you'd do things on page load. */
    });
   }
   ```
4. **Código Python:** Es el encargado de procesar todos los procesos del XBlock como renderizar las vistas, procesar la información y almacenarla. Para construir la lógica del Xblock es necesario conocer los siguientes conceptos:
   
   - **Campos o Fields:** Son los tipos de las variables que representan la información que almacena el XBlock y dependiendo de su *Alcance o Scope*, mostrará la información para uno o todos los usuarios. A continuación muestro los *Scope* y los *Fields* usados:  

      |Scope|Descripción|Sintaxis|
      |:----|:----------|:-------|
      |Estado de usuario|Este tipo de scope permite guardar la información de un estudiante en una única instancia del XBlock de un curso. Por ejemplo, un field que guarde las respuestas de un examen. |`Scope.user_state`|
      |Contenido|Este tipo de Scope es usado para guardar información que será mostrada por igual a todos los estudiantes y no necesita modificarse. Por ejemplo, un field que contenga el título del XBlock.|`Scope.content`|
      |Resumen de estados de usuario|Este Scope sirve para guardar y mostrar información general de todos los estudiantes. Por ejemplo, ver el número de estudiantes que hayan participado en una encuesta.|`Scope.user_state_summary`|

      Los otros valores de *Scope* disponibles se pueden encontrar en la <a href="https://edx.readthedocs.io/projects/xblock-tutorial/en/latest/concepts/fields.html" target="_blank" rel="noopener noreferrer">documentación oficial</a> y en uno de los <a href="https://github.com/edx/xblock-sdk/blob/master/sample_xblocks/basic/content.py" target="_blank" rel="noopener noreferrer">XBlock ejemplo</a> del SDK.

      |Field|Descripción|Sintaxis básica|
      |:----|:----------|:--------------|
      |String|Es una clase que representa una cadena, este puede ser `None` o cualquier texto.|`variable = String(default="", scope=Scope.user_state, help="String var")`|
      |Integer|Es una clase que representa un número entero, este puede ser `None`, un número entero de Python o un valor que se analizará como entero, es decir, algo para lo que `int(value)` no arroja un error.| `variable = Integer(default=0, scope=Scope.user_state, help="Integer var")`|
      |Boolean|Es una clase que representa un booleano, este puede ser un booleano de Python, una cadena o cualquier valor que se pueda convertir a booleano en el método `from_json`.|`variable = Boolean(default=False, scope=Scope.user_state, help="Boolean var")`|
      
      Como se pudo observar el valor *scope* y *help* están presentes en todos los tipos de Fields, esto es porque se debe definir a que usuario o usuarios se debe presentar la información almacenada y especificar los datos que almacena la variable respectivamente.  

      Se puede encontrar más información sobre los *Fields* <a href="https://edx.readthedocs.io/projects/xblock/en/latest/fields.html" target="_blank" rel="noopener noreferrer">aquí</a>.
      
    - **Renderizado de vistas:** Esto consiste en procesar las etiquetas especiales de la vista HTML, como los procesos contenidos dentro `{%%}` y/o reemplazar el valor de las variables contenidas en `{{}}`. Para lograr esto se hace uso de las siguientes librerías:

      | Librería | Descripción |
      | :------ | :------ |
      | Template | En Django esta clase es la encargada de compilar el código plantilla que reciba, normalmente son fragmentos HTML que incluyen propiedades que deben ser procesadas y compiladas. Un ejemplo de los fragmentos que compila es el siguiente `<p>Hola, me llamo {{nombre_usuario}}</p>`.  |
      | Context | Esta clase de Django, es la encargada de procesar las plantillas compiladas por la clase Template y mapear la información contenida en un diccionario, luego usando `Template.render(context)` se renderiza todo para generar una vista estática. Siguiendo el ejemplo anterior sería algo así:![Ejemplo de código](https://raw.githubusercontent.com/J4ckDev/XBlockPrueba/main/images/example.png)|      
    Ahora con todo más claro el código generado para el Xblock fue el siguiente:

    - **Librerías importadas**
      ```python
      import pkg_resources
      from xblock.fragment import Fragment
      from django.template import Context, Template
      from xblock.core import XBlock
      from xblock.fields import Integer, Scope, String, Boolean
      ```
      Las librerías `pkg_resources`, `XBlock`, `Integer` y `Scope`, son adicionadas automáticamente al momento de crear el [prototipo base](#31-creación-del-prototipo-base).

    - **Fields Definidos**
      Los campos creados fueron para guardar la información del usuario, el título del XBlock y el total de respuestas del formulario.
      ```python
      username = String(
        default="", scope=Scope.user_state,
        help="Nombre de usuario",
      )

      lastname = String(
          default="", scope=Scope.user_state,
          help="Apellido del usuario",
      )

      email = String(
          default="", scope=Scope.user_state,
          help="Correo del usuario",
      )

      title = String(
          default="MyXBlock", scope=Scope.content,
          help="Título del XBlock"
      )

      totalAnswers = Integer(
          default=0, scope=Scope.user_state_summary,
          help="Total de respuestas"
      )

      flag = Boolean(
          default=False, scope=Scope.user_state,
          help="Bandera para saber si fue resuelto el formulario"
      )
      ```

    - **Renderizado de las vistas**      
      ```python
        def load_resource(self, resource_path):
        """
        Gets the content of a resource
        """
        resource_content = pkg_resources.resource_string(__name__, resource_path)
        return resource_content.decode("utf8")
      ```
      Esta función será la encargada de obtener el archivo que contiene la vista del XBlock o el fragmento de código HTML para compilarlo. 
      ```python
        def render_template(self, template_path, context={}):
        """
        Evaluate a template by resource path, applying the provided context
        """
        template_str = self.load_resource(template_path)
        return Template(template_str).render(Context(context))
      ```
      Esta función se encargará de hacer uso de *load_resource* para obtener la plantilla compilada y con el diccionario de datos que reciba, realizará la renderización de la vista o fragmento HTML a mostrar.

    - **Student View**
      ```python
      def student_view(self, context=None):
        """
        The primary view of the MyXBlock, shown to students
        when viewing courses.
        """
        context = {
            'flag': self.flag,
            'name': self.username,
            'lastname': self.lastname,
            'email': self.email,
            'title': self.title,
            'total': self.totalAnswers,
        }
        
        html = self.render_template("static/html/myxblock.html", context)
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/myxblock.css"))
        frag.add_javascript(self.resource_string("static/js/src/myxblock.js"))
        frag.initialize_js('MyXBlock')
        return frag
      ```
      El diccionario de datos que se le pasa a `render_template`, es con todos los campos o fields definidos anteriormente y después, haciendo uso de frag, se adiciona el css y el javascript para retornar la vista construida en su totalidad.
    - **JSON Handler o Controlador** 
      ```python
      @XBlock.json_handler
      def get_formdata(self, data, suffix=''):
        self.username = data['name']
        self.lastname = data['lastname']
        self.email = data['email']
        self.totalAnswers += 1
        self.flag = True
        self.student_view()  
      ```
      Esta función es la encargada de procesar la solicitud enviada por el código Javascript, definido anteriormente, para guardar la información en los fields definidos anteriormente. Al final de la función se vuelve a llamar a `student_view` para renderizar de nuevo la vista y mostrar los valores registrados cuando el código Javascript actualice la página mediante `location.reload`. 
### 3.3 Probar el XBlock

Con todo construido, es momento de abrir en el navegador la dirección `http://127.0.0.1:8000/`, seleccionar nuestro XBlock y ya deberíamos tener nuestro formulario listo para funcionar. Al momento de llenar la información obtuve el siguiente resultado:

<p align="center">
  <img alt="Resultado con el formulario" src="https://i.pinimg.com/originals/bc/23/a6/bc23a6247b26761ef71b99fd3956011b.png">
</p>

Es posible simular otros usuarios escribiendo al final del enlace de cualquier XBlock `?student=valor`, donde valor puede ser un número o un texto. En mi caso simulé un estudiante con ID 17, por lo que el enlace en el navegador quedó como `http://127.0.0.1:8000/scenario/myxblock.0/?student=17`, luego de rellenar la información obtuve lo siguiente:

<p align="center">
  <img alt="Resultado con el formulario" src="https://i.pinimg.com/originals/8d/41/c9/8d41c9c52f6e6e8f96967cdbdd097e6e.png">
</p>

Como se puede observar, aumentó el valor de los estudiantes que han respondido el formulario.  
Sí deseas aprender como instalar un XBlock en la plataforma de OpenEDX y conocer como obtener datos de entorno, te invito a que visites [mi otro repositorio](https://github.com/J4ckDev/XBlockPrueba).
