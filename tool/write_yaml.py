# 导包
import yaml

# 写入 调用 dump
with open("../data/write.yaml", "w", encoding="utf-8")as f:
    # 准备写入的数据
    data = {"name": "张三", "age": 18}
    yaml.dump(data, f, allow_unicode=True)
