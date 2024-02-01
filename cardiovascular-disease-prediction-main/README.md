# cardiovascular-disease-prediction

A group project on cardiovascular disease prediction project

## Setup Initial Project

```bash
git clone https://github.com/OpenMinds-LCIT/cardiovascular-disease-prediction.git
```

## Working on Branch

- When working on new task/feature, create a new branch then work on that branch. format of the branch `git branch <your_name-task/feature>`
  - e.g. `git checkout -b prakash/data-cleaning-age`
- Developer always have to pull `git pull` code from `main` branch and sync with it.
- Make a PR(Pull Request) after completion of task/feature and always add a code reviewer in associated PR.
- Make a habit to check on your PR, so that you can follow along with status, comments, tasks of your PR.
- Once your PR is approved and merged to main branch then you can switch back to main branch and ready to work on another feature/task.

```bash
git branch # to list branch
git checkout -b <branch_name> # create new branch and move to new branch
git checkout <branch_name> # to change branch

git add . # to add your changes
git commit -m "your commit message" # to commit your changes
git status # to check your status
git log # to checkout your commit logs
git push # to push your code to github
git pull # to pull new changes from github
```

## Folder Structure

```bash
|____ data # Data sets e.g excel files
|____ docs # Add your project report, task report e.g. word files
|____ models # Trained and Serialized Models
|____ notebooks # Jupter Notebooks
|____ slides and charts # General analysis as charts in HTML/PDF/PPTS/IMAGES
|____ src # Source code that is used in the project
```

## Work on Virtualenv

```bash
> pip install virtualenv
> python -m venv venv # for windows
> python3 -m venv venv # for mac
> venv/Scripts/activate # to activate virtualenv windows
> source venv/bin/activate # to active virutalenv mac
> pip freeze > requirements.txt
> pip install -r requirements.txt # to install all the packages
```

## Collaborators

[@amannain122](https://github.com/amannain122)  
[@bikkysr](https://github.com/bikkysr)  
[@gaurav809](https://github.com/gaurav809)  
[@Janki-31](https://github.com/Janki-31)  
[@prakash-pun](https://github.com/prakash-pun)  
[@rutul7802](https://github.com/rutul7802)  
[@Swethaloyalist](https://github.com/Swethaloyalist)  
[@tirth-patel01](https://github.com/tirth-patel01)  
[@whyteeth](https://github.com/whyteeth)

### Happy Coding :smiley:
