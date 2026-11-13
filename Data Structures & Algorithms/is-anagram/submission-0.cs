public class Solution {
    public bool IsAnagram(string s, string t) {

        var word1 = new Dictionary<char, int>();
        var word2 = new Dictionary<char, int>();

        if (s.Length != t.Length) {return false;}

        for (int i = 0; i < s.Length; i++)
        {
            if (!word1.ContainsKey(s[i])) word1[s[i]] = 1;
            else word1[s[i]] += 1;

            if (!word2.ContainsKey(t[i])) word2[t[i]] = 1;
            else word2[t[i]] += 1;
        }

        foreach(var pair in word1)
        {
            if(!word2.ContainsKey(pair.Key) || word2[pair.Key] != pair.Value) {return false;}
        }
        return true;
    }
}
