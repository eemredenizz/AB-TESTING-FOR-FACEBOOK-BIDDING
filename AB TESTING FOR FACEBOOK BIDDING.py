######################################################################
# INDUSTRIAL PROJECT // AB TESTING FOR FACEBOOK BIDDING
######################################################################
#Impression: Reklam görüntüleme sayısı
#Click: Görüntülenen reklama tıklama sayısı
#Purchase: Tıklanan reklamlar sonrası satın alınan ürün sayısı
#Earning: Satın alınan ürünler sonrası elde edilen kazanç

#Görev 1: Veriyi Hazırlama ve Analiz Etme

import itertools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# !pip install statsmodels
import statsmodels.stats.api as sms
from scipy.stats import ttest_1samp, shapiro, levene, ttest_ind, mannwhitneyu, \
    pearsonr, spearmanr, kendalltau, f_oneway, kruskal
from statsmodels.stats.proportion import proportions_ztest

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 10)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

control_group = pd.read_excel("ab_testing.xlsx", sheet_name="Control Group")
test_group = pd.read_excel("ab_testing.xlsx", sheet_name="Test Group")

control_group.head()
test_group.head()

selected1 = control_group["Purchase"]
selected2 = test_group["Purchase"]

df = pd.concat([control_group["Purchase"], test_group["Purchase"]])

df.head()

control_group["Purchase"].describe().T
test_group["Purchase"].describe().T

#################
#Hipotezler
#################

####################
#Normallik varsayımı
####################
#H0 : M1 = M2
#H1 : M1!= M2
test_stats1, pvalue1 = shapiro(selected1)
print("Test Stat = %.4f, p-value1 = %.4f" % (test_stats1, pvalue1))

test_stats2, pvalue2 = shapiro(selected2)
print("Test Stat = %.4f, p-value2 = %.4f" % (test_stats2, pvalue2))

#H0 reddedilemez
#Normallik varsayımı sağlanır

####################
#Varyans homojenligi
####################
#H0 : M1 = M2
#H1 : M1!= M2

test_stats, pvalue = levene(selected1,
                            selected2)
print("Test Stat = %.4f, p-value = %.4f" % (test_stats, pvalue))

#H0 reddedilemez
#Varyans homojenliği sağlanır

########################################
# Normallik varsayımı ve varyans homojenliği sağlanıyorsa
########################################
f_oneway(selected1,
         selected2)

#pvalue > 0.05 H0 reddedilemez

# Normallik varsayımı ve varsayım homojenliği reddedilemediği için oneway anova testi yaptık.
# Yaptığımız test sonucunda pvalue değerini 0.34 bulduk.
# Bu sonuçtan çıkarımımız değişkenler arasında anlamlı bir farklılık yoktur.
