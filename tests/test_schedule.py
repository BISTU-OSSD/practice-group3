import os
import sys
# 把项目根目录加入搜索路径
root_path = os.path.abspath("..")
sys.path.append(root_path)

from schedule.schedule import parse_schedule_csv

# 拼接完整绝对路径，彻底解决找不到csv的问题
TEST_CSV_PATH = os.path.join(root_path, "schedule", "demo_schedule.csv")

def test_csv_parse():
    assert os.path.exists(TEST_CSV_PATH), "测试CSV文件缺失"
    data = parse_schedule_csv(TEST_CSV_PATH)
    assert len(data) == 3, "课表行数解析错误"
    first_class = data[0]
    assert first_class["课程名称"] == "高等数学"
    assert first_class["教室"] == "301"
    print("✅ 全部单元测试通过！")

if __name__ == "__main__":
    test_csv_parse()