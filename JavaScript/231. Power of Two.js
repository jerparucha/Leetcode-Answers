/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfTwo = function(n) {
    if (n == 1){
        return true;
    } else if ( n == 0){
        return false;
    }

    while (n % 2 == 0){
        if (n % 2 != 0 && n != 1){
            return false;
        }
        n = (n/2);
        if (n == 1){
            return true
        }
    }
    return false
};