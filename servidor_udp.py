from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):


    def do_POST(self):
        # Leer longitud del mensaje enviado por el cliente
        longitud = int(self.headers["Content-Length"])
        datos = self.rfile.read(longitud).decode()

        print(f"Mensaje recibido del cliente: {datos}")

        # Respuesta del servidor
        respuesta = f"Servidor recibió tu mensaje: {datos}"

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(respuesta.encode())

def run():
    server = HTTPServer(("0.0.0.0", 8080), MyHandler)
    print("Servidor HTTP listo en http://localhost:8080")
    server.serve_forever()

if __name__ == "__main__":
    run()