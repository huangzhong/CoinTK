from cointk.backtest import backtest
from cointk.strategies import NaiveStrategyReverse
import random

random.seed(1)
strategy = NaiveStrategyReverse(n_prices=1000, threshold=0.8)

backtest(strategy)
