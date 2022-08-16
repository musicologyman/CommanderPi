#!/usr/bin/python
import sys
import os
from pathlib import Path

# user = sys.argv[1]
user = os.environ['USER']
HOME_PATH = Path.home().as_posix()
APP_PATH = os.path.dirname(os.path.realpath(__file__))

print(APP_PATH)
desktop_file_lines = ['[Desktop Entry]',
                      'Name=CommanderPi'
                      'Comment=System info and overclocking',
                      f'Exec={APP_PATH}/src/start.sh',
                      f'Icon={APP_PATH}/src/icons/Icon.png',
                      'Categories=Utility;',
                      'Version=1.0',
                      'Type=Application',
                      'Terminal=false',
                      'StartupNotify=true']

for line in desktop_file_lines:
    print(line)

DESKTOP_PATH = f'{HOME_PATH}/Desktop/commanderpi.desktop'
MENU_PATH = '/usr/share/applications/commanderpi.desktop'

print(f'Save desktop shortcut to {DESKTOP_PATH}')
try:
    with open(DESKTOP_PATH, mode='w') as fp:
        for line in desktop_file_lines:
            print(line, file=fp)
except FileNotFoundError:
    print('Couldn\'t create desktop shortcut!')


print(f'Save menu shortcut to {MENU_PATH}')
try:
    with open(MENU_PATH, mode='w') as fp:
        for line in desktop_file_lines:
            print(line, file=fp)
except FileNotFoundError:
    print('Couldn\'t create menu shortcut!')
