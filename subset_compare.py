import csv
import os,sys

root = os.path.dirname(os.path.abspath(__file__))
# 读取csv文件内容
def read_csv(file):
    with open(file,'r',encoding='utf8') as f:
        data = csv.DictReader(f)
        data = [line['bug_name'] for line in data]
    return data

def split_name_by_project(bugs_names, split):
    splited_count = {}
    for bug_name in bugs_names:
        pid = bug_name.split(split)[0]
        if pid not in splited_count.keys():
            splited_count.update({pid: 1})
        else:
            splited_count[pid] += 1
    return splited_count

def compute_overlap(bug_patch_count, captive=True):
    bugs_names = read_csv(f'{root}{os.sep}bugs_inputs.csv')
    # print('历史版本数据集中的bug数量: ' + str(len(bugs_names)), split_name_by_project(bugs_names, '_'))
    overlap = {}
    total_count = 0
    for bug_count in bug_patch_count.items():
        bug = bug_count[0]
        count = bug_count[1]
        if not captive:
            bugs_names = [bn.lower() for bn in bugs_names]
        if bug.replace('-', '_') in bugs_names:
            overlap.update({bug:count})
            total_count += count
    return overlap, total_count

from Manual2023.tranverseManual2023 import *
# patches from Manual2023
projects, bugs, tools, patches = output_patch_stat()
project_patch_count, tool_patch_count, bug_patch_count = output_bug_patch_count(projects, bugs, tools, patches)
overlap, total_count = compute_overlap(bug_patch_count, False)
print('之前仓库中overlap的bug的数量:' + str(len(overlap)), split_name_by_project(overlap, '-'))
print('Total patches:', total_count)

from ASE2020.tranverseASE2020 import *
# patches from ASE2020
projects, bugs, tools, patches = output_patch_stat()
project_patch_count, tool_patch_count, bug_patch_count = output_bug_patch_count(projects, bugs, tools, patches)
overlap, total_count = compute_overlap(bug_patch_count)
print('ASE2020中overlap的bug的数量:' + str(len(overlap)), split_name_by_project(overlap, '-'))
print('Total patches:', total_count)

from ISSTA2024.tranverseISSTA2024 import *
# patches from ISSTA2024
projects, bugs, tools, patches = total()
project_patch_count, tool_patch_count, bug_patch_count = output_bug_patch_count(projects, bugs, tools, patches)
overlap, total_count = compute_overlap(bug_patch_count, False)
print('ISSTA2024中overlap的bug的数量:' + str(len(overlap)), split_name_by_project(overlap, '-'))
print('Total patches:', total_count)

print('多项总计的补丁数量: ')