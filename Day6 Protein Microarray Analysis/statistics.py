#-----------------------------------------------------#
#                   Library imports                   #

#-----------------------------------------------------#
from scipy import stats
import pandas as pd


#-----------------------------------------------------#
#                  Median Difference                  #
#-----------------------------------------------------#
def perform_mediandiff(dt_healthy, dt_cancer):
    gesamt = pd.merge(dt_healthy,dt_cancer,how='outer').filter(['name','description'])
    healthy_data = dt_healthy.drop(columns=['name','description']).median(axis=1)
    cancer_data = dt_cancer.drop(columns=['name', 'description']).median(axis=1)
    #print(healthy_data.median(axis=1))
    #print(dt_healthy.head().to_string())
    gesamt['median_diff'] = (healthy_data - cancer_data).abs()
    return gesamt.sort_values(by=['median_diff'],ascending=False)

#-----------------------------------------------------#
#                  Independent T-Test                 #
#-----------------------------------------------------#
def perform_ttests(dt_healthy, dt_cancer):
    gesamt = pd.merge(dt_healthy, dt_cancer, how='outer').filter(['name', 'description'])
    healthy_data = dt_healthy.drop(columns=['name', 'description'])
    cancer_data = dt_cancer.drop(columns=['name', 'description'])
    print(healthy_data)
    print(cancer_data)
    gesamt['pvalue'] = ((stats.ttest_ind(healthy_data, cancer_data,axis=1,equal_var=False))[1])
    return gesamt.sort_values(by=['pvalue'])

'''
g)
According to:
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8062265/
-> Transmembrane and coiled-coil domain family 3 (TMCC3) regulates breast cancer stem cell
-> Transmembrane protein and coiled-coil-helix-coiled-coil-helix domain containing is under top 3 from T-test

https://translational-medicine.biomedcentral.com/articles/10.1186/s12967-023-04502-y#:~:text=Low%20serum%20selenium%20and%20altered,interact%20with%20tumour%20selenoprotein%20expression.
-> Low serum selenium and altered tumour RNA expression of certain selenoproteins are associated with a poor breast cancer prognosis
(-> top 1 is selenoprotein X, 1 (SEPX1)) 

'''