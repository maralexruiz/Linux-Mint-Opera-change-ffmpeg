# Opera FFmpeg Replacement

This repository contains a Python script that downloads the latest prebuilt
`libffmpeg.so` for Linux x64 from the
[`nwjs-ffmpeg-prebuilt`](https://github.com/nwjs-ffmpeg-prebuilt/nwjs-ffmpeg-prebuilt)
GitHub releases and replaces Opera's bundled FFmpeg library.

## What it does

- Fetches the latest release metadata from GitHub
- Finds the Linux x64 build asset
- Downloads and extracts the package
- Locates `libffmpeg.so`
- Copies it to Opera's system library path
- Removes temporary files after the installation

## Requirements

- Python 3
- `requests` Python package
- Opera installed at `/usr/lib/x86_64-linux-gnu/opera-stable/`
- `sudo` privileges to replace the system library file

## Usage

Install dependencies if needed:

```bash
pip install requests
```

Run the script:

```bash
python3 opera_video_fix.py
```

If you get a permission error, run it with `sudo`:

```bash
sudo python3 opera_video_fix.py
```

## Notes

- The script currently targets Linux x64 only.
- It overwrites Opera's existing `libffmpeg.so`.
- Make sure Opera is installed in the default path used by the script.
