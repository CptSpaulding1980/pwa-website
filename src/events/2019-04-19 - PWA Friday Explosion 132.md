---
layout: event.njk
title: PWA Friday Explosion 132
date: '2019-04-19'
venue: PWA Capcom Arena
location: Boston, Massachusetts, USA
promotion: PWA
permalink: /events/2019-04-19 - PWA Friday Explosion 132/
tags:
- events
matches_json: [{"number": 1, "name": "Falls Count Anywhere: Allen Hawkins vs. Saburo Aoki Jr.", "finish": "Saburo Aoki Jr. beat Allen Hawkins in 20 Min 59 Sec with a Swift Blade", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "20:59"}, {"number": 2, "name": "Dynamite Smith vs. Nigel Pendragon", "finish": "Dynamite Smith beat Nigel Pendragon in 12 Min 56 Sec with a School Boy", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "12:56"}, {"number": 3, "name": "Avery Alexander vs. Poppa Thurgoode", "finish": "Avery Alexander beat Poppa Thurgoode in 18 Min 25 Sec with a Most Muscular", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": "18:25"}, {"number": 4, "name": "Imperium vs. Ilja Dragunov, Lex Rider, Fred Balentine & Chris Hero", "finish": "Fabian Aichner beat Chris Hero in 45 Min 5 Sec with a Super Kick", "rating_stars": "<span class=\"stars\">★★★★½</span>", "rating_num": 4.5, "time": "45:05"}]
---

# PWA Friday Explosion 132

<div class="event-header">
<div class="event-meta">
**Date:** 2019-04-19<br>
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