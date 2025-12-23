# Windows AI Eye 助手

這是一個讓 AI 能夠「看見」並「操作」Windows 桌面的自動化工具。整合了截圖視覺、座標定位與 OCR 文字辨識功能。

## 功能特色
- **視覺定位**：自動截取螢幕並疊加可自訂間距的紅色座標格線，方便 AI 或使用者精準定位。
- **OCR 辨識**：使用 `easyocr` 辨識螢幕上的文字，支援繁體中文與英文。
- **自動化操作**：支援滑鼠點擊、移動、拖曳，以及鍵盤輸入與系統組合鍵。
- **Fail-safe 機制**：內建 PyAutoGUI 安全開關，若腳本失控，將滑鼠移至螢幕四個角落即可強制停止。

## 安裝與執行

### 1. 環境設定
請確保已安裝 Python，然後執行：
```powershell
# 建立虛擬環境
python -m venv venv

# 啟動虛擬環境 (Windows)
.\venv\Scripts\Activate.ps1

# 安裝依賴套件
pip install -r requirements.txt
```

### 2. 使用方式
- **取得桌面截圖 (含格線)**：
  ```powershell
  python main.py screenshot [step]
  # 例如：python main.py screenshot 50 (每 50 像素一條線)
  ```
  截圖將儲存在 `screenshots/` 資料夾中。

- **執行 OCR 文字辨識**：
  ```powershell
  python main.py ocr
  # 辨識最新截圖中的所有文字與座標
  ```

- **尋找並點擊文字**：
  ```powershell
  python main.py find [目標文字]
  # 例如：python main.py find 檔案
  ```

- **模擬操作**：
  ```powershell
  python main.py click 500 500
  python main.py open_paint
  ```

## 檔案結構
- `core.py`: 核心視覺與控制系統 (WindowsEye, WindowsHand)。
- `reader.py`: OCR 辨識系統 (WindowsReader)。
- `main.py`: CLI 命令列進入點。
- `requirements.txt`: 專案依賴套件清單。

## AI 協作流程
1. 執行 `python main.py screenshot`。
2. 將 `screenshots/manual_capture.png` 上傳給 AI。
3. 告訴 AI 你的目標（例如：「點擊 Chrome 圖示」）。
4. AI 會根據格線分析座標並回傳指令，或透過 OCR 直接尋找文字座標。
