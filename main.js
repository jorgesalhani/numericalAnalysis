import { Matrix } from "./matrix.js"
import { DirectMethods } from "./directMethods.js";

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

// console.log(DirectMethods.progressive_substitution(L, b))
// console.log(DirectMethods.regressive_substitution(U, b))
// console.log(DirectMethods.decomposition_cholesky(A))
// console.log(DirectMethods.decomposition_LU(A))
console.log(DirectMethods.gauss_elimination_matrix(A, b))



