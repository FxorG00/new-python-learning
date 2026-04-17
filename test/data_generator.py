import csv
import random
from datetime import datetime, timedelta

# 准备生成 CSV 文件
filename = "Activity_Data_Record_Simulated.csv"

# 江村黄鸡参数设定 (养殖期70天)
batch_id = "BATCH-JC-001"
start_date = datetime(2026, 2, 1, 23, 59, 0)
days = 70

# 因子设定 (对应静态表)
ef_elec_id = "EF-CHK-003"
ef_elec_value = 0.56  # 耗电因子
mu_elec = 0.0053  # 每天耗电均值(度)
sigma_elec = 0.0005  # 耗电波动范围

ef_water_id = "EF-CHK-004"
ef_water_value = 0.0002  # 耗水因子
mu_water = 0.15  # 每天耗水均值(升)
sigma_water = 0.02  # 耗水波动范围

with open(filename, 'w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    # 写入表头
    writer.writerow(["record_id", "batch_id", "factor_id", "record_time", "activity_data", "calculated_carbon"])

    # 循环生成70天的每日耗电和耗水数据
    for i in range(days):
        current_time = start_date + timedelta(days=i)
        time_str = current_time.strftime('%Y-%m-%d %H:%M:%S')
        date_str = current_time.strftime('%Y%m%d')

        # 1. 生成耗电记录
        ad_elec = max(0, random.gauss(mu_elec, sigma_elec))  # 正态分布生成波动数据
        carbon_elec = ad_elec * ef_elec_value
        writer.writerow([f"REC-{date_str}-E01", batch_id, ef_elec_id, time_str, round(ad_elec, 5), round(carbon_elec, 6)])

        # 2. 生成耗水记录
        ad_water = max(0, random.gauss(mu_water, sigma_water))
        carbon_water = ad_water * ef_water_value
        writer.writerow([f"REC-{date_str}-W01", batch_id, ef_water_id, time_str, round(ad_water, 5), round(carbon_water, 6)])

print(f"牛逼！成功生成{days * 2}条仿真物联网数据，已保存至 {filename}")