#step- 1 Import Libraries

import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

#step- 2 Create DataFrame
df = pd.read_csv('Energy_consumption_cleaned_data1.csv')

#step- 3 Extract Input X
x = df[['temperature' , 'humidity' , 'squarefootage' , 'occupancy' , 'hvacusage' , 'lightingusage' , 'renewableenergy' , 'dayofweek' , 'holiday' ]]

# step - 4 Extract Output y
y = df['energyconsumption']

#step - 5 Create Model
model = LinearRegression()

#step - 6 Train the Model
model.fit(x,y)


fh = open('trained_model.pkl', 'wb')
pickle.dump(model, fh)
fh.close()
