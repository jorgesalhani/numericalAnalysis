class Matrix {

  static transpose(A) {
    return A.map((row,i) => row.map((_,j) => A[j][i]));
  }
  
  static matmul(A,B) {
    const BT = transpose(B)
    return A.map((row, i) => row.map((_, j) => row.reduce((s, _, k) => s + A[i][k]*BT[j][k], 0)))
  }
}

export { Matrix }