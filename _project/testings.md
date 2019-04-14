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
  height: 150px; /* Should be removed. Only for demonstration */
}

.left {
  width: 35%;
}

.right {
  width: 65%;
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
  line-height: 1;
  font-weight: bold;
}

.exps {
 
  font-size: 25px;
  color: #bd5d38;
  line-height: 0.7;
  font-family:sans-serif;
  
}
.expt {
  
  text-align: center;
  
  font-size: 45px;
  line-height: 1.7;
}

.expd {

  font-size: 15px;
  
  line-height: 0.7;
}

.horizontal-line div {
    background: #bcbcbc none repeat scroll 0 0;
    height: 2px;
    margin: 0 auto;
    width: 77px;
}
.horizontal-line div.top {
    margin-bottom: 3px;
    width: 44px;
    
}


</style>
</head>
<body>

<div>
<div class="expt">Experiences</div>
	<div class="horizontal-line">
                <div class="top"></div>
                	<div class="bottom"></div>
</div>               

<p>

</p>

<div class="row">
  <div class="column left" style="background-color:#00000;">
    <p class="exp">IHS Markit</p>
    <p class="expd">Houston, Texas</p>
    <p class="expd">June 2018 - August 2018</p>
  </div>
  <div class="column right" style="background-color:#00000;">
    <p class="exps">Data Transformation Intern</p>
    <p>Built machine learning models in Python to automate manual data parsing process,
achieved >96% accuracy rate by using random forest, MLP, DNN, hyper parameter
tuning with grid search and cross validation, resulting in time reduction by 88%
</p>
  </div>
  
  <div class="column left" style="background-color:#00000;">
    <p class="exp">Statistics Without Borders</p>
    <p class="expd">Pune, India</p>
    <p class="expd">August 2013 - July 2017</p>
  </div>
  
  <div class="column right" style="background-color:#00000;">
    <p class="exps">Research Analyst</p>
    <p>Estimated and forecasted the sales revenues and growth rates of global MICRO and
MACRO technology markets</p>
  </div>
</div>

</body>
</html>
