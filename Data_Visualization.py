import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

#read data
df = pd.read_csv("cleaned_final_project.csv")
df = df.applymap(lambda x: x.strip().title() if isinstance(x, str) else x)
values_to_drop = ["Other", "<N/S>"]

#figure 1
fig1 = plt.figure()
filtered_factors = df[~df['Primary Contributing Factors'].isin(values_to_drop)]
factors_counts = filtered_factors['Primary Contributing Factors'].value_counts()
truncated_factors = {}
for factor in factors_counts.index:
    if len(factor) > 20:
        truncated_factors[factor] = factor[:20] + "..."
    else:
        truncated_factors[factor] = factor
truncated_counts = pd.Series(factors_counts.values, index=[truncated_factors[factor] for factor in factors_counts.index])
truncated_counts.plot(kind='bar')
plt.title("Clinical/Situational Factors Contributing to Violence (Excluding 'Other')")
plt.xlabel("Contributing Factor")
plt.ylabel("Number of Incidents")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
fig1.savefig('f1.png', dpi=300, bbox_inches='tight')

#figure 2
fig2 = plt.figure()
filtered_facility = df[~df['Facility Type'].isin(values_to_drop)]
filtered_violence = filtered_facility[~filtered_facility['Type of Violence'].isin(values_to_drop)]
violence_facility = pd.crosstab(filtered_violence['Facility Type'], filtered_violence['Type of Violence'])
violence_facility.plot(kind='bar', stacked=True)
plt.title("Types of Violence by Facility Type")
plt.xlabel("Facility Type")
plt.ylabel("Number of Incidents")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
fig2.savefig('f2.png', dpi=300, bbox_inches='tight')

#figure 3
fig3 = plt.figure()
filtered_jobs = df[~df['Job Role'].isin(values_to_drop)]
filtered_jobs['Job Role'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=140)
plt.title("Proportion of Violence by Job Role")
plt.ylabel("")
plt.tight_layout()
fig3.savefig('f3.png', dpi=300, bbox_inches='tight')

#figure 4
fig4 = plt.figure()
filtered_severity = df[~df['Severity of Assault'].isin(values_to_drop)]
filtered_impact = filtered_severity[~filtered_severity['Psych Impact'].isin(values_to_drop)]
severity_order = filtered_impact['Severity of Assault'].value_counts().index
sns.countplot(data=filtered_impact, x='Severity of Assault', hue='Psych Impact', order=severity_order)
plt.title("Severity of Assault vs Psychological Impact")
plt.xlabel("Severity of Assault")
plt.ylabel("Number of Incidents")
plt.xticks(rotation=45, ha="right")
plt.legend(title="Psych Impact", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
fig4.savefig('f4.png', dpi=300, bbox_inches='tight')