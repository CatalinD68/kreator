# Kreator — slow-craft digital studio

Marketing site for **Kreator**, a studio building brand identities, custom websites and ongoing
growth systems for digital nomads, adventure creators and remote founders.

Static, dependency-light, no build step. Open `index.html` and it runs.

---

## Contents

```
index.html                 the site
assets/
  css/style.css            all styles (design tokens at the top)
  js/main.js               smooth scroll, scroll-velocity motion blur, reveals, case-study router
  img/                     photography, generated artwork, logo, favicon
dist/kreator.html          the same site as one self-contained file (every asset inlined)
tools/                     the Python generators that produced the abstract artwork
.github/workflows/         GitHub Pages deploy
```

Two builds ship on purpose. `index.html` is the one to develop against. `dist/kreator.html`
is a single 1.8 MB file with every image, style and script embedded — useful for emailing a
preview, dropping into a CMS, or opening with no server at all.

---

## Running it locally

Any static server works. From the repo root:

```bash
python3 -m http.server 8000
# then open http://localhost:8000
```

Opening `index.html` straight from the filesystem mostly works too, but a server is closer to
production and avoids `file://` quirks.

---

## Deploying

**GitHub Pages.** Push to `main`, then in *Settings → Pages* set the source to **GitHub Actions**.
The workflow in `.github/workflows/pages.yml` publishes the repo root on every push.

**Anywhere else.** It is a folder of static files — Netlify, Vercel, Cloudflare Pages or plain
nginx all work with zero configuration. Point the host at the repo root.

---

## How it is put together

**Design tokens** live at the top of `assets/css/style.css` as CSS custom properties — colours,
type stacks, spacing rhythm, easing. Change the brand there, not in the components.

| Token | Value | Role |
|---|---|---|
| `--ink` | `#10171F` | ground |
| `--orange` | `#EB4C03` | the single accent, from the wordmark |
| `--bone` | `#F3EFE9` | primary text |
| `--slate` | `#8B96A3` | secondary text |

**Type.** Jost (display), Inter (body), JetBrains Mono (labels and data), all from Google Fonts.

**Motion.** [Lenis](https://github.com/darkroomengineering/lenis) for smooth scrolling, GSAP +
ScrollTrigger for reveals and the pinned process section. The directional motion blur is an SVG
`feGaussianBlur` whose `stdDeviation` is driven by scroll velocity in a rAF loop
(`assets/js/main.js`, section 6) — it engages above a threshold and releases after the scroll
settles, so it cannot chatter. Everything respects `prefers-reduced-motion`.

**Case studies** are hash-routed inside the single page: `#work/meridian`, `#work/collective`,
`#work/terra`, `#work/wildland`. The router lives in section 1b of `main.js`. Deep links work.

**Third-party scripts** load from cdnjs and jsDelivr, pinned to exact versions. Nothing is
bundled and there is no package manager in the critical path.

---

## Editing content

Most copy is plain HTML in `index.html`. Two things are generated:

- **Case-study pages** come from `tools/cases.py` — the four `CASES` dicts hold every field
  (brief, scope, palette, deliverables). Editing the HTML directly is fine too; the generator is
  there so the four pages stay structurally identical.
- **Abstract artwork** (`hero`, `work-*`, `case-*`) is procedural. `tools/gen.py` and
  `tools/gen2.py` draw duotone ridges, contour maps, dunes, forests and constellations in the
  brand palette; `tools/geo.py` holds the geometric nature marks and the repeating pine-ridge
  tile used between sections. Requires `pillow` and `numpy`.

---

## Before this goes live

A short list of things that are deliberately placeholder:

- **The four case studies are concept work**, labelled as such on each page. Replace them with
  real client projects as they ship, and drop the "Concept study" tag and the note above the
  next-project link.
- **Contact is WhatsApp only.** Email and social links were removed on purpose; add them back in
  the CTA list and the footer when the accounts exist.
- **Availability copy** ("Two slots this quarter", "Reply within two working days") is a promise
  the site makes on your behalf. Keep it true.

---

## Credits

Design and build: Kreator. Wordmark traced to vector from the supplied artwork.
Photography of the team is the team's own.

Third-party: [GSAP](https://gsap.com) (standard licence, free tier),
[Lenis](https://github.com/darkroomengineering/lenis) (MIT),
[Google Fonts](https://fonts.google.com) (OFL).

© 2026 Kreator. Site content, brand assets and photography are all rights reserved; the
third-party libraries above keep their own licences.
