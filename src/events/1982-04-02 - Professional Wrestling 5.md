---
layout: event.njk
title: Professional Wrestling 5
date: '1982-04-02'
venue: The Vault
location: Boston, MA
promotion: PWA
permalink: /events/1982-04-02 - Professional Wrestling 5/
tags:
- events
matches_json: [{"number": 1, "name": "Bud Hemsworth vs. Unknown X", "finish": "Bud Hemsworth beat Unknown X in 10 Min 50 Sec with a Stomach Claw", "rating_stars": "<span class=\"stars\">★★★</span>", "rating_num": 3, "time": "10:50"}, {"number": 2, "name": "Iron Man Match: Preston Toddsworth vs. Rocky Wilbur", "finish": "Rocky Wilbur beat Preston Toddsworth in 30 Min 0 Sec with a 1:0", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": "30:00"}, {"number": 3, "name": "Antonio Antiguo, Diego Guerrero & Holy Diver vs. Bernardo Barros, Doctor Dorado & Felix Santana", "finish": "Antonio Antiguo beat Bernardo Barros in 16 Min 20 Sec with a Campana", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": "16:20"}, {"number": 4, "name": "Billy Fender vs. Joey Farrell", "finish": "Billy Fender beat Joey Farrell in 15 Min 18 Sec with a an Original German Suplex", "rating_stars": "<span class=\"stars\">★★★</span>", "rating_num": 3, "time": "15:18"}]
---

# Professional Wrestling 5

<div class="event-header">
<div class="event-meta">
**Date:** 1982-04-02<br>
**Venue:** The Vault<br>
**Location:** Boston, MA
</div>
<img src="/pwa-website/img/posters/1982-04-02 - Professional Wrestling 5.png" class="event-poster" alt="Poster">
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