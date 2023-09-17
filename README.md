# Mindblown

## Inspiration
ADHD and ASD therapies are time-intensive and costly. Many caregivers for ADHD and ADS children cannot afford those options.

## What it does
A web-based game for children with behavioral disorders and their caregivers. The game consists of interaction tasks for ASD and attention tasks for ADHD. These tasks will assist existing therapies and solutions, making the care of children with behavioral disorders more accessible.

## How we built it
The game is built with a MongoDB Atlas database and a HTML/CSS, JS frontend, connected with a Flask backend in Python. Specifically, the game is created using PixiJS, a Javascript rendering framework for sprites. The HTML/CSS were designed using Dreamweaver as well as using Bootstrap for our UI functions. We have also incorporated a data visualization JS framework called D3.js.

## Challenges we ran into
Connecting Flask with MongoDB Atlas was one of the biggest challenges we had. Unfortunately, most projects that integrates MongoDB frameworks to Flask are either deprecated or they only allow a specific configuration that does not work well with the Atlas version of MongoDB. 

Authentication, Authorization, and Accounting is another challenge that came about because of MongoDB integration. Due to time constraints and the Flask design, it is extremely difficult to implement it across the board. There is not enough support for an Aspect Orient Programming feature in Flask to implement security easily.

## Accomplishments that we're proud of
The MVP is complete, and the web game runs without any problems. Furthermore, all members of the team have either learnt biological research that they were not aware of or computational tools that they have never used. From a tech stack perspective, besides Flask and HTML/CSS, most of the frameworks were learnt on the fly.

## What we learned
From a tech perspective, game development in Javascript is something that none of the members had any experiences in. Thankfully, the framework is easily available, and the documentation were plenty to complete this project. In addition, data visualization through Javascript is also something new, which also had really good documentation to guide us through the project. Some members also had no web dev experience so we used a WYSIWYG editor - dreamweaver. 



## What's next for Follow the Fun!
Definitely adding in security for the user account to allow for authentication, authorization, and accounting (AAA). Due to security being a non-functional requirement, this was on the backburner, but some sort of Flask AOP should be able to integrate it easily. In addition, more games, more sprites, more scenarios are always something to add to the project. 

From a marketing and financial perspective, we can have more merchandising, maybe even a sponsor to help turn this into a product.



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
