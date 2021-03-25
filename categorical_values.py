# dropping these values


drop_X_train = X_train.select_dtypes(exclude = 'object')
drop_X_valid = X_valid.select_dtypes(exclude = 'object')
drop_X_test = X_valid.select_dtypes(exclude = 'object')

# label encoder - we do this only if there are same catgorical variables in both training and validation data,
#  if it's not, we'll drop those columns

# All categorical columns
object_cols = [col for col in X_train.columns if X_train[col].dtype == "object"]

# Columns that can be safely label encoded
good_label_cols = [col for col in object_cols if 
                   set(X_train[col]) == set(X_valid[col])]
        
# Problematic columns that will be dropped from the dataset
bad_label_cols = list(set(object_cols)-set(good_label_cols))
        
print('Categorical columns that will be label encoded:', good_label_cols)
print('\nCategorical columns that will be dropped from the dataset:', bad_label_cols)


from sklearn.preprocessing import LabelEncoder


# Drop categorical columns that will not be encoded
label_X_train = X_train.drop(bad_label_cols, axis=1)
label_X_valid = X_valid.drop(bad_label_cols, axis=1)
#label_X_test = X_test.drop(bad_label_cols, axis=1)

# Apply label encoder 
____ # Your code here
my_encoder= LabelEncoder()
for col in (good_label_cols):
    label_X_train[col] = my_encoder.fit_transform(X_train[col])
    label_X_valid[col] = my_encoder.transform(X_valid[col])
    #label_X_test[col] = my_encoder.transform(X_test[col])
    
    
# Check your answer
print(X.shape, X_test.shape)

# for one hot encoding we can only use columns with low cardinality, as more distinct entries will be there more columns we need to add

# investigating cardinality

# Get number of unique entries in each column with categorical data
object_nunique = list(map(lambda col: X_train[col].nunique(), object_cols))
d = dict(zip(object_cols, object_nunique))

# Print number of unique entries by column, in ascending order
sorted(d.items(), key=lambda x: x[1])

# Columns that will be one-hot encoded
low_cardinality_cols = [col for col in object_cols if X_train[col].nunique() < 10]

# Columns that will be dropped from the dataset
high_cardinality_cols = list(set(object_cols)-set(low_cardinality_cols))

print('Categorical columns that will be one-hot encoded:', low_cardinality_cols)
print('\nCategorical columns that will be dropped from the dataset:', high_cardinality_cols)

from sklearn.preprocessing import OneHotEncoder

# Use as many lines of code as you need!
oh_encoder = OneHotEncoder( handle_unknown = 'ignore', sparse = False)

OH_cols_train = pd.DataFrame(oh_encoder.fit_transform(X_train[low_cardinality_cols]))
OH_cols_valid = pd.DataFrame(oh_encoder.transform(X_valid[low_cardinality_cols]))

OH_cols_train.index = X_train.index
OH_cols_valid.index = X_valid.index

num_X_train = X_train.select_dtypes(exclude = 'object')
num_X_valid = X_valid.select_dtypes(exclude = 'object')

OH_X_train = pd.concat([num_X_train, OH_cols_train], axis = 1)
OH_X_valid = pd.concat([num_X_valid, OH_cols_valid], axis = 1)

print(X.shape, X_test.shape)