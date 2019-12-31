# flask_minimal_example
Example of a minimalistic flask app

# installation

Create the virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip setuptools
pip install -r requirements.txt
```

# Run application

```
python run.py
```

# Verify it's working

navigate to http://127.0.0.1:5000/auth/hello

# Development

Generate a distribution file by running `python setup.py sdist`
```
└─ $ ▶ python setup.py sdist
/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/distutils/dist.py:274: UserWarning: Unknown distribution option: 'include_package_data'
  warnings.warn(msg)
/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/distutils/dist.py:274: UserWarning: Unknown distribution option: 'install_requires'
  warnings.warn(msg)
running sdist
running check
warning: check: missing required meta-data: url

warning: check: missing meta-data: if 'author' supplied, 'author_email' must be supplied too

warning: sdist: standard file not found: should have one of README, README.txt, README.rst

reading manifest template 'MANIFEST.in'
warning: no files found matching '*' under directory 'app/static'
writing manifest file 'MANIFEST'
creating flask_minimal_example-0.1.0
creating flask_minimal_example-0.1.0/app
creating flask_minimal_example-0.1.0/app/templates
creating flask_minimal_example-0.1.0/app/templates/module_one
making hard links in flask_minimal_example-0.1.0...
hard linking setup.py -> flask_minimal_example-0.1.0
hard linking app/__init__.py -> flask_minimal_example-0.1.0/app
hard linking app/templates/module_one/hello.html -> flask_minimal_example-0.1.0/app/templates/module_one
creating dist
Creating tar archive
removing 'flask_minimal_example-0.1.0' (and everything under it)
```

This creates a new folder called dist that includes the .tar.gz file

# Installing the application
`python setup.py install`