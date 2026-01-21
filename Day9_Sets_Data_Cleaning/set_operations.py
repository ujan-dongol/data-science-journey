

day1_visitors = {"Ujan", "Ram", "Shyam"}
day2_visitors = {"Ujan", "Hari"}

print("Common visitors:", day1_visitors & day2_visitors)
print("Only Day 1:", day1_visitors - day2_visitors)


# & means INTERSECTION
# 👉 Intersection = common elements in both sets
# Common visitors: {'Ujan'}

#(minus) in SET means
#day1_visitors - day2_visitors
# 👉 Elements in day1_visitors but NOT in day2_visitors


