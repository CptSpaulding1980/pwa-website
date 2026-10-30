# PWA Wrestling — Professional Wrestling Association

**Live:** https://cptspaulding1980.github.io/pwa-website/

Standalone Python-generated wrestling archive. The redesign preserves the published
238 original event records, 269 wrestler records, 4 championships and all original page URLs.
These are the verified release counts, not hard-coded homepage counters.

The approved Landfall update adds exactly one event (239 published event URLs,
238 canonical statistical events, 875 matches and 3 separately counted segments).
No unvalidated historical reimports, profile/PWI recalculations, title-history
changes or regenerated charts are part of this scoped release.

## Build

```sh
python3 build.py
```

Requires Python 3.9+, PyYAML and Beautiful Soup. On the current Mac, `/usr/bin/python3` has these;
do not assume the separately installed default pip belongs to this interpreter.
No Node, Eleventy, Sass or external fonts are used. A small progressive-enhancement
script provides the accessible homepage promo pause/reduced-motion control.

The generator reads the Nextcloud Obsidian vault at
`/Volumes/SSD_4TB/nextcloud/app/data/hendrik/files/Obsidian/PWA`.
It writes complete HTML and copies maintained CSS to `docs/`. The only permitted
vault write is restoration of a validated event-video embed in its matching note.

### Scoped release while historical reconciliation is open

`build.py` now uses `scoped_refresh.py`: `content/published-tna295.json` freezes
the exact verified publication at `d6ed6944fe2816f8b4ae92ccdd8f6275ac3bc27d`.
It contains historical HTML/data/statistics and image/video hashes, reproducibly
extracted by `tools/freeze_published_release.py` from Git, **never from dirty docs**.
Its SHA-256 and the sole newly approved Landfall source-note SHA-256 are pinned.
Builds preserve old pages verbatim, regenerate indexes/home/statistics from these
maintained sources and reject modified published assets or unexpected routes.
They do not ingest unrelated newly regenerated vault records. `full_pipeline_preview`
is retained for future source-repair work, not called by the release entrypoint.
Further updates require explicit source review; do not merely update the pins.

This is the owner-approved bounded publication, not a repair or validation of the
full upstream pipeline. The conflicting 1982 imports and 23.07.1982 uncertainty
remain separate repair work. Original results/URLs/reigns remain exactly as published.

## Videos

The homepage video is Hendrik's explicitly designated Nextcloud fileid **449397**
(`files/Videos/ElevenLabs_video_seedance-2-5_A dynamic, high_2026-10-28T21_12_00.mp4`).
The source and its published copy are pinned by SHA-256; if the source changes,
publication fails rather than silently substituting footage. The homepage alone
is a muted autoplay/loop/playsinline promo without native controls, with a keyboard
pause control and reduced-motion support. Event videos retain native controls,
metadata preload and no autoplay. No generated posters.

Event videos are discovered recursively *only* inside the PWA vault, and assigned
only if the video filename begins with the exact event title followed by ` - `
and the rest exactly matches a participant pairing on that event's match card.
Multiple candidate events are an error; CSW/namesake video files are not imported.
The generator maintains a valid Obsidian `![[video.mp4]]` embed in a matched event
note (and scans that one changed note with Nextcloud occ), so a later note rewrite
can be repaired on the next build without modifying its match results. For this
event the original 197,920,860-byte MP4 remains untouched in the vault; a 480p
H.264/AAC two-pass 560k/80k publication (85,703,383 bytes) is checked into
`docs/video/`, below GitHub's 100 MB per-file limit. Future videos use the same
encoding when no publication exists. Rebuilds reuse existing media, verify the
approved source and output hashes, and do not generate posters. After any external
PWA vault-note regeneration, explicitly restore the previously
approved event embed with `event_media.ensure_note_embed` and scan that exact note;
the scoped renderer intentionally does not rediscover unapproved vault media.

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
posters, event-player autoplay, emoji navigation or CSS effects over the data.

The homepage explicitly distinguishes the **last event date in the archive** from
real-world time, and a poster-backed archive feature from the latest event. Champions
and ranking previews must be read from actual generated content, never guessed.

## Verification

Test-only packages: `beautifulsoup4`, `playwright` (Chromium installed).
Beautiful Soup is also used by the statistics renderer; Playwright is test-only.

```sh
python3 -m unittest discover -s tests -v
python3 tools/browser_audit.py after --strict
# Requires the pre-redesign snapshot, retained in the release evidence archive:
python3 tools/verify_integrity.py --baseline evidence/redesign/baseline-tracked.json
python3 tools/verify_statistics.py
python3 tools/browser_statistics.py after
python3 tools/browser_home_promo.py after
```

Browser audit covers home, three archive indexes, event/wrestler/title detail,
PWI ranking and top/worst match statistics at 320, 375, 768, 1440 and 1920 pixels.
It saves screenshots, overflow/image/error measurements and keyboard-scroll evidence.
The integrity gate compares every pre-existing detail-page link, media reference,
match, table value and text (excluding Markdown table separators), all original image
hashes and JSON records. The original baseline is retained; exact source-derived
exceptions allow only the homepage, event index, new Landfall page and four
statistics pages/data. Mutation tests reject altered historic/new results, JSON,
images, videos and unexpected URLs. Vault inputs are compared to the scoped
release preflight (`evidence/tna296/vault-before.json`); unrelated upstream work
predates that checkpoint. Reports, volatile editor workspace and the three explicitly
listed concurrently edited Creative documents are not website inputs; the raw
checkpoint and observed Creative-only delta remain archived, not rebaselined.

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
