import pandas as pd

# Đường dẫn file
file_path = r"C:\Users\DN-CDS-XNBB1\Downloads\CÔNG XNBB THÁNG 03.2025 - CHỐT.xlsx"

# Mở file Excel
xls = pd.ExcelFile(file_path)

# Lấy tất cả sheet
sheet_names = xls.sheet_names

# Hàm xử lý từng sheet
def extract_info(sheet_name):
    df = xls.parse(sheet_name, skiprows=3)
    df_selected = df.iloc[:, [1, 3, 4]]  # Mã NV, Họ tên, Phòng ban
    df_selected.columns = ['Mã NV', 'Họ tên', 'Phòng ban']
    df_selected['Sheet'] = sheet_name
    return df_selected.dropna(subset=['Mã NV', 'Họ tên', 'Phòng ban'])

# Gộp dữ liệu từ tất cả các bảng
all_data = pd.concat([extract_info(name) for name in sheet_names], ignore_index=True)

# Xuất ra file mới
all_data.to_excel("TONG_HOP_NHAN_VIEN.xlsx", index=False)
