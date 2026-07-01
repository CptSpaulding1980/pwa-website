---
layout: event.njk
title: PWA Friday Explosion 119
date: '2019-01-11'
venue: Buffalo, New York
location: ''
promotion: PWA
permalink: /events/2019-01-11 - PWA Friday Explosion 119/
tags:
- events
matches_json: [{"number": 1, "name": "Royal Brawl Qualifiers: Yokosumo Kawashi vs. Shredder", "finish": "Yokosumo Kawashi beat Shredder in 5 Min 57 Sec with an Avalanche Power Slam", "rating_stars": "<span class=\"stars\">★★½</span>", "rating_num": 2.5, "time": "5:57"}, {"number": 2, "name": "Royal Brawl Qualifiers: Seth Ramsey vs. Saburo Aoki Jr.", "finish": "Saburo Aoki Jr. beat Seth Ramsey in 1 Min 52 Sec with a Swift Blade", "rating_stars": "<span class=\"stars\">★½</span>", "rating_num": 1.5, "time": "1:52"}, {"number": 3, "name": "Royal Brawl Qualifiers: Ray Stantz vs. Poppa Thurgoode", "finish": "Ray Stantz beat Poppa Thurgoode in 14 Min 43 Sec with a K.O", "rating_stars": "<span class=\"stars\">★★★</span>", "rating_num": 3, "time": "14:43"}, {"number": 4, "name": "Royal Brawl Qualifiers: Jitsu  vs. Rey Horus", "finish": "Rey Horus beat Jitsu  in 8 Min 26 Sec with a Firebird Splash", "rating_stars": "<span class=\"stars\">★★★</span>", "rating_num": 3, "time": "8:26"}, {"number": 5, "name": "PWA International Chamoionship: Naomichi Marufuji vs. Lex Rider (c)", "finish": "Lex Rider beat Naomichi Marufuji in 8 Min 33 Sec with an Anaconda vice", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "8:33"}]
---

# PWA Friday Explosion 119

<div class="event-header">
<div class="event-meta">
**Date:** 2019-01-11<br>
**Venue:** Buffalo, New York<br>
**Location:** 
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