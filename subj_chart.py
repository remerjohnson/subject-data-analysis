import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_csv('subject_conversion.csv', low_memory=False)

bySubj_counts = df.groupby('new_predicate')['updated_label'].count()

plt.gcf().subplots_adjust(bottom=0.35)

bySubj_counts.plot(kind='bar', title='Subject Types in Reconciled Data')

plt.show()
