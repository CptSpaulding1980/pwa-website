# PWA Wrestling — Professional Wrestling Association

**Live:** https://cptspaulding1980.github.io/pwa-website/

Standalone Python-generated wrestling archive. The redesign preserves the published
238 event records, 269 wrestler records, 4 championships and all 518 page URLs.
These are the verified release counts, not hard-coded homepage counters.

## Build

```sh
python3 build.py
```

Requires Python 3.9+ and PyYAML. On the current Mac, `/usr/bin/python3` has PyYAML;
do not assume the separately installed default pip belongs to this interpreter.
No Node, Eleventy, Sass, external fonts or client-side JavaScript are used.

The generator reads the **read-only** Nextcloud Obsidian vault at
`/Volumes/SSD_4TB/nextcloud/app/data/hendrik/files/Obsidian/PWA`.
It writes complete HTML and copies maintained CSS to `docs/`.

## Maintained sources

- `build.py`: data pipeline, Markdown/wiki links, statistics and archive indexes.
- `presentation.py`: single shared PWA banner, independent navigation, accessibility
  and scrollable table regions for **every** page family.
- `magazine.py`: homepage derived from event JSON and generated title/ranking pages.
- `assets/styles/main.css`: authoritative stylesheet; copied to `docs/styles/main.css`
  by every build. Do not edit only the generated stylesheet.
- `content/published-legacy.json`: unchanged published bodies and metadata for two
  events and two wrestlers missing from the current vault. A restored vault record
  takes precedence. This prevents rebuilds silently deleting published canon.
- `docs/img/`: existing published assets remain valid fallbacks if the source image
  no longer exists in the vault. Do not clean this directory blindly.

## PWA design contract

Use the actual transparent `PWA_2019-ff.png` roundel and existing PWA arena banner.
Navy, red and white derive from that logo, not from another promotion. Warm rating
highlights echo the existing banner. Use one banner with a prominent uncropped logo
on the left and separate navigation below. Keep data backgrounds calm, links visible,
system display typography strong and media compact. No replacement logos, generated
posters, autoplay, emoji navigation or CSS effects over the data.

The homepage explicitly distinguishes the **last event date in the archive** from
real-world time, and a poster-backed archive feature from the latest event. Champions
and ranking previews must be read from actual generated content, never guessed.

## Verification

Test-only packages: `beautifulsoup4`, `playwright` (Chromium installed).
Production still requires only PyYAML.

```sh
python3 -m unittest discover -s tests -v
python3 tools/browser_audit.py after --strict
# Requires the pre-redesign snapshot, retained in the release evidence archive:
python3 tools/verify_integrity.py --baseline evidence/redesign/baseline-tracked.json
```

Browser audit covers home, three archive indexes, event/wrestler/title detail,
PWI ranking and top/worst match statistics at 320, 375, 768, 1440 and 1920 pixels.
It saves screenshots, overflow/image/error measurements and keyboard-scroll evidence.
The integrity gate compares every pre-existing detail-page link, media reference,
match, table value and text (excluding Markdown table separators), all original image
hashes, JSON records and the read-only vault snapshot. The only detail-page text
addition is the previously missing PWI page heading.

Some pre-existing wrestler image references and wiki targets have no published file.
They are inventoried separately from **new** regressions; never fill missing canon
with invented assets or synthetic pages. The release report lists the exact counts.

## Deployment and rollback

GitHub Pages serves `main:/docs` through the automatic `pages-build-deployment`
workflow. Commit maintained sources plus generated output, push `main`, wait for the
**exact commit SHA** workflow to succeed, then compare live HTML/CSS/images byte-for-byte
with local output. Local build success alone is not deployment evidence.

Rollback via an explicit revert of the redesign commit, followed by the same Pages
and live-byte verification. No vault changes are needed for deployment or rollback.
