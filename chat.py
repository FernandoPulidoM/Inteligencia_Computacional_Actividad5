#Proyecto de chat con Ollama, instalando el modelo qwen2.5:7b-instruct, basado en la documentacion de Ollama y la libreria requests para hacer peticiones HTTP.

#Gemini ayudo a buscar la libreria requests y la documentacion de Ollama

import requests #https://realpython.com/python-requests/ dio las ideas de como mandar post al endpoint de Ollama 

conversation = []#lista que tiene toda la conversacion

while True:
    user_input = input("Tu: ")

    if user_input.lower() == "salir":
        break

#formato de rol y contenido para cada mensaje viene de https://github.com/ollama/ollama/blob/main/docs/api.md#generate-a-chat-completion

    conversation.append({ # Guardar mensaje usuario
        "role": "user",#rol del mensaje
        "content": user_input #contenido del mensaje
    })

    response = requests.post( # idea de mandar modelo, message y stream de la seccion streaming process en https://github.com/ollama/ollama/blob/main/docs/api.md#generate-a-chat-completion
        "http://localhost:11434/api/chat",#endpoint de la API de Ollama
        json={
            "model":  "qwen2.5:7b-instruct",#modelo descargado
            "messages": conversation,
            "stream": False
        }
    )

    assistant_message = response.json()["message"]["content"]# response viene de https://github.com/ollama/ollama-python
    #se obteniea error de que no era compatible la respuesta, Gemini ayudo agregando la funcion de .json() 

    conversation.append({  # Guardar respuesta IA
        "role": "assistant",
        "content": assistant_message
    })

    print("\nAssistant:", assistant_message)#imprimir la respuesta 
    print()#espacio para legibilidad
