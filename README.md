# puzzle-box
Japanese Puzzle Box laser cut files and source

<p>Inspired by https://www.thingiverse.com/thing:17670, which was inspired by https://tinyurl.com/y98arvbx

modified to increase internal size of the puzzle box. Uses python3 and drawsvg.

## required packages

<p>to install required python packages:
<br>pip3 install drawsvg
<br>pip3 install cairosvg

<p>output is an svg file suitable for importing into lightburn or other laser cut software.
<br>For some reason I have yet to determine, importing the SVG into lightburn is scaled 33%. To get the correct size, do an immediate (X-Y linked) scale by 300%.