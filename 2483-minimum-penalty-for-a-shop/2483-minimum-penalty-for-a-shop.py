class Solution:
    def bestClosingTime(self, customers: str) -> int:
        pen = customers.count("Y")
        min_pen = pen
        sol = 0
        
        if not pen:
            return sol
        for i in range(len(customers)):
            if customers[i] == "Y":
                pen -= 1
                if min_pen > pen:
                    min_pen = pen
                    sol = i+1
            else:
                pen += 1
        
        return sol