---
layout: event.njk
title: PWA Clash of Honor X
date: '2017-04-01'
venue: ''
location: ''
promotion: PWA
permalink: /events/2017-04-01 - PWA Clash of Honor X/
tags:
- events
matches_json: [{"number": 1, "name": "Elimination Match - PWA Junior Heavyweight Championship: Blue Blazer Jr. vs. Dragon Kid vs. Mark Erickson vs. Jushin Liger vs. Katsuhiko Nakajima vs. KUSHIDA vs. Rey Mysterio vs. Tiger Mask IV (vacant)", "finish": "Blue Blazer won a Multi-Person-Match with a Sharpshooter on KUSHIDA", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": ""}, {"number": 2, "name": "Blade & Mike Hool & Snake King vs. Jean Wilson & Tatanka & The Patriot", "finish": "Blade & Mike Hool & Snake King beat Jean Wilson & Tatanka & The Patriot (Brain Claw (Blade an Tatanka))", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": ""}, {"number": 3, "name": "UK Kid vs. Tri Clops", "finish": "Tri Clops beat UK Kid (Ankle Lock)", "rating_stars": "<span class=\"stars\">★★★★½</span>", "rating_num": 4.5, "time": ""}, {"number": 4, "name": "PWA International Championship Tournament Final Match: Davey Boy Smith Jr. vs. Jitsu (vacant)", "finish": "Davey Boy Smith Jr. won (Screw Slam)", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": ""}, {"number": 5, "name": "Best 2 out of 3 Falls Match: Cody Rhodes vs. Fred Balentine", "finish": "Fred Balentine beat Cody Rhodes (1:0 Pulldown Face Buster 12:56 1:1 Leaping Cutter 17:21 1:2 Sledgehammer 18:05)", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": ""}, {"number": 6, "name": "PWA World Tag Team Championship: Davey Richards & Eddie Edwards vs. El Canek & Grizzlor (c)", "finish": "Davey Richards & Eddie Edwards beat El Canek & Grizzlor (Running High Knee (CRITICAL) (Edwards an Grizzlor))", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": ""}, {"number": 7, "name": "Alberto El Patron vs. Blue Spider", "finish": "Blue Spider beat Alberto El Patron (Roll Up (CRITICAL))", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": ""}, {"number": 8, "name": "PWA World Heavyweight Championship: Roadkill vs. Lex Rider (c)", "finish": "Roadkill beat Lex Rider (Road Diving Elbow Drop)", "rating_stars": "<span class=\"stars\">★★★★★</span>", "rating_num": 5, "time": ""}]
---

# PWA Clash of Honor X

<div class="event-header">
<div class="event-meta">
**Date:** 2017-04-01<br>
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