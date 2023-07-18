### PyStooq

This package provides simple interface for downloading 
time daily series from [Stooq](https://stooq.com) website.

Please note that author of this package is **not** affiliated with 
Stooq in any way.

#### Usage
In order to download Stooq time series of prices for tickers 
`PKO` and `TPE` for the period from 1st April 2020 to 31st October 2022 use the snippet below:
```python
from pystooq import StooqDataFetcher
from datetime import date

fetcher = StooqDataFetcher()
data_df = fetcher.get_data(
    tickers=["PKO", "TPE"],
    start=date(2020, 4, 1),
    end=date(2022, 10, 31)
)
```

Format of the output:
```
ticker          PKO                                             TPE                               
variable       open     high      low    close        volume   open   high    low  close    volume
date                                                                                              
2020-04-01  20.8531  20.9742  20.4063  20.6669  3.176696e+06  1.100  1.113  1.082  1.091   4377953
2020-04-02  20.7600  20.8904  19.7546  20.3225  4.157717e+06  1.095  1.138  1.086  1.130   8213427
2020-04-03  20.2480  20.3411  19.6895  20.3411  4.003517e+06  1.140  1.165  1.114  1.160   8037788
2020-04-06  20.8997  21.2255  20.6111  21.1138  3.749039e+06  1.180  1.210  1.175  1.188   9852203
2020-04-07  21.5327  22.7709  21.4582  21.7934  7.634852e+06  1.210  1.248  1.168  1.168  13587105
```

The returned data is a `pandas.DataFrame` with
the following indexes:
1. date index on rows (data sorted in ascending order)
2. two-level `pd.MultiIndex` on columns:
   1. first level is the ticker
   2. second level is the variable (open, high, low, close, volume)

All the available variables are downloaded for each ticker.
