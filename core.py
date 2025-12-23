import pyautogui
from PIL import Image, ImageDraw, ImageFont
import os
import time

class WindowsEye:
    """負責『看』螢幕的功能"""
    def __init__(self, output_dir="screenshots"):
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def take_screenshot(self, filename="screenshot.png", add_grid=True):
        """截取螢幕，並可選擇是否加上座標格線"""
        screenshot = pyautogui.screenshot()
        if add_grid:
            screenshot = self._draw_grid(screenshot)
        
        filepath = os.path.join(self.output_dir, filename)
        screenshot.save(filepath)
        return filepath

    def _draw_grid(self, image):
        """在圖片上繪製座標格線，方便 AI 識別位置"""
        draw = ImageDraw.Draw(image)
        width, height = image.size
        
        # 設定格線間距 (例如每 100 像素)
        step = 100
        
        # 畫垂直線
        for x in range(0, width, step):
            draw.line([(x, 0), (x, height)], fill="red", width=1)
            draw.text((x + 2, 5), str(x), fill="red")
            
        # 畫水平線
        for y in range(0, height, step):
            draw.line([(0, y), (width, y)], fill="red", width=1)
            draw.text((5, y + 2), str(y), fill="red")
            
        return image

class WindowsHand:
    """負責『操作』的功能"""
    def __init__(self):
        # 設定安全機制：將滑鼠移至角落可停止
        pyautogui.FAILSAFE = True
        pyautogui.PAUSE = 0.5 

    def click(self, x, y, clicks=1):
        print(f"正在點擊座標: ({x}, {y})")
        pyautogui.click(x, y, clicks=clicks)

    def type_text(self, text):
        print(f"正在輸入文字: {text}")
        pyautogui.write(text, interval=0.1)

    def press_key(self, key):
        print(f"正在按下按鍵: {key}")
        pyautogui.press(key)

    def open_start_menu(self):
        """快捷動作：開啟開始功能表連"""
        print("正在開啟開始功能表...")
        pyautogui.press('win')
        time.sleep(1)

    def maximize_window(self):
        """快捷動作：最大化當前視窗 (Win + Up)"""
        print("正在最大化視窗...")
        pyautogui.hotkey('win', 'up')
        time.sleep(1)

    def drag_to(self, x, y):
        """按住滑鼠左鍵拖曳到指定座標"""
        print(f"正在拖曳至座標: ({x}, {y})")
        pyautogui.dragTo(x, y, duration=0.5)

    def move_to(self, x, y):
        """移動滑鼠到指定座標"""
        pyautogui.moveTo(x, y, duration=0.3)

if __name__ == "__main__":
    eye = WindowsEye()
    hand = WindowsHand()
    
    # 範例流程
    print("3 秒後開始執行範例：截圖並開啟開始功能表")
    time.sleep(3)
    
    # 1. 截圖
    path = eye.take_screenshot("initial_state.png")
    print(f"截圖已儲存至: {path}")
    
    # 2. 開啟開始功能表
    hand.open_start_menu()
    
    # 3. 再截一張圖確認狀態
    time.sleep(1)
    eye.take_screenshot("after_start_menu.png")
