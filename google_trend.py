import pandas as pd
from datetime import datetime
import re


# Đọc file CSV
df = pd.read_csv("asset/trending_VN_1d_20250410-1010.csv")


# Gán lại tên cột nếu cần (chắc chắn đúng thứ tự 6 cột)
df.columns = ['Xu_huong', 'Luot_tim_kiem', 'Bat_dau', 'Ket_thuc', 'Chi_tiet', 'Lien_ket']

# Hàm chuyển đổi lượt tìm kiếm
def chuyen_doi_luot_tim_kiem(x):
    try:
        return int(x.lower().replace('n+', '').strip()) * 1000
    except:
        return 0
    
# Hàm chuẩn hóa định dạng thời gian
def chuan_hoa_thoi_gian(s):
    try:
        # Loại bỏ "lúc", "UTC+7", và strip chuỗi
        s = s.replace("lúc", "").replace("UTC+7", "").strip()

        # Đổi "9 tháng 4, 2025" => "09-04-2025"
        pattern = r"(\d{1,2}):(\d{2}):(\d{2})\s+(\d{1,2}) tháng (\d{1,2}), (\d{4})"
        match = re.match(pattern, s)
        if match:
            gio, phut, giay, ngay, thang, nam = match.groups()
            dt_str = f"{nam}-{int(thang):02d}-{int(ngay):02d} {gio}:{phut}:{giay}"
            return datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
    except:
        return pd.NaT
    
# Áp dụng vào cột 'Bat_dau'
df['Bat_dau'] = df['Bat_dau'].apply(chuan_hoa_thoi_gian)

# Thêm cột số hóa lượt tìm kiếm
df['Luot_tim_kiem_so'] = df['Luot_tim_kiem'].apply(chuyen_doi_luot_tim_kiem)

# Sắp xếp theo lượt tìm kiếm giảm dần
df_sorted = df.sort_values(by='Luot_tim_kiem_so', ascending=False)

# In top 10 xu hướng với đủ 6 cột
print("\n -------Top 10 xu hướng:---------")
print(df_sorted[['Xu_huong', 'Luot_tim_kiem', 'Bat_dau']].head(10))