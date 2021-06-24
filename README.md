
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

wstring("Welcome")
```
<img src="https://drive.google.com/uc?export=view&id=10S_ImnQCckdvpOkd1_V2xmJNIuvtXWay" style="zoom:150%;" />


The 4 optional arguments are length,height,symbol and color

```python
# Printing Welcome with all 4 arguments
wstring("Welcome", length=5, height=5, symbol='$', color='red')
```
<img src="https://drive.google.com/uc?export=view&id=1PrlL0v6ScUnPHAqBn0F_w15uLG0mUZ1U" style="zoom:150%;" />

## Features

- ## **Color**

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

  Color has been inspired from the work of <b>[AbhijithAJ](https://github.com/AbhijithAJ)</b> from the project <b>[clrprint](https://github.com/AbhijithAJ/clrprint)</b>
  Wstring is now platform independent and it works even in cmd in windows and terminal in linux

- ## **Exception**

  New exceptions has been included

   1. CharacterExpectedGotStringException
   2. EmptyCharacterFoundException

- ## **Command Line Interface**

  Command line interface has been added to this package

  ```bash
  usage: wstring [-h] -S [STRING ...] [-s SYMBOL] [-l LENGTH] [-H HEIGHT]
                 [-c COLOR]
  
  Welcome string to print the given string in pattern
  
  optional arguments:
    -h, --help            show this help message and exit
    -S [STRING ...], --string [STRING ...]
                          String to be printed as pattern
    -s SYMBOL, --symbol SYMBOL
                          A character to be used to print the given string as a
                          pattern
    -l LENGTH, --length LENGTH
                          Length of the pattern
    -H HEIGHT, --height HEIGHT
                          Height of the pattern
    -c COLOR, --color COLOR
                          Color the pattern should be printed
  ```
  
  

  <img src="https://drive.google.com/uc?export=view&id=1m1ad3q3bQwi-JQK4VRoiYUxO43BHF4Ct" alt="cli" style="zoom:150%;" />
  
  
  <img src="https://drive.google.com/uc?export=view&id=1l8uHF_h9gXjFhADZLeGVJ1vPBTAy-Ixa" style="zoom:150%;"  alt="cli-optional" />
  
  
  


  Test cases has been included



## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://github.com/TONYSTARK-EDITH/wstring/blob/master/LICENSE)
