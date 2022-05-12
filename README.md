[GitHub Pages](https://jameskabbes.github.io/smart_documentation)  
[PyPI](https://pypi.org/project/kabbes-smart-documentation)

# smart_documentation

Package for automatically generating documentation for Python repositories

# Steps to Set Up

1. copy the docs directory over to repository you are trying to auto document
2. make a workflows directory nested in a .github directory `mkdir .github/workflows/`
3. copy the make.yml file over to the workflows directory
4. edit conf.py project title to refect current project


### if project not in src/
1. adjust the project title in conf.py in the docs directory (found by searching "project title")
2. if project not stored in scr/**"project**title"\_\_ continue
3. replace **"src"** in the api.rst in the docs directory to the folder you want documented
4. replace the **"src"** in the **"ml_pipeline <\_autosummary/src>"** on the last line of the index.rst in the docs directory to the folder you want documented

# Usage Tips

- make sure the requirements.txt file is right since it won't build unless dependecies are installed correctly
- be sure to check that Gitpages are set up right for the repositorie
- if unable to push to gh-pages branch, create and push another to GitHub `git branch gh-pages`

# local testing 
if you want to make sure everything is workign you can test sphinx localy by following the steps below.
- navigate to the docs folder in terminal `cd docs`
- run `make html` 
- the web page should be in the `docs/_build/html` folder. you jsut need to open the index.html in chrome and you should see it.
