import socketserver, http.server

from resto_kreuzberg import *

HOST = "127.0.0.1"   
PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

restaurant_list = db_query()
# create HTML-Text from restaurants_finder.py
index = main_html(restaurant_list)

# create index file
def create_index(index):
    file= open("index.html","w+")
    file.write(index)
    file.close()

create_index(index)

# run server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Server running on port", PORT)
    httpd.serve_forever()