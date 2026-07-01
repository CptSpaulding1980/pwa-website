---
layout: event.njk
title: PWA King of the Ring 2019
date: '2019-05-19'
venue: PWA Capcom Arena
location: Boston, Massachusetts, USA
promotion: PWA
permalink: /events/2019-05-19 - PWA King of the Ring 2019/
tags:
- events
matches_json: [{"number": 1, "name": "MexiSquad (Bandido, Flamita & Rey Horus) vs. Veteran Veteran Devastators (Blazer jr., Tiziano & Bergeron) ", "finish": "Mackenzie Bergeron beat Bandido in 14 Min 0 Sec with a Heel Hold", "rating_stars": "<span class=\"stars\">★★½</span>", "rating_num": 2.5, "time": "14:00"}, {"number": 2, "name": "KotR Quarter Finals: Mr. Suplex vs. Ricklon Smasher", "finish": "Mr. Suplex beat Ricklon Smasher in 5 Min 8 Sec with a Genki Raiga-plex", "rating_stars": "<span class=\"stars\">★★</span>", "rating_num": 2, "time": "5:08"}, {"number": 3, "name": "KotR Quarter Finals: Red Dragon vs. Salvador Sosa", "finish": "Salvador Sosa beat Red Dragon in 11 Min 18 Sec with a Reverse Drop Face Buster", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": "11:18"}, {"number": 4, "name": "KotR Quarter Finals: WALTER vs. Rick Banner", "finish": "Rick Banner beat WALTER in 13 Min 5 Sec with a Chickenwing Facelock", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "13:05"}, {"number": 5, "name": "KotR Quarter Finals: Shingo Takagi vs. Blue Spider", "finish": "Blue Spider beat Shingo Takagi in 13 Min 59 Sec with a Hip Toss", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "13:59"}, {"number": 6, "name": "KotR Semi Finals: Mr. Suplex vs. Salvador Sosa", "finish": "Mr. Suplex beat Salvador Sosa in 12 Min 39 Sec with a Genki Raiga-plex", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": "12:39"}, {"number": 7, "name": "KotR Semi Finals: Rick Banner vs. Blue Spider", "finish": "Rick Banner beat Blue Spider in 11 Min 0 Sec with a Cross Arm Fire Powerbomb", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": "11:00"}, {"number": 8, "name": "PWA International #1 Contendership: Avery Alexander vs. Roadkill", "finish": "Roadkill beat Avery Alexander in 9 Min 1 Sec with an Appeal Diving Elbowdrop", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "9:01"}, {"number": 9, "name": "KotR Final: Mr. Suplex vs. Rick Banner", "finish": "Mr. Suplex beat Rick Banner in 4 Min 13 Sec with a Top Rope German Suplex", "rating_stars": "<span class=\"stars\">★★</span>", "rating_num": 2, "time": "4:13"}, {"number": 10, "name": "Street Fight - PWA World Heavyweight Championship: Ox Hemlock vs. Lex Rider (vacant)", "finish": "Lex Rider beat Ox Hemlock in 9 Min 7 Sec with a Vaulting Frog Splash", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": "9:07"}]
---

# PWA King of the Ring 2019

<div class="event-header">
<div class="event-meta">
**Date:** 2019-05-19<br>
**Venue:** PWA Capcom Arena<br>
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