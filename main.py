import http.server
import socketserver
import shutil


password = input('Create your password\n')

correct_pass = input('Enter your password\n')







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
        #change this to where the files folder path would be on your computer
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
        #change this to where the files folder path is on your computer 
        src = f'/opt/homebrew/Caskroom/miniforge/base/envs/CLI_pyproj/CLI_pythonproj/files/{take_out}'
        #change this to have it save to your desktop 
        dst = '/Users/[user]/Desktop'
        shutil.copy(src, dst)
        
        
        
        
login()






