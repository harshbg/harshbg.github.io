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


p.a {
  font-size: 20px;
}

p.b {
  font-size: 20px;
}

div.c {
  font-size: 200%;
}

</style>
</head>
<body>

<br>

<div class="row">
  <div class="column">
    <div class="card">
      <div class="c"><i class="fa fa-coffee"></i></div>
      <p class="b">55+</p>
      <p class="a">This is some text.</p>
    </div>
  </div>

  <div class="column">
    <div class="card">
      <div class="c"><i class="fa fa-coffee"></i></div>
      <p class="b">55+</p>
      <p class="a">This is some text.</p>
    </div>
  </div>
  
  <div class="column">
    <div class="card">
      <div class="c"><i class="fa fa-coffee"></i></div>
      <p class="b">55+</p>
      <p class="a">This is some text.</p>
    </div>
  </div>
  
  <div class="column">
    <div class="card">
      <div class="c"><i class="fa fa-coffee"></i></div>
      <p class="b">55+</p>
      <p class="a">This is some text.</p>
    </div>
  </div>
</div>

</body>
</html>
