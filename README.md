# numbers-tools
Some useful tools for weekly routines.

## Features
- Calculate Attendance
- ... (I don't have new ideas now.)

## How to use
### CellGroupNumbersTool
1. Edit `input` file in following format.

```c=
// 主日出席名單，每個名字用「空格」分開 e.g. John Tom Tiffany
// 小組出席名單，每個名字用「空格」分開 e.g. John Tom Tiffany
```

2. Open command line & past this command

```zsh=
python3 CellGroupNumbersTool.py < input > output
```

3. Open `output` file to get the result
