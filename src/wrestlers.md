---
layout: base.njk
title: Wrestler Index
permalink: /wrestlers/
---

<h1>🤼 Wrestler Index</h1>
<p>{{ collections.wrestlers.length }} superstars</p>

{% set groups = collections.wrestlers | groupByFirstLetter %}
{% for letter, wrestlers_list in groups %}
<h2>{{ letter }}</h2>
<div class="wrestler-grid">
{% for w in wrestlers_list %}
  <a href="{{ w.url }}" class="wrestler-card">{{ w.data.title }}</a>
{% endfor %}
</div>
{% endfor %}
