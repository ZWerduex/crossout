# Crossout Python package

The `crossout` Python package is a Python library for interacting with the Crossout API provided by the [CrossoutDB website](https://crossoutdb.com). It is designed to be simple to use and gives general information about the game items. As it is based on a third party API, data may be outdated or missing.

> **Note :** The package does not provide information about the market state and item prices.

> **Note :** This package is not affiliated with CrossoutDB, Targem Games or Gaijin Enternaiment in any way.

## How to use

### Requirements

The package was made with Python `3.10.4`. Although its dependencies should be automatically installed by `pip`, here is a list of the required packages :

- [requests>=2.30.0](https://pypi.org/project/requests/) for HTTP requests
- [urllib3>=2.0.2](https://pypi.org/project/urllib3/) to create GET parameters of requests

### Installation

The package is available on PyPI and can be installed using `pip`:

```bash
pip install crossout
```

### Usage

The package provides a core class called `CrossoutDB`. It wraps the lower level API calls and provides a simple interface to get information about the game items. Here the sample code retrieve the name of the item with the ID `1050`, which is the [ZS-33 Hulk](https://crossoutdb.com/item/1050).

```python
import crossout

# Create a CrossoutDB instance
db = crossout.CrossoutDB()
name = db.item(1050).name
# name = "ZS-33 Hulk"
```

## Possible enhancements

As I have made this very basic package to learn how to deal with posting packages on PyPi, I do not plan to work on the project in the future. Despite that, one can think of those following possible enhancements :

- Generate documentation files
- Consider adding option to scrap additionnal data from the website if allowed to
- Add support for item prices
- Add support for market data

## Resources

- [CrossoutDB repository](https://github.com/Zicore/CrossoutMarket)
