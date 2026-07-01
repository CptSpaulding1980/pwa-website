---
layout: event.njk
title: PWA Thanksgiving Thunder 2018 - Night 1
date: '2018-11-25'
venue: East Rutherford, New Jersey
location: ''
promotion: PWA
permalink: /events/2018-11-25 - PWA Thanksgiving Thunder 2018 - Night 1/
tags:
- events
matches_json: [{"number": 1, "name": "Allen Hawkins, Golden Grappler, Ox Hemlock & Zodiac vs. Felix Santana Jr., Felix Santana III, Fantasio Fantastico & Mystery Panther", "finish": "Felix Santana III beat Golden Grappler in 25 Min 33 Sec with a Diving Lariat", "rating_stars": "<span class=\"stars\">★★★★½</span>", "rating_num": 4.5, "time": "25:33"}, {"number": 2, "name": "PWA Junior Heavyweight Championship: Avery Alexander vs. Jushin Liger (c)", "finish": "Avery Alexander beat Jushin Liger in 17 Min 5 Sec with an Arm Slam", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "17:05"}, {"number": 3, "name": "Dynamite Smith vs. Red Dragon", "finish": "Red Dragon beat Dynamite Smith in 16 Min 8 Sec with a Front Dropkick", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "16:08"}, {"number": 4, "name": "PWA World Tag Team Championship: Brutes vs. Ringkampf (c)", "finish": "Mike Hool beat WALTER in 19 Min 50 Sec with a Chest Slap", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": "19:50"}, {"number": 5, "name": "Diablo Blanco vs. Blue Spider", "finish": "Diablo Blanco beat Blue Spider in 12 Min 17 Sec with a Skull End", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": "12:17"}, {"number": 6, "name": "PWA International Championship: Zack Sabre Jr. vs. Lex Rider (c)", "finish": "Lex Rider beat Zack Sabre Jr. in 13 Min 33 Sec with a Jumping Elbow", "rating_stars": "<span class=\"stars\">★★★</span>", "rating_num": 3, "time": "13:33"}]
---

# PWA Thanksgiving Thunder 2018 - Night 1

<div class="event-header">
<div class="event-meta">
**Date:** 2018-11-25<br>
**Venue:** East Rutherford, New Jersey<br>
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