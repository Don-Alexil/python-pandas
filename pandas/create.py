import pandas as pd 
from matplotlib import pyplot as plt

# initialise data of lists. 
data = {'Name':['Tom', 'Nick', 'Krish', 'Aack', 'Alex', 'Anca', 'Doru', 'Nela'], 'Age':[20, 21, 19, 18, 42, 40, 67, 67]} 
  
# Create DataFrame 
family_ages = pd.DataFrame(data) 

plt.hist(family_ages.Age)

plt.show()

