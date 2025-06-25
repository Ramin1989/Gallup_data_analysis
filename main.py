import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# Load the Stata file into a DataFrame
df = pd.read_stata('country_v11.dta')
# Display the first few rows of the DataFrame
print(df.head())

df.to_csv('country_v11.csv', index=False)
# Display the first few rows of the DataFrame after conversion

country_patience_pie = df[['country' , 'patience']].dropna()
country_patience_pie = country_patience_pie[country_patience_pie['patience'] >= 0]
# Create a pie chart for the 'country' and 'patience' columns
plt.figure(figsize=(18, 18))
plt.pie(country_patience_pie['patience'], labels= country_patience_pie['country'], autopct='%1.1f%%')
plt.title('Patience by Country')
plt.show()

Trust_per_country = df[['country', 'trust']].dropna()

plt.figure(figsize=(10, 8))
plt.bar(Trust_per_country['country'], Trust_per_country['trust'])
plt.axhline(0, color='k', linestyle='--', linewidth=1)
plt.title('Trust by Country')
plt.xlabel('country')
plt.ylabel('trust')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

risk_per_country = df[['country', 'risktaking']].dropna()

plt.figure(figsize=(10, 8))
sns.barplot(data= risk_per_country, x='country', y='risktaking', palette='viridis')
plt.xlabel('risktaking')
plt.ylabel('country')
plt.title('Risk Taking by Country')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

data = df[['country', 'risktaking', 'patience']].dropna()
data_long = data.melt(id_vars='country', value_vars=['risktaking', 'patience'],
                      var_name='feature', value_name='score')



plt.figure(figsize=(12, 10))
sns.barplot(data=data_long, x='score', y='country', hue='feature')
plt.axvline(0, color='gray', linestyle='--')
plt.title('Comparison of Risktaking and Patience by Country')
plt.tight_layout()
plt.show()

# Drop missing values
data = df[['country', 'risktaking']].dropna()

# Sort by risktaking
sorted_data = data.sort_values('risktaking')

# Select bottom 5 and top 5
limited_data = pd.concat([sorted_data.head(5), sorted_data.tail(5)])



plt.figure(figsize=(8, 6))
sns.barplot(data=limited_data, x='risktaking', y='country')
plt.axvline(0, color='gray', linestyle='--')
plt.title('Top and Bottom 5 Countries by Risktaking')
plt.tight_layout()
plt.show()






