import easyocr
import numpy as np
from PIL import Image

class WindowsReader:
    """負責『讀』螢幕上的文字"""
    def __init__(self, languages=['ch_tra', 'en']):
        print(f"正在初始化 OCR 引擎 (語言: {languages})...")
        # gpu=False 確保在沒有 CUDA 的環境也能執行
        self.reader = easyocr.Reader(languages, gpu=False)

    def read_text(self, image_path):
        """讀取圖片中的所有文字及其座標"""
        print(f"正在辨識圖片: {image_path}")
        results = self.reader.readtext(image_path)
        
        parsed_results = []
        for (bbox, text, prob) in results:
            # bbox 格式: [[x1, y1], [x2, y1], [x2, y2], [x1, y2]]
            # 計算中心點
            center_x = int(sum([p[0] for p in bbox]) / 4)
            center_y = int(sum([p[1] for p in bbox]) / 4)
            parsed_results.append({
                "text": text,
                "center": (center_x, center_y),
                "confidence": prob,
                "bbox": bbox
            })
        return parsed_results

    def find_text_location(self, image_path, target_text):
        """在圖片中尋找特定文字的座標"""
        results = self.read_text(image_path)
        for res in results:
            if target_text.lower() in res["text"].lower():
                return res["center"]
        return None

if __name__ == "__main__":
    # 測試代碼
    reader = WindowsReader()
    # 假設已經有一張截圖
    import os
    test_img = "screenshots/manual_capture.png"
    if os.path.exists(test_img):
        res = reader.read_text(test_img)
        for item in res:
            print(f"文字: {item['text']} | 座標: {item['center']}")
    else:
        print("請先執行 main.py screenshot 產生測試截圖")
