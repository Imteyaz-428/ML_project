import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder , StandardScaler
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor



#1 load the data 
df = pd.read_csv("data of gurugram real Estate.csv")

# 2 data cleaning step
df["Price"] = df["Price"].str.replace(",", "")
df["Price"] = df["Price"].astype(float) # changing price type object to float
df = df.drop(["Builder Name", "Company Name"], axis=1) # drop unnaccessary features
df["Rate per sqft"] = df["Rate per sqft"].str.replace(",", "")  # change rate per sqft ot int
df["Rate per sqft"] = df["Rate per sqft"].astype(int)
df.drop("Socity", axis=1, inplace=True) # drop socity because it is unnaccessary feature
df = df[df["Area"] < 10000] # clean data from outliers
df = df[df["BHK_Count"] >= 1] # clean bhk count
df["BHK_Count"] = df["BHK_Count"].astype(int) # change bhk type from oject to int
df = df[df["BHK_Count"] <= 10]
df["Log_Price"] = np.log1p(df["Price"]) # taking log price because price is heavily right skewed


# 3 create a stratified suffle and split
df["price_bin"] = pd.qcut(
    df["Log_Price"],
    q=5,
    labels=False
)
split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)

for train_index, test_index in split.split(df, df["price_bin"]):
    strat_train_set = df.iloc[train_index]
    strat_test_set = df.iloc[test_index]
for set_ in (strat_train_set, strat_test_set) :
    set_.drop("price_bin", axis = 1, inplace = True)
feature_train = strat_train_set.drop(["Price", "Log_Price"],axis=1)
feature_test = strat_test_set.drop(["Price", "Log_Price"], axis=1)
print(feature_train.head())

labels_train = strat_train_set["Log_Price"].copy()
labels_test = strat_test_set["Log_Price"].copy()
x_train = feature_train.copy()
x_test = feature_test.copy()

 
# data preprocessing step
class RealEstateFeatureEngineer(BaseEstimator, TransformerMixin):

    def __init__(self):
        pass

    def fit(self, X, y=None):

        X = X.copy()

        self.property_freq = X["Property Type"].value_counts()
        self.locality_freq = X["Locality"].value_counts()

        return self

    def transform(self, X):

        X = X.copy()

        X["Property_Type_freq"] = X["Property Type"].map(self.property_freq)
        X["Locality_freq"] = X["Locality"].map(self.locality_freq)

        X["BHK"] = X["Property Type"].str.extract(r'(\d+)').astype(float)

        X["Main_Type"] = X["Property Type"].str.extract(
            r'(Apartment|Floor|Plot|Villa|House|Penthouse)'
        )

        X.drop(["Property Type", "Locality"], axis=1, inplace=True)

        return X 
    
    
    
numeric_features = [
    "Area", "BHK_Count", "Rate per sqft",
    "Property_Type_freq", "Locality_freq", "BHK"
]


numeric_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])
categorical_features = [
    "Main_Type",
    "Status",
    "RERA Approval",
    "Flat Type"
]

categorical_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer([
    ("num", numeric_pipeline, numeric_features),
    ("cat", categorical_pipeline, categorical_features)
])



full_pipeline = Pipeline([
    ("feature_engineering", RealEstateFeatureEngineer()),
    ("preprocessing", preprocessor),
   

    ("model", RandomForestRegressor(
        n_estimators=200,
        random_state=42
    ))
])
print(x_train.columns)

full_pipeline.fit(x_train, labels_train)


pred = full_pipeline.predict(x_test)

rmse = np.sqrt(mean_squared_error(labels_test, pred))

# Convert back to original price
pred_price = np.expm1(pred)
actual_price = np.expm1(labels_test)

# Calculate RMSE in original scale
rmse_original = np.sqrt(mean_squared_error(actual_price, pred_price))

print("RMSE (Log scale):", rmse)
print("RMSE (Original Price):", rmse_original)


# print("Train RMSE:",
#       np.sqrt(mean_squared_error(
#           labels_train,
#           full_pipeline.predict(x_train)
#       )))

# print("Test RMSE:",
#       np.sqrt(mean_squared_error(
#           labels_test,
#           full_pipeline.predict(x_test)
#       )))






