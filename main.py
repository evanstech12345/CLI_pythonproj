import http.server
import socketserver
import shutil



correct_pass = '1234'

password = input('What is your password\n')







def login():
    if password == correct_pass:
        open = input('to save the file press S: ')
    else:
        print('Wrong password try again.')
    if open == 'S':
        file_path = input('what is the file path: ')
        src = file_path
        dst = '/opt/homebrew/Caskroom/miniforge/base/envs/CLI_pyproj/CLI_pythonproj/files'
        shutil.copy(src, dst)
        PORT = 8000
        handler = http.server.SimpleHTTPRequestHandler
        httpd = socketserver.TCPServer(("", PORT), handler)
        print(f"Server at PORT : {PORT}")
        httpd.serve_forever()
        
        
        
login()






