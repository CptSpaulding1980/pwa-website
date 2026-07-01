---
layout: event.njk
title: Pro Wrestling ZERO1
date: '2016-06-17'
venue: ''
location: ''
promotion: PWA
permalink: /events/2016-06-17 - Pro Wrestling ZERO1/
tags:
- events
matches_json: [{"number": 1, "name": "Tri Clops vs. Daisuke Sekimoto", "finish": "Tri Clops beat Daisuke Sekimoto (Ankle Lock)", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": ""}]
---

# Pro Wrestling ZERO1

<div class="event-header">
<div class="event-meta">
**Date:** 2016-06-17<br>
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