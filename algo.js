var longestPalindrome = function (s) {
    let res = '';
    for(let i = 0; i < s.length; i++){
        // Odd - if there is only 1 char in the middle, like 'bob'
        let lOdd = i, rOdd = i;
        expandAroundCenter(lOdd, rOdd)
        //Even - 2 chars in the middle, like 'kbbk'
        let lEven = i, rEven = i + 1;
        expandAroundCenter(lEven, rEven);
    }
  // helper
    function expandAroundCenter(left, right){
      while(left >= 0 && right < s.length && s[left] === s[right]){
        let subStr = s.substring(left, right + 1);
        if(subStr.length > res.length){
          res = subStr;
        }
        left--;
        right++;
      }
    }
    return res;
};
