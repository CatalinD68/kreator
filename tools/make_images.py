# -*- coding: utf-8 -*-
"""Renders every piece of generated artwork straight into ../assets/img/.

    pip install pillow numpy
    cd tools && python3 make_images.py

Team portraits are photographs and are left alone.
"""
import io, os
from PIL import Image
import gen
import gen2

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'assets', 'img')

# name -> (renderer, seed, render size, output width, jpeg quality)
JOBS = [
    ('hero.jpg',                  gen.ridges,   57, (1600, 900),  1500, 70),
    ('work-meridian.jpg',         gen.ridges,    3, (900, 1125),   760, 70),
    ('work-collective.jpg',       gen.topo,     11, (900, 1125),   760, 70),
    ('work-terra.jpg',            gen.dunes,    21, (900, 1125),   760, 70),
    ('work-wildland.jpg',         gen.forest,   33, (900, 1125),   760, 70),

    ('case-meridian-hero.jpg',    gen.ridges,  101, (1100, 620),  1100, 66),
    ('case-meridian-a.jpg',       gen.dunes,   102, (560, 700),    560, 66),
    ('case-meridian-b.jpg',       gen.forest,  103, (560, 700),    560, 66),

    ('case-collective-hero.jpg',  gen2.network, 111, (1100, 620), 1100, 66),
    ('case-collective-a.jpg',     gen.topo,     112, (560, 700),   560, 66),
    ('case-collective-b.jpg',     gen2.blocks,  113, (560, 700),   560, 66),

    ('case-terra-hero.jpg',       gen2.blocks,  121, (1100, 620), 1100, 66),
    ('case-terra-a.jpg',          gen2.mist,    122, (560, 700),   560, 66),
    ('case-terra-b.jpg',          gen.dunes,    123, (560, 700),   560, 66),

    ('case-wildland-hero.jpg',    gen2.canopy,  131, (1100, 620), 1100, 66),
    ('case-wildland-a.jpg',       gen.forest,   132, (560, 700),   560, 66),
    ('case-wildland-b.jpg',       gen2.mist,    133, (560, 700),   560, 66),
]


def main():
    os.makedirs(OUT, exist_ok=True)
    for name, fn, seed, (w, h), out_w, q in JOBS:
        gen.W, gen.H = w, h
        im = Image.fromarray(fn(seed=seed).astype('uint8'))
        if im.width != out_w:
            im = im.resize((out_w, round(im.height * out_w / im.width)), Image.LANCZOS)
        im.save(os.path.join(OUT, name), quality=q, optimize=True, progressive=True)
        print('%-28s %s  %d KB' % (name, im.size, os.path.getsize(os.path.join(OUT, name)) // 1024))


if __name__ == '__main__':
    main()
