---
layout: event.njk
title: PWA Royal Brawl 2017
date: '2017-01-21'
venue: ''
location: ''
promotion: PWA
permalink: /events/2017-01-21 - PWA Royal Brawl 2017/
tags:
- events
matches_json: [{"number": 1, "name": "PWA World Tag Team Championship Match: Davey Richards & Eddie Edwards vs. Grizzlor & El Canek (vacant)", "finish": "Grizzlor & El Canek beat Davey Richards & Eddie Edwards (Grizzlor pinnte Edwards nach einem Zusammenprall von El Canek mit diesem)", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": ""}, {"number": 2, "name": "UK Kid vs. The Patriot", "finish": "UK Kid beat The Patriot (Tombstone Piledriver)", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": ""}, {"number": 3, "name": "PWA International Championship: Zodiac vs. Roadkill (c)", "finish": "Roadkill beat Zodiac (Road Diving Elbow Drop)", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": ""}, {"number": 4, "name": "Triple Threat Match - PWA World Heavyweight Championship: Blade vs. Jean Wilson vs. Lex Rider (c)", "finish": "Lex Rider beat Blade witha a Frog Splash to win a Triple Threat Match", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": ""}, {"number": 5, "name": "PWA World Title #1 Contender Battle Royal", "finish": "Roadkill won the Royal Brawl Match - Eliminations: 1. Mark Erickson by Roadkill (08:41) 2. Snake King by Jitsu (12:50) 3. M. Elgin by Blue Spider (16:39) 4. Jitsu by Blue Spider (17:08) 5. Blue Spider by Alberto (21:28) 6. Alberto by Tri Clops (22:58) 7. Tri Clops by Roadkill (22:58))", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": ""}]
---

# PWA Royal Brawl 2017

<div class="event-header">
<div class="event-meta">
**Date:** 2017-01-21<br>
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