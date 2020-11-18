nums1 = [1,2,2,1]
nums2 = [2,2]



a=[i for i in nums1 if i in nums2]
print(a)


def intersection(self, nums1, nums2):
    if not nums1 and not nums2: return []
    if not nums1 or not nums2: return []

    d = {}
    ans = []

    for num in nums1:
        d[num] = d.get(num, 0) + 1

    for num in nums2:
        # not in dictioanry
        if d.get(num, 0) == 0:
            d[num] = -1

        else:
            if d[num] != -1:
                ans.append(num)
                d[num] = -1

    return ans