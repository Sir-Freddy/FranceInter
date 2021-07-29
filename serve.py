import http.server


port = 5000
address = ("", port)

server = http.server.HTTPServer

handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ["/"]

httpd = server(address, handler)

print(f"Serveur démarré à l'addresse http://localhost:{port}")

httpd.serve_forever()