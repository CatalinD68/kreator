# tools

The generators behind the site's artwork. Nothing here runs at page load — these produce files
that are committed into `assets/img/`.

```bash
pip install pillow numpy
cd tools
python3 make_images.py        # rewrites the abstract artwork in ../assets/img/
```

| file | what it does |
|---|---|
| `gen.py` | duotone image families: layered ridges, topographic contours, long-exposure dunes, forest in fog. Brand palette is the `STOPS` list at the top. |
| `gen2.py` | the per-case-study variants, plus three more families: architectural volumes, a constellation network, horizontal mist. |
| `geo.py` | the geometric nature marks (pine, cloud, sun, stag, wolf, bird, …) rendered as SVG symbols, and the repeating pine-ridge tile used between sections. |
| `cases.py` | content and markup for the four case-study pages. |
| `make_images.py` | entry point — renders everything at the sizes the site uses and writes it into `../assets/img/`. |

`make_images.py` will **not** touch the team portraits (`team-*.jpg`); those are photographs,
graded once to a common exposure so the three read as one set.
