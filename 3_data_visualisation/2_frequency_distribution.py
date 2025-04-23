## Step 1: Import Libraries.

# Import the necessary libraries, `pandas` for data manipulation and `matplotlib` for data visualisation.
import pandas as pd 
import matplotlib. pyplot as plt 

## Step 2: Data Collection.
data = [23, 45, 23, 67, 89, 45, 23, 56, 34, 67, 23]

## Step 3: Create a Pandas DataFrame.
df = pd.DataFrame(data, columns=['Values'])

## Step 4: Calculate Frequencies.

# Use the Pandas `value_counts()` method to calculate the frequencies of each unique value in the DataFrame. 
frequency_table = df['Values'].value_counts().reset_index() 
frequency_table.columns = ['Value', 'Frequency'] 

## Step 5: Sort the Frequency Table.
frequency_table = frequency_table.sort_values(by='Value', ascending=True) 

## Step 6: Display the Frequency Distribution Table.
plt.bar(frequency_table['Value'], frequency_table['Frequency']) 
plt.xlabel('Value') 
plt.ylabel('Frequency') 
plt.title('Frequency Distribution') 
plt.show() 