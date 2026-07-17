# TASK: Write a function called grade_report(scores) that:
# - Takes a list of integer scores (0-100)
# - Returns a dictionary with:
#     "average": the average score (rounded to 1 decimal place)
#     "highest": the highest score
#     "lowest": the lowest score
#     "passed": count of scores >= 40
#     "failed": count of scores < 40

def grade_report(scores):
    
    passed = 0
    failed = 0
    
    for i in range(len(scores)):
       if scores[i] >= 40:
           passed += 1
       else:
           failed += 1   
      
    
    average = round(sum(scores) / len(scores), 1)
    maximum = max(scores)
    minimum = min(scores)
    
    result = { 
        "average" : average,
        "highest": maximum,
        "lowest": minimum,
        "passed": passed,
        "failed": failed

    }
    
    return result
    

# Expected behavior:
print(grade_report([85, 42, 33, 91, 40, 15]))
# Expected: {'average': 51.0, 'highest': 91, 'lowest': 15, 'passed': 4, 'failed': 2}

print(grade_report([100, 100, 100]))
# Expected: {'average': 100.0, 'highest': 100, 'lowest': 100, 'passed': 3, 'failed': 0}