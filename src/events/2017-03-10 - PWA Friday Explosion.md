---
layout: event.njk
title: PWA Friday Explosion
date: '2017-03-10'
venue: ''
location: ''
promotion: PWA
permalink: /events/2017-03-10 - PWA Friday Explosion/
tags:
- events
matches_json: [{"number": 1, "name": "PWA Junior Heavyweight Title Qualifying: Naomichi Marufuji vs. Mark Erickson", "finish": "Mark Erickson beat Naomichi Marufuji (Crossface)", "rating_stars": "<span class=\"stars\">★★★★½</span>", "rating_num": 4.5, "time": ""}, {"number": 2, "name": "PWA Junior Heavyweight Title Qualifying: Will Ospreay vs. Blue Blazer Jr.", "finish": "Blue Blazer Jr. beat Will Ospreay (Sharsphooter)", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": ""}, {"number": 3, "name": "PWA Junior Heavyweight Title Qualifying: Pete Dunne vs. Blue Spider", "finish": "Pete Dunne beat Blue Spider (Tigerdriver)", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": ""}, {"number": 4, "name": "PWA Junior Heavyweight Title Qualifying: Jushin Liger vs. Mystery Panther", "finish": "Jushin Liger beat Mystery Panther (Original Jumping Bomb)", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": ""}, {"number": 5, "name": "Cody Rhodes vs. Fred Balentine", "finish": "Cody Rhodes beat Fred Balentine (Standing Moonsault)", "rating_stars": "<span class=\"stars\">★★★★¾</span>", "rating_num": 4.75, "time": ""}]
---

# PWA Friday Explosion

<div class="event-header">
<div class="event-meta">
**Date:** 2017-03-10<br>
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