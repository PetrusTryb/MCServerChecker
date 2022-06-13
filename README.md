# MCServerChecker
A simple script to notify You when someone is online on Your Minecraft server.

## Installation
1. Install Python 3 if You don't have it already installed.
2. Run `pip install -r requirements.txt` to install all the dependencies.
## Configuration
Update `config.json` according to your needs.
Set `check_interval` to the amount of time in minutes You want to wait between checks.\
Then set `servers` to an array of servers You want to check. `Name` is the name of the server that will be displayed in notifications, `IP` is the IP address, and `Port` is the port of the server.
## Usage
Run `pythonw MCServerChecker.py` to start the script. You will see an icon on the taskbar. When someone is online on Your server, You will see a notification.\
TIP: You can also place a shortcut in `shell:startup` to start the script automatically on PC startup.
## License
This project is licensed under the MIT license.
This project uses Minetools API to check if someone is online on Your server.
Minecraft is a registered trademark of Mojang AB.