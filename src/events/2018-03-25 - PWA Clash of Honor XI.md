---
layout: event.njk
title: PWA Clash of Honor XI
date: '2018-03-25'
venue: ''
location: ''
promotion: PWA
permalink: /events/2018-03-25 - PWA Clash of Honor XI/
tags:
- events
matches_json: [{"number": 1, "name": "PWA Junior Heavyweight Championship: Fantasio Fantastico vs. Mystery Panther (c)", "finish": "Fantasio Fantastico beat Mystery Panther (Sickle Hold)", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": ""}, {"number": 2, "name": "Blade vs. Snake King", "finish": "Snake King beat Blade (K.O. nach Rolling Fist Kombi.)", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": ""}, {"number": 3, "name": "PWA World Tag Team Championship: British Strong Style (Pete Dunne & Trent Seven) vs. Ringkampf (Timothy Thatcher & WALTER) (c)", "finish": "Draw (Time Limit Draw)", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": ""}, {"number": 4, "name": "Mask vs. Mask Match: Diablo Blanco vs. Tri Clops", "finish": "Diablo Blanco won (Diablo Triangle Lancer)", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": ""}, {"number": 5, "name": "Blue Blazer Jr. & Keith Owens & Montgomery Hayes & UK Kid vs. Cobra & Cobra III & El Canek & Macho Especial", "finish": "Blue Blazer Jr. & Keith Owens & Montgomery Hayes & UK Kid beat Cobra & Cobra III & El Canek & Macho Especial (Uproot Backdrop (Montgomery Hayes an Macho Especial))", "rating_stars": "<span class=\"stars\">★★★★½</span>", "rating_num": 4.5, "time": ""}, {"number": 6, "name": "No Disqualification Triple Threat Match: Kenny Omega vs. Blue Spider vs. Lex Rider", "finish": "Lex Rider won a Triple Threat Match with a Scissors Front Necklock on Kenny Omega", "rating_stars": "<span class=\"stars\">★★★★¾</span>", "rating_num": 4.75, "time": ""}, {"number": 7, "name": "Career vs. Title Match - PWA International Championship: Big Dragon vs. Ox Hemlock (c)", "finish": "Ox Hemlock beat Big Dragon (Sternness Dust und Elbow Drop Hold)", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": ""}, {"number": 8, "name": "60 Minute Iron Man Match- PWA World Heavyweight Championship: Zack Sabre Jr. vs. Roadkill (c)", "finish": "Zack Sabre Jr. beat Roadkill (7:2 Falls)", "rating_stars": "<span class=\"stars\">★★★★½</span>", "rating_num": 4.5, "time": ""}]
---

# PWA Clash of Honor XI

<div class="event-header">
<div class="event-meta">
**Date:** 2018-03-25<br>
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