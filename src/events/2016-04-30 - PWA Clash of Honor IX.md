---
layout: event.njk
title: PWA Clash of Honor IX
date: '2016-04-30'
venue: ''
location: ''
promotion: PWA
permalink: /events/2016-04-30 - PWA Clash of Honor IX/
tags:
- events
matches_json: [{"number": 1, "name": "Mike Hool & Snake King & Zodiac vs. Raven & Sabu & Too Cold Scorpio", "finish": "Mike Hool & Snake King & Zodiac beat Raven & Sabu & Too Cold Scorpio (King Knee Drop von Hool an Sabu (CRITICAL))", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": ""}, {"number": 2, "name": "Ultimo Dragon vs. Jushin Liger", "finish": "Jushin Liger beat Ultimo Dragon (Vert. Brainbuster)", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": ""}, {"number": 3, "name": "PWA World Tag Team Championship: Shredder & Delirious vs. Chris Hero & Claudio Castagnoli (c)", "finish": "Chris Hero & Claudio Castagnoli beat Shredder & Delirious (England Stretch (Hero an Delirious))", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": ""}, {"number": 4, "name": "Ray Stantz vs. Jean Wilson", "finish": "Jean Wilson beat Ray Stantz (Powerslam)", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": ""}, {"number": 5, "name": "Mask vs. Mask Match: Tri Clops vs. Mystery Panther", "finish": "Tri Clops beat Mystery Panther (Ankle Lock)", "rating_stars": "<span class=\"stars\">★★★★¾</span>", "rating_num": 4.75, "time": ""}, {"number": 6, "name": "PWA International Championship: Roadkill vs. Blue Spider (c)", "finish": "Roadkill beat Blue Spider (Gotch Piledriver)", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": ""}, {"number": 7, "name": "Last Man Standing Match: Blade vs. Fred Balentine", "finish": "Blade beat Fred Balentine (Tombstone Piledriver auf einen Stuhl)", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": ""}, {"number": 8, "name": "PWA World Heavyweight Championship: UK Kid vs. Lex Rider (c)", "finish": "Lex Rider beat UK Kid (Michinoku Driver II)", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": ""}]
---

# PWA Clash of Honor IX

<div class="event-header">
<div class="event-meta">
**Date:** 2016-04-30<br>
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