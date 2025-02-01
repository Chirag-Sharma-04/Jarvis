import webbrowser as wb

def normal_commands(commands):
    if 'open YouTube' in commands: #yt
        url='https://www.youtube.com/'
        wb.get().open_new(url)