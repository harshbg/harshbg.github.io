---
layout: page
permalink: /testings/
title: Testings
---


<div class="container">
  <div class="row">
    <div class="col">
      1/3
    </div>
    <div class="col-6">
      1/3 (col-6)
    </div>
    <div class="col">
      1/3
    </div>
  </div>
  <div class="row">
    <div class="col">
      1/3
    </div>
    <div class="col-5">
      1/3 (col-6)
    </div>
    <div class="col">
      1/3
    </div>
  </div>
</div>



<div class="container">
  <div class="row justify-content-md-center">
    <div class="col col-lg-2">
      1/3
    </div>
    <div class="col-md-auto">
      1/3 Some content
    </div>
    <div class="col col-lg-2">
      1/3
    </div>
  </div>
  <div class="row">
    <div class="col">
      1/3
    </div>
    <div class="col-md-auto">
      1/3 Some content
    </div>
    <div class="col col-lg-2">
      1/3
    </div>
  </div>
</div>



<div class="row">
  <div class="col">col</div>
  <div class="col">col</div>
  <div class="w-100"></div>
  <div class="col">col</div>
  <div class="col">col</div>
</div>






<!DOCTYPE html>
<html>
<head>
<style>
.grid-container {
  display: grid;
  grid-template-columns: 80px 200px auto 30px;
  grid-gap: 10px;
  background-color: #2196F3;
  padding: 10px;
}

.grid-container > div {
  background-color: rgba(255, 255, 255, 0.8);
  text-align: center;
  padding: 20px 0;
  font-size: 30px;
}
</style>
</head>
<body>

<h1>grid-template-columns</h1>

<p>Use the <em>grid-template-columns</em> property to specify the size of each column.</p>

<div class="grid-container">
  <div>1</div>
  <div>2</div>
  <div>3</div>  
  <div>4</div>
  <div>5</div>
  <div>6</div>  
  <div>7</div>
  <div>8</div>
</div>

</body>
</html>





<!DOCTYPE html>
<html lang="en">
<head>
<title>CSS Template</title>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
* {
  box-sizing: border-box;
}

body {
  font-family: Arial, Helvetica, sans-serif;
}

/* Style the header */
.header {
  background-color: #f1f1f1;
  padding: 30px;
  text-align: center;
  font-size: 35px;
}

/* Create three equal columns that floats next to each other */
.column {
  float: left;
  width: 33.33%;
  padding: 10px;
  height: 300px; /* Should be removed. Only for demonstration */
}

/* Clear floats after the columns */
.row:after {
  content: "";
  display: table;
  clear: both;
}

/* Style the footer */
.footer {
  background-color: #f1f1f1;
  padding: 10px;
  text-align: center;
}

/* Responsive layout - makes the three columns stack on top of each other instead of next to each other */
@media (max-width: 600px) {
  .column {
    width: 100%;
  }
}
</style>
</head>
<body>

<h2>CSS Template using Float</h2>
<p>In this example, we have created a header, three equal columns and a footer. On smaller screens, the columns will stack on top of each other.</p>
<p>Resize the browser window to see the responsive effect.</p>

<div class="header">
  <h2>Header</h2>
</div>

<div class="row">
  <div class="column" style="background-color:#aaa;">Column</div>
  <div class="column" style="background-color:#bbb;">Column</div>
  <div class="column" style="background-color:#ccc;">Column</div>
</div>

<div class="footer">
  <p>Footer</p>
</div>

</body>
</html>


