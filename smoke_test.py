# 导入别人写的代码，requests能发送网络请求的工具包
import json

import requests

# 1. 换成一个有业务逻辑的免费测试接口（获取用户数据）
# 定义要访问的接口
url = "https://jsonplaceholder.typicode.com/users/2"
# 向指定的网址发送requests的get请求。返回给res
res = requests.get(url)

# 2. 打印状态码（和之前一样）
print(f"状态码是: {res.status_code}")

# 3. 把服务器返回的 JSON 数据转成 Python 字典
data = res.json()
# 格式化打印字典
print(json.dumps(data, indent=4, ensure_ascii=False))

# 4. 【核心】用 assert 验证返回内容是否符合预期
# 已知这个接口返回的用户名应该是 "Bret"
assert data["name"] == "Ervin Howell", f"用户名不对！实际是 {data['username']}"
print(f"✅ [PASS] 用户名验证通过: {data['username']}")

# 5. 再验证一下邮箱
assert "email" in data, "返回数据里没有邮箱字段！"
print(f"✅ [PASS] 邮箱字段存在: {data['email']}")

# input("按回车键退出...")