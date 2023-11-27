import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the Iris dataset from the CSV file
iris_data = pd.read_csv('iris.csv')

# Create box plots for each feature across the three species
plt.figure(figsize=(10, 6))
plt.subplot(221)
sns.boxplot(x='species', y='sepal_length', data=iris_data)
plt.title('Sepal Length across Species')

plt.subplot(222)
sns.boxplot(x='species', y='sepal_width', data=iris_data)
plt.title('Sepal Width across Species')

plt.subplot(223)
sns.boxplot(x='species', y='petal_length', data=iris_data)
plt.title('Petal Length across Species')

plt.subplot(224)
sns.boxplot(x='species', y='petal_width', data=iris_data)
plt.title('Petal Width across Species')

plt.tight_layout()
plt.show()
