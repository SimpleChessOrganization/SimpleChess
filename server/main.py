import numpy 
class ServerSettings(obj):
    def __init__(port):
        self.port = port

def default_settings():
    return ServerSettings(26777)

def run_server(settings):
    pass

def main():
    settings = default_settings()
    run_server(settings)

