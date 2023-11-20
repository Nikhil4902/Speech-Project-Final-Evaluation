from __future__ import annotations
import os

base_path: str = "LA/ASVspoof2019_LA_cm_protocols/"
file_names: list[str] = [base_path + f"ASVspoof2019.LA.cm.{i}.txt" for i in ["dev.trl", "eval.trl", "train.trn"]]
user_subsets: list[list[int]] = [[69,72,74,77,78,108],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],[79,83,85,87,88,91,96]]
for file_name, user_subset in zip(file_names, user_subsets):
    print(file_name)
    if not os.path.exists(file_name):
        print("File does not exist")
    else:
        with open(file_name, 'r') as f:
            lines = f.readlines()

        with open(file_name, 'w') as f:
            user_strs: list[str] = ["LA_" + f"{user:0>4}" for user in user_subset]
            new_lines = [line for line in lines if line.split()[0] in user_strs]
            f.writelines(new_lines)