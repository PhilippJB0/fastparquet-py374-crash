import pandas as pd

print("Creating dataframe")
df = pd.DataFrame([[1,2],[3,4]], columns=["c1", "c2"])
print("Saving dataframe")
df.to_parquet("test.pqt", compression="uncompressed")
print("Done")
