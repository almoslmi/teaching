var colors = [
  '#1B998B',
  '#ED217C',
  '#2D3047',
  '#FFFD82',
  '#FF9B71'
];

function setup() {
  createCanvas(600, 600);
  background(255);
  stroke(0);
}

function draw() {
  background(255);
  fill(random(colors));
  ellipse(mouseX, mouseY, 15, 15);
}