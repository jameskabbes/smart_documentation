# Smart Documentation

Smart Documentation hopes to develop a pipeline to automatically generate documentation for Python libraries.

### Technologies:

- [Python](https://www.python.org/).
- [Sphinx](https://www.sphinx-doc.org/en/master/).
- [Virtualenv](https://virtualenv.pypa.io/en/latest/).
- [GitHub Actions](https://github.com/features/actions).
- [GitHub Pages](https://pages.github.com/).

### First Time Usage

```
virtualenv venv
venv\Scripts\activate
python -m pip install sphinx
pip install -r requirements.txt
sphinx-build --version
sphinx-quickstart docs
sphinx-build -b html docs/source/ docs/build/html
create project/load_config.py
create populate_config.py & customize settings
create docs/source/initial_write.py
```

### Local Usage

```
venv\Scripts\activate
make changes to source code
python populate_config.py
python docs/source/initial_write.py
make html within docs folder
```

### Deployment Process

```
venv\Scripts\activate
make changes to source code
python populate_config.py
python docs/source/initial_write.py
push your code to main on github
```

### Information

- The project to be documented is located in the `project` root directory.
- Your personal access token must have `workflow` enabled.
- Required files:

```
populate_config.py
docs/source/initial_write.py
project/load_config.py
```

- If you need to update your personal access token, do these commands:

```
git remote remove origin
git remote add origin https://<TOKEN>@github.com/<USERNAME>/<REPO>.git
git remote -v
git push origin main
```

### Local Usage Update

```
venv\Scripts\activate
update your code
python commands.py
doc site will open in a new tab
```
