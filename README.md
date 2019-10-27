### Setup

- Download flatpak, download snes9x for flatpak
- Find a Zelda ROM
- Capture the mss screenshot where the emulator window is

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
