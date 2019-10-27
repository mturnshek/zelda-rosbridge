### Setup (any linux)

- Download flatpak, download snes9x for flatpak
- Find a Zelda ROM
- Screencap with mss at the location of the emulator window
- Make sure the emulator window is selected

### SNES button mapping

A => "r" (`/interact`)

B => "d" (`/swing`)

Y => "s" (`/item`)

X => "e" (`/map`)

START => "q" (`/menu`)

### Run

`roscore`

`python zelda_bridge_node.py` (you will have to be sudo for keyboard module to work)

`rosrun image_transport repubish raw in:=/camera/rgb/image_raw compressed out:=/camera/rgb/image_raw`
