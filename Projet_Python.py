import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

data = pd.read_csv('/Loan_data.csv')

data.describe()
data.info()
data.isnull().sum()
data.head()
data=data.dropna() #Suppression de 26 lignes

#----------------------------------------------------------
#                        Etape 1
#   Visualisation des données pour la détection d'outlier
#
#----------------------------------------------------------
plt.close()
plt.figure(1)
plt.figure(figsize=(10,12))
for i in np.arange(start=0,stop=data.shape[1]):
    plt.subplot(7, 3, i+1)
    plt.plot(data.index.values,data.iloc[:,i],marker="o",ls=' ',alpha=0.7,color='#0f6f80')
    plt.xlabel('Indices d\'observation ')
    plt.ylabel(data.columns[i])
plt.tight_layout()
plt.show()

#Détection d'outliers
data=data[(data["term"]<500)] 

#----------------------------------------------------------
#                        Etape 2
#            Echantillonnage - Par Tirage stratifié
#----------------------------------------------------------

data, data_pred = train_test_split(data, test_size=0.2, random_state=5, stratify=data["approve"])

#----------------------------------------------------------
#                        Etape 3
#                   Analyse Univariée
#----------------------------------------------------------
col=[0,8,9,10,16,17]
j=1
plt.figure(figsize=(8,10))
for i in col:
    plt.subplot(2, 3, j)
    j=j+1
    data.iloc[:,i].value_counts().plot.pie(subplots=True, figsize = (3, 3) , autopct='%1.1f%%',startangle=90, colors = [ '#ae7181', '#a2bffe' ,'#a2cffe'])    
plt.tight_layout() 
plt.show()

#Si possible améliorer ce plot.pie !
data.iloc[:,15].value_counts().plot.pie(subplots=True, figsize = (6, 6) , autopct='%1.0f%%',startangle=90, colors = [ '#ae7181','#d58a94' ,'#c292a1', '#a2bffe' ,'#a2cffe','#658cbb','#3b5b92','#014182'])
 
    
#----------------------------------------------------------
#                        Etape 4
#                    Analyse Bivariée
#----------------------------------------------------------    
    
#Optimiser les histogrammes ci-dessous
t6 = pd.crosstab(data.sex, data.approve, normalize=True)
t6.plot.bar()
t7 = pd.crosstab(data.race, data.approve, normalize=True)
t7.plot.bar()
t8 = pd.crosstab(data.married, data.approve, normalize=True)
t8.plot.bar()

#Matrice de corrélation
plt.figure(figsize=(10,10))
masque  =  np.tril(data.corr())
sns.heatmap(data.corr(),annot=True,vmin=-1, vmax=1,fmt='.2f',cmap= 'bwr' ,square=True,mask = masque)
plt.show()    

#Attention c'est très long a éxécuter !
sns.pairplot(data)

#Ajouter analyse multivarié (ex: race*university*approve)

#Je veux afficher les stats descriptives sur les revenus  en fonctions de 
#si les prêt a été approuvé ou non
tab=[]
tab.append(data.loc[data['approve']==0,'atotinc'].describe())
tab.append(data.loc[data['approve']==1,'atotinc'].describe())
print(tab)

