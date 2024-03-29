# tof-frontier-clash
Only support game in full screen with FHD resolution (1920x1080).

This script assumes you can 1 shot every mods in Normal mode to do solo farming.

If you already at max level, it is still useful for farming vehicle materials to upgrade them for DC.

## Usage
1. Download executable from [Release](https://github.com/faber6/tof-frontier-clash/releases).
2. Open the game and turn on Full Screen Display, other graphic settings can be as low as possible.
3. Run the script.

## Expected behaviour
Since we are soloing, the script needs to activate the level at the beginning. If it moves over the level, the match will be canceled after 1 min 30 secs, then the script will rejoin by itself.

## Manual installations
1. Virtual environment
```
python -m venv venv ; venv\Scripts\activate
```
2. Install requirements
```
pip install -r requirements.txt
```
3. Run
```
python main.py
```
or run `start.bat`