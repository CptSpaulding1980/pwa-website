---
layout: base.njk
title: All Events
permalink: /events/
---

<h1>📅 All Events</h1>

{% set groups = collections.events | groupByYear %}
{% for year in groups | sortedYears %}
<h2>{{ year }} <small>({{ groups[year].length }} events)</small></h2>
<div class="event-list">
{% for ev in groups[year] %}
  <a href="{{ ev.url }}" class="event-link">
    <span class="event-date">{{ ev.data.date }}</span>
    <span class="event-title">{{ ev.data.title }}</span>
    <span class="event-venue">{{ ev.data.venue }}</span>
  </a>
{% endfor %}
</div>
{% endfor %}
