#import seaborn
import seaborn as sns
import pandas as pd
#flights = sns.load_dataset("flight")
flights = pd.read_csv("flight.csv")
flights.head()
sns.relplot(data=flights, x="year",y="passengers",hue="month",kind="line")
