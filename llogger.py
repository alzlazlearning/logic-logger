from win32gui import GetWindowText, GetForegroundWindow
import requests

# print(r.url)
# print(GetWindowText(GetForegroundWindow()))


active_window_name = ""


current_win = ''

def get_active_window():
    window = GetForegroundWindow()
    _active_window_name = GetWindowText(window)
    return _active_window_name


while True:
    new_window_name = get_active_window()
    if active_window_name != new_window_name:
        print(new_window_name)
        activity_name = active_window_name
        active_window_name = new_window_name


