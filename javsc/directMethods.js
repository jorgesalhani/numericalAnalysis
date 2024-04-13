class DirectMethods {

  static progressive_substitution(L, b) {
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
  
  static regressive_substitution(U, b) {
    const N = U.length
  
    const UT = U.map((row, i, U) => row.map((_,j) => i >= j ? U[j][i] : 0))
    const bRev = b.map((_, i, V) => V[V.length-1-i]);
  
    const xRev = progressive_substitution(UT, bRev)
    const X = xRev.map((_, i, V) => V[b.length-1-i]);
    return X
  }
  
  static decomposition_cholesky(A) {
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
  
  static decomposition_LU(A) {
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
  
  static gauss_elimination_matrix(A) {
  
    const N = A.length
  
    A.map((row, i) => row.map((_, j) => {
      const k = j + i + 1
      if (k >= N) return

      // let pivot = -Infinity
      // let pivotIdx = i-1

      // row.map((_, p) => {
      //   if (j > p) return

      //   if (Math.abs(A[p][j]) > pivot) {
      //     pivot = A[p][j]
      //     pivotIdx++
      //   }
      // })

      // console.log(pivot, pivotIdx)
      // console.table(A)
  
      const m_ij = - A[k][i] / A[i][i]
      row.map((_, l) => A[k][l] = A[k][l] + (m_ij * A[i][l]))
  
    }))
    return A
  }
}

export { DirectMethods }