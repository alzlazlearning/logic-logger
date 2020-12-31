import win32gui


def enumerationCallaback(hwnd, results):
    text = win32gui.GetWindowText(hwnd)
    if text.find("Mozilla Firefox") >= 0:
        results.append((hwnd, text))

mywindows = []    


def recurseChildWindow(hwnd, results):
    win32gui.EnumChildWindows(hwnd, recurseChildWindow, results)
    print(hwnd, results)
    # try to get window class, text etc using SendMessage and see if it is what we want

mychildren = []
active_window_name = ""

# window = win32gui.GetForegroundWindow()
# # text = win32gui.GetWindowText(window)
# if text.find("Visual Studio Code") >= 0:
#     recurseChildWindow(mywindows[0][0], mychildren)

def get_active_window():
    window = win32gui.GetForegroundWindow()
    _active_window_name =win32gui. GetWindowText(window)
    return _active_window_name


while True:
    window = win32gui.GetForegroundWindow()
    text = win32gui.GetWindowText(window)
    new_window_name = get_active_window()
    
    if active_window_name != new_window_name:
        activity_name = active_window_name
        active_window_name = new_window_name
        
        if text.find("Mozilla Firefox") >= 0:
            win32gui.EnumWindows(enumerationCallaback, mywindows)
            for win, text in mywindows:
                print(text)
            recurseChildWindow(mywindows[0][0], mychildren)
