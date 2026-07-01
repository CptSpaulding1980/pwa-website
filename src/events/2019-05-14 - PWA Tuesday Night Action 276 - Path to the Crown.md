---
layout: event.njk
title: PWA Tuesday Night Action 276 - Path to the Crown
date: '2019-05-14'
venue: PWA Capcom Arena
location: Boston, Massachusetts, USA
promotion: PWA
permalink: /events/2019-05-14 - PWA Tuesday Night Action 276 - Path to the Crown/
tags:
- events
matches_json: [{"number": 1, "name": "Puma King & Laredo Kid vs. Dynamite Smith & Mark Erickson", "finish": "Mark Erickson beat Laredo Kid in 18 Min 1 Sec with a Firebird Splash", "rating_stars": "<span class=\"stars\">★★★★½</span>", "rating_num": 4.5, "time": "18:01"}, {"number": 2, "name": "Chelsea Grin vs. Felix Santana Jr. vs. Saburo Aoki Jr.", "finish": "Saburo Aoki Jr. won a triple threat match against Chelsea Grin & Felix Santana Jr. in  25:14", "rating_stars": "<span class=\"stars\">★★★★¾</span>", "rating_num": 4.75, "time": ""}, {"number": 3, "name": "KotR Qualifying: Avery Alexander vs. Rick Banner", "finish": "Rick Banner beat Avery Alexander in 18 Min 53 Sec with an Original Backdrop", "rating_stars": "<span class=\"stars\">★★★★½</span>", "rating_num": 4.5, "time": "18:53"}, {"number": 4, "name": "KotR Qualifying: WALTER vs. Chris Hero", "finish": "WALTER beat Chris Hero in 15 Min 45 Sec with a Body Choke Sleeper", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": "15:45"}, {"number": 5, "name": "KotR Qualifying: Bandido vs. Blue Spider", "finish": "Blue Spider beat Bandido in 6 Min 10 Sec with an Uproot German Suplex", "rating_stars": "<span class=\"stars\">DUD</span>", "rating_num": 0, "time": "6:10"}, {"number": 6, "name": "KotR Qualifying: Diablo Blanco vs. Shingo Takagi", "finish": "Shingo Takagi beat Diablo Blanco in 13 Min 51 Sec with a Last of the Dragon", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": "13:51"}]
---

# PWA Tuesday Night Action 276 - Path to the Crown

<div class="event-header">
<div class="event-meta">
**Date:** 2019-05-14<br>
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