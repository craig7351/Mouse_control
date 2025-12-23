from core import WindowsEye, WindowsHand
import sys
import time

def main():
    eye = WindowsEye()
    hand = WindowsHand()
    _reader = None # 懶加載 OCR

    def get_reader():
        nonlocal _reader
        if _reader is None:
            from reader import WindowsReader
            _reader = WindowsReader()
        return _reader

    if len(sys.argv) < 2:
        print("使用方式:")
        print("  python main.py screenshot [step]  - 取得當前桌面截圖 (含格線，預設 100)")
        print("  python main.py open_paint        - 自動化打開小畫家 (示範)")
        print("  python main.py click <x> <y>      - 點擊指定座標")
        print("  python main.py ocr                - 辨識最近一張截圖中的文字")
        print("  python main.py find <text>        - 在畫面上尋找特定文字並點擊")
        return

    command = sys.argv[1]

    if command == "screenshot":
        step = 100
        if len(sys.argv) > 2:
            step = int(sys.argv[2])
        path = eye.take_screenshot("manual_capture.png", step=step)
        print(f"截圖已儲存：{path} (格線大小: {step})")
        print("請查看圖片中的格線來決定要操作的座標。")

    elif command == "open_paint":
        print("準備執行自動化流程...")
        hand.open_start_menu()
        time.sleep(0.5)
        hand.type_text("paint")
        time.sleep(1)
        hand.press_key('enter')
        print("已嘗試開啟小畫家。")

    elif command == "click":
        if len(sys.argv) < 4:
            print("錯誤: 請提供 x 和 y 座標")
            return
        x, y = int(sys.argv[2]), int(sys.argv[3])
        hand.click(x, y)

    elif command == "ocr":
        # 預設辨識最後一張截圖
        img_path = "screenshots/manual_capture.png"
        reader = get_reader()
        results = reader.read_text(img_path)
        print("\n--- 辨識結果 ---")
        for res in results:
            print(f"[{res['text']}] 座標: {res['center']}")

    elif command == "find":
        if len(sys.argv) < 3:
            print("請輸入要尋找的文字")
            return
        target = sys.argv[2]
        img_path = eye.take_screenshot("ocr_search.png") # 先截圖再找
        reader = get_reader()
        pos = reader.find_text_location(img_path, target)
        if pos:
            print(f"找到文字 '{target}' 在 {pos}，準備點擊...")
            hand.click(pos[0], pos[1])
        else:
            print(f"找不到文字: '{target}'")

if __name__ == "__main__":
    main()
