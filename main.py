import http.server
import socketserver
import shutil
import bcrypt

password = '1234'
hashedpass = bcrypt.hashpw(password, bcrypt.gensalt(5))

correct_pass = hashedpass
print(correct_pass)

password = input('What is your password\n')







def login():
    if password == correct_pass:
        file_open_save = input("""to save the file press S
to open the file press O
if you want to take a file out press T
\n""")
        
    else:
        print('Wrong password try again.')
    if file_open_save == 'S':
        file_path = input('what is the file path: ')
        src = file_path
        dst = '/opt/homebrew/Caskroom/miniforge/base/envs/CLI_pyproj/CLI_pythonproj/files'
        shutil.copy(src, dst)
        print(file_open_save)
    if file_open_save == 'O':
        PORT = 8000
        handler = http.server.SimpleHTTPRequestHandler
        httpd = socketserver.TCPServer(("", PORT), handler)
        print(f"Server at PORT : {PORT}")
        httpd.serve_forever()
    if file_open_save == 'T':
        take_out = input('what is the file name')
        src = f'/opt/homebrew/Caskroom/miniforge/base/envs/CLI_pyproj/CLI_pythonproj/files/{take_out}'
        dst = '/Users/evanshor/Desktop'
        shutil.copy(src, dst)
        
        
        
        
login()






