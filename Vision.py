import requests
import base64

def agente_vigilante(foto_path):
    # CAMBIA ESTA URL por la que te dio Ngrok (ej. https://1234-abcd.ngrok-free.app)
    url = "https://backing-yiddish-sprung.ngrok-free.dev/api/chat"
    
    print(f"--- 🛡️ Agente Vigilante (Vía Ngrok) ---")
    
    try:
        with open(foto_path, "rb") as image_file:
            img_base64 = base64.b64encode(image_file.read()).decode('utf-8')

        payload = {
            "model": "moondream",
            "messages": [
                {
                    "role": "user",
                    "content": "¿Qué hay en la imagen?",
                    "images": [img_base64]
                }
            ],
            "stream": False 
        }

        response = requests.post(url, json=payload)

        if response.status_code == 200:
            dictamen = response.json()['message']['content']
            print(f"\n[Dictamen]: {dictamen}")
        else:
            print(f"❌ Error: {response.status_code}")
            print(f"Detalle: {response.text[:200]}")

    except Exception as e:
        print(f"💥 Error: {e}")

agente_vigilante('imagen.jpg')
