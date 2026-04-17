# yescrypt_task_cracker

## Descripción General
Este repositorio demuestra cómo crackear hashes de contraseñas `yescrypt` usando John the Ripper. Incluye scripts para generar hashes `yescrypt` a partir de una lista de contraseñas y un Makefile para automatizar partes del proceso.
## Requisitos Previos
Antes de empezar, asegúrate de tener instalado el siguiente software:
*   `john` (John the Ripper)
*   `mkpasswd` (parte del paquete `whois` en sistemas Debian/Ubuntu)
## Uso
### 1. Generar Hashes
El repositorio ya contiene `hashes.txt` con hashes pregenerados a partir de las contraseñas del archivo `passwd`.
Si quieres regenerar estos hashes, primero dale permisos de ejecución al script:
```sh
chmod +x hash.sh
```
Luego ejecútalo. **Nota:** Esto vaciará `hashes.txt` y creará un nuevo conjunto de hashes.
```sh
./hash.sh
```
### 2. Crackear Hashes
El método principal para crackear es usar John the Ripper con el wordlist `rockyou_1k.txt` incluido.
```sh
john hashes.txt --wordlist=rockyou_1k.txt --format=crypt
```
Alternativamente, el `Makefile` proporciona un comando `run` que acepta una cadena de palabras separadas por espacios.
```sh
make run WORDS='123456 password qwerty'
```
### 3. Ver Contraseñas Crackeadas
John the Ripper almacena las contraseñas crackeadas en `~/.john/john.pot`. Puedes ver los resultados con:
```sh
cat ~/.john/john.pot
```
La salida tendrá el formato `hash:contraseña`.
### 4. Limpiar
Para eliminar el directorio y los archivos generados por John the Ripper, ejecuta:
```sh
make clean
```
## Descripción de Archivos
*   `Makefile`: Contiene comandos de ayuda para ejecutar el proceso de crackeo (`make run`) y limpiar los archivos de salida (`make clean`).
*   `config.toml`: Archivo de configuración para el task runner, que especifica los requisitos del paquete y los archivos de entrada/salida.
*   `hash.sh`: Script para generar hashes `yescrypt` a partir del archivo `passwd`.
*   `hashes.txt`: El archivo objetivo que contiene los hashes `yescrypt` a crackear.
*   `passwd`: Lista de contraseñas en texto plano que usa `hash.sh` para generar `hashes.txt`.
*   `rockyou_1k.txt`: Archivo de diccionario de muestra con 1.000 contraseñas comunes para el crackeo.
