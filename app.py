# 匯入 Flask 類和其他必需的函式
from flask import Flask, render_template, jsonify
import requests

# 初始化 Flask 應用
app = Flask(__name__)

# 設定 "/api/rates" 路由，當訪問此路由時，會調用 get_exchange_rates 函數
@app.route("/api/rates")
def get_exchange_rates():
    # 向外部 API (https://tw.rter.info/capi.php) 發送 GET 請求，獲取匯率數據
    response = requests.get("https://tw.rter.info/capi.php")
    # 以 JSON 格式返回匯率數據
    return jsonify(response.json())

# 設定根路由 ("/")，當用戶訪問主頁時會加載 index.html
@app.route("/", methods=["GET"])
def index():
    # 渲染並返回 index.html 頁面
    return render_template("index.html")

# 應用程序運行，debug 模式開啟
if __name__ == "__main__":
    app.run(debug=True)
