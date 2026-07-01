---
layout: event.njk
title: PWA Tuesday Night Action 258 - Glory by the Royals
date: '2019-01-08'
venue: Syracuse, New York
location: ''
promotion: PWA
permalink: /events/2019-01-08 - PWA Tuesday Night Action 258 - Glory by the Royals/
tags:
- events
matches_json: [{"number": 1, "name": "Mackenzie Bergeron vs. Mark Erickson", "finish": "Mark Erickson beat Mackenzie Bergeron in 13 Min 31 Sec with a Firebird Splash", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": "13:31"}, {"number": 2, "name": "Royal Brawl Qualifiers: Red Dragon vs. Nigel Pendragon", "finish": "Red Dragon battled Nigel Pendragon to a  time limit draw", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": ""}, {"number": 3, "name": "Michael Elgin vs. Hiroto Nakamichi", "finish": "Hiroto Nakamichi beat Michael Elgin in 14 Min 31 Sec with a Rising Sun Stretch", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": "14:31"}, {"number": 4, "name": "Royal Brawl Qualifiers: El Experto vs. Cobra III", "finish": "Cobra III beat El Experto in 14 Min 39 Sec with a Diving Body Press", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": "14:39"}, {"number": 5, "name": "Royal Brawl Qualifiers: Keith Rowans vs. Ricklon Smasher", "finish": "Keith Rowans beat Ricklon Smasher in 19 Min 48 Sec with a German Suplex", "rating_stars": "<span class=\"stars\">★★★★¾</span>", "rating_num": 4.75, "time": "19:48"}, {"number": 6, "name": "PWA Junior Heavyweight Championship: Avery Alexander vs. Felix Santana Jr. (c)", "finish": "Avery Alexander battled Felix Santana Jr. to a  double KO draw", "rating_stars": "<span class=\"stars\">★★</span>", "rating_num": 2, "time": ""}]
---

# PWA Tuesday Night Action 258 - Glory by the Royals

<div class="event-header">
<div class="event-meta">
**Date:** 2019-01-08<br>
**Venue:** Syracuse, New York<br>
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