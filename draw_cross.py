from core import WindowsHand
import time

def auto_draw_cross():
    hand = WindowsHand()
    
    print("=== 開始自動化任務：小畫家畫叉叉 ===")
    
    # 1. 打開小畫家
    hand.open_start_menu()
    hand.type_text("paint")
    time.sleep(1)
    hand.press_key('enter')
    time.sleep(3) # 等待程式開啟
    
    # 2. 最大化視窗
    hand.maximize_window()
    
    # 3. 準備畫叉叉 (假設最大化後中間區域為畫布)
    # 取螢幕中心點附近進行繪製 (PyAutoGUI 可取得螢幕大小)
    import pyautogui
    screen_w, screen_h = pyautogui.size()
    
    center_x = screen_w // 2
    center_y = screen_h // 2
    offset = 200 # 叉叉的大小半徑
    
    print(f"正在畫布中央 ({center_x}, {center_y}) 畫叉叉...")
    
    # 第一條線: 左上到右下
    hand.move_to(center_x - offset, center_y - offset)
    hand.drag_to(center_x + offset, center_y + offset)
    
    time.sleep(0.5)
    
    # 第二條線: 右上到左下
    hand.move_to(center_x + offset, center_y - offset)
    hand.drag_to(center_x - offset, center_y + offset)
    
    print("任務完成！")

if __name__ == "__main__":
    auto_draw_cross()
