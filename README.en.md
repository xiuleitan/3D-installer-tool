# 3D Installer Tool

[中文](README.md)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![PyQt5](https://img.shields.io/badge/PyQt5-desktop-green)
![Platform](https://img.shields.io/badge/Windows-installer-blue)
![PyInstaller](https://img.shields.io/badge/PyInstaller-ready-green)

3D Installer Tool is a Windows PyQt5 desktop helper for launching and coordinating local installer resources for 3D and post-production software. This repository should contain only the launcher code and safe configuration examples. Do not commit commercial installers, license files, account data, or machine-specific private paths.

## Features

- Provides a PyQt5 desktop interface grouped by software category.
- Launches external installers, helper tools, folders, and test commands from a local software resource directory.
- Current code includes entries for AE, Cinema 4D, 3ds Max, Maya, Houdini, Nuke, Maxon, Redshift, and WinRAR.
- Reads the local software resource root from `data/software_route.csv`.
- Includes `main.spec` for packaging a Windows executable with PyInstaller.

## Requirements

- Windows 10/11.
- Python 3.8 or newer.
- A local directory containing legally licensed installer resources.
- Python dependencies:
  - `PyQt5`
  - `qt-material`
  - `pyinstaller`, only when packaging.

## Installation And Configuration

Install runtime dependencies:

```bash
pip install PyQt5 qt-material
```

Install PyInstaller if you need to build an executable:

```bash
pip install pyinstaller
```

Copy the example configuration to a local configuration file:

```bash
copy data\software_route.example.csv data\software_route.csv
```

Edit `data\software_route.csv` and set the first line to your software resource root, for example:

```csv
D:\path\to\software-packages
```

## Configuration

| File | Purpose | Commit |
| --- | --- | --- |
| `data/software_route.example.csv` | Example configuration with a placeholder path | Yes |
| `data/software_route.csv` | Real local software resource path | No |
| `build/`, `dist/` | PyInstaller output | No |
| `__pycache__/` | Python bytecode cache | No |

## Usage

Run the desktop app:

```bash
python main.py
```

At startup, the app reads the first row of `data/software_route.csv` as the software resource root. Buttons in the UI append relative paths to that root and call Windows commands to launch installers, open folders, or run rendering tests.

## Packaging

```bash
pyinstaller main.spec
```

Build artifacts are generated under `build/` and `dist/`. These directories are ignored by Git and should not be committed.

## Development

- `main.py`: main window and software installer actions.
- `fileReadAndWrite.py`: CSV read/write helpers.
- `main.spec`: PyInstaller packaging configuration.
- `data/software_route.example.csv`: local resource path configuration template.

Before committing, run:

```bash
python -m py_compile main.py fileReadAndWrite.py
git diff --check
git status --short
```

## Privacy And Security

- Do not commit real installers, license files, account notes, private keys, tokens, browser sessions, licenses, or commercial software assets.
- Do not commit `data/software_route.csv`; it usually contains a local machine path.
- This project launches Windows commands through `subprocess.Popen`, so use only trusted and legally licensed local installer resources.
- If large or private files have already been committed in history, deleting them in a later commit does not clean Git history. Review whether history cleanup or credential rotation is needed before publishing.

## License

No license file is currently provided. Add a `LICENSE` file before public release according to your intended usage.
