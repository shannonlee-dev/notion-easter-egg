# Number Font Size Adjustment Design

## Goal

Increase every generated number's default type size by approximately 5% while preserving the
existing evidence mapping, density, interaction, responsive behavior, and collision-free layout.

## Change

Update the shared fallback size used by noise numbers, the minute key, and evidence links:

```css
clamp(0.9rem, 2.1vw, 2.2rem)
```

to:

```css
clamp(0.95rem, 2.2vw, 2.3rem)
```

No element-specific size override or layout algorithm change is needed. The existing required-first
placement may select a smaller scale only when necessary to keep all rendered numbers disjoint.

## Acceptance Criteria

1. The shared default number size is `clamp(0.95rem, 2.2vw, 2.3rem)`.
2. All 106 evidence links remain present and exact.
3. Integer and real-form decoy limits remain 66 and 48.
4. Markdown links retain `?plain=1` source-line behavior.
5. Chrome renders 106 evidence links with zero numeric overlaps at the supported verification sizes.
