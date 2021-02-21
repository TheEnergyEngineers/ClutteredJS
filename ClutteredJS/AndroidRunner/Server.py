from http.server import BaseHTTPRequestHandler, HTTPServer
import json

httpd = 0
PAGE_LOADED = False

class ExperimentHandler(BaseHTTPRequestHandler):

    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.end_headers()

    def do_GET(self):
        self._set_response()

        response = json.dumps({ 
            "path" : self.path,
            "message" : "Server is running!"
            }).encode('utf-8')

        self.wfile.write(response)

    def do_POST(self):
        global PAGE_LOADED

        length = int(self.headers['Content-Length'])
        data_string = self.rfile.read(length)
        data_string = data_string.decode("utf-8")
        
        PAGE_LOADED = True
        
        self._set_response()
        response = json.dumps({ 
            "message" : "Request recieved."
            }).encode('utf-8')

        self.wfile.write(response)

def start_server():
    """Start the server."""
    server_address = ('0.0.0.0', 8080)
    global httpd
    httpd = HTTPServer(server_address, ExperimentHandler)
    httpd.serve_forever()

def stop_server():
   """Stop the server."""
   global httpd
   httpd.server_close()

def reset_pageload():
    global PAGE_LOADED
    PAGE_LOADED = False

def wait_for_pageload():
    global PAGE_LOADED
    
    print("Waiting for PAGE_LOAD")
    while not PAGE_LOADED:
        pass
    print("PAGE_LOADED")

    return

if __name__=="__main__":
    start_server()