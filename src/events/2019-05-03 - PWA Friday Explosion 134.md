---
layout: event.njk
title: PWA Friday Explosion 134
date: '2019-05-03'
venue: PWA Capcom Arena
location: Boston, Massachusetts, USA
promotion: PWA
permalink: /events/2019-05-03 - PWA Friday Explosion 134/
tags:
- events
matches_json: [{"number": 1, "name": "Villano III Jr. vs. Casper Winkel", "finish": "Casper Winkel beat Villano III Jr. in 13 Min 25 Sec with a Buffalo Sleeper", "rating_stars": "<span class=\"stars\">★★★</span>", "rating_num": 3, "time": "13:25"}, {"number": 2, "name": "World Title Tournament League: Ox Hemlock [4] vs. Roadkill [4]", "finish": "Ox Hemlock beat Roadkill in 5 Min 50 Sec with a Kamigoye", "rating_stars": "<span class=\"stars\">★½</span>", "rating_num": 1.5, "time": "5:50"}, {"number": 3, "name": "World Title Tournament League: Diablo Blanco [0] vs. Rick Banner [0]", "finish": "Diablo Blanco beat Rick Banner in 14 Min 1 Sec with a Skull End", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "14:01"}, {"number": 4, "name": "World Title Tournament League: WALTER [2] vs. Avery Alexander [2]", "finish": "WALTER beat Avery Alexander in 12 Min 31 Sec with a Body Choke Sleeper", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": "12:31"}, {"number": 5, "name": "World Title Tournament League: Shingo Takagi [0] vs. Lex Rider [4]", "finish": "Lex Rider beat Shingo Takagi in 11 Min 36 Sec with a Michinoku Driver", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": "11:36"}]
---

# PWA Friday Explosion 134

<div class="event-header">
<div class="event-meta">
**Date:** 2019-05-03<br>
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