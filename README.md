# SAMPLE-KIVYMD-APP

[![GitHub Workflow Build](https://img.shields.io/github/actions/workflow/status/Novfensec/SAMPLE-KIVYMD-APP/buildozer_action.yml?label=Android%20Build&logo=android&style=for-the-badge)](https://github.com/Novfensec/SAMPLE-KIVYMD-APP/actions)
[![License](https://img.shields.io/github/license/Novfensec/SAMPLE-KIVYMD-APP?style=for-the-badge)](https://github.com/Novfensec/SAMPLE-KIVYMD-APP/blob/main/LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg?style=for-the-badge)](https://www.python.org/)

This repository contains a sample Kivy and KivyMD Python application, showcasing an Android APK build workflow using Buildozer. It serves as an example for **[KvDeveloper's](https://github.com/Novfensec/KvDeveloper)** build workflow, providing a streamlined process for converting Kivy and KivyMD applications into Android APKs and AABs `(Required by Google Play)`.

## Features

- A basic KivyMD app structure.
- A ready-to-use **GitHub Actions** workflow for building APKs and AABs `(Required by Google Play)`.
- Full compatibility with **Kivy** and **KivyMD** frameworks.

## Getting Started

### Prerequisites

- Python 3.8+
- [Buildozer](https://github.com/kivy/buildozer) for APK packaging.
- Kivy & KivyMD libraries installed:

    ```bash
    pip install kivy kivymd
    ```

### Running Locally

To run the app locally, clone the repository and install the necessary dependencies:

```bash
git clone https://github.com/Novfensec/SAMPLE-KIVYMD-APP.git \
cd SAMPLE-KIVYMD-APP \
python main.py
```