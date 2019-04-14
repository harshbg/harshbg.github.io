---
layout: page
permalink: /testings/
title: Testings
---


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
  height: 140px; /* Should be removed. Only for demonstration */
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

.exp {
 
  font-size: 25px;
  color: #bd5d38;
  line-height: 0.7
}

.expt {
  
  text-align: center;
  
  font-size: 45px;
}



</style>
</head>
<body>

<div class="expt">Experiences</div>

<div class="row">
  <div class="column left" style="background-color:#00000;">
    <p class="exp">IHS Markit</p>
    <p>Houston, Texas</p>
    <p>June-August 2018</p>
  </div>
  <div class="column right" style="background-color:#00000;">
    <p class="exp">Data Transformation Intern</p>
    <p>Built machine learning models in Python to automate manual data parsing process,
achieved >96% accuracy rate by using random forest, MLP, DNN, hyper parameter
tuning with grid search and cross validation, resulting in time reduction by 88%
</p>
  </div>
  
  <div class="column left" style="background-color:#00000;">
    <p class="exp">MarketsandMarkets</p>
    <p>August 2013-July 2017</p>
  </div>
  
  <div class="column right" style="background-color:#00000;">
    <p class="exp">Research Analyst</p>
    <p>Estimated and forecasted the sales revenues and growth rates of global MICRO and
MACRO technology markets</p>
  </div>
</div>

</body>
</html>
