---
layout: event.njk
title: PWA Royal Brawl 2018
date: '2018-01-13'
venue: ''
location: ''
promotion: PWA
permalink: /events/2018-01-13 - PWA Royal Brawl 2018/
tags:
- events
matches_json: [{"number": 1, "name": "PWA Junior Heavyweight Championship: Blue Blazer Jr. vs. Mystery Panther (c)", "finish": "Mystery Panther beat Blue Blazer Jr. (Huracanrana)", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": ""}, {"number": 2, "name": "PWA World Tag Team Championship: British Strong Style (Pete Dunne & Tyler Bate) vs. Ringkampf (Timothy Thatcher & WALTER) (c)", "finish": "Ringkampf (Timothy Thatcher & WALTER) beat British Strong Style (Pete Dunne & Tyler Bate) (Lariat (WALTER an Tyler Bate) (CRITICAL))", "rating_stars": "<span class=\"stars\">★★★★½</span>", "rating_num": 4.5, "time": ""}, {"number": 3, "name": "PWA International Championship: Big Dragon vs. Montgomery Hayes (c)", "finish": "Big Dragon beat Montgomery Hayes (Scissors Body Attack)", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": ""}, {"number": 4, "name": "PWA World Heavyweight Championship: Keith Owens vs. Roadkill (c)", "finish": "Roadkill beat Keith Owens (Road Diving Elbow Drop)", "rating_stars": "<span class=\"stars\">★★★★½</span>", "rating_num": 4.5, "time": ""}, {"number": 5, "name": "PWA World Title #1 Contender Battle Royal", "finish": "Rey Mysterio Jr. win the  Royal Brawl in 58 Min 13 Sec by eliminating Ox Hemlock to become the last remaining Wrestler", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": "58:13"}]
---

# PWA Royal Brawl 2018

<div class="event-header">
<div class="event-meta">
**Date:** 2018-01-13<br>
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