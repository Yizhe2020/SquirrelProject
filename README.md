# Squirrel-Tracker

## Background Description
This is a web-app to keep track of all the known squirrels in Central Park. The users are allowed to view, update and add squirrel data. This web-app is created based on Django framework and Python3 tools.  

### Project Group: L&Z, Section 001
#### UNIs: [yl4559, jz3282]
* Yizhe Li: yl4559
* Jiaqi Zhu: jz3282

## Features
### Main page
* Link to Map can be found at this page
* Link to Sightings can be found at this page
* Link to add can be found at this page
* Link to general stats of all squirrels can be found at this page
```bash
Located at: /
```

### Sightings
#### View all squirrels sightings
A list of all the squirrels sightings with their recorded date can be found at this page and users can access to details and update the information of existing sightings through the link of unique squirrel ID. 
```bash
Located at: /sightings/
```
#### Update sightings
Details of all squirrels sightings and request of updating the information of those can be found at this page.
```bash
Located at: /sightings/<Unique_Squirrel_ID>/
```

#### Create sightings
The form to add a new squirrel sighting can be found at this page.
```bash
Located at: /sightings/add/
```
#### View general statistics
Some general stats of squirrels can be found at this page.
```bash
Located at: /sightings/stats/
```

### Map
A map of locations of 100 squirrels sightings in Central Park can be found at this page.
```bash
Located at: /map/
``` 
## Launch Instruction
* Clone this repositary to you machine
* Activate the environment using:
```bash
source env/bin/activate
```
* And make sure you have installed all required packages using:
```bash
pip install -r requirement.txt
```
* Import the data using:
```bash
python manage.py import_squirrels /path/to/file.csv
```
* In order to run External IP using:
```bash 
sudo home/username/SquirrelProject/env/bin/python manage.py runserver 0.0.0.0:80
```


