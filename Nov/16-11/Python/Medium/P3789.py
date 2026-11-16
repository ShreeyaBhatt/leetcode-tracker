class Solution:
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):
        def bound(need_a, cost_a, need_b, cost_b):
            p_a = min(cost_a, costBoth)  # a takes its full price
            p_b = min(cost_b, costBoth - p_a)  # b gets what's left of the bundle
            return need_a * p_a + need_b * p_b

        return max(bound(need1, cost1, need2, cost2), bound(need2, cost2, need1, cost1))