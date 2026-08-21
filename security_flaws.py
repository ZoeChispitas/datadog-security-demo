import os

# Fuga de API Key simulada (Secret Scanning)
DATADOG_API_KEY_LEAK = "ddp_fakeKeyForDatadogSecretScanningTest12345"

# Inyección de comandos vulnerable (SAST)
def execute_system_task(user_input):
    os.system(f"echo Proceso: {user_input}")
