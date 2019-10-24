# 导包
import yaml
# 获取文件流 并调用load方法
with open("../data/data.yaml","r",encoding="utf-8")as f:
    # 解析文件流
    print(yaml.load(f))

