### Setup (any linux)

- Download flatpak, download snes9x for flatpak
- Find a Zelda ROM
- Screencap with mss at the location of the emulator window

### SNES button mapping

A => `/interact`

B => `/swing`

Y => `/item`

X => `/map`

START => `/menu`

### Run

`roscore`

`python zelda_bridge_node.py` (you will have to be sudo for keyboard module to work)

`rosrun image_transport repubish raw in:=/camera/rgb/image_raw compressed out:=/camera/rgb/image_raw`
