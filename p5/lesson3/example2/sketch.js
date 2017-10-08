var colors = [
  '#1B998B',
  '#ED217C',
  '#2D3047',
  '#FFFD82',
  '#FF9B71'
];
var xValues = [];
var yValues = [];
var dotColors = [];

function setup() {
  createCanvas(600, 600);
  background(255);
  stroke(0);
}

function draw() {
  xValues.unshift(mouseX);
  yValues.unshift(mouseY);
  dotColors.unshift(random(colors));

  background(255);
  
  var count = xValues.length;
  for (var i=0; i<count; i++) {
    fill(dotColors[i]);
    ellipse(xValues[i], yValues[i], 15, 15);
  }

  if (count > 10) {
    xValues.pop();
    yValues.pop();
    dotColors.pop();
  }
}