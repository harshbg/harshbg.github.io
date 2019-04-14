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

.fa 
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
      <p>Projects</p>
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
      <p><i class="fa fa-coffee"></i></p>
      <h3>100+</h3>
      <p>Meetings</p>
    </div>
  </div>
</div>

| head1        | 					head two          | three |
|:-------------|					:------------------|:------|
| ok           | 					good swedish fish | nice  |
| out of stock |					good and plenty   | nice  |
| ok           | 					good `oreos`      | hmm   |
| ok           | 					good `zoute` drop | yumm  |

</body>
</html>



<div class="container">
  <div class="row">
    <div class="col">
      1/2
    </div>
    <div class="col">
      1/2
    </div>
  </div>
  <div class="row">
    <div class="col">
      1/3
    </div>
    <div class="col">
      1/3
    </div>
    <div class="col">
      1/3
    </div>
  </div>
</div>











<!DOCTYPE html>
<html lang="en">
<head>
  <title>Bootstrap Example</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>
</head>
<body>

<div class="container-fluid">
  <h1>Small Grid</h1>
  <p>The following example will result in a 25%/75% split on small, medium and large devices. On extra small devices, it will stack (100% width).</p>
  <p>Resize the browser window to see the effect.</p>
  <div class="row">
    <div class="col-sm-3" style="background-color:yellow;">
      Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.<br>
      Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
    </div>
    <div class="col-sm-9" style="background-color:pink;">
      Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo.
    </div>
  </div>
</div>

</body>
</html>





<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
* {
  box-sizing: border-box;
}

.row {
  display: flex;
}

/* Create two equal columns that sits next to each other */
.column {
  flex: 80%;
  padding: 10px;
  height: 300px; /* Should be removed. Only for demonstration */
}
</style>
</head>
<body>

<h2>Two Equal Columns</h2>

<div class="row">
  <div class="column" style="background-color:#aaa;">
    <h2>Column 1</h2>
    <p>Some text..</p>
  </div>
  <div class="column" style="background-color:#bbb;">
    <h2>Column 2</h2>
    <p>Some text..</p>
  </div>
</div>

</body>
</html>



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
