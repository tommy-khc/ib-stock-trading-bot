# Interactive Broker Stock Trading bot

## Background

This is a simple trading bot which is connected to the Trader Workstation (TWS) of Interactive Broker (IB). It doesn't involve any trading strategy.</br>

## Description

It provides a basic framework for the reader to write down their strategy and don't need to worry about other technical thing. </br>

## Motivation

It comes from the trading bot I used in the 2017 Hong Kong Society of Financial Analysts - Hong Kong Exchanges and Clearing Ltd. Portfolio Management Competition.

## Features

- Connecting to your IB trading account
- Getting real-time market data of any instruments
- Having Buy and Sell Order objects for future usage

## Build status
It is completed.

## Code style
[Google Python Style](https://google.github.io/styleguide/pyguide.html)

## Tech used
### Tech
- Multithreading

## Installation
No installation is required

## How to use it?
1. Change the socket port number to the one specified in your TWS global configuration in bot.py
2. Write the symbol of instrument in bot.py
2. Run bot.py

## License
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
