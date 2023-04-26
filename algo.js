var isValid = function (s) {
    // Parse string to array
    let splitString = s.split('')
    let stack = []
    let dictionary = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    if (splitString.length === 1) return false
    // Loop through array.  Check count of each character and update values for ordering
    for (let i = 0; i < splitString.length; i++) {
        // If it's an opening character, push it to the end of the stack
        if (splitString[i] === '{' || splitString[i] === '[' || splitString[i] === '(') {
            stack.push(splitString[i])
        }
        // If it's a closing character, compare the last character on the stack to the dictionary and see if it matches the closing character
        else if (dictionary[stack[stack.length - 1]] === splitString[i]) {
            // Pop the character off the stack if it matches
            stack.pop()
        } else return false
    }

    if (stack.length === 0) { return true } else return false
};
