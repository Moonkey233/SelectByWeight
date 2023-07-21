# -*- coding: utf-8 -*-
# Author: Moonkey_
# Date: 2023/7/21
# Github: https://github.com/Moonkey233/SelectByWeight
# Copyright (c) 2023, Moonkey_
# All rights reserved.

import os
import random

def main():
    os.system("cls")
    try:
        with open("select.txt", "r", encoding="utf-8") as file:
            linelist = file.readlines()
            file.close()
    except Exception as e:
        print("File Open Error", e)
        return

    weight = 0
    playlist = []
    for i in linelist:
        s = str(i).strip()
        b = s.find("[")
        e = s.find("]")
        num = s[b+1 : e]

        s = (s[:b] + s[e+1:]).strip()
        if s == "":
            continue
        if s[0] == "#":
            print(f"Excluded: '{s[1:]}'")
            continue
        if b == -1 or e == -1 or not num.isnumeric():
            print(f"Invaild Weight Error: '{s}'")
            continue

        if num.isnumeric():
            weight += int(num)
        playlist.append({s: weight})

    if weight == 0:
        print("Weight Error: Total weight is 0")
        return
    
    num = 0
    print(f"\nAll Selections: \n")
    try:
        for i in playlist:
            for key in i:
                percent = round((i[key] - num) / weight * 100, 2)
                print(f"'{key}' Weight: {percent}% Range: [{num}, {i[key]})")
                num = i[key]
    except Exception as e:
        print("Calculate Weight Error", e)

    print("Total Weight:", weight)
    print()
    flag = True
    rand = random.randint(0, weight-1)

    try:
        for i in playlist:
            for key in i:
                if i[key] > rand:
                    print(f"Random Selected ({rand}):", "\033[33m" + key + "\033[0m")
                    flag = False
            if not flag:
                break
    except Exception as e:
        print("Random Select Error", e)

if __name__ == "__main__":
    while True:
        main()
        print()
        os.system("pause")
