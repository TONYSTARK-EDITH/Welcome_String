
# Welcome String

Welcome String is a Python library for printing the Title in patterns

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Welcome-String.

```bash
pip install wstring
```

## Usage

The wstring takes 1 argument and 4 optional arguments

```python
# Printing Welcome with default arguments
from wstring import wstring

wstring.wString("Welcome")
```
![](normal.jpg)


The 4 optional arguments are length,height,symbol and color

```python
# Printing Welcome with all 4 arguments
wstring.wString("Welcome", length=5, height=5, symbol='$', color='red')
```
![](clr.jpg)

## Features


Color has been added to the welcome string which makes it more attractive.
For now there are 5 different colors they are

<ul>
<li>red
</li>
<li>green
</li>
<li>blue</li>
<li>yellow</li>
<li>purple</li>
</ul>

Users are allowed to pass the color name as an optional attribute, if the color you entered is not present in the mentioned above colors then it will print in the default color
<ul>
<li>Windows --> black</li>
<li>Linux --> white</li>
</ul>

Wstring is now platform independent and it works even in cmd in windows and terminal in linux

New exceptions has been included

 1. CharacterExpectedGotStringException
 2. EmptyCharacterFoundException
 
Test cases has been included

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://github.com/TONYSTARK-EDITH/wstring/blob/master/LICENSE)
