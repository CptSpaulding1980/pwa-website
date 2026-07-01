---
layout: event.njk
title: NJPW-PWA Collision 2016
date: '2016-06-19'
venue: ''
location: ''
promotion: PWA
permalink: /events/2016-06-19 - NJPW-PWA Collision 2016/
tags:
- events
matches_json: [{"number": 1, "name": "8 Man Tag Team Elimination Match: Slicer & Jitsu & Scott Norton & Big Strong Machine vs. Fred Balentine & Masahiro Chono & Koji Kanemoto & Masato Tanaka", "finish": "Fred Balentine & Masahiro Chono & Koji Kanemoto & Masato Tanaka beat Slicer & Jitsu & Scott Norton & Big Strong Machine (Ankle Lock (Kanemoto an Jitsu))", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": ""}, {"number": 2, "name": "Non Title Match: Hiroshi Tanahashi vs. Roadkill", "finish": "Hiroshi Tanahashi beat Roadkill (Powerbomb)", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": ""}, {"number": 3, "name": "Shinsuke Nakamura vs. Tri Clops", "finish": "Shinsuke Nakamura beat Tri Clops (Tiger Suplex)", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": ""}, {"number": 4, "name": "PWA World Heavyweight Championship: UK Kid vs. Lex Rider (c)", "finish": "Lex Rider beat UK Kid (Foothold Arm Hold)", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": ""}]
---

# NJPW-PWA Collision 2016

<div class="event-header">
<div class="event-meta">
**Date:** 2016-06-19<br>
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