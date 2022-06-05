# My Juypter Notes
#### (from the book Hands-on Machine Learning by [A.Geron](https://github.com/ageron))

### Details
This notebook will serve has a space for learning and experimenting with the material from
Geron's book.

#### Setup
```bash

Step [1]: Create virtual python environment (Do once on set-up).

	> python -m virtualenv ml_env

Step 2: Activate virtual python environment.		

	> .\ml_env\Scripts\activate

Step [3]: Install dependencies (Do once on set-up).

	> python -m pip install -U jupyter matplotlib numpy pandas scipy scikit-learn

Step 4: Deactivate environment (when finished).

	> deactivate
```	
#### JUPYTER NOTEBOOK
```bash
Step [1]: Register your virtual env to jupyter (Do once on set-up).

	> python -m ipykernel install --user --name=ml_env

Step [2]: Set Jupyter password (Do once on set-up).

	> jupyter notebook password

Step 3: Start up notebook.

	> jupyter notebook
		
```		
### DATA
```bash
Step 1: In Juypter now... load the data.
	
	> import util.housing_data 
	> fetch_housing_data()

Step 2: Load the data.

	> load_housing_data()
```
