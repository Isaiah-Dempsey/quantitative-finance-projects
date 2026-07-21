# Quantitative Finance & Data Analytics Projects

This repository contains algorithmic trading and financial mathematical models developed using Python and SQL. The scripts leverage statistical frameworks to analyze market data patterns and evaluate time-series trends.

## Projects Blueprint

### 1. Vectorized Moving Average Crossover Backtester (`backtester.py`)
An automated algorithmic trading signal engine that utilizes vectorized operations to parse historical market data and flag momentum pivot points.
* **Mathematical Concept:** Low-pass filtering via sliding-window simple moving averages ($MA_t = \frac{1}{n} \sum_{i=0}^{n-1} X_{t-i}$).
* **Execution:** Dynamically fetches time-series asset matrices via the `yfinance` API and applies Pandas vector operations to identify bullish momentum crossover configurations ($MA_{20} > MA_{50}$).

### 2. Compound Interest Modeling Matrix (`finance_math.py`)
A functional modeling tool designed to map the future valuation domain of capital assets over multiple discrete rate variables and temporal horizons.
* **Mathematical Concept:** Continuous compounding scalar equations ($A = P(1 + r)^t$).
* **Execution:** Utilizes Python lists to simulate asset trajectories across dynamic interest domains.

## Environment & Requirements
* Language: Python 3.12+
* Core Dependencies: `pandas`, `yfinance`
