/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var rotate = function(matrix) {
    let rotate = 0;
    for(row = 0; row < matrix.length/2; row++){
        for(col = row; col < matrix.length - 1 - row; col++){
            rotate = matrix[row][col];
            matrix[row][col] = matrix[matrix.length - 1 - col][row];
            matrix[matrix.length-1-col][row] = matrix[matrix.length-1-row][matrix.length-1-col];
            matrix[matrix.length-1-row][matrix.length-1-col] = matrix[col][matrix.length-1-row];
            matrix[col][matrix.length-1-row] = rotate;
        }
    }
};
