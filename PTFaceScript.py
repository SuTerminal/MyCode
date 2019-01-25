# Scripted by SUTerminal550
#
# Install on terminal
# pip install pynput

from pynput import keyboard
from pynput.keyboard import Key, Listener
from pynput.keyboard import Key, Controller

keyboardC = Controller()

face_expression = False


def on_release(key):
    global face_expression
    if key == keyboard.Key.esc:
        if face_expression == False:
            quit()
        face_expression = False

    #SET FACE EXPRESSION:
    elif key == keyboard.KeyCode(char='+'):
        face_expression = 'c'
    elif key == keyboard.KeyCode(char='-'):
        face_expression = '-'
    elif key == keyboard.Key.delete:
        face_expression = '.'
    elif key == keyboard.KeyCode(char='*'):
        face_expression = '~'
    elif key == keyboard.Key.f9:
        face_expression = 'm'
    elif key == keyboard.Key.f10:
        face_expression = '-'

    #SET EYES AND FACE: 
    elif key == keyboard.Key.home:
        left_up(face_expression)
    elif key == keyboard.Key.up:
        up_up(face_expression)
    elif key == keyboard.Key.page_up:
        right_up(face_expression)
    elif key == keyboard.Key.left:
        left(face_expression)
    # elif key == keyboard.<12>: Numpad clear key dosen't work
    elif key == keyboard.Key.insert:  #numpade insert
        mid(face_expression)
    elif key == keyboard.Key.right:
        right(face_expression)
    elif key == keyboard.Key.end:
        left_down(face_expression)
    elif key == keyboard.Key.down:
        down(face_expression)
    elif key == keyboard.Key.page_down:
        right_down(face_expression)

    #else:
    #    print(f"relessed {key}") 


def left_up(face):
    if face != False:
        enter()
        keyboardC.type(f'/e g{face}g')
        enter()


def up_up(face):
    if face != False:
        enter()
        keyboardC.type(f'/e 9{face}9')
        enter()


def right_up(face):
    if face != False:
        enter()
        keyboardC.type(f'/e e{face}e')
        enter()


def left(face):
    if face != False:
        enter()
        keyboardC.type(f'/e <{face}<')
        enter()


def mid(face):
    if face != False:
        enter()
        keyboardC.type(f'/e o{face}o')
        enter()


def right(face):
    if face != False:
        enter()
        keyboardC.type(f'/e >{face}>')
        enter()


def left_down(face):
    if face != False:
        enter()
        keyboardC.type(f'/e d{face}d')
        enter()


def down(face):
    if face != False:
        enter()
        keyboardC.type(f'/e 6{face}6')
        enter()


def right_down(face):
    if face != False:
        enter()
        keyboardC.type(f'/e b{face}b')
        enter()


def enter():
    keyboardC.press(Key.enter)
    keyboardC.release(Key.enter)


with keyboard.Listener(on_release=on_release) as listener:
    listener.join()
