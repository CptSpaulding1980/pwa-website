---
layout: base.njk
title: Championships
permalink: /championships/
---

<h1>🏆 Championships</h1>

<div class="champ-grid">
{% for ch in collections.championships %}
  <a href="{{ ch.url }}" class="champ-card">
    <h2>{{ ch.data.title }}</h2>
  </a>
{% endfor %}
</div>
