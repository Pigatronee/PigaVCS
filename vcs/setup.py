from setuptools import setup 

setup(
    name="PigaVCS",
    version="0.2",
    py_modules=["vcs"],
    install_requires=[
        "argparse",
        "datetime",
    ],
    entry_points={
        "console_scripts":[
            "pigavcs = vcs:cli"
        ]
    }
)
