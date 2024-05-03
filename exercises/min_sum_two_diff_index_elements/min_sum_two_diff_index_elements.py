class Solution:

    def find_min(self, arr):
        min_arr = None

        i = 0
        while i < len(arr):
            if min_arr == None:
                min_arr = {'val': arr[i], 'idx': i}
            elif arr[i] < min_arr['val']:
                min_arr = {'val': arr[i], 'idx': i}
            i += 1

        return min_arr

    def min_sum(self, a, b, n):
        min_a = self.find_min(a)
        min_b = self.find_min(b)

        if min_a['idx'] != min_b['idx']:
            return min_a['val'] + min_b['val']
        else:
            a.pop(min_a['idx'])
            b.pop(min_b['idx'])

            min_a2 = self.find_min(a)
            min_b2 = self.find_min(b)

            return min_a['val'] + min_b2['val'] if min_a['val'] + min_b2['val'] < min_a2['val'] + min_b['val'] else \
            min_a2['val'] + min_b['val']