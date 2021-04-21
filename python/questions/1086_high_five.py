# Given a list of scores of different students, return the average score of each student's top five scores in the order of each student's id.
#
# Each entry items[i] has items[i][0] the student's id, and items[i][1] the student's score.  The average score is calculated using integer division.
#
#
#
# Example 1:
#
# Input: [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
# Output: [[1,87],[2,88]]
# Explanation:
# The average of the student with id = 1 is 87.
# The average of the student with id = 2 is 88.6. But with integer division their average converts to 88.
#
#
#
# Note:
#
# 1 <= items.length <= 1000
# items[i].length == 2
# The IDs of the students is between 1 to 1000
# The score of the students is between 1 to 100
# For each student, there are at least 5 scores


class Solution(object):

    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """

        # 1. Store all the ID's and respective scores in a dictionary.
        # {1: [91, 92, 60, 65, 87, 100], 2: [93, 97, 77, 100, 76]}
        dic = {}
        for item in items:
            if item[0] in dic:
                dic[item[0]].append(item[1])
            else:
                dic[item[0]] = [item[1]]
        print(dic)

        # 2. Function to sort list and return average of top 5
        def sort_avg(list):
            list = sorted(list, reverse=True)
            return int(sum(list[0:5]) / 5)

        # 3. Create a final return dict, append the averages in that list.
        final = []
        for item in dic:
            final.append([item, sort_avg(dic[item])])

        return final


input = [[1, 91], [1, 92], [2, 93], [2, 97], [1, 60], [2, 77], [1, 65], [1, 87], [1, 100], [2, 100], [2, 76]]
print(Solution.highFive(0, input))
