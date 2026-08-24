import subprocess

def execute_system_task(user_input):
    # Ejecución segura mediante lista sin invocar un shell interactivo
    subprocess.run(["echo", f"Proceso: {user_input}"], check=False)
