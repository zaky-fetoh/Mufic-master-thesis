import pandas as pd
  
df = pd.read_excel("./Tables/reltx.xlsx")

rltx = df.to_latex(index=False)

f = open("Tables/relatedlatex111.tex","w")
f.write(rltx)
f.close(); 