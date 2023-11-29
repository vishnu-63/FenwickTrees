import math


class FenwickTree:
    def __init__(self, n):
        self.n = n+1
        self.fen = [0]*self.n

    def update(self, ind, value):
        """
        Update the value at index and keep updating the value at next index
        To Find the Next Index.Do the Below Steps
            1-->find 2's complement
            2-> Perform AND with the 2's complement
            3-> Add to The Original index
        """
        while ind < self.n:
            self.fen[ind] += value
            ind += (ind & (-ind))

    def sum(self, ind):
        """
        Take binary of index off right most Bit To Turn Off Follow the below Steps.
            1-->find 2's complement
            2-> Perform AND with the 2's complement
            3-> Subtract to The Original index
        """
        sum1 = 0
        while ind < self.n:
            sum1 += self.fen[ind]
            ind = ind - (ind & (-ind))
        return sum1

    def range(self, left, right):
        """
        To Find The Sum In Range between left to Right
            --> Find the sum till right and subtract till the left-1 TO get the result.
        """
        self.sum(right) - self.sum(left-1)

    def find(self, target):
        highest_power = int(math.log2(self.n))
        ind = 0
        sum1 = 0
        for i in range(highest_power, -1, -1):
            if sum1+self.fen[ind+(2**i)] < target:
                sum1 = sum1 + self.fen[ind+(2**i)]
                ind = ind + (2 ** i)
        return ind+1


if __name__ == '__main__':
    arr = [1, 0, 2, 1, 1, 3, 0, 4, 2, 5, 2, 2, 3, 1, 0, 2]
    n = len(arr)
    ftree = FenwickTree(n)
    for i in range(n):
        ftree.update(i+1, arr[i])
    ans = ftree.find(27)
    print(ans)
