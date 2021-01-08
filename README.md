# Banktivity-tool
Basic command line tool to import security prices into Banktivity from a csv file.

### CSV format
```
Security Code, Date, Opening Price, High Sale Price, Low Sale Price, Closing Price
COH,07 Jan 2021,188.6,189.99,182.29,182.5
...
```
Note this is the CSV format of daily price data from CommSec.

The constants `CSV_DELIMITER` and `CSV_DATEFORMAT` may be changed as required.

### Usage
```
usage: importbanktivityasx [-h] csv_file [csv_file ...]

optional arguments:
  -h, --help  show this help message and exit

```
The constants `BANKTIVITY_FILES_ROOT`, `BANKTIVITY_FILES` and `EQUITY_SYMBOL_SUFFIX` need to be set.