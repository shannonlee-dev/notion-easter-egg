# Evidence Link and Collision-Free Layout Implementation Plan

> **Current-state note (2026-08-12):** This plan records the original 96-link rollout. A subsequent
> PASS evaluation review added 10 direct implementation grounds and reduced integer decoys by the
> same amount. The deployed contract is now 106 evidence links, 48 real-form decoys, and 66 integer
> decoys; the design spec and executable test are the current sources of truth.

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the evidence page with the approved 96 exact `main` line-range links, reduce integer decoys by 34, and guarantee that every rendered DOM number has a non-overlapping rotated bounding box.

**Architecture:** `index.html` remains the deployable page and source of runtime behavior. A Node built-in test reads the approved design spec as the mapping source of truth and compares it with the HTML array. The browser layout measures each number, places required evidence and the minute key first, then fills remaining space with optional decoys while rejecting collisions.

**Tech Stack:** Static HTML/CSS, browser JavaScript, Node.js 18 built-in test runner, Windows Chrome headless mode, GitHub Pages.

## Global Constraints

- All evidence URLs use `https://github.com/wilderif/codyssey-b7-1/blob/main/<path>#L...`.
- The 31 items contain exactly 96 evidence blocks from `docs/superpowers/specs/2026-08-12-evidence-link-and-layout-design.md`.
- Integer decoys decrease from 110 to 76; real-form decoys remain 48.
- Required evidence numbers and the minute key are never omitted.
- Optional decoys may be omitted only when the current viewport cannot place them without collision.
- Existing double-click unlock, one-link relock, new-tab, column assignment, and minute refresh behavior remain intact.

---

### Task 1: Add an executable evidence-map contract

**Files:**

- Create: `tests/evidence-page.test.mjs`
- Read: `docs/superpowers/specs/2026-08-12-evidence-link-and-layout-design.md`
- Read: `index.html`

**Interfaces:**

- Consumes: Markdown rows in the design spec and `[label, path]` entries in `index.html`.
- Produces: `node --test tests/evidence-page.test.mjs`, which exits non-zero for mapping, anchor, count, README-specific, or noise-count regressions.

- [ ] **Step 1: Create the failing Node test**

The test must:

```js
import assert from 'node:assert/strict';
import fs from 'node:fs';
import test from 'node:test';

const html = fs.readFileSync(new URL('../index.html', import.meta.url), 'utf8');
const spec = fs.readFileSync(
  new URL('../docs/superpowers/specs/2026-08-12-evidence-link-and-layout-design.md', import.meta.url),
  'utf8',
);

const expected = [...spec.matchAll(/^\| (\d+) \| (.+) \|$/gm)].flatMap(([, label, cell]) =>
  [...cell.matchAll(/`([^`]+#L\d+(?:-L\d+)?)`/g)].map(([, path]) => [label, path]),
);
const actual = [...html.matchAll(/\['(\d+)',\s*'([^']+)'\]/g)].map((match) => [match[1], match[2]]);

test('matches the approved 96-block evidence design', () => {
  assert.equal(expected.length, 96);
  assert.deepEqual(actual, expected);
});

test('covers all items with exact line anchors and keeps README-only item 3 in README', () => {
  assert.deepEqual([...new Set(actual.map(([label]) => Number(label)))], Array.from({ length: 31 }, (_, index) => index + 1));
  assert.ok(actual.every(([, path]) => /^.+#L[1-9]\d*(?:-L[1-9]\d*)?$/.test(path)));
  assert.ok(actual.filter(([label]) => label === '3').every(([, path]) => path.startsWith('README.md#')));
  assert.doesNotMatch(html, /\/pull\/|pull\/\d+/);
});

test('uses the approved decoy limits and the main URL builder', () => {
  assert.match(html, /NOISE_REAL_COUNT = 48/);
  assert.match(html, /NOISE_INTEGER_COUNT = 76/);
  assert.match(html, /`\$\{repository\}\/blob\/main\/\$\{path\}`/);
});
```

- [ ] **Step 2: Run the test and verify RED**

Run: `node --test tests/evidence-page.test.mjs`

Expected: mapping comparison fails because `index.html` still contains 62 entries, and the integer-decoy assertion fails because it still contains 110.

- [ ] **Step 3: Commit the executable contract with the implementation plan**

```bash
git add tests/evidence-page.test.mjs docs/superpowers/plans/2026-08-12-evidence-link-and-layout.md
git commit -m "test: define evidence page contract"
```

### Task 2: Apply the exact 96-block mapping and density change

**Files:**

- Modify: `index.html`
- Test: `tests/evidence-page.test.mjs`

**Interfaces:**

- Consumes: the exact 31-row mapping in the approved design spec.
- Produces: `paths` with 96 `[label, path]` entries and `NOISE_INTEGER_COUNT = 76`.

- [ ] **Step 1: Replace `paths` from the spec in item order**

Copy every path from the mapping table without shortening line ranges. Keep each item on its own source line so review can compare HTML and spec row by row.

- [ ] **Step 2: Reduce integer decoys by exactly 34**

Change:

```js
const NOISE_INTEGER_COUNT = 110;
```

to:

```js
const NOISE_INTEGER_COUNT = 76;
```

- [ ] **Step 3: Run the contract test**

Run: `node --test tests/evidence-page.test.mjs`

Expected: all three tests pass.

- [ ] **Step 4: Validate every target against the latest target-repository main checkout**

Run a Node assertion with `EVIDENCE_REPO_ROOT=/tmp/codyssey-b7-1-main` that parses each `#Lstart-Lend`, confirms the file exists, and confirms `1 <= start <= end <= file line count`.

- [ ] **Step 5: Commit the link mapping**

```bash
git add index.html
git commit -m "fix: align evidence links with criteria"
```

### Task 3: Implement collision-free number placement

**Files:**

- Modify: `index.html`
- Test: `tests/evidence-page.test.mjs`

**Interfaces:**

- `rotatedBounds(width, height, rotation)` produces an axis-aligned rotated width and height.
- `intersects(candidate, placed, padding)` returns whether two padded rectangles overlap.
- `tryPlace(element, options, placed)` returns a placed rectangle or `null` after bounded attempts.
- `layoutScene()` places required elements first, then optional decoys, and writes diagnostic counts to `#numbers.dataset`.
- `scheduleLayout()` coalesces resize-driven layouts with `requestAnimationFrame`.

- [ ] **Step 1: Extend the contract test with structural layout expectations**

Assert that the HTML contains `ResizeObserver`, `getBoundingClientRect`, `rotatedBounds`, `intersects`, `layoutScene`, `dataset.overlapCount`, and collision padding greater than zero. Run the test and verify it fails because these do not yet exist.

- [ ] **Step 2: Replace direct random positioning with measured placement**

Implement rotated AABB calculation using:

```js
const radians = rotation * Math.PI / 180;
return {
  width: Math.abs(width * Math.cos(radians)) + Math.abs(height * Math.sin(radians)),
  height: Math.abs(width * Math.sin(radians)) + Math.abs(height * Math.cos(radians)),
};
```

Reject candidates outside `#numbers` or intersecting any stored rectangle with `COLLISION_PADDING_PX`.

- [ ] **Step 3: Add required-first responsive layout**

Create evidence and minute-key elements before the first layout. Try font scales from `1` down to `0.4`; at each scale clear positions and retry all required elements. Evidence X candidates remain inside their evaluation column, and Y candidates remain inside the panel. A failed required pass restarts at the next smaller scale.

- [ ] **Step 4: Fill remaining space with optional decoys**

Create at most 48 real-form and 76 integer-form decoys. Attempt each against the required and already placed decoy rectangles. Remove a decoy when no candidate succeeds; never overlap it as a fallback.

- [ ] **Step 5: Reflow on minute and size changes**

Preserve the existing minute-key refresh. Add `ResizeObserver` and an animation-frame scheduler so font measurement and positions are recomputed after a viewport change without recursive synchronous layouts.

- [ ] **Step 6: Expose and verify runtime diagnostics**

After layout, calculate actual `getBoundingClientRect()` intersections for all visible generated numbers and set:

```js
numbers.dataset.overlapCount = String(overlapCount);
numbers.dataset.evidenceCount = String(field.children.length);
numbers.dataset.noiseCount = String(noise.children.length);
```

The evidence count must be 96 and overlap count must be 0.

- [ ] **Step 7: Run the Node contract and syntax checks**

Run `node --test tests/evidence-page.test.mjs`, extract the inline script, and compile it with `new Function(script)`. Both commands must exit zero.

- [ ] **Step 8: Commit the collision-free layout**

```bash
git add index.html tests/evidence-page.test.mjs
git commit -m "fix: prevent numeric overlaps"
```

### Task 4: Verify in a real browser and deploy

**Files:**

- Verify: `index.html`
- Verify: GitHub Pages deployment

**Interfaces:**

- Consumes: `data-overlap-count`, `data-evidence-count`, and `data-noise-count` emitted by Task 3.
- Produces: evidence that multiple browser viewport sizes render 96 required evidence numbers with zero overlaps.

- [ ] **Step 1: Start a local static server**

Run `python3 -m http.server 4173 --bind 0.0.0.0` in the repository and retain its process ID for cleanup.

- [ ] **Step 2: Check several real Chrome viewport sizes**

Use Windows Chrome headless `--dump-dom` at `320x180`, `768x432`, `1280x720`, and `1920x1080`. For every dump assert `data-evidence-count="96"` and `data-overlap-count="0"`; assert noise count is at most 124.

- [ ] **Step 3: Verify interaction logic and diff hygiene**

Run the Node contract, inline-script syntax check, `git diff --check`, and inspect the full diff. Confirm the double-click threshold, unlock/relock handlers, `_blank`, and `noreferrer` are unchanged.

- [ ] **Step 4: Push main**

Run `git push origin main` after all checks pass.

- [ ] **Step 5: Wait for and verify GitHub Pages**

Poll the Pages workflow for the pushed SHA until it reports `completed/success`. Fetch the public HTML with a cache-busting query and assert the 96-entry mapping, item 3 README ranges, `NOISE_INTEGER_COUNT = 76`, collision layout functions, and absence of the old mapping.
