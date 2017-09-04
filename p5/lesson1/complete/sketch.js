var x, y, rand;

function setup() {
  createCanvas(600, 400);
  x = width/2;
  y = height/2;
  stroke(0);
}

function draw() {
  rand = floor(random(4));
  if (rand === 0) {
    x++;
  } else if (rand === 1) {
    x--;
  } else if (rand === 2) {
    y++;
  } else {
    y--;
  }

  point(x, y);
}