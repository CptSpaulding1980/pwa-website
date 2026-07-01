---
layout: event.njk
title: PWA Power Hour 11
date: '2019-04-18'
venue: PWA Power Studio
location: Boston, Massachusetts, USA
promotion: PWA
permalink: /events/2019-04-18 - PWA Power Hour 11/
tags:
- events
matches_json: [{"number": 1, "name": "Mr. Suplex vs. Mark Erickson", "finish": "Mr. Suplex beat Mark Erickson in 12 Min 52 Sec with a Genki Raiga-plex", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": "12:52"}, {"number": 2, "name": "Hiroto Nakamichi vs. Spitfire", "finish": "Hiroto Nakamichi beat Spitfire in 13 Min 13 Sec with a Foot Stunner", "rating_stars": "<span class=\"stars\">★★★</span>", "rating_num": 3, "time": "13:13"}, {"number": 3, "name": "Brutes vs. Santana Family", "finish": "Skullface Killah beat Felix Santana Jr. in 2 Min 43 Sec with a RING OUT", "rating_stars": "<span class=\"stars\">DUD</span>", "rating_num": 0, "time": "2:43"}]
---

# PWA Power Hour 11

<div class="event-header">
<div class="event-meta">
**Date:** 2019-04-18<br>
**Venue:** PWA Power Studio<br>
**Location:** Boston, Massachusetts, USA
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