# gainz
Calculates returns of equities available on AlphaVantage.

## Installation

```python
pip install gainz-jwf
```

## Usage

You'll need to get your own API key from AlphaVantage [here](https://www.alphavantage.co/support/#api-key).

```python
import gainz

apiKey = 'TXVAQ58GJA0KFLAC'
ticker = 'ivv'
startDate = dt.datetime(2017,8,31)
endDate = dt.datetime(2020,8,31)

gainz.totalReturn(startDate, endDate, ticker, apiKey)
```
