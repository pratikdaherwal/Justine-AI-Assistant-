# Task 2 -using user input shutdown/restart machine.

    elif 'shutdown' in query:
            if platform == "win32":
                os.system('shutdown /p /f')
            elif platform == "linux" or platform == "linux2" or "darwin":
                os.system('poweroff')

        elif 'restart' in query:
            if platform == "win32":
                os.system("restart /r /t  1")
            elif platform == "linux" or platform == "linux2" or "darwin":
                os.system("restart /r /t  1")
