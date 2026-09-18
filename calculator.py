print("Please input Periods and Rate")
print("Periods = ", end="")
periods = int(input())
print("Rate = ", end="")
rate = float(input()) * 0.01
# print(n, r)
cost = periods
value = 0
for i in range(0, periods):
    value += (1 + rate) ** i
# print(value)
roi = (value / cost) - 1
print(f"ROI = {roi:.2%}")
