from distutils.core import setup

setup(
    name="flask_minimal_example",
    version="0.1.0",

    url="https://github.com/mosquito/flask-example/tree/master/flask_example",

    author="BooNooNooNouS",

    packages=["app"],

    # include additional files
    include_package_data=True,

    description="minimalistic example of a PyPi packaged flask application",

    long_description=open("README.md").read(),

    # TODO: install from readme file
    install_requires=[
        "flask"
    ]
)