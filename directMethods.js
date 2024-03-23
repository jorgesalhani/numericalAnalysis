const mathjs = require('mathjs')

function progressive_substitution(L, b) {
  const N = L._size[0];

  const x = mathjs.zeros(N);
  for (let i = 0; i < N; i++ ) {
    let x_i = b.get([i])

    for (let j = 0; j < i; j++) {
      x_i -= L.get([i,j]) * x.get([j])
    }

    x_i /= L.get([i,i])
    x.set([i], x_i)
  }

  return x;
}

function regressive_substitution(U, b) {
  const N = U._size[0]

  const x = mathjs.zeros(N)
  for (let i = N-1; i >= 0; i--) {
    
    let x_i = b.get([i])
    for (let j = i; j < N; j++) {
      x_i -= U.get([i,j]) * x.get([j])
    }

    x_i /= U.get([i,i])
    x.set([i], x_i)
  }

  return x
}

const A = mathjs.matrix([[1,2,3],[10,20,30],[100,200,300]])
const b = mathjs.matrix([20,40,60])

// const L = mathjs.matrix([[1,0,0],[10,20,0],[100,200,300]])
// const U = mathjs.matrix([[100,200,300], [0,20,10], [0,0,20]])

// const x = progressive_substitution(L, b)
// const x = regressive_substitution(U, b)

console.log(x)