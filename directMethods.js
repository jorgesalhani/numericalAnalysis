function transpose(A) {
  return A.map((row,i) => row.map((_,j) => A[j][i]));
}

function matmul(A,B) {
  const BT = transpose(B)
  return A.map((row, i) => row.map((_, j) => row.reduce((s, _, k) => s + A[i][k]*BT[j][k], 0)))
}

function progressive_substitution(L, b) {
  const N = L.length

  const Z = Array(N).fill(0)
  const X = Z.map((_, i, V) => {
    
    // let formula = `x_${i} = `
    // formula += `[b_${i} - `
    // L[i].reduce((s, _, j) => i > j ? formula += `L_${i}${j}*x_${j} + ` : '', 0)
    // formula += `] / a_${i}${i}`
    // console.log(formula)

    const sumTerm = L[i].reduce((s, _, j) => i > j ? s + L[i][j]*V[j] : s, 0)
    V[i] = (b[i] - sumTerm) / L[i][i]

    return V[i]
  })

  return X;
}

function regressive_substitution(U, b) {
  const N = U.length

  const UT = U.map((row, i, U) => row.map((_,j) => i >= j ? U[j][i] : 0))
  const bRev = b.map((_, i, V) => V[V.length-1-i]);

  const xRev = progressive_substitution(UT, bRev)
  const X = xRev.map((_, i, V) => V[b.length-1-i]);
  return X
}

function decomposition_cholesky(A) {
  const N = A.length
  const Z = [...Array(N)].map(_ => Array(N).fill(0));

  const H = Z.map((row, i, mat) => row.map((a, j) => {
    let sumTerm;

    // let formula = `h_${i}${j} = `
    if (i == j) {
      // formula += `sqrt[`
      // formula += `a_${i}${j} - `
      // row.reduce((s, _, k) => k < j ? formula += `(h_${i}${k})^2 +` : s, 0)
      // formula += `]`
      // console.log(formula)

      sumTerm = row.reduce((s, _, k) => k < j ? s + mat[i][k] * mat[j][k] : s, 0)
      mat[i][j] = Math.sqrt(A[i][j] - sumTerm)
      return mat[i][j]
    }

    if (j < i ) {
      // formula += `[`
      // formula += `a_${i}${j} - `
      // row.reduce((s, _, k) => k < j ? formula += `(h_${i}${k})^2 +` : s, 0)
      // formula += `] / h_${j}${j}`
      // console.log(formula)

      sumTerm = row.reduce((s, _, k) => k < j ? s + mat[i][k] * mat[j][k] : s, 0)
      mat[i][j] = (A[i][j] - sumTerm) / mat[j][j]
      return mat[i][j]
    }
    
    // formula += '0'
    // console.log(formula)

    mat[i][j] = a
    return mat[i][j]
  }))


  return H
}

function decomposition_LU(A) {
  const N = A.length

  const L = [...Array(N)].map(() => Array(N).fill(0))
  const U = [...Array(N)].map(() => Array(N).fill(0))

  L.map((_, i) => L[i][i] = 1)
  A.map((row, i, M) => row.map((v, j) => {

    if (i <= j) {
      const sumTerm = row.reduce((s, _, k) => k < i ? s + L[i][k]*U[k][j] : s, 0)
      const u_ij = A[i][j] - sumTerm
      U[i][j] = u_ij
      return U[i][j]
    }

    if (i > j) {
      const sumTerm = row.reduce((s, _, k) => k < j ? L[i][k]*U[k][j] : s, 0)
      const l_ij = (A[i][j] - sumTerm) / U[j][j]
      L[i][j] = l_ij
      return L[i][j]
    }
  }))

  return {L, U}
}

function gauss_elimination_matrix(A) {

  const N = A.length

  A.map((row, i) => row.map((_, j) => {
    const k = j + i + 1
    if (k >= N) return

    const m_ij = - A[k][i] / A[i][i]
    row.map((_, l) => A[k][l] = A[k][l] + (m_ij * A[i][l]))

  }))
  return A
}



// const L = mathjs.matrix([[1,0,0],[10,20,0],[100,200,300]])
// const U = mathjs.matrix([[100,200,300], [0,20,10], [0,0,20]])

// const x = progressive_substitution(L, b)
// const x = regressive_substitution(U, b)
const A = [
  [2, 1, 2],
  [4, 3, 3],
  [6, 5, -1],
]

const L = [
  [10, 0, 0],
  [5, 3, 0],
  [2, 2, 3],
]

const U = [
  [10, 5, 2],
  [0, 3, 2],
  [0, 0, 3],
]
const b = [10, 20, 4]

// console.log(progressive_substitution(L, b))
// console.log(regressive_substitution(U, b))
// console.log(decomposition_cholesky(A))
// console.log(decomposition_LU(A))
console.log(gauss_elimination_matrix(A, b))

