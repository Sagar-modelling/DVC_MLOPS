# Commands Used

```bash
conda create -n wineq python==3.7 -y
conda activate <env name> 
touch requirements.txt
pip install -r requirements.txt
touch README.md
touch template.py
python template.py
mkdir data_given # we will be putting wine quality data here and acting as a remote repository data.
git init #It can be used to convert an existing, unversioned project to a Git repository or initialize a new, empty repository.
dvc init
dvc add data_given/winequality.csv #to start tracking the data
git add .
git commit -m "message type"
#create a remote Github repository and push the changes
git remote add origin https://github.com/Sagar-modelling/DVC_MLOPS.git
git branch #check your git branch and change it to main branch instead of master branch
git branch -M main
git push origin main
git remote remove origin
git remote add origin https://github.com/Sagar-modelling/DVC_MLOPS.git
git push -f orgin main

#Start writing params.yaml file
#create EMPTY dvc.yaml file

#loading the data
touch src/get_data.py
python src/get_data.py # to check the working of this file
touch src/load_data.py

#update LOAD DATA stage in dvc.yaml files
dvc repro # (reproduce), check the dvc.yaml and will run the cahnges made in the stages

touch src/split_data.py
dvc repro 
#update SPLIT DATA stage in dvc.yaml files

mkdir report # To track the params and metrics
touch reports/params.json
touch reports/metrics.json

dvc metrics show # Tracking the metrics
dvc metrics diff # Tracking the past values
```