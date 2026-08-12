import assert from 'node:assert/strict';
import fs from 'node:fs';
import test from 'node:test';

const html = fs.readFileSync(new URL('../index.html', import.meta.url), 'utf8');
const spec = fs.readFileSync(
  new URL(
    '../docs/superpowers/specs/2026-08-12-evidence-link-and-layout-design.md',
    import.meta.url,
  ),
  'utf8',
);

const expected = [...spec.matchAll(/^\| (\d+) \| (.+) \|$/gm)].flatMap(
  ([, label, cell]) =>
    [...cell.matchAll(/`([^`]+#L\d+(?:-L\d+)?)`/g)].map(([, path]) => [
      label,
      path,
    ]),
);
const actual = [...html.matchAll(/\['(\d+)',\s*'([^']+)'\]/g)].map(
  (match) => [match[1], match[2]],
);

test('matches the approved 96-block evidence design', () => {
  assert.equal(expected.length, 96);
  assert.deepEqual(actual, expected);
});

test('covers all items with exact line anchors and keeps item 3 in README', () => {
  assert.deepEqual(
    [...new Set(actual.map(([label]) => Number(label)))],
    Array.from({ length: 31 }, (_, index) => index + 1),
  );
  assert.ok(
    actual.every(([, path]) => /^.+#L[1-9]\d*(?:-L[1-9]\d*)?$/.test(path)),
  );
  assert.ok(
    actual
      .filter(([label]) => label === '3')
      .every(([, path]) => path.startsWith('README.md#')),
  );
  assert.doesNotMatch(html, /\/pull\/|pull\/\d+/);
});

test('uses the approved decoy limits and the main URL builder', () => {
  assert.match(html, /NOISE_REAL_COUNT = 48/);
  assert.match(html, /NOISE_INTEGER_COUNT = 76/);
  assert.match(html, /`\$\{repository\}\/blob\/main\/\$\{path\}`/);
});

test('defines measured collision-free responsive placement', () => {
  assert.match(html, /const COLLISION_PADDING_PX = [1-9]\d*/);
  assert.match(html, /function rotatedBounds|const rotatedBounds/);
  assert.match(html, /function intersects|const intersects/);
  assert.match(html, /getBoundingClientRect\(\)/);
  assert.match(html, /function layoutScene|const layoutScene/);
  assert.match(html, /dataset\.overlapCount/);
  assert.match(html, /new ResizeObserver/);
});
