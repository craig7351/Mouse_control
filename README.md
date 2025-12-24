# Windows AI Eye 助手 (Windows AI Eye Assistant)

[繁體中文](#繁體中文) | [English](#english)

---

## 繁體中文

這是一個專為 **AI 視覺協作** 設計的 Windows 桌面自動化工具。透過在本機截取帶有「座標格線」的畫面，AI (如 Gemini 或 ChatGPT) 就能像人類一樣「看見」您的桌面，並給出精確的操作指令。

### 為什麼選擇 Windows AI Eye？
- **AI 具備空間感**：透過紅線座標系統，AI 能精準判斷按鈕、圖示或視窗的物理座標。
- **不受 OCR 限制**：即使是沒有文字的圖示，AI 也能透過影像解義並下達操作指令。
- **人機協作校準**：內建 `pick` 模式，允許使用者手動校準起始座標，解決像素偏移問題。
- **極簡化驅動**：本機端僅保留輕量化控制邏輯，將「辨識」任務完全交給最強大的 AI 大腦。

### 使用情境 (Use Cases)
- **表單自動填寫**：將複雜且欄位眾多的網頁表單交給 AI 識別，並由 AI 自動產生成百上千字的內容一鍵填入。
- **遺留軟體自動化**：針對沒有 API、甚至文字無法被傳統工具擷取的舊式 ERP 或內部系統，AI 透過「格線」能直接點擊座標。
- **跨應用程式任務**：例如「幫我把記事本裡的內容貼到 LINE 給指定的聯絡人」，AI 能理解多個視窗間的空間意涵。
- **醫療/專業操作輔助**：輔助填寫如電子病歷 (EMR) 等結構化資料，減少重複性的滑鼠移動。
- **遊戲或動態分析**：在無法取得內部數據的情況下，透過視覺掌握位置資訊。

### 安裝與執行

1. **環境設定**：
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

2. **核心指令**：
   - `python main.py screenshot [step]`：截取帶有格線的桌面截圖（預設間距 100px）。
   - `python main.py pick`：輔助定位，5 秒後取得滑鼠目前座標，用於校準。
   - `python main.py click <x> <y>`：點擊指定座標。
   - `python main.py type <text>`：輸入文字。
   - `python main.py move <x> <y>`：移動滑鼠。

### AI 協作流程
1. 執行 `python main.py screenshot`。
2. 將 `screenshots/manual_capture.png` 上傳給 AI。
3. AI 分析影像後提供操作指令（例如：`python main.py click 500 500`）。
#### Step 4: 執行指令
在終端機複製並執行 AI 給您的指令。

### 搭配 Cursor / Antigravity 使用 (推薦)
若您使用具備 Agent 能力的開發工具（如 **Cursor** 或 **Antigravity**），建議進行以下設定以獲得最佳自動化體驗：

0. **讀取指南**：您可以直接要求 AI Agent 先閱讀本專案中的 `AI_AGENT_GUIDE.md`，這能讓 AI 立即掌握所有操作技巧與最佳實作流程。
1. **開啟自動執行 (Auto-run)**：在工具設定中開啟 `Auto-approve safe commands`，讓 AI Agent 能直接執行點擊與輸入指令。
2. **延遲緩衝**：在要求 AI 執行動作時，可以加上「sleep 5秒後幫我...」的指令，這讓您有足夠的時間完成視窗切換。
3. **人機校準**：若發現 AI 點擊位置偏離，請執行 `python main.py pick` 手動定位第一個欄位，AI 將自動修正後續所有座標。

---

## English

A Windows desktop automation tool designed specifically for **AI Visual Collaboration**. By capturing screenshots with a "coordinate grid," AI (such as Gemini or ChatGPT) can "see" your desktop and provide precise operational commands.

### Why Windows AI Eye?
- **AI Spatial Awareness**: Using the red grid system, AI can accurately judge the physical coordinates of buttons, icons, or windows.
- **No OCR Limitations**: Even icons without text can be interpreted by AI to generate commands.
- **Human-AI Calibration**: Built-in `pick` mode allows users to manually calibrate starting coordinates, solving pixel offset issues.
- **Minimalist Driver**: Only lightweight control logic is kept locally, leaving the "recognition" task to powerful AI models.

### Use Cases
- **Form Automation**: Delegate complex web forms with numerous fields to AI for recognition, and have AI generate and fill hundreds of words with one click.
- **Legacy Software Automation**: Automate old ERP or internal systems that lack APIs and have unselectable text. AI can click coordinates directly via the "grid."
- **Cross-App Tasks**: E.g., "Copy content from Notepad and paste it to a specific LINE contact." AI understands the spatial context of multiple windows.
- **Healthcare/Professional Data Entry**: Assist in filling out structured data like Electronic Medical Records (EMR), reducing repetitive mouse movements.
- **Dynamic Analysis**: Gain location information through vision in scenarios where internal data is inaccessible, such as specific interactive software.

### Installation & Execution

1. **Environment Setup**:
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

2. **Core Commands**:
   - `python main.py screenshot [step]`: Capture a desktop screenshot with grid lines (default step 100px).
   - `python main.py pick`: Assist location by getting current mouse coordinates after 5 seconds.
   - `python main.py click <x> <y>`: Click specified coordinates.
   - `python main.py type <text>`: Type text.
   - `python main.py move <x> <y>`: Move mouse.

### AI Collaboration Workflow
1. Run `python main.py screenshot`.
2. Upload `screenshots/manual_capture.png` to your AI.
3. AI analyzes the image and provides commands (e.g., `python main.py click 500 500`).
4. Execute the command provided by AI in your terminal.

### Usage with AI Agents (Cursor / Antigravity)
For the best experience with AI Agents like **Cursor** or **Antigravity**, we recommend the following:

0. **Read the Guide**: You can ask your AI Agent to read `AI_AGENT_GUIDE.md` first. This will help the AI understand exactly how to interact with your desktop accurately.
1. **Enable Auto-run**: Turn on `Auto-approve safe commands` in your agent's settings. This allows the agent to execute click and type commands directly without manual approval.
2. **Time Buffering**: When asking the agent to perform an action, append "sleep for 5 seconds before..." to give yourself time to switch window focus.
3. **Manual Calibration**: If you notice the agent's clicks are offset, run `python main.py pick` to manually locate the first field. The agent will then recalibrate all subsequent coordinates automatically.

## License
MIT License
