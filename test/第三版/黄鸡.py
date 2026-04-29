import csv
import random
from datetime import datetime, timedelta

# 输出文件
output_file = "江村黄鸡_生产活动记录_严格版.csv"
batch_id = "BATCH-JC-001"
start_date = datetime(2026, 2, 1, 12, 0)  # 批次开始时间
total_days = 71  # 2月1日至4月12日
scale = 5000  # 生产规模：5000只

# 江村黄鸡排放因子配置（完全来自字典表）
factor_configs = [
    # 1. 育种阶段 (第1-20天)
    {"id": "EF-CHK-001", "name": "饲料消耗", "stage": "1.育种阶段", "days_offset": 0, "duration": 20, "mu_per": 0.028, "sigma_per": 0.004, "ef": 0.65, "act_unit": "kg", "calc_type": "per_bird"},
    {"id": "EF-CHK-002", "name": "种苗繁育耗电", "stage": "1.育种阶段", "days_offset": 0, "duration": 20, "mu_total": 45.0, "sigma_total": 8.0, "ef": 0.56, "act_unit": "度", "calc_type": "total"},
    # 2. 养殖阶段 (第21-70天)
    {"id": "EF-CHK-003", "name": "养殖场耗电", "stage": "2.养殖阶段", "days_offset": 20, "duration": 50, "mu_total": 85.0, "sigma_total": 12.0, "ef": 0.56, "act_unit": "度", "calc_type": "total"},
    {"id": "EF-CHK-004", "name": "养殖用水", "stage": "2.养殖阶段", "days_offset": 20, "duration": 50, "mu_total": 820.0, "sigma_total": 110.0, "ef": 0.0002, "act_unit": "升", "calc_type": "total"},
    {"id": "EF-CHK-005", "name": "粪污处理", "stage": "2.养殖阶段", "days_offset": 20, "duration": 50, "mu_total": 120.0, "sigma_total": 20.0, "ef": 0.12608, "act_unit": "kg", "calc_type": "total"},
    # 3. 加工阶段 (第71-75天)
    {"id": "EF-CHK-006", "name": "屠宰线耗电", "stage": "3.加工阶段", "days_offset": 70, "duration": 5, "mu_total": 320.0, "sigma_total": 40.0, "ef": 0.56, "act_unit": "度", "calc_type": "total"},
    {"id": "EF-CHK-007", "name": "烫毛热能", "stage": "3.加工阶段", "days_offset": 70, "duration": 5, "mu_total": 12.5, "sigma_total": 2.5, "ef": 2.1622, "act_unit": "m³", "calc_type": "total"},
    # 4. 运输阶段 (第76天)
    {"id": "EF-CHK-008", "name": "活体运输", "stage": "4.运输阶段", "days_offset": 75, "duration": 1, "mu_total": 85.0, "sigma_total": 10.0, "ef": 2.68, "act_unit": "L", "calc_type": "total"},
    # 5. 仓储销售 (第77-86天) 注：批次表结束于第71天，但仓储阶段通常独立于批次周期。此处按文档逻辑模拟10天。
    {"id": "EF-CHK-009", "name": "冷库耗电", "stage": "5.仓储销售", "days_offset": 76, "duration": 10, "mu_total": 180.0, "sigma_total": 25.0, "ef": 0.6379, "act_unit": "度", "calc_type": "total"},
]

def format_value(val, unit):
    """格式化数值与单位：数值(单位)"""
    return f"{round(val, 5)}({unit})"

def format_carbon(val):
    """格式化碳排量：数值(kgCO₂e)"""
    return f"{round(val, 6)}(kgCO₂e)"

with open(output_file, 'w', newline='', encoding='utf-8-sig') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["record_id", "batch_id", "factor_id", "record_time", "activity_data", "calculated_carbon"])

    for cfg in factor_configs:
        stage_start_date = start_date + timedelta(days=cfg["days_offset"])
        for day in range(cfg["duration"]):
            current_date = stage_start_date + timedelta(days=day)
            date_str = current_date.strftime('%Y%m%d')
            time_str = current_date.strftime('%Y/%m/%d %H:%M')

            # 1. 生成模拟的活动数据
            if cfg["calc_type"] == "per_bird":
                activity_val = max(0.01, random.gauss(cfg["mu_per"], cfg["sigma_per"])) * scale
            else:  # calc_type == "total"
                activity_val = max(0.01, random.gauss(cfg["mu_total"], cfg["sigma_total"]))

            # 2. 计算单次碳排放
            carbon_val = activity_val * cfg["ef"]

            # 3. 生成记录ID (参考示例：REC-日期-类型码)
            type_map = {"EF-CHK-001": "F01", "EF-CHK-002": "E01", "EF-CHK-003": "E01",
                       "EF-CHK-004": "W01", "EF-CHK-005": "M01", "EF-CHK-006": "E01",
                       "EF-CHK-007": "G01", "EF-CHK-008": "D01", "EF-CHK-009": "E01"}
            suffix = type_map.get(cfg["id"], "X01")
            record_id = f"REC-{date_str}-{suffix}"

            writer.writerow([
                record_id,
                batch_id,
                cfg["id"],
                time_str,
                format_value(activity_val, cfg["act_unit"]),
                format_carbon(carbon_val)
            ])

print(f"✅ 江村黄鸡仿真数据生成完毕！文件：{output_file}")