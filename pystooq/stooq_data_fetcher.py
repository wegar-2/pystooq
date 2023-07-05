import typing as t

import pandas as pd
from datetime import date, datetime
import logging
from functools import reduce

logger = logging.getLogger(__name__)


class StooqDataFetcher:

    def __init__(self):
        pass

    @staticmethod
    def _get_url(ticker: str, start: date, end: date):
        return f"https://stooq.com/q/d/l/?s={ticker}&d1={start.strftime('%Y%m%d')}&d2={end.strftime('%Y%m%d')}&i=d"

    def _get_data_for_ticker(self, ticker: str, start: date, end: date) -> pd.DataFrame:
        df = pd.read_csv(self._get_url(ticker, start, end))
        df.columns = [el.lower() for el in df.columns]
        df["date"] = [datetime.strptime(el, "%Y-%m-%d").date() for el in df["date"]]
        df.set_index(inplace=True, keys=["date"])
        df.columns = pd.MultiIndex.from_product([[ticker], list(df.columns)], names=["ticker", "variable"])
        return df

    def get_data(
            self,
            tickers: t.Union[str, t.List[str]],
            start: date,
            end: date
    ) -> pd.DataFrame:
        data = dict(zip(tickers, [None] * len(tickers)))
        no_data = []
        for ticker in tickers:
            try:
                data[ticker] = self._get_data_for_ticker(ticker, start, end)
            except Exception as e:
                logger.exception(f"Caught exception {e} when fetching data for ticker {ticker} for dates range "
                                 f"{start.strftime('%Y-%m-%d')} to {end.strftime('%Y-%m-%d')}")

        for ticker_, data_ in data.items():
            if data_ is None:
                no_data.append(ticker_)
        logger.warning(f"No data has been fetched for the following tickers: {', '.join(no_data)}")
        for ticker in no_data:
            data.pop(ticker)

        data = reduce(
            lambda left, right: pd.merge(left, right, left_index=True, right_index=True, how="outer"), data.values()
        )
        return data
