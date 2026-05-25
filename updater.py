import json
import os
from datetime import datetime

def fetch_and_update_politics():
    # 1. 模拟从大马政治新闻源或公开 API 获取实时数据 (Live Data)
    # 实际开发中，这里可以写 requests 去抓取本地媒体或特定选区数据
    print("正在连接大马政治数据源...")
    
    # 获取大马当前时间 (GMT+8)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    # 2. 实时政治阵营席位矩阵数据
    live_data = {
        "last_updated": current_time,
        "total_seats": 222,
        "required_majority": 112,
        "alert_news": "GE16 选区划分谈判进入白热化，各联盟在东马及北马核心选区的暗涌加剧。",
        "coalitions": [
            {
                "id": "ph",
                "name": "Pakatan Harapan (PH)",
                "seats": 86,
                "color": "#dc3545",
                "trend": "up",
                "strategy": "专注巩固西马朝野混战中的城市与华裔基本盘。"
            },
            {
                "id": "pn",
                "name": "Perikatan Nasional (PN)",
                "seats": 73,
                "color": "#0d6efd",
                "trend": "stable",
                "strategy": "利用马来核心选区优势，全面渗透半岛西海岸郊区。"
            },
            {
                "id": "bn",
                "name": "Barisan Nasional (BN)",
                "seats": 35,
                "color": "#0a2240",
                "trend": "down",
                "strategy": "走传统基层路线，在混合选区扮演关键少数平衡者。"
            },
            {
                "id": "borneo",
                "name": "Borneo Blocks (GPS/GRS)",
                "seats": 28,
                "color": "#ffc107",
                "trend": "up",
                "strategy": "东马本土意识高涨，保持高姿态的‘造王者’政治筹码。"
            }
        ]
    }
    
    # 3. 确保 data 文件夹存在
    if not os.path.exists('data'):
        os.makedirs('data')
        
    # 4. 自动写入并覆盖 JSON 文件
    with open('data/ge16_live.json', 'w', encoding='utf-8') as f:
        json.dump(live_data, f, ensure_ascii=False, indent=2)
        
    print(f"成功同步 Live Data！更新时间：{current_time}")

if __name__ == "__main__":
    fetch_and_update_politics()
