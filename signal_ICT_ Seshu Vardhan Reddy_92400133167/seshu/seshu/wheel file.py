# -*- coding: utf-8 -*-
"""
Created on Sat Sep  6 16:09:58 2025

@author: seshu
"""

from setuptools import setup, find_packages

setup(
    name="signal_ict_Seshu Vardhan Reddy",        # unique name for TestPyPI
    version="0.1.0",
    author="Seshu Vardhan Reddy",
    description="Signal processing experiments package",
    packages=find_packages(),        # automatically finds your package folder
    install_requires=[
        "numpy",
        "matplotlib"
    ],
    python_requires=">=3.10",
)

