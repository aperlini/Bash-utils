# Preset update for max patch

Automation script for `concrete-wf` patch. Script update *pattrstorage* preset file (`.json`) and will either add or remove audio file based on its position index in folder.

## Structure

```bash
.
├── ...
├── concrete-wf.maxpat
├── player1.json
├── player1.maxpat
├── player2.json
├── player2.maxpat
├── ...
└── sources
    ├── player1
    │   ├── audio-a.WAV
    │   ├── audio-b.WAV
    │   └── ...
    └── player2
      	├── audio-b.WAV
        ├── audio-c.WAV
        └── ...

```

## Scenario

> to be completed...

## Installation

`preset_update.py` must be added in `~/.local/bin` folder. then add function to be called from `.bashrc` or `.bash_profile` depending of your system :

```bash
function preset_update() {
	python3 ~/.local/bin/preset_update.py "$@"
}
```

`.local/bin` must be added to your path if not already present :

```bash
export PATH="$HOME/.local/bin:$PATH"
```

## Example usage

### Remove file and update preset

```bash
preset_update player1.json 2 0 
```

Command will remove second index audio file in player folder and update `player1.json` preset

### Add new file and update preset

```bash
preset_update player1.json 4 1
```

Command will check for new file added at index 4 in player folder and update `player1.json` preset
