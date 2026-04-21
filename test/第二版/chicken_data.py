import csv
import random
from datetime import datetime, timedelta

filename = "黄鸡_生产活动记录.csv"
batch_id = "BATCH-JC-001"
start_date = datetime(2026, 2, 1, 23, 59, 0)
days = 70

# ⭐ 严格按文档定义：因子值取自字典表，活动单位按常识设定
factors = [
    {"id": "EF-CHK-003", "ef": 0.56, "mu": 18.5, "sigma": 2.5, "act_unit": "度"},  # 文档：kgCO2e/kWh
    {"id": "EF-CHK-004", "ef": 0.0002, "mu": 850, "sigma": 95, "act_unit": "升"}  # 文档：kgCO2e/L
]


def fmt_act(val, unit):
    """格式化实际消耗量：数值(单位)"""
    return f"{round(val, 5)}({unit})"


def fmt_carb(val):
    """格式化碳排量：文档规定必须为 kgCO₂e"""
    return f"{round(val, 6)}(kgCO₂e)"


with open(filename, 'w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    writer.writerow(["record_id", "batch_id", "factor_id", "record_time", "activity_data", "calculated_carbon"])

    for i in range(days):
        current_time = start_date + timedelta(days=i)
        time_str = current_time.strftime('%Y-%m-%d %H:%M:%S')
        date_str = current_time.strftime('%Y%m%d')

        for idx, factor in enumerate(factors):
            # 生成符合真实场景的活动数据（耗电度数、耗水升数）
            ad_val = max(0, random.gauss(factor["mu"], factor["sigma"]))
            # ⭐ 计算：活动数据 × 文档中的排放因子
            carbon = ad_val * factor["ef"]
            suffix = "E01" if idx == 0 else "W01"

            writer.writerow([
                f"REC-{date_str}-{suffix}",
                batch_id,
                factor["id"],
                time_str,
                fmt_act(ad_val, factor["act_unit"]),  # 如：18.52341(度)
                fmt_carb(carbon)  # 如：10.373109(kgCO₂e)
            ])

print(f"✅ 黄鸡数据生成完毕 -> {filename}")