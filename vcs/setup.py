from setuptools import setup 

setup(
    name="PigaVCS",
    version="0.2",
    py_modules=["app"],
    install_requires=[
        "argparse",
    ],
    entry_points='''
        [console_scripts]
        pigavcs=app:cli 
    ''',
)
