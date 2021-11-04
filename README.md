# crypto-markets

Python bindings for the [crypto-markets](https://github.com/soulmachine/crypto-crawler-rs/tree/main/crypto-markets) library.

## Quickstart

Install,

```bash
pip3 install crypto-markets
```

```python
from crypto_markets import MarketType, fetch_markets

markets = fetch_markets("binance", MarketType['inverse_swap'])

assert len(markets) > 0
market = markets[0]
assert market['exchange'] == 'binance'
assert market['market_type'] == 'inverse_swap'
```

## How to build

On Mac OS X,

```bash
conda install --file requirements-dev.txt

rm -rf build crypto-markets-ffi/target
python3 setup.py bdist_wheel

# Need to create a ~/.pypirc file first
twine upload --repository testpypi dist/*
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps crypto-markets

twine upload dist/*
```

For Linux,

```bash
docker run -it --rm -v $(pwd):/project soulmachine/rust:manylinux2014 bash

/opt/python/cp36-cp36m/bin/pip3 install -r requirements-dev.txt
rm -rf build crypto-markets-ffi/target
/opt/python/cp36-cp36m/bin/python3 setup.py bdist_wheel
auditwheel repair dist/*linux*.whl --plat manylinux2014_x86_64
/opt/python/cp36-cp36m/bin/twine upload --repository testpypi wheelhouse/*
```

## Test

```bash
python3 setup.py develop
pytest -s
```
