---
layout: event.njk
title: PWA Tuesday Night Action
date: '2017-05-09'
venue: ''
location: ''
promotion: PWA
permalink: /events/2017-05-09 - PWA Tuesday Night Action/
tags:
- events
matches_json: [{"number": 1, "name": "King of the Ring – First Round: Travis Banks vs. Cobra III", "finish": "Travis Banks beat Cobra III (Ki Crusher)", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": ""}, {"number": 2, "name": "PWA World Heavyweight Championship: Jack Swagger vs. Roadkill (c)", "finish": "Roadkill beat Jack Swagger (Flying Cross Body)", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": ""}, {"number": 3, "name": "King of the Ring – First Round: Michael Elgin vs. Jean Wilson", "finish": "Michael Elgin beat Jean Wilson (Death Valley Driver (CRITICAL))", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": ""}, {"number": 4, "name": "King of the Ring – First Round: Juice Robinson vs. Shredder", "finish": "Juice Robinson beat Shredder (Sunset Flip Powerbomb)", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": ""}, {"number": 5, "name": "King of the Ring – First Round: Kota Ibushi vs. Blue Spider", "finish": "Blue Spider beat Kota Ibushi (Small Package)", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": ""}, {"number": 6, "name": "Best 2 out of 3 Falls Match - PWA World Heavyweight Championship: Lex Rider vs. Roadkill (c)", "finish": "Lex Rider beat Roadkill (1:0 Anaconda Vise 14:12 1:1 Small Package 17:45 2:1 Frog Splash 20:15)", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": ""}]
---

# PWA Tuesday Night Action

<div class="event-header">
<div class="event-meta">
**Date:** 2017-05-09<br>
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