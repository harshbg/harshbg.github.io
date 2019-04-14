---
layout: page
permalink: /testings/
title: Testings
---



<pre><code class="language-c">int foo (void) 
{
    int i;
}
</code></pre>
So, the final document that is sure to work in all (most?) Markdown parsers would look like this:

# Rule 1
Description for rule 1.

<div style="-webkit-column-count: 2; -moz-column-count: 2; column-count: 2; -webkit-column-rule: 1px dotted #e0e0e0; -moz-column-rule: 1px dotted #e0e0e0; column-rule: 1px dotted #e0e0e0;">
    <div style="display: inline-block;">
        <h2>Good</h2>
        <pre><code class="language-c">int foo (void) 
{
    int i;

	}
</code></pre>
    </div>
    <div style="display: inline-block;">
        <h2>Bad</h2>
        <pre><code class="language-c">int foo (void) {
    int i;
}
</code></pre>
    </div>
</div>

