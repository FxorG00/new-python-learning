import csv
import random
from datetime import datetime, timedelta

filename = "瘦身鱼_生产活动记录.csv"
batch_id = "BATCH-FS-003"  # ⚠️ 文档中瘦身鱼批次ID为 FS
start_date = datetime(2026, 3, 10, 23, 59, 0)
days = 46  # 文档截止到4月25日

# ⭐ 严格按文档定义：渔业因子
factors = [
    {"id": "EF-FSH-003", "ef": 0.4419, "mu": 11.245, "sigma": 1.875, "act_unit": "度"},  # 增氧机电
    {"id": "EF-FSH-004", "ef": 0.0002, "mu": 3800, "sigma": 480, "act_unit": "升"}  # ⚠️ 加工耗水(L)
]


def fmt_act(val, unit):
    return f"{round(val, 5)}({unit})"


def fmt_carb(val):
    return f"{round(val, 6)}(kgCO₂e)"


with open(filename, 'w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    writer.writerow(["record_id", "batch_id", "factor_id", "record_time", "activity_data", "calculated_carbon"])

    for i in range(days):
        current_time = start_date + timedelta(days=i)
        time_str = current_time.strftime('%Y-%m-%d %H:%M:%S')
        date_str = current_time.strftime('%Y%m%d')

        for idx, factor in enumerate(factors):
            ad_val = max(0, random.gauss(factor["mu"], factor["sigma"]))
            carbon = ad_val * factor["ef"]
            suffix = "S01" if idx == 0 else "W01"  # S设备, W水

            writer.writerow([
                f"REC-{date_str}-{suffix}",
                batch_id,
                factor["id"],
                time_str,
                fmt_act(ad_val, factor["act_unit"]),
                fmt_carb(carbon)
            ])

print(f"✅ 瘦身鱼数据生成完毕 -> {filename}")