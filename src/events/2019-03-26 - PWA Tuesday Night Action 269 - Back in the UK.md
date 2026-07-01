---
layout: event.njk
title: PWA Tuesday Night Action 269 - Back in the UK
date: '2019-03-26'
venue: Empress Ballroom
location: London, England, UK
promotion: PWA
permalink: /events/2019-03-26 - PWA Tuesday Night Action 269 - Back in the UK/
tags:
- events
matches_json: [{"number": 1, "name": "Veteran Veteran Devastators vs. Moustache Mountain", "finish": "Tyler Bate beat Blue Blazer Jr. in 18 Min 0 Sec with a Firebird Splash", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "18:00"}, {"number": 2, "name": "Red Dragon vs. Trevor Murdoch", "finish": "Red Dragon battled Trevor Murdoch to a  time limit draw", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": ""}, {"number": 3, "name": "Hiroto Nakamichi vs. Timothy Thatcher", "finish": "Hiroto Nakamichi beat Timothy Thatcher in 12 Min 35 Sec with a Rising Sun Stretch", "rating_stars": "<span class=\"stars\">★★½</span>", "rating_num": 2.5, "time": "12:35"}, {"number": 4, "name": "Los Rudos Diablos, Allen Hawkins & Golden Grappler vs. Masked Lucha Alliance", "finish": "Cobra III beat Diablo Blanco in 40 Min 15 Sec with a Headbutt", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": "40:15"}, {"number": 5, "name": "PWA International Championship: Tri Clops vs. WALTER (c)", "finish": "WALTER beat Tri Clops in 12 Min 51 Sec with a Boston Crab", "rating_stars": "<span class=\"stars\">★★½</span>", "rating_num": 2.5, "time": "12:51"}, {"number": 6, "name": "Non Title Match: Will Ospreay vs. UK Kid", "finish": "UK Kid beat Will Ospreay in 14 Min 0 Sec with a Camel Clutch", "rating_stars": "<span class=\"stars\">★★★</span>", "rating_num": 3, "time": "14:00"}]
---

# PWA Tuesday Night Action 269 - Back in the UK

<div class="event-header">
<div class="event-meta">
**Date:** 2019-03-26<br>
**Venue:** Empress Ballroom<br>
**Location:** London, England, UK
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