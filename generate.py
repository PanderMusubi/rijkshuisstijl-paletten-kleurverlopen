#!/usr/bin/env python3

# Use gpick to open GPL file for exporting to ASE and MTL formats.


_NUMERALS = '0123456789abcdefABCDEF'
_HEXDEC = {v: int(v, 16)
           for v in (x + y for x in _NUMERALS for y in _NUMERALS)}
LOWERCASE, UPPERCASE = 'x', 'X'


def rgb(triplet):
    return _HEXDEC[triplet[0:2]], _HEXDEC[triplet[2:4]], _HEXDEC[triplet[4:6]]


def triplet(rgb, lettercase=LOWERCASE):
    return format(rgb[0] << 16 | rgb[1] << 8 | rgb[2], '06' + lettercase)

gpl = open('rijkshuisstijl.gpl', 'w')
gpl.write('GIMP Palette\n')
gpl.write('Name: Rijkshuisstijl\n')
gpl.write('Columns: 3\n')
gpl.write('# See https://github.com/PanderMusubi/rijkshuisstijl-palleten-kleurverlopen\n')

soc = open('rijkshuisstijl.soc', 'w')
soc.write('<?xml version="1.0" encoding="UTF-8"?>\n')
soc.write('<ooo:color-table xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0" xmlns:draw="urn:oasis:names:tc:opendocument:xmlns:drawing:1.0" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:svg="http://www.w3.org/2000/svg" xmlns:ooo="http://openoffice.org/2004/office">\n')
soc.write(
    '<!-- See https://github.com/PanderMusubi/rijkshuisstijl-palleten-kleurverlopen -->\n')

unique_colors = {}

for line in open('rijkshuisstijl.txt', 'r'):
    if line[0] == '#':
        continue
    line = line[:-1]
    (name, color) = line.split(' #')
    if color in unique_colors:
        print('WARNING: Encountered identical colors')
        print('  {} #{}'.format(name, color))
        print('and')
        print('  {}'.format(unique_colors[color]))
    else:
        unique_colors[color] = '{} #{}'.format(name, color)
    (r, g, b) = rgb(color)
    gpl.write('{0: >3} {1: >3} {2: >3}  {3} #{4}\n'.format(
        r, g, b, name, color))
    soc.write('<draw:color draw:name="{} #{}" draw:color="#{}"/>\n'.format(name, color, color))

soc.write('</ooo:color-table>\n')
