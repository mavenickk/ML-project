print(X_train.shape)

# Number of missing values in each column of training data
missing_val_count_by_column = (X_train.isnull().sum())
print(missing_val_count_by_column[missing_val_count_by_column > 0])

# drop missing values

reduced_X_train = X_train.drop([col for col in X_train.columns if X_train[col].isnull().any()], axis=1 )
reduced_X_valid = X_valid.drop([col for col in X_valid.columns if X_valid[col].isnull().any()], axis=1 )

# imputation ( filling missing values with mean values) 

from sklearn.impute import SimpleImputer

# Fill in the lines below: imputation
my_imputer = SimpleImputer() # Your code here
imputed_X_train = pd.DataFrame(my_imputer.fit_transform(X_train))
imputed_X_valid = pd.DataFrame(my_imputer.transform(X_valid))

# Fill in the lines below: imputation removed column names; put them back
imputed_X_train.columns = X_train.columns
imputed_X_valid.columns = X_valid.columns