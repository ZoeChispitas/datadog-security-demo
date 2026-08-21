import subprocess
import os

# AWS Secret Key filtrada intencionalmente
AWS_SECRET_KEY = "AKIAIMNOJVGFDXYZEXAMPLEKEY12345"

def ping_host(host_address):
    # Vulnerabilidad de inyección de comandos en subprocess
    subprocess.call("ping -c 1 " + host_address, shell=True)
