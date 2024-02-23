class StockSpanner(object):

    def __init__(self):
        self.st = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        count = 1
        while self.st and self.st[-1][0] <= price:
            count += self.st.pop()[1]
        self.st.append((price, count))
        return count
