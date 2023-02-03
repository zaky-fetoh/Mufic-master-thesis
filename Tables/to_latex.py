import pandas as pd
  
df = pd.read_excel("Tables/modifiedMBl.xlsx")

rltx = df.to_latex(index=False)

f = open("Tables/modifMoble.tex","w")
f.write(rltx)
f.close(); 