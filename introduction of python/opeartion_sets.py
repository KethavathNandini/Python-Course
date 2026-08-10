std1 = {"english", "math", "social", "hindi"}
std2 = {"english", "chemistry", "social", "phy"}
# intersection() / |{phi}
common_sub = std1.intersection(std2)
print(common_sub)
# union()
all_sub = std1.union(std2)
print(all_sub)

# difference of sets
diff_std = std1.difference(std2)
print(diff_std)
