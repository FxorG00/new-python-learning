import csv
import random
from datetime import datetime, timedelta

filename = "黄皮_生产活动记录.csv"
start_date = datetime(2026, 3, 1, 23, 59, 0)  # 对齐文档批次时间
total_days = 136  # 约4.5个月种植期

# ⭐ 严格按文档定义：黄皮因子语义修正
factors = [
    {"id": "EF-FRT-001", "ef": 3.285, "mu": 1.58, "sigma": 0.48, "act_unit": "kg"},  # 化肥(kg)
    {"id": "EF-FRT-003", "ef": 75.08, "mu": 0.124, "sigma": 0.035, "act_unit": "hm²"}  # ⚠️ 灌溉面积(hm²)
]


def fmt_act(val, unit):
    return f"{round(val, 5)}({unit})"


def fmt_carb(val):
    return f"{round(val, 6)}(kgCO₂e)"


with open(filename, 'w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    writer.writerow(["record_id", "batch_id", "factor_id", "record_time", "activity_data", "calculated_carbon"])

    # 动态多批次：HP-001, HP-002, HP-003
    batch_num = 3
    days_per_batch = total_days // batch_num

    for b in range(batch_num):
        batch_id = f"BATCH-HP-{str(b + 1).zfill(3)}"
        start_day = b * days_per_batch

        for d in range(days_per_batch):
            cur_time = start_date + timedelta(days=start_day + d)
            time_str = cur_time.strftime('%Y-%m-%d %H:%M:%S')
            date_str = cur_time.strftime('%Y%m%d')

            for idx, factor in enumerate(factors):
                ad_val = max(0, random.gauss(factor["mu"], factor["sigma"]))
                carbon = ad_val * factor["ef"]
                suffix = "F01" if idx == 0 else "I01"  # F化肥, I灌溉

                writer.writerow([
                    f"REC-{date_str}-{suffix}",
                    batch_id,
                    factor["id"],
                    time_str,
                    fmt_act(ad_val, factor["act_unit"]),  # 如：0.12780(hm²)
                    fmt_carb(carbon)
                ])

print(f"✅ 黄皮数据生成完毕 -> {filename}")