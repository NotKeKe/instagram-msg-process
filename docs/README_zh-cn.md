<div align="center">

# Instagram Message Json Resolver

![Stars](https://img.shields.io/github/stars/NotKeKe/instagram-msg-process?style=social)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
<br>
[![Docs](https://img.shields.io/badge/Docs-繁體中文-blue.svg)](../README.md) 
[![Docs](https://img.shields.io/badge/Docs-简体中文-blue.svg)](README_zh-cn.md) 
[![Docs](https://img.shields.io/badge/Docs-English-blue.svg)](README_en-us.md)

</div>

使用 [Meta 帐号中心](https://accountscenter.instagram.com/info_and_permissions/) 下载自己的聊天记录时 ( json 格式 )，会遇到中文的乱码( 2025/5/3遇到的 )，如: `\u97F3\u6C50`<br>
此项目主要使用以下代码解决此问题 (可查看 [此文档](docs/ai_response.md) 来看 Qwen 给我的回答)
```python
text.encode('latin-1').decode('utf-8')
```

---

## 🚀 使用方式
1. 安装 [python3](https://www.python.org/downloads/)

2. 安装项目依赖<br>
任选以下一种方式安装依赖环境
    * 方式一：使用 pip
        * 在终端内进入当前项目目录
        * 修改 `setting.json` 文件 (参阅以下第3点)
        * 于终端内执行以下指令 (安装所需的库)
            ```bash
            pip install -r requirements.txt
            ```
            * 如果 pip 没有反应的话，使用以下指令来确保 pip 已被安装
            ```bash
            python -m ensurepip --upgrade
            ```
        
    * 方式二：使用 [uv](https://github.com/astral-sh/uv)
        * 在终端内进入当前项目目录
        * 修改 `setting.json` 文件 (参阅以下第3点)
        * 于终端内执行 (此时会多出现一个 `.venv` 文件夹)
        ```bash
        uv sync
        ```
        * 确认创建完毕后，执行 
        ```bash
        uv run main.py
        ```

3. 修改 setting.json
* 将 `setting.json.example` 重命名为 `setting.json`
    1. 将 `path` (**！必须修改！**) 字段修改为你下载完后，文件的路径。
        * 示例: 
            ```json
            {
                "path": "D:\\instagram-USERNAME-2025-05-03-AbncaAFn\\your_instagram_activity\\messages\\inbox",
            }
            ```
    2. `output_path` (可选) 你预期最后将这些 json 文件放在哪里。
        * 例如底下这样的路径，代表他将会把文件存放在当前文件夹的 output 文件夹内:
            ```json
            {
                "output_path": "./output"
            }
            ```
            ```
            ../                        # 当前文件夹
            ├── output/                # 你输入的 output_path
            │   ├── USERNAME1_ID1/     # 第一个用户文件夹
            │   │   └── message_1.json
            │   ├── USERNAME2_ID2/     # 第二个用户文件夹
            │   │   └── message_1.json
            │   └── ...                # 其他用户文件夹
            ├── docs/
            └── ...
            ```
        * 如果将 `output_path` 留空，则会将修改过后的 json 文件修改至刚刚第 1 点所提到的 `path`。
---

## 📜 授权说明

本项目使用 [MIT License](LICENSE)

---