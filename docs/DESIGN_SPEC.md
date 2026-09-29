# Insurix — Frontend Design Spec

**Working title for the look: "The Policy, Dissected."**

Everyone else in insurtech shows a shield, a smiling family and a blue gradient. Insurix does the opposite: it treats a 60-page policy as a physical object on a lab bench. You pull it apart, stamp it, cut it, weigh it, and pin the evidence to the wall with red string. Neo-Brutalism is the grammar (hard borders, hard shadows, flat colour). The tactile paper, rubber-stamp and lab-bench world is the point of view.

Every visual choice below answers one question: **does it make the fine print feel physical and checkable?** If it doesn't, cut it.

---

## 1. Principles

1. **Paper is the material.** Pages, stamps, sticker tags, receipts, punched holes, photocopy grain. Never glass, glow or soft gradients.
2. **One hero, many small proofs.** The 3D policy stack is the one big memorable object. Every other 3D piece is small, tied to a specific number, and exists because a flat chart explains it worse.
3. **Colour is information.** Each colour has one job (see tokens). Users learn the legend without reading it.
4. **Motion answers actions.** One orchestrated load moment, then the page is quiet. Everything else moves because you did something.
5. **Every claim has a pin.** No answer appears without a page reference. The UI makes evidence the most tactile thing on screen.
6. **Hard light only.** One directional light, stepped shading, hard shadows that match the CSS offset shadows. No blur.

---

Scale (fluid, ratio about 1.333):

```css
--t-hero: clamp(3.5rem, 9vw + 1rem, 9rem);   /* wght 800, wdth 75, tracking -0.03em */
--t-h1:   clamp(2.5rem, 5vw + 1rem, 5rem);
--t-h2:   clamp(1.75rem, 2.5vw + 1rem, 3rem);
--t-h3:   1.5rem;
--t-body: 1.0625rem;                          /* Bricolage, wght 400 */
--t-clause: 1.125rem;                         /* Newsreader */
--t-small: 0.875rem;
```

Type as an active element:
- Hero headline is set at `wdth 75` (condensed) and **expands to `wdth 100` on scroll** as the stack fans open. The words physically loosen as the policy does.
- Numbers (₹ amounts, days, percentages) are always Bricolage 700 with `tabular-nums`, sized one step larger than surrounding text. Money is the loudest thing in any sentence.
- No all-caps eyebrows above headings. No middle-dot meta strings. Sentence case everywhere, except verdict stamps (Section 6), which are caps because real rubber stamps are.

### Shape, border, shadow

```css
--bw: 3px;            /* default border; 5px on hero objects */
--shadow-1: 6px 6px 0 var(--ink);
--shadow-2: 10px 10px 0 var(--ink);
--radius-sheet: 0;            /* pages and receipts are square */
--radius-sticker: 18px;       /* stickers and tags are die-cut, so rounded */
--radius-pill: 999px;         /* only for chips and toggles */
```

Different objects get different corners on purpose: square paper, rounded stickers, pill chips. Not one radius on everything.

Background: replace the plain 34px grid with a **cutting-mat grid**: 34px minor lines, a heavier line every 5th, tiny tick marks along the viewport edges like a ruler. The mat scrolls at 0.9x page speed for a faint depth cue.

├── scripts/scenes/stack.js  # hero page stack
├── scripts/scenes/slab.js   # penalty slab
├── scripts/scenes/dial.js   # waiting dial
├── scripts/motion.js        # GSAP timelines, Stamp-in
├── scripts/pinboard.js      # red string SVG
└── assets/                  # page textures, grain, stamp filters
```

Hard-shadow toon material starter:

```js
const ramp = new THREE.DataTexture(new Uint8Array([70, 150, 255]), 3, 1, THREE.RedFormat);
ramp.needsUpdate = true;
const paper = new THREE.MeshToonMaterial({ color: 0xFFFDF8, gradientMap: ramp });
const light = new THREE.DirectionalLight(0xffffff, 2.2);
light.position.set(-4, 6, 5);
light.castShadow = true;
light.shadow.radius = 0;          // hard edges
```

Stamp-in timeline starter:

```js
const tl = gsap.timeline({ defaults: { ease: 'power3.out' } });
tl.from('.mat-grid', { clipPath: 'inset(0 100% 100% 0)', duration: .5 })
  .from('.stack', { y: -240, duration: .4, ease: 'bounce.out' })
  .to('.stack-highlight', { scaleX: 1, duration: .35 }, '>-0.1')
  .to('.hero-title', { fontVariationSettings: '"wdth" 100', duration: .7 }, '<')
  .from('.stamp', { scale: 1.6, rotate: -12, opacity: 0, duration: .18, ease: 'back.out(3)' });
```

---

## 11. Final check before shipping any screen

1. Is there exactly one memorable object on this screen? If two compete, shrink one.
2. Does every colour on screen mean something from the legend?
3. Does every number, claim or stamp have a source, a label, or both?
4. Could this screen belong to any other insurtech product? If yes, add something only Insurix has (paper, stamps, string, slab) or cut something generic.
5. Does it still work in one flat frame, with motion off and 3D off?
