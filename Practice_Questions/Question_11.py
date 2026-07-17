department_visits = ["ER", "OPD", "ER", "Radiology", "OPD", "ER", "Lab", "OPD"]

visit_counts = {}

# Your loop here
for i, j in enumerate(department_visits):
    if j not in visit_counts:
        print(f"New department seen at position {i}: {j}")
        visit_counts[j] = 0
    visit_counts[j] += 1 


print(visit_counts)

