if __name__ == '__main__':
    students = []
    scores = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        students.append([name, score])
        scores.append(score)
        
    # sort students list based on their scores
    students.sort(key=lambda x: x[1])
    
    scores = set(scores)
    sorted_scores = sorted(list(scores))
    
    second_lowest_grade = sorted_scores[1]
    
    second_lowest_grade_students = sorted(student[0] for student in students if student[1] == second_lowest_grade)
    
    for name in second_lowest_grade_students:
        print(name)
    
