# TheIsle

TheIsle is a small python library that allows you to edit player files for servers on a game called [The Isle](https://store.steampowered.com/app/376210/The_Isle/)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install TheIsle.

```bash
pip install theisle
```

## Usage

```python
from theisle import Server

theisle = Server('[PLAYERS DIRECTORY]')

for player in theisle.players():
    print(player.Health)

```
This will print the health for every player saved on the server.



## License
[MIT](https://choosealicense.com/licenses/mit/)
