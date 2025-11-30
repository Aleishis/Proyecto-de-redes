import http.client

def main():
    host = "127.0.0.1"
    port = 8080

    conn = http.client.HTTPConnection(host, port)
    mensaje = ''
    while mensaje != 'salir':
        
        mensaje = input("Escribe tu mensaje para enviar al servidor: ")
        

        # Enviar mensaje como POST
        conn.request("POST", "/", mensaje.encode(), {
            "Content-Type": "text/plain"
        })

        respuesta = conn.getresponse()
        cuerpo = respuesta.read().decode()

        print("\n--- Respuesta del servidor ---")
        print(cuerpo)

    conn.close()

if __name__ == "__main__":
    main()
