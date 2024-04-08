var groupAnagrams = function(strs) {

        let i = 0;
        let k = 0;
        let res = [];
        while (i < strs.length)
        {
            
            if(k == 0 || !res[k - 1].includes(strs[i]))
            {
                res[k] = [];
                res[k].push(strs[i]);
                k++;
            }
            else {
                i++;
                continue;
    
            }
            j = i + 1;
            while(j < strs.length)
            {
                if(checkAnagrams(strs[i], strs[j]))
                {
                    res[k - 1].push(strs[j]);
    
                }
                j++;
            }
            i++;
        }
        return res; 
    };
    
    const checkAnagrams =(w1, w2)=>{
    
        let w2Clone = w2.slice();
        if(w1.length != w2Clone.length) return false;
        counter = 0;
    
        for (letter of w1)
        {
            if(w2Clone.includes(letter))
            {
                counter++;
                w2Clone = w2Clone.replace(letter, '');
            }
            else return false;
        }
        if(counter == w1.length && w2Clone.length == 0) return true;
    }
    
console.log('teste');
console.log(groupAnagrams(["eat","tea","tab", "bat"]));