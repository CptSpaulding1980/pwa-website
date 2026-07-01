---
layout: event.njk
title: PWA Tuesday Night Action 274 - The League of the fighting Gentlemen
date: '2019-04-30'
venue: PWA Capcom Arena
location: Bosotn, Massachusetts, USA
promotion: PWA
permalink: /events/2019-04-30 - PWA Tuesday Night Action 274 - The League of the fighting
  Gentlemen/
tags:
- events
matches_json: [{"number": 1, "name": "Non Title Match: Dynamite Smith vs. Blue Blazer Jr.", "finish": "Blue Blazer Jr. beat Dynamite Smith in 8 Min 51 Sec with a Sharpshooter", "rating_stars": "<span class=\"stars\">★★★</span>", "rating_num": 3, "time": "8:51"}, {"number": 2, "name": "World Title Tournament League: Rick Banner [0] vs. Roadkill [2]", "finish": "Roadkill beat Rick Banner in 14 Min 29 Sec with a Mexican Stretch", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "14:29"}, {"number": 3, "name": "World Title Tournament League: Diablo Blanco [0] vs. Ox Hemlock [2]", "finish": "Ox Hemlock beat Diablo Blanco in 14 Min 10 Sec with a Turn Belly-to-Belly", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": "14:10"}, {"number": 4, "name": "World Title Tournament League: Shingo Takagi [0] vs. WALTER [0]", "finish": "WALTER beat Shingo Takagi in 14 Min 7 Sec with a Deadlift German Suplex", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "14:07"}, {"number": 5, "name": "World Title Tournament League: Avery Alexander [2] vs. Lex Rider [2]", "finish": "Lex Rider beat Avery Alexander in 10 Min 56 Sec with a Vaulting Frog Splash", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": "10:56"}]
---

# PWA Tuesday Night Action 274 - The League of the fighting Gentlemen

<div class="event-header">
<div class="event-meta">
**Date:** 2019-04-30<br>
**Venue:** PWA Capcom Arena<br>
**Location:** Bosotn, Massachusetts, USA
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