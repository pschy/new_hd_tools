# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""


from setuptools import setup


version = '1.0'

REQUIRES = [
    "base58==1.0.3",
    "base58check==1.0.2",
    "eth-utils==1.7.0",
    "pycrypto==2.6.1",
    "pycryptodome==3.9.0",
    "two1",
]


setup(
    name="new_hd_tools",
    packages=["new_hd_tools"],
    version=version,
    install_requires=REQUIRES,
    description="HD wallet Tools.",
    long_description="",
    author="pschy",
    author_email="cj82@qq.com",
    url="https://github.com/pschy/new_hd_tools",
)
