---
layout: event.njk
title: Professional Wrestling 12 - The Championship 2
date: '1982-08-27'
venue: Korakuen Hall
location: Tokyo, Japan
promotion: PWA
permalink: /events/1982-08-27 - Professional Wrestling 12 - The Championship 2/
tags:
- events
matches_json: [{"number": 1, "name": "PWA World Title Tournament: Quarter Finals - Mil Mascaras vs. Harley Race", "finish": "Mil Mascaras beat Harley Race via DQ in 7 Min 40 Sec", "rating_stars": "<span class=\"stars\">★★</span>", "rating_num": 2, "time": "7:40"}, {"number": 2, "name": "PWA World Title Tournament: Quarter Finals - Rocky Wilbur vs. Ric Flair", "finish": "Rocky Wilbur beat Ric Flair with a Chickenwing Facelock in 32 Min 31 Sec", "rating_stars": "<span class=\"stars\">★★★★¾</span>", "rating_num": 4.75, "time": "32:31"}, {"number": 3, "name": "PWA World Title Tournament:  Quarter Finals - Nick Bockwinkel vs. Paullus the Colossus", "finish": "Nick Bockwinkel beat Paullus the Colossus via DQ in 15 Min 34 Sec", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": "15:34"}, {"number": 4, "name": "PWA World Title Tournament: Quarter Finals - The Destroyer vs. Dory Funk Jr.", "finish": "The Destroyer battled Dory Funk Jr. to a Double Countout in 14 Min. 45 Sec", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": ""}]
---

# Professional Wrestling 12 - The Championship 2

<div class="event-header">
<div class="event-meta">
**Date:** 1982-08-27<br>
**Venue:** Korakuen Hall<br>
**Location:** Tokyo, Japan
</div>
<img src="/pwa-website/img/posters/1982-08-27 - Professional Wrestling 12 - The Championship 2.png" class="event-poster" alt="Poster">
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