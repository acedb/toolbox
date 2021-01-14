import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
​
num_feat = ['gene1', 'gene2', 'gene3', 'gene4', 'gene5']
​
for numerical_feature in num_feat:

    fig, ax = plt.subplots(1, 3, figsize = (20, 8))

    ax[0].set_title(f'Distribution of: {numerical_feature.capitalize()}')
    sns.histplot(data = df[numerical_feature], kde = True, ax = ax[0])

    ax[1].set_title(f'Boxplot of: {numerical_feature.capitalize()}')
    sns.boxplot(data = df[numerical_feature], ax = ax[1])

    ax[2].set_title(f'Gaussianity of: {numerical_feature.capitalize()}')
    # line 's' depicts standardised line
    sm.qqplot(df[numerical_feature], line = 's', ax = ax[2])
