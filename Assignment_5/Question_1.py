# Write a Python class to implement pow(x, n)

# Explanation:

# Use should be able to find the nth power of the x.(i.e x*x*x*x...n times)

# You must implement it using Class

# Sample Input:

# x: 10
# n: 2

# Sample Output:

# 100


# ----> Solutions <------


class py_solution:
    def pow(self, x, n):
         if x == 0 or x == 1 or n == 1:
            return x

            if x == -1:
                if n % 2 == 0:
                    return 1
                else:
                    return -1

            if n == 0:
                return 1
            if n < 0:
                return 1/self.pow(x, -n)
            val = self.pow(x, n//2)
            if n % 2 == 0:
                return val*val
            return val*val*x

x = int(input("Base value: "))
n = int(input("Power value: "))
p = pow(x, n)

print("sample Input:\nx:", x, "\nn:", n, "\nSample Output:\n", p)
