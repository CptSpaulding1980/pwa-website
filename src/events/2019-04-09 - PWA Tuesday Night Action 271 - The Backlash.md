---
layout: event.njk
title: PWA Tuesday Night Action 271 - The Backlash
date: '2019-04-09'
venue: PWA Capcom Arena
location: Boston, Massachusetts, USA
promotion: PWA
permalink: /events/2019-04-09 - PWA Tuesday Night Action 271 - The Backlash/
tags:
- events
matches_json: [{"number": 1, "name": "PWA World Tag Team Championship: Brutes vs. Masked Lucha Alliance (c)", "finish": "Rampage Rage beat Macho Especial in 17 Min 31 Sec with a Splash of Rage", "rating_stars": "<span class=\"stars\">★★★</span>", "rating_num": 3, "time": "17:31"}, {"number": 2, "name": "Mr. Suplex vs. Poppa Thurgoode", "finish": "Mr. Suplex beat Poppa Thurgoode in 25 Min 45 Sec with a Genki Raiga-plex", "rating_stars": "<span class=\"stars\">★★★★½</span>", "rating_num": 4.5, "time": "25:45"}, {"number": 3, "name": "Foreign Fanatics vs. Mysterious Fantasticos", "finish": "Jitsu  beat Mystery Panther in 24 Min 51 Sec with a Dragon Sleeper", "rating_stars": "<span class=\"stars\">★★★</span>", "rating_num": 3, "time": "24:51"}, {"number": 4, "name": "PWA Junior Heavyweight Championship: Felix Santana Jr. vs. Blue Blazer Jr. (c)", "finish": "Blue Blazer Jr. beat Felix Santana Jr. in 11 Min 37 Sec with a Sharpshooter", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": "11:37"}, {"number": 5, "name": "Triple Threat Match: Ox Hemlock vs. Rick Banner vs. Roadkill", "finish": "Roadkill won a triple threat match against Ox Hemlock & Rick Banner in  12:54", "rating_stars": "<span class=\"stars\">★★★</span>", "rating_num": 3, "time": ""}]
---

# PWA Tuesday Night Action 271 - The Backlash

<div class="event-header">
<div class="event-meta">
**Date:** 2019-04-09<br>
**Venue:** PWA Capcom Arena<br>
**Location:** Boston, Massachusetts, USA
</div>

</div>

## Matches

{% for match in matches_json %}
<div class="match-card">
<span class="match-number">#{{ match.number }}</span>
<div class="match-details">
<div class="match-name">{{ match.name | safe }}</div>
<div class="match-finish">{{ match.finish | safe }}</div>
<div class="match-meta">
<span class="match-time">{{ match.time }}</span>
<span class="match-rating">{{ match.rating_stars | safe }}</span>
</div>
</div>
</div>
{% endfor %}