let num = 50
let x = []
let y = []

function setup() {
  createCanvas(400, 400);
  for(let i = 0; i < num; i++) {
    x.push(0)
    y.push(0)
  }
  noStroke();
  fill(255,102);
}

function draw() {
  background(0);
  for(let i = num - 1; i >= 0; i--){
    x[i] = x[i - 1];
    y[i] = y[i - 1];
  }
    
  x[0] = mouseX;
  y[0] = mouseY;
    
  for(let i = 0; i < num; i++){
    ellipse(x[i], y[i], i / 2, i / 2);
  }
}

