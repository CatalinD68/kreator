import numpy as np
from PIL import Image, ImageFilter

rng = np.random.default_rng(7)

INK = np.array([16, 23, 31], float)
MID = np.array([92, 33, 12], float)
ORG = np.array([235, 76, 3], float)
HOT = np.array([255, 186, 140], float)

STOPS = [(0.0, INK), (0.42, MID), (0.78, ORG), (1.0, HOT)]


def duotone(t):
    t = np.clip(t, 0, 1)
    out = np.zeros(t.shape + (3,), float)
    for i in range(len(STOPS) - 1):
        p0, c0 = STOPS[i]
        p1, c1 = STOPS[i + 1]
        m = (t >= p0) & (t <= p1)
        f = np.zeros_like(t)
        f[m] = (t[m] - p0) / (p1 - p0)
        for ch in range(3):
            out[..., ch] += m * (c0[ch] + (c1[ch] - c0[ch]) * f)
    return out


def value_noise(h, w, res, seed):
    r = np.random.default_rng(seed)
    g = r.random((res + 1, res + 1))
    im = Image.fromarray((g * 255).astype(np.uint8)).resize((w, h), Image.BICUBIC)
    return np.asarray(im, float) / 255.0


def fbm(h, w, seed, octaves=6, base=3):
    out = np.zeros((h, w))
    amp, tot = 1.0, 0.0
    for o in range(octaves):
        out += amp * value_noise(h, w, base * 2 ** o, seed + o * 17)
        tot += amp
        amp *= 0.5
    return out / tot


def grain(img, amount=9.0, seed=1):
    r = np.random.default_rng(seed)
    n = r.normal(0, amount, img.shape[:2])[..., None]
    return np.clip(img + n, 0, 255)


def vignette(img, strength=0.55):
    h, w = img.shape[:2]
    y, x = np.mgrid[0:h, 0:w]
    d = np.sqrt(((x - w / 2) / (w / 2)) ** 2 + ((y - h / 2) / (h / 2)) ** 2)
    v = 1 - strength * np.clip((d - 0.45) / 0.9, 0, 1) ** 1.6
    return img * v[..., None]


def save(arr, path, q=74):
    Image.fromarray(arr.astype(np.uint8)).save(path, quality=q, optimize=True, progressive=True)


W, H = 900, 1125


# ---------- 1. Layered ridges at dawn ----------
def ridges(seed=3):
    h, w = H, W
    y, x = np.mgrid[0:h, 0:w]
    yn = y / h
    t = np.zeros((h, w))
    # sky gradient
    t += (1 - yn) ** 1.5 * 0.95
    layers = 6
    for i in range(layers):
        depth = i / (layers - 1)
        n = fbm(1, w, seed + i * 31, octaves=5, base=2)[0]
        n = (n - n.min()) / (np.ptp(n) + 1e-9)
        baseline = 0.34 + 0.115 * i
        amp = 0.16 * (1 - depth * 0.55)
        line = baseline + n * amp
        mask = yn > line[None, :]
        shade = 0.60 - 0.11 * i
        t = np.where(mask, shade * (1 - (yn - line[None, :]) * 0.30), t)
    # atmospheric fog bands
    f = fbm(h, w, seed + 400, octaves=5, base=2)
    t = t * (0.86 + 0.28 * f)
    img = duotone(t)
    img = vignette(img, 0.6)
    return grain(img, 8, seed)


# ---------- 2. Topographic contours ----------
def topo(seed=11):
    h, w = H, W
    f = fbm(h, w, seed, octaves=4, base=2)
    f = (f - f.min()) / np.ptp(f)
    lines = np.abs(np.sin(f * np.pi * 15))
    edge = 1 - np.clip(lines / 0.14, 0, 1)
    base = 0.06 + 0.20 * (f ** 1.6)
    t = base + edge ** 0.7 * (0.46 + 0.5 * f)
    img = duotone(t)
    img = Image.fromarray(np.clip(img, 0, 255).astype(np.uint8)).filter(
        ImageFilter.GaussianBlur(0.5))
    img = np.asarray(img, float)
    img = vignette(img, 0.5)
    return grain(img, 7, seed)


# ---------- 3. Dunes / long exposure waves ----------
def dunes(seed=21):
    h, w = H, W
    y, x = np.mgrid[0:h, 0:w]
    xn, yn = x / w, y / h
    n = fbm(h, w, seed, octaves=5, base=2)
    warp = np.sin((xn * 2.4 + n * 0.85 + yn * 0.5) * np.pi * 2.3)
    t = 0.5 + 0.42 * warp * (0.35 + 0.75 * (1 - yn))
    t = t * (0.55 + 0.75 * (1 - yn) ** 1.2)
    t = np.clip(t, 0, 1) ** 1.15
    img = duotone(t)
    img = Image.fromarray(np.clip(img, 0, 255).astype(np.uint8)).filter(
        ImageFilter.GaussianBlur(1.6))
    img = np.asarray(img, float)
    img = vignette(img, 0.5)
    return grain(img, 8, seed)


# ---------- 4. Forest / vertical field in fog ----------
def forest(seed=33):
    h, w = H, W
    y, x = np.mgrid[0:h, 0:w]
    yn = y / h
    t = 0.20 + 0.72 * (1 - yn) ** 1.3
    r = np.random.default_rng(seed)
    for band in range(4):
        depth = band / 3
        count = 34 + band * 26
        col = 0.55 - 0.12 * band
        wide = (7 - band) * 1.5
        for _ in range(count):
            cx = r.random() * w
            top = (0.16 + 0.16 * depth + r.random() * 0.30) * h
            bot = h * (0.80 + 0.22 * r.random())
            ww = wide * (0.5 + r.random())
            m = (np.abs(x - cx) < ww * (0.35 + 0.65 * (y - top) / max(bot - top, 1))) & (y > top) & (y < bot)
            t = np.where(m, col * (1 - 0.25 * depth), t)
    f = fbm(h, w, seed + 90, octaves=4, base=2)
    t = t * (0.80 + 0.42 * f)
    img = duotone(np.clip(t, 0, 1))
    img = Image.fromarray(np.clip(img, 0, 255).astype(np.uint8)).filter(
        ImageFilter.GaussianBlur(1.1))
    img = np.asarray(img, float)
    img = vignette(img, 0.6)
    return grain(img, 9, seed)


if __name__ == '__main__':
    save(ridges(), 'p1.jpg')
    save(topo(), 'p2.jpg')
    save(dunes(), 'p3.jpg')
    save(forest(), 'p4.jpg')

# ---------- hero: wide atmospheric ridge ----------
    W, H = 1600, 900
    save(ridges(seed=57), 'hero.jpg', q=72)
    print('done')
