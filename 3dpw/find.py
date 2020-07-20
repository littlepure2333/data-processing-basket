# encoding: utf-8

import script
import os
from findposition1 import findposition1

pkl_dir = "G:/sequenceFiles/train"
json_folder = "G:/imageFiles"
mew_pkl_dir = ""
script.get_path(pkl_dir, "pkl")
pkl_list = script.path_list
# print(pkl_list)
for pkl in pkl_list:
    class_name = pkl.split("\\")[3].split(".")[0]
    json_dir = os.path.join(json_folder, class_name,"result")
    # print(json_dir)
    print(pkl)
    new_pkl_dir = pkl_dir + "/new/" + class_name + ".pkl"
    # print(new_pkl_dir)
    findposition1(json_dir, pkl, new_pkl_dir)

