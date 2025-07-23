<div align="center">

# Instagram Message Json Resolver

![Stars](https://img.shields.io/github/stars/NotKeKe/instagram-msg-process?style=social)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
<br>
[![Docs](https://img.shields.io/badge/Docs-繁體中文-blue.svg)](README.md) 
[![Docs](https://img.shields.io/badge/Docs-简体中文-blue.svg)](docs/README_zh-cn.md) 
[![Docs](https://img.shields.io/badge/Docs-English-blue.svg)](docs/README_en-us.md)

</div>

使用 [Meta 帳號中心](https://accountscenter.instagram.com/info_and_permissions/) 下載自己的聊天紀錄時 ( json 格式 )，會遇到中文的亂碼( 2025/5/3遇到的 )，如: `\u97F3\u6C50`<br>
此專案主要使用以下代碼解決此問題 (可查看 [此文檔](docs/ai_response.md) 來看 Qwen 給我的回答)
```python
text.encode('latin-1').decode('utf-8')
```

---

## 🚀 使用方式
1. 安裝 [python3](https://www.python.org/downloads/)

2. 安裝項目依賴<br>
任選以下一種方式安裝依賴環境
    * 方式一：使用 pip
        * 在終端機內進入當前專案目錄
        * 修改 `setting.json` 檔 (參閱以下第3點)
        * 於終端機內執行以下指令 (安裝所需的庫)
            ```bash
            pip install -r requirements.txt
            ```
            * 如果 pip 沒用反應的話，使用以下指令來確保 pip 已被安裝
            ```bash
            python -m ensurepip --upgrade
            ```
        
    * 方式二：使用 [uv](https://github.com/astral-sh/uv)
        * 在終端機內進入當前專案目錄
        * 修改 `setting.json` 檔 (參閱以下第3點)
        * 於終端機內執行 (此時會多出現一個 `.venv` 資料夾)
        ```bash
        uv sync
        ```
        * 確認創建完畢後，執行 
        ```bash
        uv run main.py
        ```

3. 修改 setting.json
* 將 `setting.json.example` 重命名為 `setting.json`
    1. 將 `path` (**！必須修改！**) 欄位修改為你下載完後，檔案的路徑。
        * 範例: 
            ```json
            {
                "path": "D:\\instagram-USERNAME-2025-05-03-AbncaAFn\\your_instagram_activity\\messages\\inbox",
            }
            ```
    2. `output_path` (可選) 你預期最後將這些 json 檔放在哪裡。
        * 例如底下這樣的路徑，代表他將會把檔案存放在當前資料夾的 output 資料夾內:
            ```json
            {
                "output_path": "./output"
            }
            ```
            ```
            ../                        # 當前資料夾
            ├── output/                # 你輸入的 output_path
            │   ├── USERNAME1_ID1/     # 第一個用戶資料夾
            │   │   └── message_1.json
            │   ├── USERNAME2_ID2/     # 第二個用戶資料夾
            │   │   └── message_1.json
            │   └── ...                # 其他用戶資料夾
            ├── docs/
            └── ...                    
            ```
        * 如果將 `output_path` 留空，則會將修改過後的 json 檔修改至剛剛第 1 點所提到的 `path`。
---

## 📜 授權說明

本項目使用 [MIT License](LICENSE)

---