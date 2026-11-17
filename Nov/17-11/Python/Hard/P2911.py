from itertools import combinations

class Solution(object):
    def minimumChanges(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        memo_partition = {}
        memo_substring = {}
        memo_minimum = {}
        
        def changesRequired(s, length):
            if s in memo_substring:
                return memo_substring[s]
            i = 0
            j = length - 1
            count = 0
            while i < j:
                if s[i] != s[j]:
                    count += 1
                i += 1
                j -= 1
                
            memo_substring[s] = count
            return count
            
        def partitionate(s, k):
            
            n = len(s)

            # Impossible if each of the k parts must have length >= 2
            if k < 1 or n < 2 * k:
                raise StopIteration

            for cuts in combinations(range(1, n), k - 1):
                parts = []
                start = 0

                valid = True
                for cut in cuts:
                    part = s[start:cut]
                    if len(part) < 2:
                        valid = False
                        break
                    parts.append(part)
                    start = cut

                last_part = s[start:]
                if valid and len(last_part) >= 2:
                    parts.append(last_part)
                    yield parts

        
        def partitionate2(s, k):
            if k < 1:
                raise StopIteration
            elif k == 1:
                yield [s]
            else:
                last = len(s) - (k - 1) * 2 + 1
                if last <= 2:
                    raise StopIteration
                for i in range(2, last):
                    car = s[:i]
                    cdr = s[i:]
                    for subparts in partitionate2(cdr, k - 1):
                        yield [car] + subparts
        
        def getSubstring(s, start, step):
            length = len(s)
            i = start
            newString = ""
            while i < length:
                newString += s[i]
                i += step
            return newString
            
        def changesInSemi(partition, min_changes = 1000000):
            if partition in memo_partition:
                return memo_partition[partition]
                
            min_accum = 1000000
            length = len(partition)
            half = length // 2 + 1
            for d in range(half - 1, 0, -1):
                accum = 0
                part_len, mod = divmod(length, d)
                if mod != 0:
                    continue
                for idx in range(d):
                    substring = getSubstring(partition, idx, d)
                    accum += changesRequired(substring, part_len)
                    # print("   - ", substring, accum)
                    if accum > min_changes:
                        break
                if accum == 0:
                    memo_partition[partition] = accum
                    return accum
                elif accum < min_accum:
                    min_accum = accum
                
            memo_partition[partition] = min_accum
            return min_accum
            
        def changesIn(partitions, min_changes):
            accum = 0
            for partition in partitions:
                # print(" *", partition)
                accum += changesInSemi(partition, min_changes - accum)
                if accum > min_changes:
                    return accum
            return accum  
        
        def originalProcess():    
            min_changes = 1000000
            for partitions in partitionate(s, k):
                required = changesIn(partitions, min_changes)
                # print(partitions, required)
                if required == 0:
                    return 0
                elif required < min_changes:
                    min_changes = required
                
            return min_changes
            
        def getRecurrentMinimum(start, partitions):
            if memo_minimum.get(start, None):
                if memo_minimum[start].get(partitions, None):
                    return memo_minimum[start][partitions]
            else:
                memo_minimum[start] = {}
            
            if partitions == 1:
                this_min = changesInSemi(s[start:])
                memo_minimum[start][partitions] = this_min
                return this_min
                
            max_length = len(s) - 2 * (partitions - 1) - start
            if max_length < 2:
                memo_minimum[start][partitions] = 1000000
                return 1000000
                
            minimum = 1000000
            for this_len in range(2, max_length + 1):
                this_string = s[start:this_len + start]
                this_min = changesInSemi(this_string)
                other_min = getRecurrentMinimum(this_len + start, partitions - 1)
                new_min = this_min + other_min
                if new_min == 0:
                    memo_minimum[start][partitions] = 0
                    return 0

                if new_min < minimum:
                    minimum = new_min
                    
            memo_minimum[start][partitions] = minimum
            return minimum
        
        return getRecurrentMinimum(0, k)