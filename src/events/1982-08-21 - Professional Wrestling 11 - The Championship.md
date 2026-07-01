---
layout: event.njk
title: Professional Wrestling 11 - The Championship
date: '1982-08-21'
venue: The Vault
location: Boston, MA
promotion: PWA
permalink: /events/1982-08-21 - Professional Wrestling 11 - The Championship/
tags:
- events
matches_json: [{"number": 1, "name": "CWC Light Heavyweight Championship: Steve Brockman vs. Tiger Mask (c)", "finish": "Tiger Mask beat Steve Brockman with a Vert German Suplex in 12 Min 11 Sec", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": "12:11"}, {"number": 2, "name": "PWA World Title Tournament: Dutch Leeman vs. Harley Race", "finish": "Harley Race beat Dutch Leeman with a Diving Headbutt in 13 Min 31 Sec", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": "13:31"}, {"number": 3, "name": "PWA World Title Tournament: Dos Caras vs. Mil Mascaras", "finish": "Mil Mascaras beat Dos Caras with a Flying Rollup Pin in 24 Min 56 Sec", "rating_stars": "<span class=\"stars\">★★★★½</span>", "rating_num": 4.5, "time": "24:56"}, {"number": 4, "name": "PWA World Title Tournament: Ric Flair vs. Ted DiBiase", "finish": "Ric Flair beat Ted DiBiase via Count Out in 9 Min 41 Sec", "rating_stars": "<span class=\"stars\">★★★</span>", "rating_num": 3, "time": "9:41"}, {"number": 5, "name": "PWA World Title Tournament: Jack Brisco vs. Rocky Wilbur", "finish": "Rocky Wilbur beat Jack Brisco with a an European Side Headlock in 14 Min 2 Sec", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": "14:02"}, {"number": 6, "name": "PWA World Title Tournament:  Johnny Effigy vs. Nick Bockwinkel", "finish": "Nick Bockwinkel beat Johnny Effigy with a Piledriver in 15 Min 34 Sec", "rating_stars": "<span class=\"stars\">★★★</span>", "rating_num": 3, "time": "15:34"}, {"number": 7, "name": "PWA World Title Tournament: El Canek vs. Paullus the Colossus", "finish": "Paullus the Colossus beat El Canek via DQ in 11 Min 37 Sec", "rating_stars": "<span class=\"stars\">★★★</span>", "rating_num": 3, "time": "11:37"}, {"number": 8, "name": "PWA World Title Tournament: Dory Funk Jr. vs. Felix Santana", "finish": "Dory Funk Jr. beat Felix Santana with a Spinning Toe Hold in 10 Min 43 Sec", "rating_stars": "<span class=\"stars\">★★★</span>", "rating_num": 3, "time": "10:43"}, {"number": 9, "name": "PWA World Title Tournament: Buddy Yorke vs. The Destroyer", "finish": "The Destroyer beat Buddy Yorke with a Lariat in 22 Min 18 Sec", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": "22:18"}]
---

# Professional Wrestling 11 - The Championship

<div class="event-header">
<div class="event-meta">
**Date:** 1982-08-21<br>
**Venue:** The Vault<br>
**Location:** Boston, MA
</div>
<img src="/pwa-website/img/posters/1982-08-21 - Professional Wrestling 11 - The Championship.png" class="event-poster" alt="Poster">
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