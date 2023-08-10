# Taiwan Lottery Crawler Release Guide

## Build

```shell
python setup.py sdist bdist_wheel
```

## Publish

```shell
pip install twine
twine check .\dist\*
twine upload .\dist\*
```
