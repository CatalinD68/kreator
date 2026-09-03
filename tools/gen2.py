import numpy as np
from PIL import Image, ImageFilter
import gen
from gen import duotone, fbm, grain, vignette, save

# --- new visual families -------------------------------------------------

def blocks(seed=41):
    """Architectural rhythm: hard-edged vertical volumes in warm light."""
    h, w = gen.H, gen.W
    y, x = np.mgrid[0:h, 0:w]
    yn, xn = y / h, x / w
    t = 0.16 + 0.55 * (1 - yn) ** 1.6
    r = np.random.default_rng(seed)
    cuts = np.sort(r.random(9))
    edges = np.concatenate(([0.0], cuts, [1.0]))
    for i in range(len(edges) - 1):
        a, b = edges[i], edges[i + 1]
        top = 0.20 + 0.55 * r.random()
        val = 0.20 + 0.55 * r.random()
        m = (xn >= a) & (xn < b) & (yn > top)
        t = np.where(m, val * (1 - (yn - top) * 0.45), t)
    f = fbm(h, w, seed + 5, octaves=4, base=2)
    t = t * (0.84 + 0.32 * f)
    img = duotone(np.clip(t, 0, 1))
    img = np.asarray(Image.fromarray(np.clip(img, 0, 255).astype(np.uint8))
                     .filter(ImageFilter.GaussianBlur(0.6)), float)
    return grain(vignette(img, 0.55), 8, seed)


def network(seed=51):
    """Constellation of nodes and links — a distributed collective."""
    h, w = gen.H, gen.W
    y, x = np.mgrid[0:h, 0:w]
    t = 0.10 + 0.16 * fbm(h, w, seed + 3, octaves=4, base=2)
    r = np.random.default_rng(seed)
    pts = np.stack([r.random(26) * w, r.random(26) * h], 1)
    for i in range(len(pts)):
        d = np.hypot(pts[:, 0] - pts[i, 0], pts[:, 1] - pts[i, 1])
        for j in np.argsort(d)[1:3]:
            p, q = pts[i], pts[j]
            v = q - p
            L2 = max(v @ v, 1e-6)
            u = np.clip(((x - p[0]) * v[0] + (y - p[1]) * v[1]) / L2, 0, 1)
            dist = np.hypot(x - (p[0] + u * v[0]), y - (p[1] + u * v[1]))
            t = np.maximum(t, np.clip(1 - dist / 1.6, 0, 1) * 0.62)
    for p in pts:
        d = np.hypot(x - p[0], y - p[1])
        t = np.maximum(t, np.clip(1 - d / 7.0, 0, 1) * 0.95)
        t = np.maximum(t, np.clip(1 - d / 46.0, 0, 1) ** 2 * 0.30)
    img = duotone(np.clip(t, 0, 1))
    img = np.asarray(Image.fromarray(np.clip(img, 0, 255).astype(np.uint8))
                     .filter(ImageFilter.GaussianBlur(0.7)), float)
    return grain(vignette(img, 0.55), 7, seed)


def mist(seed=61):
    """Horizontal fog bands — a slow, quiet gradient."""
    h, w = gen.H, gen.W
    y, x = np.mgrid[0:h, 0:w]
    yn = y / h
    n = fbm(h, w, seed, octaves=5, base=2)
    bands = np.sin((yn * 5.5 + n * 0.9) * np.pi)
    t = (0.30 + 0.42 * bands) * (0.42 + 0.9 * (1 - yn) ** 1.4)
    img = duotone(np.clip(t, 0, 1))
    img = np.asarray(Image.fromarray(np.clip(img, 0, 255).astype(np.uint8))
                     .filter(ImageFilter.GaussianBlur(2.4)), float)
    return grain(vignette(img, 0.5), 9, seed)


def canopy(seed=71):
    """Dense foliage speckle under light."""
    h, w = gen.H, gen.W
    y, x = np.mgrid[0:h, 0:w]
    yn = y / h
    f1 = fbm(h, w, seed, octaves=6, base=6)
    f2 = fbm(h, w, seed + 40, octaves=3, base=2)
    t = (1 - yn) ** 1.2 * 0.85
    leaf = np.clip((f1 - 0.52) / 0.16, 0, 1)
    t = t * (0.30 + 0.55 * f2) + leaf * 0.42 * (0.35 + 0.9 * (1 - yn))
    img = duotone(np.clip(t, 0, 1))
    img = np.asarray(Image.fromarray(np.clip(img, 0, 255).astype(np.uint8))
                     .filter(ImageFilter.GaussianBlur(0.8)), float)
    return grain(vignette(img, 0.62), 9, seed)


# --- render --------------------------------------------------------------
JOBS = [
    # slug,        hero fn/seed,          shot A,               shot B
    ('meridian',  (gen.ridges, 101), (gen.dunes, 102), (gen.forest, 103)),
    ('collective', (network, 111), (gen.topo, 112), (blocks, 113)),
    ('terra',     (blocks, 121), (mist, 122), (gen.dunes, 123)),
    ('wildland',  (canopy, 131), (gen.forest, 132), (mist, 133)),
]

if __name__ == '__main__':
    # standalone preview render; the site's assets are produced by make_images.py
    for slug, hero, a, b in JOBS:
        gen.W, gen.H = 1100, 620
        save(hero[0](seed=hero[1]), 'c_%s_hero.jpg' % slug, q=68)
        gen.W, gen.H = 560, 700
        save(a[0](seed=a[1]), 'c_%s_a.jpg' % slug, q=68)
        save(b[0](seed=b[1]), 'c_%s_b.jpg' % slug, q=68)
        print(slug, 'ok')
