---
layout: event.njk
title: PWA Tuesday Night Action 249 - Road to celebration
date: '2018-10-30'
venue: East Rutherford, New Jersey
location: ''
promotion: PWA
permalink: /events/2018-10-30 - PWA Tuesday Night Action 249 - Road to celebration/
tags:
- events
matches_json: [{"number": 1, "name": "Brutes vs. Misterio Guerrero & Theobold Lovecraft", "finish": "Jack Fury beat Misterio Guerrero in 22 Min 50 Sec with a Scissors Texas Clover Clutch", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": "22:50"}, {"number": 2, "name": "Timothy Thatcher, Veit Müller & WALTER vs. Avery Alexander, Poppa Thurgoode & Red Dragon", "finish": "Red Dragon beat Timothy Thatcher in 19 Min 21 Sec with a K.O", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": "19:21"}, {"number": 3, "name": "El Canek vs. Diablo Blanco", "finish": "Diablo Blanco beat El Canek in 26 Min 47 Sec with a Skull End", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": "26:47"}, {"number": 4, "name": "Keith Rowans vs. Tri Clops", "finish": "Keith Rowans beat Tri Clops in 11 Min 38 Sec with a Rapid Double Arm Suplex", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": "11:38"}, {"number": 5, "name": "PWA World Heavyweight Title #1 Contender: UK Kid vs. Zack Sabre Jr. vs. PAC vs. Roadkill", "finish": "UK Kid beats Zack Sabre Jr. & PAC & Roadkill", "rating_stars": "<span class=\"stars\">★★★★¾</span>", "rating_num": 4.75, "time": ""}]
---

# PWA Tuesday Night Action 249 - Road to celebration

<div class="event-header">
<div class="event-meta">
**Date:** 2018-10-30<br>
**Venue:** East Rutherford, New Jersey<br>
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