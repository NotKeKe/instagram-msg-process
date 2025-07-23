<div align="center">

# Instagram Message Json Resolver

![Stars](https://img.shields.io/github/stars/NotKeKe/instagram-msg-process?style=social)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
<br>
[![Docs](https://img.shields.io/badge/Docs-繁體中文-blue.svg)](../README.md) 
[![Docs](https://img.shields.io/badge/Docs-简体中文-blue.svg)](README_zh-cn.md) 
[![Docs](https://img.shields.io/badge/Docs-English-blue.svg)](README_en-us.md)

</div>

When downloading your chat history (in json format) from the [Meta Accounts Center](https://accountscenter.instagram.com/info_and_permissions/), you may encounter garbled Chinese characters (as of 2025/5/3), such as: `\u97F3\u6C50`<br>
This project mainly uses the following code to solve this problem (you can check [this document](docs/ai_response.md) to see the answer Qwen gave me)
```python
text.encode('latin-1').decode('utf-8')
```

---

## 🚀 How to use
1. Install [python3](https://www.python.org/downloads/)

2. Install project dependencies<br>
Choose one of the following ways to install the dependency environment
    * Method 1: Use pip
        * Enter the current project directory in the terminal
        * Modify the `setting.json` file (see point 3 below)
        * Execute the following command in the terminal (to install the required libraries)
            ```bash
            pip install -r requirements.txt
            ```
            * If pip does not respond, use the following command to ensure that pip is installed
            ```bash
            python -m ensurepip --upgrade
            ```
        
    * Method 2: Use [uv](https://github.com/astral-sh/uv)
        * Enter the current project directory in the terminal
        * Modify the `setting.json` file (see point 3 below)
        * Execute in the terminal (a `.venv` folder will appear at this time)
        ```bash
        uv sync
        ```
        * After confirming the creation, execute
        ```bash
        uv run main.py
        ```

3. Modify setting.json
* Rename `setting.json.example` to `setting.json`
    1. Modify the `path` (**!must be modified!**) field to the path of the file after you download it.
        * Example:
            ```json
            {
                "path": "D:\\instagram-USERNAME-2025-05-03-AbncaAFn\\your_instagram_activity\\messages\\inbox",
            }
            ```
    2. `output_path` (optional) Where you expect to finally place these json files.
        * For example, a path like the one below means that it will store the files in the output folder of the current folder:
            ```json
            {
                "output_path": "./output"
            }
            ```
            ```
            ../                        # Current folder
            ├── output/                # The output_path you entered
            │   ├── USERNAME1_ID1/     # First user folder
            │   │   └── message_1.json
            │   ├── USERNAME2_ID2/     # Second user folder
            │   │   └── message_1.json
            │   └── ...                # Other user folders
            ├── docs/
            └── ...
            ```
        * If `output_path` is left blank, the modified json file will be modified to the `path` mentioned in point 1.
---

## 📜 License

This project is licensed under the [MIT License](LICENSE)

---