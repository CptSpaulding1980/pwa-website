---
layout: event.njk
title: PWA Counter Blast
date: '2019-05-05'
venue: PWA Capcom Arena
location: Boston, Massachusetts, USA
promotion: PWA
permalink: /events/2019-05-05 - PWA Counter Blast/
tags:
- events
matches_json: [{"number": 1, "name": "Triple Threat Match - PWA World Tag Team Championship: Blake Twins vs. Masked Lucha Alliance vs. Brutes (c)", "finish": "Macho Especial won a six-pack scramble match against Elias Blake, Sammy Blake, Mike Hool, Rampage Rage, &Cobra III in  13:14", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": ""}, {"number": 2, "name": "Extreme Rules - Falls Count Anywhere: Allen Hawkins vs. Saburo Aoki Jr.", "finish": "Saburo Aoki Jr. beat Allen Hawkins in 10 Min 58 Sec with an El Es Culero", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": "10:58"}, {"number": 3, "name": "Avery Alexander vs. Roadkill", "finish": "Roadkill beat Avery Alexander in 20 Min 54 Sec with a Mexican Stretch", "rating_stars": "<span class=\"stars\">★★★★¾</span>", "rating_num": 4.75, "time": "20:54"}, {"number": 4, "name": "PWA Junior Heavyweight Championship: Keith Rowans vs. Blue Blazer Jr. (c)", "finish": "Blue Blazer Jr. beat Keith Rowans in 10 Min 3 Sec with a Moonsault Press", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": "10:03"}, {"number": 5, "name": "Imperium vs. Chris Hero & Fred Balentine", "finish": "Imperium battled Chris Hero & Fred Balentine to a  time limit draw", "rating_stars": "<span class=\"stars\">★★★★¾</span>", "rating_num": 4.75, "time": ""}, {"number": 6, "name": "World Title Tournament League - Finals: Ox Hemlock vs. Lex Rider (vacant)", "finish": "Lex Rider beat Ox Hemlock in 12 Min 21 Sec with a DQ", "rating_stars": "<span class=\"stars\">★★</span>", "rating_num": 2, "time": "12:21"}]
---

# PWA Counter Blast

<div class="event-header">
<div class="event-meta">
**Date:** 2019-05-05<br>
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