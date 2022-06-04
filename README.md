# My Juypter Notes (from the book Hands-on Machine Learning)


#### Setup
```bash

Step [1]: Create virtual python environment (Do once on set up).

	> python -m virtualenv ml_env

Step 2: Activate virtual python environment.		

	> .\ml_env\Scripts\activate

Step [3]: Install dependencies (Do once on set up).

	> python -m pip install -U jupyter matplotlib numpy pandas scipy scikit-learn

Step 4: Deactivate environment (when finished).

	> deactivate
```	
#### JUPYTER NOTEBOOK
```bash
Step [1]: Register your virtual env to jupyter (Do once on set up).

	> python -m ipykernel install --user --name=ml_env

Step [2]: Set Jupyter password (Do once on set up).

	> jupyter notebook password

Step 3: Start up notebook.

	> jupyter notebook
		
```		
### DATA
```bash
Step 1: Get data
	
	import util.housing_data and run fetch_housing_data()

Step 2: Load the data.

	import util.housing_data and run load_housing_data()
```
