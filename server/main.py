import http.server
import socketserver
from server_settings import ServerSettings

def default_settings():
    return ServerSettings(26777)

def run_server(settings):
    port = settings.port
    handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", port), handler) as httpd:
        print("serving at port", port)
        httpd.serve_forever()

def main():
    settings = default_settings()
    run_server(settings)

if __name__ == "__main__":
    main()

