# cambio_ip
Detecta un cambio de IP de un dominio y manda correo

*prerrequisitos *

```
sudo apt-get update
sudo apt-get install python3
sudo apt-get install python3-pip
pip3 install dnspython
```

*configurar parametros dentro de cambio_ip.py*

```
# Configuración de variables
fqdn = "wcentrix.net"
mail_to = "prueba@prueba.com"
mail_from = "prueba@prueba.com"
smtp_server = ""
smtp_port = 587
smtp_user = "prueba"
smtp_password = "password"
```

*correr el script *
```
python3 cambio_ip.py
```
