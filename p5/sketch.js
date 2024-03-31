function drawVector(V, options = {Apos: {x: 300, y: 100}, AcellSize: {x: 40, y: 40}}) {
  const Apos = options.Apos
  const AcellSize = options.AcellSize
  let AcellPos;

  const range = Array.from({length: V.length}, (_, i) => i)
  AcellPos = range.map((_, i) => range.map((_, j) => [AcellSize.x * i + Apos.x, AcellSize.y * j + Apos.y]))

  strokeWeight(2)
  range.map(
    (_, j) => {
      fill(255 - V[j]*3)
      // fill(255 - random()*300)
      rect(
      ...[AcellPos[0][j][0], AcellPos[0][j][1]], AcellSize.x
    )}
  )

  textAlign(CENTER,CENTER)

  range.map((_, i) => text(`${V[i]}`, 
    ...[
      AcellPos[0][i][0] + (AcellSize.x/2), 
      AcellPos[0][i][1] + (AcellSize.y/2)
    ])
  )
}

function drawMatrix(A, options = {Apos: {x: 100, y: 100}, AcellSize: {x: 40, y: 40}}) {
  const Apos = options.Apos
  const AcellSize = options.AcellSize
  let AcellPos;

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
  createCanvas(800, 400);
}

function draw() {
  background(220);
  
  const A = [
    [1,2,3,4],
    [3,20,30,40],
    [-2,23,15,42],
    [8,20,35,40],
  ]

  const X = Array(4).fill(0)

  drawMatrix(A, {Apos: {x: 100, y: 100}, AcellSize: {x: 40, y: 40}})
  drawVector(X, {Apos: {x: 300, y: 100}, AcellSize: {x: 40, y: 40}})
  drawMatrix(A, {Apos: {x: 450, y: 100}, AcellSize: {x: 40, y: 40}})
}
