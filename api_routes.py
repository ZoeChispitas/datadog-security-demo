import subprocess

def ping_host(host_address):
    # Ejecución segura pasando argumentos como lista y sin shell=True
    subprocess.run(["ping", "-c", "1", host_address], check=False)
