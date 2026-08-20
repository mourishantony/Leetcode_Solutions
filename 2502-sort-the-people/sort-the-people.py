class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        ans = []
        store ={}
        for i in range(len(names)):
            store[heights[i]] = names[i]
        heights.sort(reverse = True)

        for i in range(len(names)):
            ans.append(store[heights[i]])
        return ans