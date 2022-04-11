# wosfile

[![Build Status](https://travis-ci.org/rafguns/wosfile.svg?branch=master)](https://travis-ci.org/rafguns/wosfile)
[![Coverage Status](https://coveralls.io/repos/rafguns/wosfile/badge.svg?branch=master&service=github)](https://coveralls.io/github/rafguns/wosfile?branch=master)

**wosfile** is a Python package designed to read and handle data exported from Clarivate Analytics [Web of Science™](https://www.webofknowledge.com). It converts the original txt format file to xlsx format file.

## Examples

These examples use a dataset exported from Web of Science in multiple separate files(the maximum number of exported records per file is 500).
Put the raw files exported from wos into the raw_data folder, which must be exported as ‘Full Record and Cited References’.

```python
import os
import Paper

out_file = "result/Papers.xlsx"

if __name__ == '__main__':
    filedir = os.getcwd() + '/raw_data'
    filenames = os.listdir(filedir)

    for filename in filenames:
        filepath = filedir + '/' + filename
        paper_list = Paper.read_paper(filepath)
        Paper.write_excel_file(out_file, paper_list)
```

## Other Python packages

The following packages also read WoS files (+ sometimes much more):
* [WOS+](https://pypi.org/project/WOSplus/)
* [metaknowledge](https://pypi.org/project/metaknowledge/)
* [wostools](https://pypi.org/project/wostools/)

Other packages query WoS directly through the API and/or by scraping the web interface:
* [pywos](https://pypi.org/project/pywos/) (elsewhere called [wos-statistics](https://github.com/refraction-ray/wos-statistics))
* [wos](https://pypi.org/project/wos/)
* [wosclient](https://pypi.org/project/wosclient/)
