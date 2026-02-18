import pandas as pd
data = {
    'Transmission': ['Automatic', '

# Create sample datasetManual', 'Automatic', 'Manual', 'Automatic'],
    'Color': ['Red', 'Blue', 'Green', 'Blue', 'Red']
}

df = pd.DataFrame(data)
print("Original Data:")
print(df)

import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Dataset
data = {
    'Transmission': ['Automatic', 'Manual', 'Automatic', 'Manual', 'Automatic'],
    'Color': ['Red', 'Blue', 'Green', 'Blue', 'Red']
}

df = pd.DataFrame(data)

# Label Encoding
le = LabelEncoder()
df['Transmission'] = le.fit_transform(df['Transmission'])

# One-Hot Encoding with drop_first
df = pd.get_dummies(df, columns=['Color'], drop_first=True)

print(df)
