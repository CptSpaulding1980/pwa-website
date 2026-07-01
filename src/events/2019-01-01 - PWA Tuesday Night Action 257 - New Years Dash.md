---
layout: event.njk
title: PWA Tuesday Night Action 257 - New Years Dash
date: '2019-01-01'
venue: Hartford, Connecticut
location: ''
promotion: PWA
permalink: /events/2019-01-01 - PWA Tuesday Night Action 257 - New Years Dash/
tags:
- events
matches_json: [{"number": 1, "name": "Casper Winkel, Nigel Pendragon & Rick Banner vs. Chelsea Grin, Golden Grappler & Allen Hawkins", "finish": "Casper Winkel, Nigel Pendragon, & Rick Banner battled Chelsea Grin,  Golden Grappler, & Allen Hawkins to a  time limit draw", "rating_stars": "<span class=\"stars\">★★★</span>", "rating_num": 3, "time": ""}, {"number": 2, "name": "Royal Brawl Qualifiers: Skullface Killah vs. Jean Wilson", "finish": "Skullface Killah beat Jean Wilson in 13 Min 39 Sec with a Kill You Dead", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "13:39"}, {"number": 3, "name": "Royal Brawl Qualifiers: Lex Rider vs. Montgomery Hayes", "finish": "Lex Rider beat Montgomery Hayes in 10 Min 41 Sec with a Vaulting Frog Splash", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "10:41"}, {"number": 4, "name": "Royal Brawl Qualifiers: Avery Alexander vs. Felix Santana III", "finish": "Avery Alexander beat Felix Santana III in 11 Min 22 Sec with a Double Knee Stomach Crusher", "rating_stars": "<span class=\"stars\">★★½</span>", "rating_num": 2.5, "time": "11:22"}, {"number": 5, "name": "Royal Brawl Qualifiers: Blue Spider vs. Macho Especial", "finish": "Blue Spider beat Macho Especial in 16 Min 49 Sec with a Japanese Leg Roll Clutch", "rating_stars": "<span class=\"stars\">★★★★¾</span>", "rating_num": 4.75, "time": "16:49"}, {"number": 6, "name": "Royal Brawl Qualifiers: Ox Hemlock vs. Michael Elgin", "finish": "Michael Elgin beat Ox Hemlock in 13 Min 10 Sec with a Spiral Bomb", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": "13:10"}]
---

# PWA Tuesday Night Action 257 - New Years Dash

<div class="event-header">
<div class="event-meta">
**Date:** 2019-01-01<br>
**Venue:** Hartford, Connecticut<br>
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