import random

def evaluate_clauses(clauses, assignment):
    satisfied_clauses = sum(1 for (x, y, z) in clauses if assignment[abs(x)-1] == x or assignment[abs(y)-1] == y or assignment[abs(z)-1] == z)
    return satisfied_clauses

def max_3sat(n, clauses):
    best_assignment = None
    best_satisfied = 0
    for _ in range(10000): 
        assignment = [random.choice([-1, 1]) for _ in range(n)]
        satisfied = evaluate_clauses(clauses, assignment)
        if satisfied > best_satisfied:
            best_satisfied = satisfied
            best_assignment = assignment
            if satisfied >= round(len(clauses) * 7 / 8): 
                break
    return best_assignment

def main():
    n = int(input())
    m = int(input())
    clauses = []
    for _ in range(m):
        clause = list(map(int, input().split()))
        clauses.append(tuple(clause))
    
    solution = max_3sat(n, clauses)
    if solution:
        print(' '.join(map(str, solution)))
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()