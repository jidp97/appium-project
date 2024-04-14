#Pruebas Automatizadas de Aplicaciones Android con Appium en Python
Este repositorio contiene un proyecto de ejemplo para realizar pruebas automatizadas en aplicaciones Android utilizando Appium en Python. Appium es un marco de automatización de pruebas móviles de código abierto que permite probar aplicaciones nativas, híbridas y web en dispositivos móviles.

#Requisitos Previos
Python 3.x instalado en tu sistema.
Android Studio para la configuración y gestión de emuladores Android.
Conocimientos básicos de Python y pruebas automatizadas.
Instalación
Clona este repositorio en tu máquina local:
bash
Copy code
git clone https://github.com/jidp97/appium-project/
Instala las dependencias necesarias utilizando pip:
bash
Copy code
pip install Appium-Python-Client
Configuración del Proyecto
Configuración del Emulador
Asegúrate de tener un emulador Android configurado y en funcionamiento. Puedes usar Android Studio para crear y gestionar emuladores con diferentes configuraciones de dispositivos.

#Inicia Android Studio.
Navega a la sección AVD Manager (Android Virtual Device Manager).
Crea un nuevo emulador con la configuración deseada (modelo de dispositivo, versión de Android, RAM, almacenamiento, etc.).
Inicia el emulador para verificar que esté funcionando correctamente.
Descarga de la Aplicación
Descarga el archivo APK de la aplicación que deseas probar y guárdalo en la carpeta del proyecto.

#Configuración del Script
Abre el archivo script.py y modifica la ruta del archivo APK en el diccionario desired_caps con la ruta de tu archivo APK descargado.

Ejecución de las Pruebas
Asegúrate de tener el emulador Android en funcionamiento.
Inicia Appium Server en el puerto 4723.
Ejecuta el script de prueba automatizada utilizando Python:
bash
Copy code
python test_script.py
Contribuciones
¡Las contribuciones son bienvenidas! Si encuentras algún problema o tienes alguna mejora, por favor abre un issue o envía un pull request.

Licencia
Este proyecto está licenciado bajo la Licencia MIT.
