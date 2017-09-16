
function setup() {
  createCanvas(600, 600);
  background(125);
  noStroke();
  noLoop();
}

function createTarget(x, y, maxSize, steps) {
  var sizeStep = maxSize / steps;  // We'll use this to define our ring sizes
  var colorStep = 255/(steps - 1);
  for (var i=0; i<steps; i++) {
    fill(i * colorStep);
    var thisSize = maxSize - (i * sizeStep);
    ellipse(x, y, thisSize, thisSize);
  }
}

function draw() {
  // pass
} 

function mouseClicked() {
  createTarget(mouseX, mouseY, 400, 10);
}