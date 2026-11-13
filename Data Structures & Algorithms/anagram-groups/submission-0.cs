public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {

        var dicti = new Dictionary<string, List<string>>();

        for (int i = 0; i < strs.Length; i++)
        {
            char[] chars = strs[i].ToCharArray();
            Array.Sort(chars);
            string key = new string(chars);
            if (!dicti.ContainsKey(key))
            {
                dicti[key] = new List<String>();
            }

            dicti[key].Add(strs[i]);

        }

        var ans = new List<List<string>>();

        foreach (var pair in dicti)
        {
            ans.Add(pair.Value);
        }

        return ans;
    }
}
