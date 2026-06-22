# 3D Installer Tool

[English](README.en.md)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![PyQt5](https://img.shields.io/badge/PyQt5-desktop-green)
![Platform](https://img.shields.io/badge/Windows-installer-blue)
![PyInstaller](https://img.shields.io/badge/PyInstaller-ready-green)

3D Installer Tool 是一个面向 Windows 的 PyQt5 桌面安装辅助工具，用来集中启动和调度本地三维、后期软件安装资源。项目本身只保存启动器代码和配置示例，不应提交商业软件安装包、授权文件、账号信息或本机私有路径。

## 功能

- 提供 PyQt5 桌面界面，按软件类别展示安装入口。
- 支持从本地软件资源目录启动外部安装程序、工具和测试命令。
- 当前代码包含 AE、Cinema 4D、3ds Max、Maya、Houdini、Nuke、Maxon、Redshift、WinRAR 等入口。
- 使用 `data/software_route.csv` 配置本地软件资源根目录。
- 提供 `main.spec`，可用 PyInstaller 打包为 Windows 可执行程序。

## 环境要求

- Windows 10/11。
- Python 3.8 或更高版本。
- 已准备合法授权的本地安装资源目录。
- Python 依赖：
  - `PyQt5`
  - `qt-material`
  - `pyinstaller`，仅打包时需要。

## 安装与配置

安装运行依赖：

```bash
pip install PyQt5 qt-material
```

如需打包，再安装 PyInstaller：

```bash
pip install pyinstaller
```

复制示例配置为本地配置：

```bash
copy data\software_route.example.csv data\software_route.csv
```

编辑 `data\software_route.csv`，把第一行改成你的软件资源根目录，例如：

```csv
D:\path\to\software-packages
```

## 配置项

| 文件 | 说明 | 是否提交 |
| --- | --- | --- |
| `data/software_route.example.csv` | 示例配置，使用占位路径 | 是 |
| `data/software_route.csv` | 本机真实软件资源路径 | 否 |
| `build/`、`dist/` | PyInstaller 生成产物 | 否 |
| `__pycache__/` | Python 字节码缓存 | 否 |

## 使用方法

运行桌面程序：

```bash
python main.py
```

程序启动后会读取 `data/software_route.csv` 第一行作为软件资源根目录。界面里的按钮会拼接这个根目录并调用 Windows 命令启动对应安装程序、打开目录或运行渲染测试。

## 打包

```bash
pyinstaller main.spec
```

打包产物会生成到 `build/` 和 `dist/`，这些目录已加入 `.gitignore`，不建议提交到仓库。

## 开发

- `main.py`：主窗口和各软件安装入口。
- `fileReadAndWrite.py`：CSV 读写辅助函数。
- `main.spec`：PyInstaller 打包配置。
- `data/software_route.example.csv`：本地资源路径配置模板。

在提交前建议运行：

```bash
python -m py_compile main.py fileReadAndWrite.py
git diff --check
git status --short
```

## 隐私与安全

- 不要提交真实安装包、授权文件、账号文本、私钥、令牌、浏览器会话、许可证或任何商业软件资源。
- 不要提交 `data/software_route.csv`，它通常包含本机磁盘路径。
- 本项目会通过 `subprocess.Popen` 调用 Windows 命令，请只使用你信任且合法授权的本地安装资源。
- 如果已经把大文件或私有文件提交到历史记录，普通删除不会清理 Git 历史；发布前应评估是否需要清理历史并轮换相关凭据。

## 许可证

当前仓库未提供许可证文件。公开发布前请根据你的实际意图补充 `LICENSE`。
