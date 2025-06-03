import random

# 生徒データを作成
students = []
for i in range(1, 21):
    student = {
        "name": f"生徒{i}",
        "国語": random.randint(40, 100),
        "英語": random.randint(40, 100),
        "情報": random.randint(40, 100)
    }
    student["合計"] = student["国語"] + student["英語"] + student["情報"]
    students.append(student)

# 合計点で降順に並び替え
students_sorted = sorted(students, key=lambda x: x["合計"], reverse=True)

# 結果を表示
for s in students_sorted:
    print(f'{s["name"]}: 国語={s["国語"]}, 英語={s["英語"]}, 情報={s["情報"]}, 合計={s["合計"]}')
# 平均点を計算
average = sum(s["合計"] for s in students_sorted) / len(students_sorted)
print(f'平均点: {average:.2f}')
# 上位5名を表示
print("\n上位5名:")
for s in students_sorted[:5]:
    print(f'{s["name"]}: 合計={s["合計"]}')
# 下位5名を表示
print("\n下位5名:")
for s in students_sorted[-5:]:
    print(f'{s["name"]}: 合計={s["合計"]}')
# 合計点の最高点と最低点を表示
max_score = max(s["合計"] for s in students_sorted)
min_score = min(s["合計"] for s in students_sorted)
print(f'\n最高点: {max_score}, 最低点: {min_score}')
# 合計点の中央値を計算
def median(lst):
    n = len(lst)
    sorted_lst = sorted(lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]
median_score = median([s["合計"] for s in students_sorted])
print(f'中央値: {median_score:.2f}')
# 合計点の標準偏差を計算
import statistics
std_dev = statistics.stdev([s["合計"] for s in students_sorted])
print(f'標準偏差: {std_dev:.2f}')
# 各科目の平均点を計算
def subject_average(subject):
    return sum(s[subject] for s in students_sorted) / len(students_sorted)
print(f'国語の平均点: {subject_average("国語"):.2f}')
print(f'英語の平均点: {subject_average("英語"):.2f}')
print(f'情報の平均点: {subject_average("情報"):.2f}')
# 各科目の最高点と最低点を表示
def subject_max_min(subject):
    max_score = max(s[subject] for s in students_sorted)
    min_score = min(s[subject] for s in students_sorted)
    return max_score, min_score
max_kokugo, min_kokugo = subject_max_min("国語")
max_eigo, min_eigo = subject_max_min("英語")
max_jouhou, min_jouhou = subject_max_min("情報")
print(f'国語の最高点: {max_kokugo}, 最低点: {min_kokugo}')
print(f'英語の最高点: {max_eigo}, 最低点: {min_eigo}')
print(f'情報の最高点: {max_jouhou}, 最低点: {min_jouhou}')