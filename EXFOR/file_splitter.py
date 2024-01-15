import pandas as pd
import numpy as np

df = pd.read_csv("EXFOR_protons_MF3_AME_no_RawNaN.csv")
for key in np.unique(df.Isotope):
  df2 = df[df.Isotope == key]
  df2.to_csv("reactions_isotope_" + key + "_nuisance.csv")

  
  
