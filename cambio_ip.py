import smtplib
import subprocess

# Configuración de variables
fqdn = "wcentrix.net"
mail_to = "prueba@prueba.com"
mail_from = "prueba@prueba.com"
smtp_server = ""
smtp_port = 587
smtp_user = "prueba"
smtp_password = "password"
file = "cambio_ip.txt"

# Obtiene la dirección IP actual del FQDN
ip_temp = subprocess.check_output(['dig', '+short', fqdn, ]).decode().strip()
ip = ip_temp.split('\n')
ip.sort()

# Verifica si el archivo existe
try:
    with open(file, 'r') as f:
        last_ip_temp = f.read()
except FileNotFoundError:
    last_ip_temp = 'pepe'

last_ip = last_ip_temp.split('\n')
last_ip.sort()
if '' in last_ip: last_ip.remove('')

# Compara la dirección IP actual con la última dirección IP registrada
#print("IP \n" + str(ip))
#print("DIG \n" + str(last_ip))
if ip != last_ip:
    print("Las direcciones IP Cambiaron")
    # Si la dirección IP cambió, notifica por correo electrónico
    message = "La dirección IP de " + fqdn + " cambió a " + str(ip) + "."
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_user, smtp_password)
    server.sendmail(mail_from, mail_to, message.encode('utf-8'))
    server.quit()
    # Registra la nueva dirección IP en el archivo
    with open(file, 'w') as f:
        for elemento in ip:
            f.write(elemento + '\n')