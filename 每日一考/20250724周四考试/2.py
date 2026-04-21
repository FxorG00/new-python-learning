def sol(students) :
    new_dict=dict()
    for k in students.keys() :
        new_dict[k]=sum(students[k].values())/len(students[k])
        new_dict[k]=f"{new_dict[k]:.2f}"
    return new_dict
students = {
    "Alice": {
        "Math": 85,
        "English": 90,
        "Science": 78
    },
    "Bob": {
        "Math": 92,
        "English": 88,
        "Science": 95
    },
    "Charlie": {
        "Math": 70,
        "English": 75,
        "Science": 80
    }
}
ans=sol(students)
for k in ans.keys() :
    print(f"{k} {ans[k]}")