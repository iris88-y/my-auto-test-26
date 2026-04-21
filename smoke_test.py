import requests

# 定义颜色代码
GREEN = '\033[92m'
RESET = '\033[0m'  # 重置颜色，避免影响后续输出

response = requests.get("https://api.github.com")
print(f"状态码：{response.status_code}")

assert response.status_code == 200, f"出错了！状态码是：{response.status_code}"
print(f"{GREEN}✅ 断言通过！接口状态正常。{RESET}")

# input("按回车键退出...")