from pathlib import Path
from win32gui import GetWindowText, GetForegroundWindow
from pyautogui import hotkey, press
from time import sleep, time

def remove_blank_lines(file_path: str) -> None:
    """
    Removes all blank lines from a text file in-place.

    Parameters:
    - file_path (str): Path to the text file.

    Raises:
    - FileNotFoundError: If the specified file does not exist.
    """
    file = Path(file_path)
    if not file.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    with open(file, "r") as f:
        lines = [line for line in f if not line.isspace()]

    with open(file, "w") as f:
        f.writelines(lines)


def find_window_by_title(window_title: str, timeout: int = 12) -> bool:
    """
    Attempts to switch to a window by title using ALT+TAB navigation.

    Parameters:
    - window_title (str): The exact title of the window to switch to.
    - timeout (int): Max time (in seconds) to attempt the search. Default is 12.

    Returns:
    - bool: True if the window was found and switched to, False otherwise.
    """
    start_time = time()
    current_window = GetWindowText(GetForegroundWindow())

    while True:
        hotkey("win", "tab")
        sleep(0.75)
        press("left")
        sleep(0.25)
        press("enter")

        active_window = GetWindowText(GetForegroundWindow())
        if active_window == window_title:
            return True
        elif active_window == current_window or (time() - start_time > timeout):
            return False
