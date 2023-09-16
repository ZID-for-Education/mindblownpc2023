# Mindblown

## Installation Instructions for Devs and Testers
Ensure that you have a version of python installed on your system that comes with the venv package, if it does not try installing via pip:
```
pip install venv
```
Then navigate to the directory where you have downloaded this repository and open a terminal in that location. Use the following command to create a virtual environment on your terminal:
```
python -m venv venv
```
You should notice a new folder called venv in your directory, however you are not done yet. To activate the virtual environment, use:
```
./venv/Scripts/activate
```
You will notice that there is a (venv) in your terminal, this indicates a successful virtual environment activation. If you do not see it, please refer to the documentation online: https://docs.python.org/3/library/venv.html
Then install the required packages via:
```
pip install -r requirements.txt
```
Your virtual environment is now ready and to run the flask web app, use:
```
flask run
```
You can then access the web app at localhost:5000.
To deactivate the virtual environment, simply type into the terminal:
```
deactivate
```
