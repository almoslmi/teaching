
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
  for (var i=0; i < 5; i++) {
    createTarget(40 + i*100, 50 + i*125, 100 + i*50, 5 + i);
  }
} 

function mouseClicked() {
  fill(255);
  ellipse(mouseX, mouseY, 50, 50);
}