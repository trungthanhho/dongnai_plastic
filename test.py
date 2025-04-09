import pandas as pd

df = pd.read_excel(r"C:\Users\DN-CDS-XNBB1\Downloads\DANH_MUC_SAN_PHAM_FINAL_DATA.xlsx")

# Lấy 4 cột đầu tiên
first_four_columns = df.iloc[:, :4]

print(first_four_columns.head())  # In 5 dòng đầu của 4 cột đầu

# test github