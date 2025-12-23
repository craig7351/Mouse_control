from core import WindowsEye, WindowsHand
import sys
import time

def main():
    eye = WindowsEye()
    hand = WindowsHand()

    if len(sys.argv) < 2:
        print("使用方式:")
        print("  python main.py screenshot         - 取得當前桌面截圖 (含格線)")
        print("  python main.py open_paint        - 自動化打開小畫家 (示範)")
        print("  python main.py click <x> <y>      - 點擊指定座標")
        return

    command = sys.argv[1]

    if command == "screenshot":
        path = eye.take_screenshot("manual_capture.png")
        print(f"截圖已儲存：{path}")
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

if __name__ == "__main__":
    main()
