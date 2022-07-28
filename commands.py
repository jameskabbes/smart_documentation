import os
import webbrowser

os.system("python populate_config.py")
cwd = os.getcwd()
os.chdir(cwd + '\docs' + '\source')
os.system('python initial_write.py')
os.chdir(cwd + '\docs')
os.system("make html")
url = cwd + '\docs' + "\\build" + '\html' + '\index.html'
webbrowser.open(url, new=2)