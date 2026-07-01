---
layout: event.njk
title: PWA Tuesday Night Action 263 - Trait the Traitor
date: '2019-02-12'
venue: DCU Center
location: Worcester, Massachusetts, USA
promotion: PWA
permalink: /events/2019-02-12 - PWA Tuesday Night Action 263 - Trait the Traitor/
tags:
- events
matches_json: [{"number": 1, "name": "World Title #1 Contendership on the Line: Saburo Aoki Jr. vs. Rick Banner", "finish": "Rick Banner beat Saburo Aoki Jr. in 11 Min 29 Sec with a Backslide", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": "11:29"}, {"number": 2, "name": "Rampage Rage vs. Ricklon Smasher", "finish": "Rampage Rage beat Ricklon Smasher in 7 Min 25 Sec with a Back Hook-Leg Pinfall", "rating_stars": "<span class=\"stars\">★½</span>", "rating_num": 1.5, "time": "7:25"}, {"number": 3, "name": "The Blake Twins vs. Mysterious Fantasticos", "finish": "Sammy Blake beat Mystery Panther in 21 Min 43 Sec with an Octopus Hold", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": "21:43"}, {"number": 4, "name": "Keith Rowans vs. Julio Rivera", "finish": "Keith Rowans beat Julio Rivera in 19 Min 34 Sec with a Jumping Pile Driver", "rating_stars": "<span class=\"stars\">★★★★½</span>", "rating_num": 4.5, "time": "19:34"}, {"number": 5, "name": "Non Title Match: Timothy Thatcher vs. UK Kid", "finish": "UK Kid beat Timothy Thatcher in 5 Min 34 Sec with a Vert German Suplex", "rating_stars": "<span class=\"stars\">★</span>", "rating_num": 1, "time": "5:34"}]
---

# PWA Tuesday Night Action 263 - Trait the Traitor

<div class="event-header">
<div class="event-meta">
**Date:** 2019-02-12<br>
**Venue:** DCU Center<br>
**Location:** Worcester, Massachusetts, USA
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