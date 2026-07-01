---
layout: event.njk
title: Professional Wrestling 24
date: '1995-08-02'
venue: ''
location: ''
promotion: PWA
permalink: /events/1995-08-02 - Professional Wrestling 24/
tags:
- events
matches_json: [{"number": 1, "name": "PWA World Heavyweight Championship:  Yokosumo Kawashi vs. Blue Spider (c)", "finish": "Yokosumo Kawashi beat Blue Spider with a Leg Drop", "rating_stars": "<span class=\"stars\">★★★</span>", "rating_num": 3, "time": ""}]
---

# Professional Wrestling 24

<div class="event-header">
<div class="event-meta">
**Date:** 1995-08-02<br>
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