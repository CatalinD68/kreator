# -*- coding: utf-8 -*-
"""Generates the four case-study pages injected into src.html at __CASE_PAGES__."""

ARROW = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">'
         '<path d="M7 17 17 7M9 7h8v8"/></svg>')
BACK = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">'
        '<path d="M19 12H5M11 6l-6 6 6 6"/></svg>')

CASES = [
    dict(
        slug='meridian', num='01', name='Project Meridian',
        services='Positioning · Identity · Web',
        lede='A four-person adventure-film collective with festival-grade work and a brand that '
             'looked like a free template. We built the identity and the site that let them pitch '
             'outdoor brands instead of chasing them.',
        meta=[('Client', 'Adventure-film collective'), ('Year', '2025'),
              ('Engagement', 'Foundation + Momentum'), ('Build', 'Webflow')],
        brief=[
            'Meridian shoots in high alpine terrain — long approaches, bad weather, patient footage. '
            'The reel was landing festival slots, but everything around it was borrowed: a stock '
            'wordmark, four different colour treatments across four platforms, and a Vimeo link doing '
            'the work of a portfolio.',
            'The problem was never quality. It was that nothing in their brand signalled the standard '
            'of the work, so every commercial conversation started from zero.'],
        made=[
            'A wordmark drawn from surveying and topographic marks — a language the crew already '
            'lived inside — with a fixed duotone grade that every still and frame is pushed through, '
            'so the body of work reads as one body of work.',
            'The site is a single scroll: the reel plays full-bleed at the top, then each project '
            'opens as field notes — altitude, conditions, crew, kit — before it shows a single frame. '
            'It reads like the people who made it, not like a portfolio theme.'],
        quote='The reel was already good enough. The job was to stop the brand undercutting it.',
        side=['Wordmark, monogram and topographic mark set', 'Duotone grading recipe for stills and video',
              'Art direction guide for shoots', 'Single-scroll site with full-bleed reel',
              'Field-notes project template', 'Pitch one-pager for brand enquiries'],
        shots=[('Grade study — dawn ridge, duotone pass 03', 'a'),
               ('Frame test — long-exposure, low light', 'b')],
        palette=[('#0B1015', 'Base'), ('#2A3440', 'Slate'), ('#EB4C03', 'Signal'),
                 ('#C9B79A', 'Dust'), ('#F3EFE9', 'Paper')],
        deliver=[('Positioning and narrative platform', 'Discovery'),
                 ('Identity system and mark set', 'Craft'),
                 ('Art direction and grading guide', 'Craft'),
                 ('Webflow build, single scroll', 'Build'),
                 ('Ongoing edit and content care', 'Momentum')],
        nxt='collective'),

    dict(
        slug='collective', num='02', name='Off-Grid Collective',
        services='Ecosystem · Membership · Retainer',
        lede='A private network of remote founders run out of a Notion page and a Slack invite. '
             'We gave it an ecosystem quiet enough to feel exclusive and structured enough to grow.',
        meta=[('Client', 'Private founder network'), ('Year', '2025'),
              ('Engagement', 'Foundation + Momentum'), ('Build', 'Webflow + member area')],
        brief=[
            'Around three hundred founders, spread across fourteen time zones, held together by a '
            'shared doc and goodwill. Every new member arrived through a forwarded link and a '
            'personal vouch, which worked beautifully and did not scale at all.',
            'They wanted to double without becoming another loud community brand — no cohort '
            'language, no countdown timers, no growth-hacking sheen.'],
        made=[
            'A restrained identity built on a constellation motif: individual points, real distance '
            'between them, connections that only appear when you look. It carries the idea of the '
            'network without ever drawing an actual network diagram twice.',
            'The ecosystem is three surfaces on one system — a public page that explains almost '
            'nothing on purpose, an application that reads as an invitation rather than a form, and '
            'a member area with a directory, a quiet events rail and a fortnightly letter.'],
        quote='Exclusivity is a design problem. Say less, and mean all of it.',
        side=['Identity and constellation mark system', 'Public page and application flow',
              'Member directory and profile structure', 'Fortnightly letter template',
              'Tone of voice guide for the community team', 'Monthly retainer: content and care'],
        shots=[('Contour study — density map of member locations', 'a'),
               ('Structure test — directory grid at three widths', 'b')],
        palette=[('#080C11', 'Void'), ('#1B2430', 'Deep'), ('#EB4C03', 'Signal'),
                 ('#6E7B8A', 'Steel'), ('#EDEAE4', 'Bone')],
        deliver=[('Positioning and membership proposition', 'Discovery'),
                 ('Identity and mark system', 'Craft'),
                 ('Application and onboarding flow', 'Craft'),
                 ('Public site and member area build', 'Build'),
                 ('Letter, events and directory upkeep', 'Momentum')],
        nxt='terra'),

    dict(
        slug='terra', num='03', name='Terra Alta Studio',
        services='Identity · Art direction · Web',
        lede='An architecture studio building low-impact houses in the Carpathians, with a portfolio '
             'trapped in PDFs. We gave the work the editorial treatment it already deserved.',
        meta=[('Client', 'Architecture studio'), ('Year', '2026'),
              ('Engagement', 'Foundation'), ('Build', 'Webflow')],
        brief=[
            'Terra Alta had eleven finished houses, a decade of drawings and a site that reduced all '
            'of it to three thumbnails and a contact form. Clients were arriving through word of '
            'mouth and then being asked to imagine the rest.',
            'The studio also had a genuine constraint most practices only claim: every house is built '
            'from what the site and the region can give it. That needed to be structural in the brand, '
            'not a sustainability badge in the footer.'],
        made=[
            'An architectural type scale — one measure, held everywhere — and a layout system where '
            'drawings and photography carry equal weight. Plans and sections are not supporting '
            'material here; they open the project.',
            'Each house gets an editorial page with a materials index: what it is made of, where each '
            'material came from, how far it travelled. The constraint became the most interesting page '
            'on the site.'],
        quote='If the constraint is real, put it in the layout — not in a badge.',
        side=['Identity and architectural type scale', 'Editorial project page system',
              'Materials index structure', 'Photography and drawing art direction',
              'Webflow build with CMS for houses', 'Print one-pager for site visits'],
        shots=[('Volume study — massing rhythm, west elevation', 'a'),
               ('Light study — interior, late afternoon', 'b')],
        palette=[('#12100E', 'Char'), ('#3A2E25', 'Timber'), ('#E4571E', 'Ember'),
                 ('#B79E7E', 'Clay'), ('#F1ECE3', 'Lime')],
        deliver=[('Positioning and studio narrative', 'Discovery'),
                 ('Identity and editorial type system', 'Craft'),
                 ('Project page and materials index design', 'Craft'),
                 ('Webflow build with house CMS', 'Build'),
                 ('Handover, training and documentation', 'Build')],
        nxt='wildland'),

    dict(
        slug='wildland', num='04', name='Wildland Sanctuary',
        services='Identity · Motion · Booking',
        lede='Three off-grid cabins, a wood-fired sauna and a waiting list living in a spreadsheet. '
             'We built the brand and the booking flow that turned interest into nights.',
        meta=[('Client', 'Off-grid retreat'), ('Year', '2026'),
              ('Engagement', 'Foundation + Momentum'), ('Build', 'Showit + booking')],
        brief=[
            'Guests were finding Wildland through a friend or a saved post, then emailing to ask if a '
            'weekend in October was free. Someone answered those emails by hand, sometimes two days '
            'later. Most people did not wait.',
            'The place itself does the selling — fog in the valley at six in the morning, no signal, a '
            'stove you have to feed. None of that survived the trip to the website.'],
        made=[
            'A brand rooted in the site rather than the category: seasonal art direction with four '
            'distinct grades, a mark that reads as both a ridge and a roofline, and copy written in '
            'the register of someone who actually lives there.',
            'Booking takes three taps — dates, cabin, confirm — with live availability and a deposit '
            'held at the first step. The waiting list moved out of the spreadsheet and into something '
            'that answers instantly at two in the morning.'],
        quote='The place was never the problem. The two-day reply was.',
        side=['Identity, ridge mark and seasonal grades', 'Photography and motion art direction',
              'Three-step booking flow design', 'Showit build with live availability',
              'Guest email and pre-arrival sequence', 'Seasonal content retainer'],
        shots=[('Season study — autumn canopy, morning fog', 'a'),
               ('Atmosphere test — valley mist, blue hour', 'b')],
        palette=[('#0A0F0C', 'Peat'), ('#1E2A22', 'Moss'), ('#E9540C', 'Ember'),
                 ('#8FA08F', 'Lichen'), ('#F0EDE6', 'Ash')],
        deliver=[('Positioning and guest narrative', 'Discovery'),
                 ('Identity and seasonal art direction', 'Craft'),
                 ('Booking flow design and copy', 'Craft'),
                 ('Showit build with live availability', 'Build'),
                 ('Seasonal content and campaign care', 'Momentum')],
        nxt='meridian'),
]

BY_SLUG = {c['slug']: c for c in CASES}
MOTIF = {'meridian': 'n-mountain', 'collective': 'n-bird', 'terra': 'n-pine', 'wildland': 'n-bear'}


def render():
    out = []
    for c in CASES:
        nxt = BY_SLUG[c['nxt']]
        meta = ''.join('<div><span>%s</span><span>%s</span></div>' % kv for kv in c['meta'])
        brief = ''.join('<p>%s</p>' % p for p in c['brief'])
        made = ''.join('<p>%s</p>' % p for p in c['made'])
        side = ''.join('<li><svg class="bul" aria-hidden="true"><use href="#n-pine"/></svg>%s</li>' % li for li in c['side'])
        shots = ''.join(
            '<figure><img class="mb" src="__IMG_C_%s_%s__" alt="%s"><figcaption>%s</figcaption></figure>'
            % (c['slug'].upper(), key.upper(), cap, cap) for cap, key in c['shots'])
        sw = ''.join(
            '<div class="swatch" style="background:%s;color:%s">%s<br>%s</div>'
            % (hexv, '#0B1015' if i >= 3 else '#F3EFE9', name, hexv.upper())
            for i, (hexv, name) in enumerate(c['palette']))
        deliver = ''.join('<div><span>%s</span><span>%s</span></div>' % kv for kv in c['deliver'])

        out.append('''
<article class="cpage" id="case-%(slug)s" hidden>
  <header class="chero">
    <img class="cbg mb" src="__IMG_C_%(SLUG)s_HERO__" alt="">
    <div class="cveil"></div>
    <div class="wrap in">
      <a class="backlink anim" href="#work" data-cursor>%(back)s All work</a>
      <div>
        <span class="ctag anim a2"><svg class="gi" aria-hidden="true"><use href="#%(motif)s"/></svg>Concept study — %(num)s</span>
        <h1 class="display anim a2">%(name)s</h1>
        <p class="lede anim a3">%(lede)s</p>
        <div class="cmeta anim a4">%(meta)s</div>
      </div>
    </div>
  </header>

  <section class="cbody">
    <div>
      <div class="blk">
        <span class="eyebrow">The brief</span>
        <h2 style="margin-top:.7rem">What they came with</h2>
        %(brief)s
      </div>
      <div class="blk">
        <span class="eyebrow">The work</span>
        <h2 style="margin-top:.7rem">What we made</h2>
        %(made)s
      </div>
      <div class="blk"><p class="cquote">%(quote)s</p></div>
    </div>
    <aside class="cside">
      <div>
        <span class="eyebrow">Scope</span>
        <ul style="margin-top:1rem">%(side)s</ul>
      </div>
      <div>
        <span class="eyebrow">Services</span>
        <p style="margin-top:.8rem;font-size:.9rem">%(services)s</p>
      </div>
    </aside>
  </section>

  <section class="cshots">%(shots)s</section>

  <section class="csystem">
    <div>
      <span class="eyebrow">Palette</span>
      <div class="swatches" style="margin-top:1.1rem">%(sw)s</div>
    </div>
    <div>
      <span class="eyebrow">Delivered</span>
      <div class="deliver" style="margin-top:1.1rem">%(deliver)s</div>
    </div>
  </section>

  <p class="cnote">These case studies are concept work, made to show how Kreator thinks. Live client
    projects replace them as they ship.</p>

  <div class="cnext">
    <a href="#work/%(nslug)s" data-cursor>
      <span class="label">Next project — %(nnum)s</span>
      <strong>%(nname)s</strong>
      <span class="arrowlink">View case %(arrow)s</span>
    </a>
  </div>
</article>
''' % dict(slug=c['slug'], SLUG=c['slug'].upper(), num=c['num'], name=c['name'], lede=c['lede'],
           meta=meta, brief=brief, made=made, quote=c['quote'], side=side,
           services=c['services'], shots=shots, sw=sw, deliver=deliver,
           nslug=nxt['slug'], nnum=nxt['num'], nname=nxt['name'], arrow=ARROW, back=BACK,
           motif=MOTIF[c['slug']]))
    return '\n'.join(out)


if __name__ == '__main__':
    open('cases.html', 'w').write(render())
    print('cases rendered')
