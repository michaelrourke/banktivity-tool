# Banktivity-tool
Basic command line tool to import security prices into Banktivity from a csv file.

### CSV format
    SYMBOL ; date (YYYY/MM/DD) ; CLOSINGPRICE

### Usage
```
usage: main.py [-h] [-d [D]] f [f ...] c [c ...]

positional arguments:
  f           Banktivity file
  c           csv file

optional arguments:
  -h, --help  show this help message and exit
  -d [D]      Use "," as delimiter or define another, default ";"
```
