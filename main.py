import http.server
import socketserver




correct_pass = '1234'

password = input('What is your password\n')







def login():
    if password == correct_pass:
        open = input('to save the file press S: ')
    if open == 'S':
        input('what is the file path: ')
        PORT = 8000
        handler = http.server.SimpleHTTPRequestHandler
        httpd = socketserver.TCPServer(("", PORT), handler)
        print(f"Server at PORT : {PORT}")
        httpd.serve_forever()
        userinput = input(':')
    else:
        print('try again')
    if userinput == 'S':
        global path 
        path = input('what is the file path : ')
    if path == path:
        print(f"To access your files go to : {PORT}")
        
login()






