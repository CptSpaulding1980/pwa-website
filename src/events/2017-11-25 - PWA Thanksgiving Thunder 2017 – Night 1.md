---
layout: event.njk
title: PWA Thanksgiving Thunder 2017 – Night 1
date: '2017-11-25'
venue: ''
location: ''
promotion: PWA
permalink: /events/2017-11-25 - PWA Thanksgiving Thunder 2017 – Night 1/
tags:
- events
matches_json: [{"number": 1, "name": "Blue Blazer Jr. & UK Kid vs. Fantasio Fantastico & Mystery Panther", "finish": "Blue Blazer Jr. & UK Kid beat Fantasio Fantastico & Mystery Panther (Vert. Brainbuster (UK Kid an Fantastico))", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": ""}, {"number": 2, "name": "Golden Grappler vs. Macho Especial", "finish": "Golden Grappler beat Macho Especial (Piledriver)", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": ""}, {"number": 3, "name": "PWA International Championship: Montgomery Hayes vs. Dalton Castle (c)", "finish": "Montgomery Hayes beat Dalton Castle (Uproot Backdrop)", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": ""}, {"number": 4, "name": "Marty Scurll vs. Tri Clops", "finish": "Tri Clops beat Marty Scurll (Ankle Lock)", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": ""}, {"number": 5, "name": "PWA World Tag Team Championship: Ringkampf (Timothy Thatcher & WALTER) vs. The Young Bucks (Matt Jackson & Nick Jackson) (c)", "finish": "Ringkampf (Timothy Thatcher & WALTER) beat The Young Bucks (Matt Jackson & Nick Jackson) (Striking Lariat (WALTER an Matt Jackson))", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": ""}, {"number": 6, "name": "Hiroto Nakamichi & Minoru Suzuki & Yokosumo Kawashi vs. Fabrizio Tiziano & Mark Erickson & Roadkill", "finish": "Draw (Double K.O. Kawashi and Mark Erickson)", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": ""}, {"number": 7, "name": "Kenny Omega vs. Blue Spider", "finish": "Blue Spider beat Kenny Omega (La Magistral (CRITICAL))", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": ""}]
---

# PWA Thanksgiving Thunder 2017 – Night 1

<div class="event-header">
<div class="event-meta">
**Date:** 2017-11-25<br>
**Venue:** <br>
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