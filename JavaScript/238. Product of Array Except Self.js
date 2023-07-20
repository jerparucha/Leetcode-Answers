/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    let answer = [];
    var multiplier = 1;
    for(var i = 0; i < nums.length; i++){
        for(var j = 0; j < nums.length; j++){
            if(i != j){
                multiplier = multiplier * nums[j];
            }
        }
        answer.push(multiplier)
        multiplier = 1;
    }
    return answer;
};