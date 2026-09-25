# quant-bot

Autonomous spot-crypto trading bot for the Roostoo Quant Trading Hackathon (live trading Oct 4-17, 2026).

**Status:** in development. Backtester first, strategy second, live execution last.

## Inspiration and prior work

The author studied the public repository of last year's SG vs HK hackathon entry
[APEX](https://github.com/OccupiedPorcupine/HKvSG-TradingBot) (no license) to understand the problem
and its pitfalls. No code from that repository is used here; everything in this repo is written
from scratch. Lessons taken as ideas only: backtest before tuning, account for commission drag, and
never change parameters live without evidence.

## Competition constraints this bot is designed around

- $100k mock portfolio, spot only, no leverage; maker fee 0.05%, taker fee 0.10%
- No high-frequency, market-making or arbitrage strategies
- Fully autonomous execution with a traceable commit history
- Score: 0.4 Sortino + 0.3 Sharpe + 0.3 Calmar (after a portfolio-return screen)
