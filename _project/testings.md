---
layout: page
permalink: /testings/
title: Testings
---

<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
* {
  box-sizing: border-box;
}

body {
  
}

/* Float four columns side by side */
.column {
  float: left;
  width: 25%;
  padding: 0 5px;
}

.row {margin: 0 5px;}

/* Clear floats after the columns */
.row:after {
  content: "";
  display: table;
  clear: both;
}

/* Responsive columns */
@media screen and (max-width: 600px) {
  .column {
    width: 100%;
    display: block;
    margin-bottom: 15px;
  }
}

/* Style the counter cards */
.card {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
  padding: 14px;
  text-align: center;
  background-color: #444;
  color: white;
}


div.a {
  font-size: 15px;
}

div.b {
  font-size: large;
}

div.c {
  font-size: 150%;
}

</style>
</head>
<body>

<h2>Responsive Section Counter</h2>
<p>Resize the browser window to see the effect.</p>
<br>

<div class="row">
  <div class="column">
    <div class="card">
      <h1><i class="fa fa-trophy"></i></h1>
      <h2>11+</h2>
      <h2>Partners</h2>
    </div>
  </div>

  <div class="column">
    <div class="card">
      <h2><i class="fa fa-check"></i></h2>
      <h3>55+</h3>
      <div class="a">This is some text.</div>
    </div>
  </div>
  
  <div class="column">
    <div class="card">
      <p><i class="fa fa-smile-o"></i></p>
      <h3>100+</h3>
      <p>Happy Clients</p>
    </div>
  </div>
  
  <div class="column">
    <div class="card">
      <div class="c"><i class="fa fa-coffee"></i></div>
      <h3>100+</h3>
      <p>Meetings</p>
    </div>
  </div>
</div>

</body>
</html>
