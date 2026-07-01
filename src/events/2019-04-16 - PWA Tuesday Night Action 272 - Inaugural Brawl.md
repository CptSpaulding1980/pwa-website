---
layout: event.njk
title: PWA Tuesday Night Action 272 - Inaugural Brawl
date: '2019-04-16'
venue: PWA Capcom Arena
location: Boston, Massachusetts, USA
promotion: PWA
permalink: /events/2019-04-16 - PWA Tuesday Night Action 272 - Inaugural Brawl/
tags:
- events
matches_json: [{"number": 1, "name": "Chelsea Grin vs. Villano III Jr.", "finish": "Chelsea Grin battled Villano III Jr. to a  time limit draw", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": ""}, {"number": 2, "name": "Blake Twins & Brutes vs. Masked Lucha Alliance", "finish": "Rampage Rage beat Grizzlor  in 19 Min 28 Sec with a Pop-up Power Bomb", "rating_stars": "<span class=\"stars\">★★½</span>", "rating_num": 2.5, "time": "19:28"}, {"number": 3, "name": "Ox Hemlock vs. Roadkill", "finish": "Ox Hemlock beat Roadkill in 7 Min 58 Sec with a Kamigoye", "rating_stars": "<span class=\"stars\">DUD</span>", "rating_num": 0, "time": "7:58"}, {"number": 4, "name": "Diablo Blanco vs. Rick Banner", "finish": "Diablo Blanco beat Rick Banner in 12 Min 21 Sec with a La Magistral", "rating_stars": "<span class=\"stars\">★★½</span>", "rating_num": 2.5, "time": "12:21"}, {"number": 5, "name": "Non Title Match: Shingo Takagi vs. UK Kid", "finish": "Shingo Takagi beat UK Kid in 11 Min 54 Sec with a Last of the Dragon", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": "11:54"}]
---

# PWA Tuesday Night Action 272 - Inaugural Brawl

<div class="event-header">
<div class="event-meta">
**Date:** 2019-04-16<br>
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