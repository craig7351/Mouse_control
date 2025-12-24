from core import WindowsEye, WindowsHand
import sys
import time

def main():
    eye = WindowsEye()
    hand = WindowsHand()

    if len(sys.argv) < 2:
        print("使用方式:")
        print("  python main.py screenshot [step]  - 取得當前桌面截圖 (含格線，預設 100)")
        print("  python main.py open_paint        - 自動化打開小畫家 (示範)")
        print("  python main.py click <x> <y>      - 點擊指定座標")
        print("  python main.py move <x> <y>       - 移動滑鼠到座標")
        print("  python main.py type <text>       - 輸入文字")
        print("  python main.py pick              - 輔助定位：5 秒後取得滑鼠所在位置")
        return

    command = sys.argv[1]

    if command == "screenshot":
        step = 100
        if len(sys.argv) > 2:
            step = int(sys.argv[2])
        path = eye.take_screenshot("manual_capture.png", step=step)
        print(f"截圖已儲存：{path} (格線大小: {step})")
        print("請將此截圖上傳給 AI，讓 AI 幫您分析座標。")

    elif command == "pick":
        print("--- 輔助定位模式 ---")
        print("請在 5 秒內將滑鼠移動到目標位置（例如：輸入框中心）...")
        for i in range(5, 0, -1):
            print(f"{i}...")
            time.sleep(1)
        pos = hand.get_mouse_pos()
        print(f"\n成功取得座標！")
        print(f"目標座標為: {pos.x} {pos.y}")
        print(f"您可以告訴 AI：『我幫你定位好了，起始座標是 {pos.x} {pos.y}』")

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

    elif command == "move":
        if len(sys.argv) < 4:
            print("錯誤: 請提供 x 和 y 座標")
            return
        x, y = int(sys.argv[2]), int(sys.argv[3])
        hand.move_to(x, y)

    elif command == "type":
        if len(sys.argv) < 3:
            print("錯誤: 請提供文字內容")
            return
        text = " ".join(sys.argv[2:])
        hand.type_text(text)

if __name__ == "__main__":
    main()
