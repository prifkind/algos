/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function (nums, target) {
    let counter = nums.length - 1

    while (counter >= 0) {
        if (nums.pop() === target) {
            return counter
        } else counter--
    }

    return -1
};
