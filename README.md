# Sango Bemoledor

SANGO BEMOLEDOR es una maravillosa aplicación web que además de ayudar a los músicos en necesidad, hace al mundo un mejor lugar, y más...

## Links

* [Website](http://54.149.97.239/)
* [Forum](http://54.149.97.239/foro/categoria/sitio)
* [Source code](https://github.com/CABT/proyecto-03/)

## Thanks

Gracias a:

* AndreaGonz
* Pernath

por la mayoria de la contribución de código.

Gracias a:

* Chucho
* Baez/CABT
* JuanCarlos

por apoyo general.




## Installation

**Instrucciones para correr la aplicación localmente**

Las instrucciones son muy sencillas, basta con descomprimir el tar.gz adjunto en el correo, 
colocarse en el directorio con una sesión de terminal activa, de tal manera que sea posible acceder modularmente
al contenido de los directorios como se ve a continuación:
## Diagrama
└── sangobemoledor
    
    ├── sangobemoledor/ -----> !!! /settings.py
    
    ├── registro/	
    
    ├── cuenta/ 		
    ├── foro/		
    ├── static/		
    ├── perfil/		
    
    └── registro/	
    
    ├── static/		
    ├── templates/
    ├── README.md	
    ├── Integrantes.txt
    ├── sangodb.sql       !!!
    └── manage.py         !!!
    ├── python_proy3/     !!!

    
 Prestaremos especial atención a los ficheros señalados con asteriscos. 
 
 Lo primero es restaurar la base de datos a partir del dump incluido con el comando psql 
 también es posible comenzar con una base de datos vacía y después hacer las migraciones de Django, lo dejamos a su consideración :
 	**[usuario@host sangobemoledor]$ psql base < sangodb.sql**
 Para completar este paso suponemos que PostgreSQL ya está instalado y configurado en su sistema operativo.
 
	Nota: para el ejemplo expuesto 'usuario' debe ser un Rol de Postgres, y ya debe existir una base de datos vacía con 	el nombre 'base' para que tenga éxito ($ createdb base). No nos detendremos a explicar la instalación de Postgres pues varia de sistema operativo a sistema operativo (recomendamos referirse a la documentación o wiki correspondiente, sin embargo podemos asegurar que el procedimiento no presenta problemas en Linux: ubuntu, 	archlinux y fedora.
	 
A continuación es muy importante que se configure correctamente la base de datos del proyecto en el fichero sangobemoledor/settings.py
a partir de la línea 62 el archivo, se encuentra algo como lo siguiente:
	
 Editar donde se señala para que corresponda con la base de datos local
 1//Nombre de la base de datos, donde se virtió el dump.sql.
 2//Role de postgres al que se asocia la base.
 3//Contraseña del dueño de la base de datos, puede no tener, como en este ejemplo (no recomendable).

	DATABASES = {
    		'default': {
        	'ENGINE': 'django.db.backends.postgresql_psycopg2',
        	'NAME': 'base',                                  //1 
	        'USER': 'usuario',                               //2
	        'PASSWORD': '',                                  //3  
	        'HOST': 'localhost',
	        'PORT': '5432',
    }
}

Fin de la edición para el usuario

Ya listo lo anterior, no antes de preferencia, prestamos atención al directorio python_proy3, ¿de qué se trata?, es un directorio que preparamos especialmente para facilitar al usuario la más pronta instalación de nuestra aplicación, gracias a Python-VirtualEnviroment, de tal manera que la aplicación no se vea afectada por los paquetes de python del sistema operativo donde se ejecute. E igualmente, evita al usuario instalar muchas más cosas necesarias para el  correcto funcionamiento del servidor. Si acaso la aventura de instalar y configurar PostgreSQL si nunca se ha vivido antes.

Para activar el entorno virtual basta con ejecutar lo siguiente:
	**[usuario@host sangobemoledor]$ source python_proy3/bin/activate**
Que resultará en algo parecido a:
	 (python_proy3)[usuario@host sangobemoledor]$ 
	
Finalmente corremos el servidor local de Django (nuestro querido FrameWork), de la manera que sigue:
	(python_proy3)[usuario@host sangobemoledor]$ python manage.py runserver

Que debe resultar en 
		Performing system checks...

		System check identified no issues (0 silenced).
		January 02, 2015 - 13:09:09
		Django version 1.7.1, using settings 'sangobemoledor.settings'
		Starting development server at http://127.0.0.1:8000/
		Quit the server with CONTROL-C.

Así que ya podemos visitar nuestro dirección local desde algún navegador para comenzar a navegar por la aplicación.
Si se presenta algún problema en este paso o desde un inicio deseaba utilizar una base de datos limpia, este par de comandos deben hacer que todo
marche bien (se ejecutan las migraciones de Django):
	(python_proy3)[usuario@host sangobemoledor]$ python manage.py makemigrations
	(python_proy3)[usuario@host sangobemoledor]$ python manage.py migrate
	Y volvemos a correr el servidor ;)
 
 

	
