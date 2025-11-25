from setuptools import setup 

setup(
    name="PigaVCS",
    version="0.2",
    py_modules=["main"],
    install_requires=[
        "argparse",
        "datetime",
    ],
    entry_points='''
        [console_scripts]
        pigavcs=main:cli 
    ''',
)
