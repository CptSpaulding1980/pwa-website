"""Exact, vault-derived PWA event video publication (no cross-promotion guessing)."""
from html import escape
from pathlib import Path
import hashlib
import re
import shutil
import subprocess
import tempfile
from urllib.parse import quote

MAX_GITHUB_BYTES = 100_000_000
VIDEO_SUFFIXES = {'.mp4'}  # Browsers on GitHub Pages need an MP4 source.
KNOWN_EVENT_SOURCE = '927f803cbcf9e19b30e414119d2e1396e462793fcae23ebebd289f018ea4a82a'
KNOWN_EVENT_PUBLICATION = 'c8d81b1e01236eea8fcba9cfb48f208f4b255e0c8804302e690590c4aef436d4'
KNOWN_HOME_SOURCE = 'c8a1bc6eee98d89f45b994d2d5a1b2859ba583e31dc014393a8036461692055e'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _match_suffix(name, suffix):
    """Require a complete match pairing, not a fuzzy title/participant hit."""
    name = re.sub(r'\s*\(c\)', '', name, flags=re.I)
    return name.split(': ', 1)[-1].strip().casefold() == suffix.casefold()


def discover(vault, event_rows):
    """Map a video only when exactly one event's title AND card pairing match."""
    assigned = {}
    for video in sorted(vault.rglob('*')):
        if not video.is_file() or video.suffix.lower() not in VIDEO_SUFFIXES:
            continue
        # Never ingest other promotions, even if accidentally copied into the vault.
        if video.name[:4].casefold() != 'pwa ':
            continue
        candidates = []
        for date, title, matches in event_rows:
            prefix = title + ' - '
            if not video.stem.casefold().startswith(prefix.casefold()):
                continue
            pairing = video.stem[len(prefix):]
            if any(_match_suffix(m.get('name', ''), pairing) for m in matches):
                candidates.append(date)
        if len(candidates) == 1:
            assigned.setdefault(candidates[0], []).append(video)
        elif candidates:
            raise ValueError('Ambiguous event video: {}'.format(video))
    return assigned


def ensure_note_embed(note, video):
    """Restore the source annotation if an upstream note generator replaced it."""
    text = note.read_text(encoding='utf-8')
    embed = '![[{}]]'.format(video.name)
    if embed in text:
        return False
    if not text.startswith('---\n'):
        raise ValueError('Refusing to edit non-event note: {}'.format(note))
    block = '\n## Video · {}\n{}\n'.format(video.stem.split(' - ', 1)[-1], embed)
    if '\n## Anmerkungen' in text:
        text = text.replace('\n## Anmerkungen', block + '\n## Anmerkungen', 1)
    else:
        text = text.rstrip() + '\n' + block
    note.write_text(text, encoding='utf-8')
    subprocess.run(['docker', 'exec', '--user', 'www-data', 'nextcloud-app', 'php', 'occ',
                    'files:scan', '--path=hendrik/files/Obsidian/PWA/Events/' + note.name], check=True)
    return True


def publish(source, target):
    """Keep the original untouched; encode only when a published MP4 is missing."""
    known = source.name == 'PWA Clash of Honor XII - Rick Banner vs. UK Kid.mp4'
    if known and digest(source) != KNOWN_EVENT_SOURCE:
        raise ValueError('Approved event video source changed; review before publication')
    if target.is_file() and (known or target.stat().st_mtime >= source.stat().st_mtime):
        if target.stat().st_size >= MAX_GITHUB_BYTES:
            raise ValueError('Published MP4 exceeds GitHub file limit: {}'.format(target))
        if known and digest(target) != KNOWN_EVENT_PUBLICATION:
            raise ValueError('Approved event MP4 differs from verified transcode')
        return
    target.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='pwa-video-') as tmp:
        log = str(Path(tmp) / 'pass')
        common = ['ffmpeg', '-hide_banner', '-loglevel', 'error', '-y', '-i', str(source),
                  '-vf', 'scale=854:480', '-c:v', 'libx264', '-preset', 'veryfast',
                  '-b:v', '560k', '-maxrate', '700k', '-bufsize', '1400k']
        subprocess.run(common + ['-pass', '1', '-passlogfile', log, '-an', '-f', 'null', '/dev/null'], check=True)
        staged = Path(tmp) / 'encoded.mp4'
        subprocess.run(common + ['-pass', '2', '-passlogfile', log, '-c:a', 'aac', '-b:a', '80k',
                                 '-movflags', '+faststart', str(staged)], check=True)
        if not staged.is_file() or staged.stat().st_size >= MAX_GITHUB_BYTES:
            raise ValueError('Encoded video not publishable: {}'.format(source))
        shutil.move(str(staged), str(target))


def event_player(source, date, docs, prefix):
    filename = date + '-' + re.sub(r'-+', '-', re.sub(r'[^a-z0-9-]+', '-', source.stem.lower())).strip('-') + '.mp4'
    target = docs / 'video' / filename
    publish(source, target)
    caption = source.stem.split(' - ', 1)[-1]
    url = prefix + '/video/' + quote(filename)
    return ('<section class="event-video" aria-label="Eventvideo"><h2>Video · {caption}</h2>'
            '<video controls preload="metadata" playsinline aria-label="{caption} – Video von diesem PWA-Event">'
            '<source src="{url}" type="video/mp4">'
            'Dein Browser unterstützt kein HTML5-Video. <a href="{url}">Video herunterladen</a>.'
            '</video></section>\n').format(caption=escape(caption), url=escape(url, quote=True))


def homepage_player(source, docs, prefix):
    if digest(source) != KNOWN_HOME_SOURCE:
        raise ValueError('Nextcloud fileid 449397 source changed; review before publication')
    target = docs / 'video' / 'pwa-homepage.mp4'
    if not target.is_file() or digest(target) != KNOWN_HOME_SOURCE:
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
    if target.stat().st_size >= MAX_GITHUB_BYTES:
        raise ValueError('Homepage video exceeds GitHub file limit')
    url = escape(prefix + '/video/pwa-homepage.mp4', quote=True)
    return ('<section class="home-video" aria-labelledby="home-video-title">'
            '<div class="section-heading"><h2 id="home-video-title">PWA im Video</h2></div>'
            '<video controls preload="metadata" playsinline aria-label="PWA – Homepage-Video">'
            '<source src="{url}" type="video/mp4">'
            'Dein Browser unterstützt kein HTML5-Video. <a href="{url}">Video herunterladen</a>.'
            '</video></section>').format(url=url)
