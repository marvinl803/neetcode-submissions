public class Solution {
    public bool hasDuplicate(int[] nums) {

        var dict = new Dictionary<int, int>();
        
        for (int i = 0; i < nums.Length; i++) 
        {
            if (!dict.ContainsKey(nums[i]))
            {
                dict[nums[i]] = 1;
            }
            else
            {
                dict[nums[i]] += 1;
            }
        }

        foreach (var pair in dict)
            if (pair.Value > 1) return true;
        return false;
    }
}