import os, sys
import subprocess
import tranverseManual2023

buggy_file_root = '/mnt/d4j_bug_info/buggyfiles'
# diff -up <(awk '{ gsub(/[ \t\n]+/, ""); print }' file1.java) <(awk '{ gsub(/[ \t\n]+/, ""); print }' file2.java)
diff_command = "diff -urwE --exclude='*.patch' --exclude='*.fix.java' {buggy} {patched} > {output}"

def get_diff_dict(pId, bId):
    pId = pId.lower()
    bId = bId.lower()
    work_dir = os.sep.join([pId, '_'.join([pId, bId, 'buggy'])])
    return work_dir

def get_duplicate_patch(proj_bId_path):
    results = []
    for proj, bId, path in proj_bId_path:
        base_name = os.path.basename(path)
        buggy_file = buggy_file_root + os.sep + get_diff_dict(proj, bId)
        # 对比差异

        # 去重

        # 输出patch文件
        output_name = path + os.sep + base_name + '.patch'
        if 'plasusible' in path:
            output_name = base_name + '-plausible.patch'
        command = diff_command.format(buggy=buggy_file, patched=path, output=output_name)
        # print(command)
        # 执行一个简单的shell命令
        result = subprocess.run(command, capture_output=True, text=True, shell=True)
        results.append(result)
    return results
        

# Manual2023
r = get_duplicate_patch(tranverseManual2023.get_diff_path())
print(r)