# -*- coding: utf-8 -*-
"""
Created on Mon May  9 10:47:20 2022

@author: simon.
"""

import os
import tarfile
import urllib

import pandas as pd

DWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master"
HOUSING_URL = DWNLOAD_ROOT + "/datasets/housing/housing.tgz"
HOUSING_PATH = os.path.join("datsets", "housing");

def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    os.makedirs(housing_path, exist_ok=True)
    tgz_path = os.path.join(housing_path, "houseing.tgz")
    urllib.request.urlretrieve(housing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()

def load_housing_data(housing_path=HOUSING_PATH):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)

    


