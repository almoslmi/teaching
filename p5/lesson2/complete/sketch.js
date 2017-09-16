
function setup() {
  createCanvas(600, 600);
  background(125);
  noStroke();
  noLoop();
}

function draw() {
  
}

function mouseClicked() {
  createRandomTarget(mouseX, mouseY);
}

function createTarget(x, y, maxSize, steps) {
  var sizeStep = maxSize / steps;
  var colorStep = 255/(steps - 1);
  for (var i=0; i<steps; i++) {
    fill(i * colorStep);
    var thisSize = maxSize - (i * sizeStep);
    ellipse(x, y, thisSize, thisSize);
  }
}

function createRandomTarget(x, y) {
  var maxSize = random(25, 350);
  var steps = random(1, 10);
  createTarget(x, y, maxSize, steps);
}