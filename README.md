# Commands Used

```bash
conda create -n wineq python==3.7 -y
conda activate <env name> 
touch requirements.txt
pip install -r requirements.txt
touch README.md
touch template.py
mkdir data_given
git init #It can be used to convert an existing, unversioned project to a Git repository or initialize a new, empty repository.
dvc init
dvc add data_given/winequality.csv #to start tracking the data
git add .
git commit -m "message type"
create a remote repository and push the changes
git remote add origin https://github.com/Sagar-modelling/DVC_MLOPS.git
git branch #check your git branch and change it to main branch instead of master branch
git branch -M main
git push origin main
git remote remove origin
git remote add origin https://github.com/Sagar-modelling/DVC_MLOPS.git
git push -f orgin main

#loading the data
touch src/get_data.py
touch src/load_data.py
#update the stages in dvc.yaml files
dvc repro #reproduce
```