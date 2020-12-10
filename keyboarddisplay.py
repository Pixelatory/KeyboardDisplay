import sys
import tkinter as tk
from concurrent.futures.thread import ThreadPoolExecutor
from pynput import keyboard
from pynput.keyboard import Key

global window, canvas, listenerrrr
labels = []


#  https://stackoverflow.com/questions/45905665/is-there-a-way-to-clear-all-widgets-from-a-tkinter-window-in-one-go-without-refe
def allWindowElements():
    global window
    _list = window.winfo_children()

    for item in _list:
        if item.winfo_children():
            _list.extend(item.winfo_children())

    return _list


def parseKey(key):
    if key == Key.esc:
        return 'esc'
    elif key == Key.space:
        return 'space'
    elif key == Key.shift_r:
        return 'shiftr'
    elif key == Key.shift:
        return 'shift'
    elif key == Key.backspace:
        return 'backspace'
    elif key == Key.tab:
        return 'tab'
    elif key == Key.caps_lock:
        return 'capslock'
    elif key == Key.ctrl_l:
        return 'ctrl'
    elif key == Key.ctrl_r:
        return 'ctrlr'
    elif key == Key.cmd:
        return 'cmd'
    elif key == Key.alt_l:
        return 'alt'
    elif key == Key.alt_gr:
        return 'altr'
    elif key == Key.menu:
        return 'menu'
    elif key == Key.enter:
        return 'enter'
    elif key == Key.f1:
        return 'f1'
    elif key == Key.f2:
        return 'f2'
    elif key == Key.f3:
        return 'f3'
    elif key == Key.f4:
        return 'f4'
    elif key == Key.f5:
        return 'f5'
    elif key == Key.f6:
        return 'f6'
    elif key == Key.f7:
        return 'f7'
    elif key == Key.f8:
        return 'f8'
    elif key == Key.f9:
        return 'f9'
    elif key == Key.f10:
        return 'f10'
    elif key == Key.f11:
        return 'f11'
    elif key == Key.f12:
        return 'f12'
    elif key == Key.print_screen:
        return 'printscreen'
    elif key == Key.scroll_lock:
        return 'scrolllock'
    elif key == Key.pause:
        return 'pause'
    elif key == Key.insert:
        return 'insert'
    elif key == Key.home:
        return 'home'
    elif key == Key.page_up:
        return 'pageup'
    elif key == Key.delete:
        return 'delete'
    elif key == Key.end:
        return 'end'
    elif key == Key.page_down:
        return 'pagedown'
    elif key == Key.up:
        return 'up'
    elif key == Key.left:
        return 'left'
    elif key == Key.down:
        return 'down'
    elif key == Key.right:
        return 'right'
    else:
        return key.char


def createButton(id, key, r, c, colSpan=1):
    global window
    tmp = tk.Label(window,
                   text=key,
                   fg="black",
                   bg="white",
                   width=5 * colSpan,
                   height=2)
    tmp.grid(row=r, column=c, columnspan=colSpan)
    labels.append((id, tmp))


def createSpace(r, c):
    global window
    tmp = tk.Label(window,
                   text=None,
                   fg=None,
                   bg=None,
                   width=5,
                   height=2)
    tmp.grid(row=r, column=c)


def on_press(key):
    key = parseKey(key)
    for label in labels:
        if type(label[0]) is list:
            for l in label[0]:
                if l == key:
                    label[1].config(bg="deep sky blue")
                    break
        elif label[0] == key:
            label[1].config(bg="deep sky blue")


def on_release(key):
    key = parseKey(key)
    for label in labels:
        if type(label[0]) is list:
            for l in label[0]:
                if l == key:
                    label[1].config(bg="white")
                    break
        elif label[0] == key:
            label[1].config(bg="white")


def qwertyLayout():
    global labels, window
    labels = []  # clear out labels

    widget_list = allWindowElements()  # delete all window elements
    for item in widget_list:
        item.destroy()

    setUpBaseFrame()

    createButton('esc', "ESC", 0, 0)
    createSpace(0, 1)
    createButton('f1', "F1", 0, 1)
    createButton('f2', "F2", 0, 2)
    createButton('f3', "F3", 0, 3)
    createButton('f4', "F4", 0, 4)

    createButton('f5', 'F5', 0, 5)
    createButton('f6', 'F6', 0, 6)
    createButton('f7', 'F7', 0, 7)
    createButton('f8', 'F8', 0, 8)
    createButton('f9', 'F9', 0, 9)
    createButton('f10', 'F10', 0, 10)
    createButton('f11', 'F11', 0, 11)
    createButton('f12', 'F12', 0, 12)

    createButton(['`', '~'], "~\n`", 1, 0)
    createButton(['1', '!'], '!\n1', 1, 1)
    createButton(['2', '@'], '@\n2', 1, 2)
    createButton(['3', '#'], '#\n3', 1, 3)
    createButton(['4', '$'], '$\n4', 1, 4)
    createButton(['5', '%'], '%\n5', 1, 5)
    createButton(['6', '^'], '^\n6', 1, 6)
    createButton(['7', '&'], '&\n7', 1, 7)
    createButton(['8', '*'], '*\n8', 1, 8)
    createButton(['9', '('], '(\n9', 1, 9)
    createButton(['0', ')'], ')\n0', 1, 10)
    createButton(['-', '_'], '_\n-', 1, 11)
    createButton(['=', '+'], '+\n=', 1, 12)
    createButton('backspace', '<--', 1, 13)

    createButton('tab', 'TAB', 2, 0)
    createButton(['q', 'Q'], 'Q', 2, 1)
    createButton(['w', 'W'], 'W', 2, 2)
    createButton(['e', 'E'], 'E', 2, 3)
    createButton(['r', 'R'], 'R', 2, 4)
    createButton(['t', 'T'], 'T', 2, 5)
    createButton(['y', 'Y'], 'Y', 2, 6)
    createButton(['u', 'U'], 'U', 2, 7)
    createButton(['i', 'I'], 'I', 2, 8)
    createButton(['o', 'O'], 'O', 2, 9)
    createButton(['p', 'P'], 'P', 2, 10)
    createButton(['[', '{'], '{\n[', 2, 11)
    createButton([']', '}'], '}\n]', 2, 12)
    createButton(['\\', '|'], '|\n\\', 2, 13)

    createButton('capslock', 'CAPS', 3, 0)
    createButton(['a', 'A'], 'A', 3, 1)
    createButton(['s', 'S'], 'S', 3, 2)
    createButton(['d', 'D'], 'D', 3, 3)
    createButton(['f', 'F'], 'F', 3, 4)
    createButton(['g', 'G'], 'G', 3, 5)
    createButton(['h', 'H'], 'H', 3, 6)
    createButton(['j', 'J'], 'J', 3, 7)
    createButton(['k', 'K'], 'K', 3, 8)
    createButton(['l', 'L'], 'L', 3, 9)
    createButton([':', ';'], ':\n;', 3, 10)
    createButton(['"', '\''], '"\n\'', 3, 11)
    createButton('enter', 'ENTER', 3, 12, 2)

    createButton('shift', 'SHIFT', 4, 0, 2)
    createButton(['z', 'Z'], 'Z', 4, 2)
    createButton(['x', 'X'], 'X', 4, 3)
    createButton(['c', 'C'], 'C', 4, 4)
    createButton(['v', 'V'], 'V', 4, 5)
    createButton(['b', 'B'], 'B', 4, 6)
    createButton(['n', 'N'], 'N', 4, 7)
    createButton(['m', 'M'], 'M', 4, 8)
    createButton([',', '<'], '<\n,', 4, 9)
    createButton(['>', '.'], '>\n.', 4, 10)
    createButton(['?', '/'], '?\n/', 4, 11)
    createButton('shiftr', 'SHIFT', 4, 12, 2)

    createButton('ctrl', 'CTRL', 5, 0)
    createButton('cmd', 'CMD', 5, 1)
    createButton('alt', 'ALT', 5, 2)
    createButton('space', 'SPACE', 5, 3, 7)
    createButton('altr', 'ALT', 5, 10)
    createButton(None, 'FN', 5, 11)
    createButton('menu', 'MENU', 5, 12)
    createButton('ctrlr', 'CTRL', 5, 13)


def colemakLayout():
    global labels
    labels = []  # clear out labels

    widget_list = allWindowElements()  # delete all window elements
    for item in widget_list:
        item.destroy()

    setUpBaseFrame()

    createButton('esc', "ESC", 0, 0)
    createSpace(0, 1)
    createButton('f1', "F1", 0, 1)
    createButton('f2', "F2", 0, 2)
    createButton('f3', "F3", 0, 3)
    createButton('f4', "F4", 0, 4)

    createButton('f5', 'F5', 0, 5)
    createButton('f6', 'F6', 0, 6)
    createButton('f7', 'F7', 0, 7)
    createButton('f8', 'F8', 0, 8)
    createButton('f9', 'F9', 0, 9)
    createButton('f10', 'F10', 0, 10)
    createButton('f11', 'F11', 0, 11)
    createButton('f12', 'F12', 0, 12)

    createButton(['`', '~'], "~\n`", 1, 0)
    createButton(['1', '!'], '!\n1', 1, 1)
    createButton(['2', '@'], '@\n2', 1, 2)
    createButton(['3', '#'], '#\n3', 1, 3)
    createButton(['4', '$'], '$\n4', 1, 4)
    createButton(['5', '%'], '%\n5', 1, 5)
    createButton(['6', '^'], '^\n6', 1, 6)
    createButton(['7', '&'], '&\n7', 1, 7)
    createButton(['8', '*'], '*\n8', 1, 8)
    createButton(['9', '('], '(\n9', 1, 9)
    createButton(['0', ')'], ')\n0', 1, 10)
    createButton(['-', '_'], '_\n-', 1, 11)
    createButton(['=', '+'], '+\n=', 1, 12)
    createButton('backspace', '<--', 1, 13)

    createButton('tab', 'TAB', 2, 0)
    createButton(['q', 'Q'], 'Q', 2, 1)
    createButton(['w', 'W'], 'W', 2, 2)
    createButton(['f', 'F'], 'F', 2, 3)
    createButton(['p', 'P'], 'P', 2, 4)
    createButton(['g', 'G'], 'G', 2, 5)
    createButton(['j', 'J'], 'J', 2, 6)
    createButton(['l', 'L'], 'L', 2, 7)
    createButton(['u', 'U'], 'U', 2, 8)
    createButton(['y', 'Y'], 'Y', 2, 9)
    createButton([';', ':'], ':\n;', 2, 10)
    createButton(['[', '{'], '{\n[', 2, 11)
    createButton([']', '}'], '}\n]', 2, 12)
    createButton(['\\', '|'], '|\n\\', 2, 13)

    createButton('capslock', 'CAPS', 3, 0)
    createButton(['a', 'A'], 'A', 3, 1)
    createButton(['r', 'R'], 'R', 3, 2)
    createButton(['s', 'S'], 'S', 3, 3)
    createButton(['t', 'T'], 'T', 3, 4)
    createButton(['d', 'D'], 'D', 3, 5)
    createButton(['h', 'H'], 'H', 3, 6)
    createButton(['n', 'N'], 'N', 3, 7)
    createButton(['e', 'E'], 'E', 3, 8)
    createButton(['i', 'I'], 'I', 3, 9)
    createButton(['o', 'O'], 'O', 3, 10)
    createButton(['"', '\''], '"\n\'', 3, 11)
    createButton('enter', 'ENTER', 3, 12, 2)

    createButton('shift', 'SHIFT', 4, 0, 2)
    createButton(['z', 'Z'], 'Z', 4, 2)
    createButton(['x', 'X'], 'X', 4, 3)
    createButton(['c', 'C'], 'C', 4, 4)
    createButton(['v', 'V'], 'V', 4, 5)
    createButton(['b', 'B'], 'B', 4, 6)
    createButton(['k', 'K'], 'K', 4, 7)
    createButton(['m', 'M'], 'M', 4, 8)
    createButton([',', '<'], '<\n,', 4, 9)
    createButton(['>', '.'], '>\n.', 4, 10)
    createButton(['?', '/'], '?\n/', 4, 11)
    createButton('shiftr', 'SHIFT', 4, 12, 2)

    createButton('ctrl', 'CTRL', 5, 0)
    createButton('cmd', 'CMD', 5, 1)
    createButton('alt', 'ALT', 5, 2)
    createButton('space', 'SPACE', 5, 3, 7)
    createButton('altr', 'ALT', 5, 10)
    createButton(None, 'FN', 5, 11)
    createButton('menu', 'MENU', 5, 12)
    createButton('ctrlr', 'CTRL', 5, 13)


def setUpBaseFrame():
    global window

    menubar = tk.Menu(window)
    layoutMenu = tk.Menu(menubar, tearoff=0)
    layoutMenu.add_command(label="QWERTY", command=qwertyLayout)
    layoutMenu.add_command(label="Colemak", command=colemakLayout)

    menubar.add_cascade(label="Layouts", menu=layoutMenu)

    window.config(menu=menubar)


def deletedWindow():
    global listenerrrr
    listenerrrr.stop()
    sys.exit()


def startWindowLoop():
    global window, canvas
    window = tk.Tk()
    window.title('Keyboard')

    setUpBaseFrame()
    qwertyLayout()

    window.protocol("WM_DELETE_WINDOW", deletedWindow)
    window.mainloop()


def startKeyBoardInputLoop():
    global listenerrrr
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listenerrrr = listener
        listenerrrr.join()


with ThreadPoolExecutor(max_workers=2) as executor:
    t1 = executor.submit(startWindowLoop)
    t2 = executor.submit(startKeyBoardInputLoop)
