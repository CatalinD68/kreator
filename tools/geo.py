# -*- coding: utf-8 -*-
"""Geometric nature marks: an icon set and a repeating pine-ridge tile."""
from urllib.parse import quote


def pine(x, base, h, w=None):
    """A fir built from three stacked triangles plus a trunk."""
    w = w or h * 0.42
    d = []
    for i in range(3):
        apex = base - h * (1 - i * 0.28)
        by = base - h * (0.55 - i * 0.28)
        hw = w * (0.45 + i * 0.275)
        d.append('M%.1f %.1fL%.1f %.1fH%.1fZ' % (x, apex, x + hw, by, x - hw))
    d.append('M%.1f %.1fh3v%.1fh-3z' % (x - 1.5, base - h * 0.06, h * 0.06 + 3))
    return '<path d="%s"/>' % ''.join(d)


def ridge_tile(color, opacity, line, line_opacity, w=320, h=84, base=76):
    """A repeating fir horizon. Colours are passed raw ('#RRGGBB'); quote() encodes the '#'."""
    trees = [(28, 36), (60, 23), (95, 46), (128, 20), (168, 33),
             (206, 27), (244, 41), (286, 24)]
    paths = ''.join(pine(x, base, ph) for x, ph in trees)
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" '
           'viewBox="0 0 %d %d"><path d="M0 %d H%d" stroke="%s" stroke-opacity="%s" '
           'stroke-width="1.4"/><g fill="%s" fill-opacity="%s">%s</g></svg>'
           % (w, h, w, h, base + 3, w, line, line_opacity, color, opacity, paths))
    return 'url("data:image/svg+xml,%s")' % quote(svg, safe="")


# ---------------------------------------------------------------- icon set
ICONS = {}

ICONS['n-sun'] = '''<circle cx="16" cy="16" r="6.5" fill="currentColor"/>
<g stroke="currentColor" stroke-width="2.6"><path d="M16 1v4M16 27v4M1 16h4M27 16h4"/>
<path d="M5.4 5.4l2.8 2.8M23.8 23.8l2.8 2.8M26.6 5.4l-2.8 2.8M8.2 23.8l-2.8 2.8"/></g>'''

ICONS['n-sunset'] = '''<path d="M6 23a10 10 0 0 1 20 0z" fill="currentColor"/>
<g stroke="currentColor" stroke-width="2.6"><path d="M1 27h9M14 27h4M22 27h9M16 2v5M4.5 8.5l3 3M27.5 8.5l-3 3"/></g>'''

ICONS['n-pine'] = '''<path d="M16 2l6 10h-12zM16 9l8.5 11h-17zM16 16l11 12h-22z" fill="currentColor"/>
<path d="M14.5 27h3v4h-3z" fill="currentColor"/>'''

ICONS['n-forest'] = '''<path d="M9 6l5 8H4zM9 11l7 9H2z" fill="currentColor"/>
<path d="M7.6 19h2.8v6H7.6z" fill="currentColor"/>
<path d="M22 10l4.5 7h-9zM22 15l6.5 8h-13z" fill="currentColor"/>
<path d="M20.8 22h2.4v5h-2.4z" fill="currentColor"/>
<path d="M2 28h28" stroke="currentColor" stroke-width="2"/>'''

ICONS['n-cloud'] = '''<circle cx="11" cy="16" r="6" fill="currentColor"/>
<circle cx="20" cy="13.5" r="8" fill="currentColor"/>
<rect x="5" y="16" width="23" height="6" fill="currentColor"/>
<path d="M4 27h11M19 27h9" stroke="currentColor" stroke-width="2.6"/>'''

ICONS['n-mountain'] = '''<path d="M2 27L12 8l5.5 10.5L21 12l9 15z" fill="currentColor"/>
<path d="M8.4 17.2L12 10.5l3.6 6.7-3.6-2z" fill="var(--ink)" opacity=".55"/>'''

ICONS['n-stag'] = '''<circle cx="16" cy="22.5" r="7" fill="currentColor"/>
<g stroke="currentColor" stroke-width="2.8" fill="none">
<path d="M12 16L7.5 9M7.5 9H3M7.5 9V4M20 16l4.5-7M24.5 9H29M24.5 9V4"/></g>'''

ICONS['n-wolf'] = '''<g stroke="currentColor" stroke-width="2.8" fill="none" stroke-linejoin="miter">
<path d="M6 11V3l5.5 5M26 11V3l-5.5 5M6 11l10 18 10-18"/></g>
<circle cx="12" cy="15" r="1.8" fill="currentColor"/>
<circle cx="20" cy="15" r="1.8" fill="currentColor"/>'''

ICONS['n-bird'] = '''<path d="M2 19c5.5 0 9-4.5 12-9 3 4.5 6.5 9 12 9" stroke="currentColor"
stroke-width="3" fill="none"/><circle cx="16" cy="24" r="2.4" fill="currentColor"/>'''

ICONS['n-bear'] = '''<circle cx="7.5" cy="9" r="4.5" fill="currentColor"/>
<circle cx="24.5" cy="9" r="4.5" fill="currentColor"/>
<circle cx="16" cy="19" r="10" fill="currentColor"/>
<circle cx="12.5" cy="17" r="1.8" fill="var(--ink)"/>
<circle cx="19.5" cy="17" r="1.8" fill="var(--ink)"/>'''

ICONS['n-moon'] = '''<path d="M20 2a14 14 0 1 0 0 28 15 15 0 0 1 0-28z" fill="currentColor"/>'''

ICONS['n-river'] = '''<g stroke="currentColor" stroke-width="2.8" fill="none">
<path d="M2 11c5-5 8 5 13 0s8 5 13 0"/><path d="M2 21c5-5 8 5 13 0s8 5 13 0"/></g>'''

ICONS['n-arrow'] = '''<path d="M4 16h22M19 8l8 8-8 8" stroke="currentColor" stroke-width="2.2" fill="none"/>'''


def symbols():
    return '\n'.join(
        '<symbol id="%s" viewBox="0 0 32 32">%s</symbol>' % (k, v)
        for k, v in ICONS.items())


# ------------------------------------------------------- ambient artwork
HERO_DECO = '''<svg viewBox="0 0 460 460" fill="none" aria-hidden="true">
  <g class="rays" stroke="currentColor" stroke-width="1.4" opacity=".55">
    <circle cx="230" cy="230" r="228" stroke-dasharray="3 13"/>
    <circle cx="230" cy="230" r="182"/>
    <path d="M230 2v56M230 402v56M2 230h56M402 230h56"/>
    <path d="M69 69l40 40M351 351l40 40M391 69l-40 40M109 351l-40 40"/>
    <circle cx="230" cy="2" r="6" fill="currentColor" stroke="none"/>
  </g>
  <circle cx="230" cy="230" r="118" stroke="currentColor" stroke-width="1.4" opacity=".5"/>
  <path d="M136 268a94 94 0 0 1 188 0z" fill="currentColor" opacity=".14"/>
  <path d="M60 268h340" stroke="currentColor" stroke-width="1.4" opacity=".45"/>
  <g fill="currentColor" opacity=".32">%s</g>
</svg>''' % (pine(120, 268, 44) + pine(152, 268, 28) + pine(320, 268, 36) + pine(348, 268, 22))

CTA_DECO = '''<svg viewBox="0 0 520 300" fill="none" aria-hidden="true">
  <path d="M70 220a190 190 0 0 1 380 0z" fill="currentColor" opacity=".13"/>
  <g stroke="currentColor" stroke-width="2" opacity=".18">
    <path d="M0 220h40M70 220h60M160 220h80M270 220h70M370 220h60M470 220h50"/>
    <path d="M260 10v42M110 62l30 30M410 62l-30 30"/>
  </g>
  <g fill="currentColor" opacity=".16">%s</g>
</svg>''' % (pine(40, 220, 40) + pine(66, 220, 26) + pine(452, 220, 34) + pine(482, 220, 22))

CLOUDS = '''<svg viewBox="0 0 132 56" aria-hidden="true">
  <g fill="currentColor" opacity=".30">
    <circle cx="38" cy="26" r="15"/><circle cx="66" cy="20" r="20"/>
    <circle cx="93" cy="28" r="13"/><rect x="23" y="26" width="83" height="15"/>
  </g>
  <g fill="none" stroke="currentColor" stroke-width="1.1" opacity=".9">
    <circle cx="38" cy="26" r="15"/><circle cx="66" cy="20" r="20"/>
    <circle cx="93" cy="28" r="13"/><path d="M6 41h120"/>
    <path d="M66 0v6M38 44v6M93 44v6"/>
  </g>
</svg>'''
