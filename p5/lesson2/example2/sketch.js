
function setup() {
  createCanvas(600, 600);
  background(125);
  noStroke();
  noLoop();
}

function draw() {
  var maxSize = 400;  // pixels
  var steps = 10;
  var sizeStep = maxSize / steps;  // We'll use this to define our ring sizes
  var colorStep = 255/(steps - 1);
  var x = width/2;  // pixels 
  var y = height/2;  // pixels
  for (var i=0; i<steps; i++) {
    fill(i * colorStep);
    var thisSize = maxSize - (i * sizeStep);
    ellipse(x, y, thisSize, thisSize);
  }
}

function mouseClicked() {
  fill(255);
  ellipse(mouseX, mouseY, 50, 50);
}