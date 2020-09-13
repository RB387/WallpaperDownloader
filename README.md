# Wallpaper Downloader
CLI crawler that downloads all calendar wallpapers from smashingmagazine for required year-month

(test task from ostrovok.ru)

## Install
For Python 3.7
```
make install
```
or 
```
pip install -r requirements.txt
```

## Usage
Arguments:
* `--year`: year of wallpapers that should be downloaded (current year by default)
* `--month`: month of wallpapers that should be downloaded (all `12` months by default)
* `--resolution`: resolution of wallpapers that should be downloaded (`1920x1080` by default)

This command will download all wallpapers for `march` of `2020` with resolution `800x600`:
```
python run.py --year 2020 --month 3 --resolution 800x600
```
This command will download all wallpapers for every month of `2020` with resolution `1920x1080`:
```
python run.py
```
All wallpapers will be downloaded in current users folder with name `wallpapers_{CURRENT_DATETIME}`

## Tests
```
make install-dev
pytest -vv
```
Test also has integration and unit marks. Read `pytest.ini` for more information 
