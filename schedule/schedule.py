import csv
from typing import List, Dict

def parse_schedule_csv(file_path: str) -> List[Dict]:
    """
    解析课表CSV文件，返回标准化课表数据列表
    :param file_path: csv文件本地路径
    :return: 列表，每个元素是单节课字典{课程名称,星期,节次,教室,授课老师}
    """
    schedule_data = []
    # utf-8-sig 兼容Windows导出CSV的中文乱码
    with open(file_path, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # 清洗字段，去除多余空格
            clean_row = {k.strip(): v.strip() for k, v in row.items()}
            schedule_data.append(clean_row)
    return schedule_data

# 本地调试入口
if __name__ == "__main__":
    res = parse_schedule_csv("demo_schedule.csv")
    for lesson in res:
        print(lesson)