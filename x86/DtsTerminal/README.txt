
This script authenticates with the DUT and executes AT command(s) entered by user.

REQUIREMENTS: python3;

1) Installing the script:

a) Create and activate a python virtual environment:
"python -m virtualenv venv"
"venv\Scripts\activate"
b) Install the package (within the DtsTerminal root directory):
"python -m pip install . "

2) Running Commands from command line interface:

The script can execute a single command specified as a command-line argument, or run multiple commands
from an interactive shell.

2.1) Run a single command:
"python -m dts_terminal --comport COMX --command COMMAND"
(where X is COM port number and COMMAND is the AT command).
2.2) Run interactive shell:
"python -m dts_terminal --comport COMX"
(where X is COM port number).

3) Changing the authentication key:

To change the key used to authenticate with the device, update the key in the dts_terminal\unlock.key file.
After changing the key, reinstall the wheel:
"python -m pip install --force-reinstall ."