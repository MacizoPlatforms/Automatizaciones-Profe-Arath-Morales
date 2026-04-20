import requests
import json
import os

def agente_analista(ruta_archivo):
    # 1. Verificar si el archivo existe
    if not os.path.exists(ruta_archivo):
        print(f"❌ Error: No encontré el archivo {ruta_archivo}")
        return

    # 2. Leer el contenido del .txt
    with open(ruta_archivo, 'r', encoding='utf-8') as f:
        fragmento_codigo = f.read()

    print(f"🔍 Analizando fragmento de: {ruta_archivo}...")

    # 3. Configuración de la petición al servidor
    url = "http://localhost:11434/api/chat"
    
    prompt_sistema = """Eres un experto en optimización de código y seguridad. 
    Analiza el siguiente código, encuentra posibles bugs y sugiere una versión más eficiente."""

    payload = {
        "model": "deepseek-coder:1.3b",
        "messages": [
            {"role": "system", "content": prompt_sistema},
            {"role": "user", "content": f"Aquí está el código:\n\n{fragmento_codigo}"}
        ],
        "stream": False # Para recibir el reporte completo de un solo golpe
    }

    # 4. Llamada al servidor mediante POST
    try:
        response = requests.post(url, json=payload)
        
        if response.status_code == 200:
            # 5. Procesar y mostrar el análisis
            resultado = response.json()
            print("\n" + "="*40)
            print("🚀 REPORTE DE OPTIMIZACIÓN DEEPSEEK")
            print("="*40)
            print(resultado['message']['content'])
        else:
            print(f"⚠️ Error del servidor: {response.status_code} - {response.text}")
        
    except Exception as e:
        print(f"💥 Error de conexión: {e}")

# Ejecución
if __name__ == "__main__":
    # Asegúrate de que este archivo existe en tu carpeta
    agente_analista('codigo_a_revisar.txt')
