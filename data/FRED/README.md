
# FRED data

Data from [FRED](https://fred.stlouisfed.org/), a standard data source for macroeconomic time series.

## Individual time series

Frequency: `Q` = Quarterly, `M` = Monthly

| File | Description | Units | Frequency | Source |
|------|-------------|-------|-----------|--------|
| `CPI.csv` | Consumer Price Index for All Urban Consumers: All Items in U.S. City Average | Index (1982-84 = 100) | `M` | [Source](https://fred.stlouisfed.org/series/CPIAUCSL) |
| `FEDFUNDS.csv` | Effective Federal Funds Rate | Percent | `M` | [Source](https://fred.stlouisfed.org/series/FEDFUNDS) |
| `GDP.csv` | Real gross domestic product | Billions of chained 2017 US dollars | `Q` | [Source](https://fred.stlouisfed.org/series/GDPC1) |
| `GDPPOT.csv` | Real Potential Gross Domestic Product | Billions of Chained 2017 Dollars | `Q` | [Source](https://fred.stlouisfed.org/series/GDPPOT) |
| `LFPART.csv` | Labor Force Participation Rate | Percent | `M` | [Source](https://fred.stlouisfed.org/series/CIVPART) |  
| `NROU.csv` | Noncyclical Rate of Unemployment | Percent | `Q` | [Source](https://fred.stlouisfed.org/series/NROU) |
| `UNRATE.csv` | Unemployment rate | Percent | `M` | [Source](https://fred.stlouisfed.org/series/UNRATE) |
| `REALRATE.csv` | 1-Year Real Interest Rate | Percent | `M` | [Source](https://fred.stlouisfed.org/series/REAINTRATREARAT1YE) |

## Files with multiple time series

### Annual data

- `FRED_annual.csv`: Contains *annualized* data for selected time series listed above.

    *Variables:*

    1.  `Year`
    2.  `GDP`
    3.  `CPI`
    4.  `UNRATE`
    5.  `FEDFUNDS`
    6.  `INFLATION`: Computed as percentage change of CPI

- `FRED_annual.xslx`:
    Contains the same data as `FRED_annual.csv`, but in Excel format.


### Quarterly data

- `FRED_quarterly.csv`: 
    Contains selected time series from above at quarterly frequency.

    *Variables:*

    1.  `DATE`
    2.  `Year`
    3.  `Quarter`
    4.  `CPI`
    5.  `UNRATE`
    6.  `FEDFUNDS`
    7.  `REALRATE`
    8.  `LFPART`


### Monthly data

- `FRED_monthly.csv`: 
    Contains selected time series from above at monthly frequency.

    *Variables:*

    1.  `DATE`
    2.  `Year`
    3.  `Month`
    4.  `CPI`
    5.  `UNRATE`
    6.  `FEDFUNDS`
    7.  `REALRATE`
    8.  `LFPART`

- `FRED_monthly_XXXX.csv`: Contains selected time series from above at monthly
    frequency, split by decade.

    *Variables:*

    1.  `DATE`
    2.  `CPI`
    3.  `UNRATE`
    4.  `FEDFUNDS`
    5.  `REALRATE`
    6.  `LFPART`