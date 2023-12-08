function setup(){
    createCanvas(400, 400);
    noStroke();
}
    
function draw(){
    background(204);
    eye(mouseX, mouseY);
}

function eye(x, y){
    fill(255);
    ellipse(x, y, 60, 60);
    fill(0);
    ellipse(x+10, y, 30, 30);
    fill(255);
    ellipse(x+16, y-5, 6, 6);  
}

