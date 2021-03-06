#!/usr/bin/env python
colortable = \
((0x0,0x0,0x0),(0xcd,0x0,0x0),(0x0,0xcd,0x0),(0xcd,0xcd,0x0),
(0x0,0x0,0xee),(0xcd,0x0,0xcd),(0x0,0xcd,0xcd),(0xe5,0xe5,0xe5),
(0x7f,0x7f,0x7f),(0xff,0x0,0x0),(0x0,0xff,0x0),(0xff,0xff,0x0),
(0x5c,0x5c,0xff),(0xff,0x0,0xff),(0x0,0xff,0xff),(0xff,0xff,0xff),
(0x0,0x0,0x0),(0x0,0x0,0x5f),(0x0,0x0,0x87),(0x0,0x0,0xaf),
(0x0,0x0,0xd7),(0x0,0x0,0xff),(0x0,0x5f,0x0),(0x0,0x5f,0x5f),
(0x0,0x5f,0x87),(0x0,0x5f,0xaf),(0x0,0x5f,0xd7),(0x0,0x5f,0xff),
(0x0,0x87,0x0),(0x0,0x87,0x5f),(0x0,0x87,0x87),(0x0,0x87,0xaf),
(0x0,0x87,0xd7),(0x0,0x87,0xff),(0x0,0xaf,0x0),(0x0,0xaf,0x5f),
(0x0,0xaf,0x87),(0x0,0xaf,0xaf),(0x0,0xaf,0xd7),(0x0,0xaf,0xff),
(0x0,0xd7,0x0),(0x0,0xd7,0x5f),(0x0,0xd7,0x87),(0x0,0xd7,0xaf),
(0x0,0xd7,0xd7),(0x0,0xd7,0xff),(0x0,0xff,0x0),(0x0,0xff,0x5f),
(0x0,0xff,0x87),(0x0,0xff,0xaf),(0x0,0xff,0xd7),(0x0,0xff,0xff),
(0x5f,0x0,0x0),(0x5f,0x0,0x5f),(0x5f,0x0,0x87),(0x5f,0x0,0xaf),
(0x5f,0x0,0xd7),(0x5f,0x0,0xff),(0x5f,0x5f,0x0),(0x5f,0x5f,0x5f),
(0x5f,0x5f,0x87),(0x5f,0x5f,0xaf),(0x5f,0x5f,0xd7),(0x5f,0x5f,0xff),
(0x5f,0x87,0x0),(0x5f,0x87,0x5f),(0x5f,0x87,0x87),(0x5f,0x87,0xaf),
(0x5f,0x87,0xd7),(0x5f,0x87,0xff),(0x5f,0xaf,0x0),(0x5f,0xaf,0x5f),
(0x5f,0xaf,0x87),(0x5f,0xaf,0xaf),(0x5f,0xaf,0xd7),(0x5f,0xaf,0xff),
(0x5f,0xd7,0x0),(0x5f,0xd7,0x5f),(0x5f,0xd7,0x87),(0x5f,0xd7,0xaf),
(0x5f,0xd7,0xd7),(0x5f,0xd7,0xff),(0x5f,0xff,0x0),(0x5f,0xff,0x5f),
(0x5f,0xff,0x87),(0x5f,0xff,0xaf),(0x5f,0xff,0xd7),(0x5f,0xff,0xff),
(0x87,0x0,0x0),(0x87,0x0,0x5f),(0x87,0x0,0x87),(0x87,0x0,0xaf),
(0x87,0x0,0xd7),(0x87,0x0,0xff),(0x87,0x5f,0x0),(0x87,0x5f,0x5f),
(0x87,0x5f,0x87),(0x87,0x5f,0xaf),(0x87,0x5f,0xd7),(0x87,0x5f,0xff),
(0x87,0x87,0x0),(0x87,0x87,0x5f),(0x87,0x87,0x87),(0x87,0x87,0xaf),
(0x87,0x87,0xd7),(0x87,0x87,0xff),(0x87,0xaf,0x0),(0x87,0xaf,0x5f),
(0x87,0xaf,0x87),(0x87,0xaf,0xaf),(0x87,0xaf,0xd7),(0x87,0xaf,0xff),
(0x87,0xd7,0x0),(0x87,0xd7,0x5f),(0x87,0xd7,0x87),(0x87,0xd7,0xaf),
(0x87,0xd7,0xd7),(0x87,0xd7,0xff),(0x87,0xff,0x0),(0x87,0xff,0x5f),
(0x87,0xff,0x87),(0x87,0xff,0xaf),(0x87,0xff,0xd7),(0x87,0xff,0xff),
(0xaf,0x0,0x0),(0xaf,0x0,0x5f),(0xaf,0x0,0x87),(0xaf,0x0,0xaf),
(0xaf,0x0,0xd7),(0xaf,0x0,0xff),(0xaf,0x5f,0x0),(0xaf,0x5f,0x5f),
(0xaf,0x5f,0x87),(0xaf,0x5f,0xaf),(0xaf,0x5f,0xd7),(0xaf,0x5f,0xff),
(0xaf,0x87,0x0),(0xaf,0x87,0x5f),(0xaf,0x87,0x87),(0xaf,0x87,0xaf),
(0xaf,0x87,0xd7),(0xaf,0x87,0xff),(0xaf,0xaf,0x0),(0xaf,0xaf,0x5f),
(0xaf,0xaf,0x87),(0xaf,0xaf,0xaf),(0xaf,0xaf,0xd7),(0xaf,0xaf,0xff),
(0xaf,0xd7,0x0),(0xaf,0xd7,0x5f),(0xaf,0xd7,0x87),(0xaf,0xd7,0xaf),
(0xaf,0xd7,0xd7),(0xaf,0xd7,0xff),(0xaf,0xff,0x0),(0xaf,0xff,0x5f),
(0xaf,0xff,0x87),(0xaf,0xff,0xaf),(0xaf,0xff,0xd7),(0xaf,0xff,0xff),
(0xd7,0x0,0x0),(0xd7,0x0,0x5f),(0xd7,0x0,0x87),(0xd7,0x0,0xaf),
(0xd7,0x0,0xd7),(0xd7,0x0,0xff),(0xd7,0x5f,0x0),(0xd7,0x5f,0x5f),
(0xd7,0x5f,0x87),(0xd7,0x5f,0xaf),(0xd7,0x5f,0xd7),(0xd7,0x5f,0xff),
(0xd7,0x87,0x0),(0xd7,0x87,0x5f),(0xd7,0x87,0x87),(0xd7,0x87,0xaf),
(0xd7,0x87,0xd7),(0xd7,0x87,0xff),(0xd7,0xaf,0x0),(0xd7,0xaf,0x5f),
(0xd7,0xaf,0x87),(0xd7,0xaf,0xaf),(0xd7,0xaf,0xd7),(0xd7,0xaf,0xff),
(0xd7,0xd7,0x0),(0xd7,0xd7,0x5f),(0xd7,0xd7,0x87),(0xd7,0xd7,0xaf),
(0xd7,0xd7,0xd7),(0xd7,0xd7,0xff),(0xd7,0xff,0x0),(0xd7,0xff,0x5f),
(0xd7,0xff,0x87),(0xd7,0xff,0xaf),(0xd7,0xff,0xd7),(0xd7,0xff,0xff),
(0xff,0x0,0x0),(0xff,0x0,0x5f),(0xff,0x0,0x87),(0xff,0x0,0xaf),
(0xff,0x0,0xd7),(0xff,0x0,0xff),(0xff,0x5f,0x0),(0xff,0x5f,0x5f),
(0xff,0x5f,0x87),(0xff,0x5f,0xaf),(0xff,0x5f,0xd7),(0xff,0x5f,0xff),
(0xff,0x87,0x0),(0xff,0x87,0x5f),(0xff,0x87,0x87),(0xff,0x87,0xaf),
(0xff,0x87,0xd7),(0xff,0x87,0xff),(0xff,0xaf,0x0),(0xff,0xaf,0x5f),
(0xff,0xaf,0x87),(0xff,0xaf,0xaf),(0xff,0xaf,0xd7),(0xff,0xaf,0xff),
(0xff,0xd7,0x0),(0xff,0xd7,0x5f),(0xff,0xd7,0x87),(0xff,0xd7,0xaf),
(0xff,0xd7,0xd7),(0xff,0xd7,0xff),(0xff,0xff,0x0),(0xff,0xff,0x5f),
(0xff,0xff,0x87),(0xff,0xff,0xaf),(0xff,0xff,0xd7),(0xff,0xff,0xff),
(0x0,0x0,0x0),(0x12,0x12,0x12),(0x1c,0x1c,0x1c),(0x26,0x26,0x26),
(0x30,0x30,0x30),(0x3a,0x3a,0x3a),(0x44,0x44,0x44),(0x4e,0x4e,0x4e),
(0x58,0x58,0x58),(0x62,0x62,0x62),(0x6c,0x6c,0x6c),(0x76,0x76,0x76),
(0x80,0x80,0x80),(0x8a,0x8a,0x8a),(0x94,0x94,0x94),(0x9e,0x9e,0x9e),
(0xa8,0xa8,0xa8),(0xb2,0xb2,0xb2),(0xbc,0xbc,0xbc),(0xc6,0xc6,0xc6),
(0xd0,0xd0,0xd0))

import sys

def rgb2xterm(rgb):
    min = 1000000
    mini = 0
    i = 0
    for c in colortable:
        dist = (c[0]-rgb[0])**2+(c[1]-rgb[1])**2+(c[2]-rgb[2])**2
        if dist < min:
            min = dist
            mini = i
        i += 1
    return mini

def main():
    if len(sys.argv) < 3:
        print 'usage: vcsc in.vim out.vim'
        exit(1)
    f = open(sys.argv[1], 'r')
    o = open(sys.argv[2], 'w')
    for l in f:
        token = l.split()
        if len(token) == 0:
            continue
        elif token[0] != 'hi':
            o.write(l)
            continue
        else:
            for t in token:
                if t.startswith('guifg=#'):
                    c = t.partition('guifg=#')[2]
                    r = int(c[0:2],16)
                    g = int(c[2:4],16)
                    b = int(c[4:6],16)
                    o.write(t+' ')
                    o.write('ctermfg=%d ' % rgb2xterm((r,g,b)))
                elif t.startswith('guibg=#'):
                    c = t.partition('guibg=#')[2]
                    r = int(c[0:2],16)
                    g = int(c[2:4],16)
                    b = int(c[4:6],16)
                    o.write(t+' ')
                    o.write('ctermbg=%d ' % rgb2xterm((r,g,b)))
                else:
                    o.write(t+' ')
            o.write('\n')

if __name__ == '__main__':
    main()
