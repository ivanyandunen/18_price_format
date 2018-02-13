# Price Formatter

This script converts price output to more comfortable for user view.
(e.g. 3245.000000 will be converted to 3 245)

Python 3 has to be installed.

# How to run
To run in command line:
```commandline
python format_price.py -h
  -h, --help            show this help message and exit
  -i, --input           Input price
  
python format_price.py -i 12345.6789
12 346
``` 
To run tests:
```commandline
python -m unittest tests.py
..........
----------------------------------------------------------------------
Ran 10 tests in 0.001s

OK
```
To use outside:
```python
from format_price import format_price

format_price(price)
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
