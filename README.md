# Windows AI Eye 助手

這是一個讓 AI 能夠「看見」並「操作」Windows 桌面的自動化工具。

## 功能特色
- **視覺定位**：自動截取螢幕並疊加 100px 間距的紅色座標格線，方便 AI 或使用者精準定位。
- **自動化操作**：支援滑鼠點擊、鍵盤輸入與系統組合鍵（如 Win 鍵）。
- **Fail-safe 機制**：內建 PyAutoGUI 安全開關，若腳本失控，將滑鼠移至螢幕四個角落即可強制停止。

## 安裝與執行

### 1. 環境設定
請確保已安裝 Python，然後執行：
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install pyautogui Pillow
```

### 2. 使用方式
- **取得當前桌面截圖 (含格線)**：
  ```powershell
  python main.py screenshot
  ```
  截圖將儲存在 `screenshots/` 資料夾中。

- **自動開啟「小畫家」範例**：
  ```powershell
  python main.py open_paint
  ```

- **精確點擊某座標**：
  ```powershell
  python main.py click 500 500
  ```

## AI 協作流程
1. 執行 `python main.py screenshot`。
2. 將 `screenshots/manual_capture.png` 上傳給 AI。
3. 告訴 AI 你的目標（例如：「點擊 Chrome 圖示」）。
4. AI 會根據格線分析座標並回傳指令。
5. 你複製指令並在終端機執行即可。
