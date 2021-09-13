# Fix Screenshot

def screenshot():
    now = datetime.datetime.now()
    now_str = now.strftime("%Y-%m-%d-%H-%M-%S")
    outFile = pyautogui.screenshot('C:\\Users\\BeingMF\\Pictures\\ImageFile{}.PNG'.format(now_str))
