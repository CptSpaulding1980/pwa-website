---
layout: event.njk
title: PWA Tuesday Night Action 251 - Kid is in the Block
date: '2018-11-13'
venue: Chicago, Illinois
location: ''
promotion: PWA
permalink: /events/2018-11-13 - PWA Tuesday Night Action 251 - Kid is in the Block/
tags:
- events
matches_json: [{"number": 1, "name": "Dynamite Smith vs. Avery Alexander", "finish": "Avery Alexander beat Dynamite Smith in 13 Min 15 Sec with a Double Knee Stomach Crusher", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": "13:15"}, {"number": 2, "name": "Dragon Lee vs. Felix Santana Jr.", "finish": "Felix Santana Jr. beat Dragon Lee in 8 Min 13 Sec with a La Esparda", "rating_stars": "<span class=\"stars\">★★½</span>", "rating_num": 2.5, "time": "8:13"}, {"number": 3, "name": "Rick Banner vs. Misterio Guerrero", "finish": "Misterio Guerrero beat Rick Banner in 23 Min 35 Sec with a Mystery Splash", "rating_stars": "<span class=\"stars\">★★★★½</span>", "rating_num": 4.5, "time": "23:35"}, {"number": 4, "name": "Montgomery Hayes, Blue Blazer Jr. & Keith Rowans vs. Tri Clops, Zack Sabre Jr. & Lex Rider", "finish": "Montgomery Hayes beat Tri Clops in 24 Min 6 Sec with a K.O", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": "24:06"}, {"number": 5, "name": "El Experto vs. Roadkill", "finish": "El Experto beat Roadkill in 22 Min 14 Sec with an Agarre Perfecto", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "22:14"}]
---

# PWA Tuesday Night Action 251 - Kid is in the Block

<div class="event-header">
<div class="event-meta">
**Date:** 2018-11-13<br>
**Venue:** Chicago, Illinois<br>
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