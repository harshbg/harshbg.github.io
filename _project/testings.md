---
layout: page
permalink: /testings/
title: Testings
---

<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
* {
  box-sizing: border-box;
}

/* Create two unequal columns that floats next to each other */
.column {
  float: left;
  padding: 10px;
  height: 200px; /* Should be removed. Only for demonstration */
}

.left {
  width: 30%;
}

.right {
  width: 70%;
}

/* Clear floats after the columns */
.row:after {
  content: "";
  display: table;
  clear: both;
}
</style>
</head>
<body>

<h2>Experience</h2>

<div class="row">
  <div class="column left" style="background-color:#00000;">
    <h2>IHS Markit</h2>
    <h3>June-August 2018</h3>
  </div>
  <div class="column right" style="background-color:#00000;">
    <h2>Data Transformation Intern</h2>
    <p>Built machine learning models in Python to automate manual data parsing process,
achieved >96% accuracy rate by using random forest, MLP, DNN, hyper parameter
tuning with grid search and cross validation, resulting in time reduction by 88%
</p>
  </div>
  
  <div class="column left" style="background-color:#aaa;">
    <h2>MarketsandMarkets</h2>
    <p>August 2013-July 2017</p>
  </div>
  
  <div class="column right" style="background-color:#bbb;">
    <h2>Column 2</h2>
    <p>Some text..</p>
  </div>
</div>

</body>
</html>
