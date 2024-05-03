const estudantes = require("./teste.json");

nums = [2,7,11,15], target = 9

const twoSum = (nums, target) =>
{
    const map = new Map();
    const res = []
    for(let [pos, numb] of Object.entries(nums))
    {
        var dif = target - numb;
        if(map.has(dif))
        {
            res.push(map.get(dif), pos)
        }
        map.set(numb, pos);


    }
    return res;
}

console.log(twoSum(nums, target));

