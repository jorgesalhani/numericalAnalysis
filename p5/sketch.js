const Apos = {x: 100, y: 100}
const AcellSize = {x: 40, y: 40}
let AcellPos;

function drawMatrixLines(A) {
  const range = Array.from({length: A.length}, (_, i) => i)
  AcellPos = range.map((_, i) => range.map((_, j) => [AcellSize.x * i + Apos.x, AcellSize.y * j + Apos.y]))

  strokeWeight(2)
  range.map((_, i) => range.map(
    (_, j) => {
      fill(255 - A[i][j]*3)
      // fill(255 - random()*300)
      rect(
      ...[AcellPos[i][j][0], AcellPos[i][j][1]], AcellSize.x
    )}
  ))

  textAlign(CENTER,CENTER)
  range.map((_, i) => range.map(
    (_, j) => text(`${A[j][i]}`, 
    ...[
      AcellPos[i][j][0] + (AcellSize.x/2), 
      AcellPos[i][j][1] + (AcellSize.y/2)
    ])
  ))
}

function setup() {
  createCanvas(500, 500);
}

function draw() {
  background(220);
  
  const A = [
    [1,2,3,4],
    [3,20,30,40],
    [-2,23,15,42],
    [8,20,35,40],
  ]

  drawMatrixLines(A)
}
