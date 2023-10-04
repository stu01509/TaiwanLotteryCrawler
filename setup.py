# -*- coding: utf-8 -*-
import os
from pathlib import Path

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

setup(
    name="taiwanlottery",
    version="1.4.0",
    author="Cliff Su",
    author_email="stu01509@gmail.com",
    description="Taiwan Lottery Crawler 台灣彩券爬蟲",
    long_description_content_type="text/markdown",
    long_description=Path("README.md").read_text(encoding="utf-8"),
    packages=find_packages(),
    install_requires=[
        "requests>=2",
        "beautifulsoup4>=4",
        "terminaltables>=3",
        "pytest>=7.0",
        "pytest-cov>=4.0",
        "flake8>=6.0",
        "pre-commit>=3.3"
    ],
    keywords=['python', 'taiwanlottery', 'crawler', 'lottery', 'taiwan', '台灣彩券', '樂透', '彩券'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "License :: OSI Approved :: MIT License",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries",
    ],
    project_urls={
        "Source": "https://github.com/stu01509/TaiwanLotteryCrawler",
    },
)
