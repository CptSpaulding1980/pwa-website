---
layout: event.njk
title: PWA Friday Explosion 110
date: '2018-11-02'
venue: Syracuse, New York
location: ''
promotion: PWA
permalink: /events/2018-11-02 - PWA Friday Explosion 110/
tags:
- events
matches_json: [{"number": 1, "name": "Dragon Lee vs. Saburo Aoki Jr.", "finish": "Saburo Aoki Jr. beat Dragon Lee in 12 Min 3 Sec with a Diving Body Attack", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": "12:03"}, {"number": 2, "name": "Allen Hawkins & Zodiac vs. Santana Family", "finish": "Felix Santana Jr. beat Allen Hawkins in 18 Min 9 Sec with a Flying Rollup Pin", "rating_stars": "<span class=\"stars\">★★★</span>", "rating_num": 3, "time": "18:09"}, {"number": 3, "name": "Golden Grappler vs. Dynamite Smith", "finish": "Golden Grappler beat Dynamite Smith in 22 Min 33 Sec with a Piledriver", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "22:33"}, {"number": 4, "name": "Ox Hemlock vs. Misterio Guerrero", "finish": "Ox Hemlock beat Misterio Guerrero in 4 Min 46 Sec with an Elbow Drop Hold", "rating_stars": "<span class=\"stars\">★★</span>", "rating_num": 2, "time": "4:46"}, {"number": 5, "name": "PWA Jr. Heavyweight #1 Contender: Jushin Liger vs. Mark Erickson", "finish": "Jushin Liger beat Mark Erickson in 11 Min 44 Sec with a Shooting Star Press", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": "11:44"}]
---

# PWA Friday Explosion 110

<div class="event-header">
<div class="event-meta">
**Date:** 2018-11-02<br>
**Venue:** Syracuse, New York<br>
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