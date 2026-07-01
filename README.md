# PWA Wrestling Static Site — Professional Wrestling Association

**Live:** [cptspaulding1980.github.io/pwa-website](https://cptspaulding1980.github.io/pwa-website/)

Static archive of a parallel wrestling universe. 234 events, 269 wrestlers, 4 championships spanning 1982–2019.

## Build

```bash
python3 build.py
```

Pulls data from the Obsidian PWA Vault (`/Volumes/SSD_4TB/nextcloud/app/data/hendrik/files/Obsidian/PWA`), generates complete self-contained HTML in `docs/`. No Node.js, no Eleventy, no runtime dependencies beyond Python 3 and PyYAML.

## Deploy

Push to `main` branch. GitHub Pages serves from `/docs`. That's it.

## Structure

```
.
├── build.py          # Python build pipeline (Obsidian → HTML)
├── docs/             # Generated static site (committed, served by GitHub Pages)
│   ├── index.html    # Home page
│   ├── events/       # 234 event pages
│   ├── wrestlers/    # 269 wrestler profiles
│   ├── championships/# Championship history
│   ├── rankings/     # Ranking pages
│   ├── img/          # Images
│   └── styles/       # CSS
└── .gitignore
```

## Data Source

All content lives in the Obsidian PWA Vault (Nextcloud). `build.py` reads Markdown files with YAML frontmatter and generates static HTML. Edit content in Obsidian, run the build, commit, push.
