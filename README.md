# importbanktivityasx
Command line tool to import security prices into Banktivity from a CSV file. 

Applies every CSV file to every Banktivity database defined in the script.

Only securitites in the CSV which are already defined in Banktivity and not excluded from quote updates are updated.

Existing price data isn't replaced or added to.

Assumes Banktivity 7 schema.

### CSV format
```
Security Code, Date, Opening Price, High Sale Price, Low Sale Price, Closing Price
COH,07 Jan 2021,188.6,189.99,182.29,182.5
...
```
Note this is the CSV format of daily ASX price data from CommSec.

The constants `CSV_DELIMITER` and `CSV_DATEFORMAT` may be changed as required.

### Usage
```
usage: importbanktivityasx [-h] csv_file [csv_file ...]

optional arguments:
  -h, --help  show this help message and exit

```
The constants `BANKTIVITY_FILES_ROOT`, `BANKTIVITY_FILES` and `EQUITY_SYMBOL_SUFFIX` need to be set.
