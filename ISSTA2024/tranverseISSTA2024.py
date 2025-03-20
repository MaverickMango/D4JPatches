import os
# https://dl.acm.org/doi/pdf/10.1145/3650212.3652140

# 按编号分patch
def get_alpharepair_stat(work_directory):
    tool_name = 'alphaRepair'
    directory = work_directory + os.sep + tool_name + '_patches'
    # print(directory)
    pathes = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            # print(file_path)
            if '.java' not in file_path:
                continue
            pathes.append(file_path)
    
    projects = set()
    bugs = set()
    patches = []
    for path in pathes:
        sub_path = path.replace(directory + os.sep, '')
        proj, bid, patchId = sub_path.split(os.sep)
        projects.add(proj)
        bugs.add(proj + '-' + bid)
        patches.append('-'.join([tool_name, proj, bid, patchId]))
    return projects, bugs, patches

def get_recoder_stat(work_directory):
    tool_name = 'recoder'
    directory = work_directory + os.sep + tool_name + '_patches'
    # print(directory)
    pathes = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            # print(file_path)
            if '.java' not in file_path:
                continue
            pathes.append(file_path)
    
    projects = set()
    bugs = set()
    patches = []
    for path in pathes:
        sub_path = path.replace(directory + os.sep, '')
        proj, bid, patchId = sub_path.split(os.sep)
        projects.add(proj)
        bugs.add(proj + '-' + bid)
        patches.append('-'.join([tool_name, proj, bid, patchId]))
    return projects, bugs, patches

def get_rewardrepair_stat(work_directory):
    tool_name = 'rewardRepair'
    directory = work_directory + os.sep + tool_name + '_patches'
    # print(directory)
    pathes = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            # print(file_path)
            if '.java' not in file_path:
                continue
            pathes.append(file_path)
    
    projects = set()
    bugs = set()
    patches = []
    for path in pathes:
        sub_path = path.replace(directory + os.sep, '')
        proj, bid, patchId = sub_path.split(os.sep)
        projects.add(proj)
        bugs.add(proj + '-' + bid)
        patches.append('-'.join([tool_name, proj, bid, patchId]))
    return projects, bugs, patches

def get_selfapr_stat(work_directory):
    tool_name = 'selfapr'
    directory = work_directory + os.sep + tool_name + '_patches'
    # print(directory)
    pathes = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            # print(file_path)
            if '.java' not in file_path:
                continue
            pathes.append(file_path)
    
    projects = set()
    bugs = set()
    patches = []
    for path in pathes:
        sub_path = path.replace(directory + os.sep, '')
        proj, bid, patchId = sub_path.split(os.sep)
        projects.add(proj)
        bugs.add(proj + '-' + bid)
        patches.append('-'.join([tool_name, proj, bid, patchId]))
    return projects, bugs, patches

def get_simfix_stat(work_directory):
    tool_name = 'simfix'
    directory = work_directory + os.sep + tool_name + '_patches'
    # print(directory)
    pathes = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            # print(file_path)
            if '.java' not in file_path:
                continue
            pathes.append(file_path)
    
    projects = set()
    bugs = set()
    patches = []
    for path in pathes:
        sub_path = path.replace(directory + os.sep, '')
        proj, bid, patchId = sub_path.split(os.sep)
        projects.add(proj)
        bugs.add(proj + '-' + bid)
        patches.append('-'.join([tool_name, proj, bid, patchId]))
    return projects, bugs, patches

# 按patches-pool分patch，有完整文件路径和文件名
def get_coconut_stat(work_directory):
    tool_name = 'coconut'
    directory = work_directory + os.sep + tool_name + '_patches'
    pathes = []
    for root, dirs, files in os.walk(directory):
        # 获取当前层级相对于root_dir的深度
        depth = root[len(directory):].count(os.sep)
        # 仅保留深度在三层的目录路径
        if depth == 3:
            pathes.append(root)
    
    projects = set()
    bugs = set()
    patches = []
    for path in pathes:
        sub_path = path.replace(directory + os.sep, '')
        proj_bug, tmp, patchId = sub_path.split(os.sep)
        projects.add(proj_bug.split('_')[0])
        bug_name = proj_bug.replace('_', '-')
        bugs.add(bug_name)
        patches.append('-'.join([tool_name, bug_name, patchId]))
    return projects, bugs, patches

def get_cure_stat(work_directory):
    tool_name = 'cure'
    directory = work_directory + os.sep + tool_name + '_patches'
    pathes = []
    for root, dirs, files in os.walk(directory):
        # 获取当前层级相对于root_dir的深度
        depth = root[len(directory):].count(os.sep)
        # 仅保留深度在三层的目录路径
        if depth == 3:
            pathes.append(root)
    
    projects = set()
    bugs = set()
    patches = []
    for path in pathes:
        sub_path = path.replace(directory + os.sep, '')
        proj_bug, tmp, patchId = sub_path.split(os.sep)
        projects.add(proj_bug.split('_')[0])
        bug_name = proj_bug.replace('_', '-')
        bugs.add(bug_name)
        patches.append('-'.join([tool_name, bug_name, patchId]))
    return projects, bugs, patches

def get_edits_stat(work_directory):
    tool_name = 'edits'
    directory = work_directory + os.sep + tool_name + '_patches'
    pathes = []
    for root, dirs, files in os.walk(directory):
        # 获取当前层级相对于root_dir的深度
        depth = root[len(directory):].count(os.sep)
        # 仅保留深度在三层的目录路径
        if depth == 3:
            pathes.append(root)
    
    projects = set()
    bugs = set()
    patches = []
    for path in pathes:
        sub_path = path.replace(directory + os.sep, '')
        proj_bug, tmp, patchId = sub_path.split(os.sep)
        projects.add(proj_bug.split('_')[0])
        bug_name = proj_bug.replace('_', '-')
        bugs.add(bug_name)
        patches.append('-'.join([tool_name, bug_name, patchId]))
    return projects, bugs, patches

def get_tbar_stat(work_directory):
    tool_name = 'tbar'
    directory = work_directory + os.sep + tool_name + '_patches'
    pathes = []
    for root, dirs, files in os.walk(directory):
        # 获取当前层级相对于root_dir的深度
        depth = root[len(directory):].count(os.sep)
        # 仅保留深度在三层的目录路径
        if depth == 3:
            pathes.append(root)
    
    projects = set()
    bugs = set()
    patches = []
    for path in pathes:
        sub_path = path.replace(directory + os.sep, '')
        proj_bug, tmp, patchId = sub_path.split(os.sep)
        projects.add(proj_bug.split('_')[0])
        bug_name = proj_bug.replace('_', '-')
        bugs.add(bug_name)
        patches.append('-'.join([tool_name, bug_name, patchId]))
    return projects, bugs, patches

def get_tbar_stat(work_directory):
    tool_name = 'tbar'
    directory = work_directory + os.sep + tool_name + '_patches'
    pathes = []
    for root, dirs, files in os.walk(directory):
        # 获取当前层级相对于root_dir的深度
        depth = root[len(directory):].count(os.sep)
        # 仅保留深度在三层的目录路径
        if depth == 3:
            pathes.append(root)
    
    projects = set()
    bugs = set()
    patches = []
    for path in pathes:
        sub_path = path.replace(directory + os.sep, '')
        proj_bug, tmp, patchId = sub_path.split(os.sep)
        projects.add(proj_bug.split('_')[0])
        bug_name = proj_bug.replace('_', '-')
        bugs.add(bug_name)
        patches.append('-'.join([tool_name, bug_name, patchId]))
    return projects, bugs, patches

def get_tufano_stat(work_directory):
    tool_name = 'tufano'
    directory = work_directory + os.sep + tool_name + '_patches'
    pathes = []
    for root, dirs, files in os.walk(directory):
        # 获取当前层级相对于root_dir的深度
        depth = root[len(directory):].count(os.sep)
        # 仅保留深度在三层的目录路径
        if depth == 3:
            pathes.append(root)
    
    projects = set()
    bugs = set()
    patches = []
    for path in pathes:
        sub_path = path.replace(directory + os.sep, '')
        proj_bug, tmp, patchId = sub_path.split(os.sep)
        projects.add(proj_bug.split('_')[0])
        bug_name = proj_bug.replace('_', '-')
        bugs.add(bug_name)
        patches.append('-'.join([tool_name, bug_name, patchId]))
    return projects, bugs, patches

# proj和bid直接相连，patchId做目录，basename只有文件名
def get_sequencer_stat(work_directory):
    tool_name = 'sequencer'
    directory = work_directory + os.sep + tool_name + '_patches'
    pathes = []
    for root, dirs, files in os.walk(directory):
        # 获取当前层级相对于root_dir的深度
        depth = root[len(directory):].count(os.sep)
        # 仅保留深度在三层的目录路径
        if depth == 2:
            pathes.append(root)
    
    projects = set()
    bugs = set()
    patches = []
    for path in pathes:
        sub_path = path.replace(directory + os.sep, '')
        combine, patchId = sub_path.split(os.sep)
        split_index = next(i for i, char in enumerate(combine) if char.isdigit())
        pid = combine[:split_index]
        bid = combine[split_index:]
        projects.add(pid)
        bug_name = pid + '-' + bid
        bugs.add(bug_name)
        patches.append('-'.join([tool_name, bug_name, patchId]))
    return projects, bugs, patches

def output_bug_patch_count(projects, bugs, tools, patches):
    # 按projects统计patches的数量
    project_patch_count = {}
    for pid in projects:
        count = len([pt for pt in patches if pid in pt])
        project_patch_count.update({pid: count})

    # 按tools统计patches的数量
    tool_patch_count = {}
    for tool in tools:
        count = len([pt for pt in patches if tool in pt])
        tool_patch_count.update({tool: count})

    # 按bugs统计patches的数量
    bug_patch_count = {}
    for bug in bugs:
        count = len([pt for pt in patches if bug in pt])
        bug_patch_count.update({bug: count})
    return project_patch_count, tool_patch_count, bug_patch_count

def total():
    work_directory = os.path.dirname(os.path.abspath(__file__)) + os.sep + 'src_d4j_ori_patches'
    # print(work_directory)
    tools = ['alpharepair', 'coconut', 'cure', 'edits', 'recoder', 'rewardrepair', 'selfapr', 'sequencer', 'simfix', 'tbar', 'tufano']
    projects = set()
    bugs = set()
    patches = set()
    for tool in tools:
        func = f'get_{tool}_stat'
        proj, b, p = globals()[func](work_directory)
        projects.update(proj)
        bugs.update(b)
        patches.update(p)
    return projects, bugs, tools, patches


def find_compilable(projects, bugs, tools):
    compilable = []
    with open('/mnt/D4JPatches/ISSTA2024/compilable_patches_ISSTA24.txt', 'r') as f:
        lines = f.readlines()
        compilable.extend(lines)
    compilable = [p.lower() for p in compilable]
    projs_lower = {p.split('-')[1] for p in compilable}
    projects = [p for p in projects if p in projs_lower]
    vids_lower = {'-'.join([p.split('-')[1], p.split('-')[2]]) for p in compilable}
    bugs = [b for b in bugs if b in vids_lower]
    ts_lower = {p.split('-')[0] for p in compilable}
    tools = [t for t in tools if t in ts_lower]
    return projects, bugs, tools, compilable


if __name__ == '__main__':
    projects, bugs, tools, patches = total()
    project_patch_count, tool_patch_count, bug_patch_count = output_bug_patch_count(projects, bugs, tools, patches)
    print('project的数量(value为patch数): ' + str(len(project_patch_count)), project_patch_count)
    print('tool的数量(value为patch数): ' + str(len(tool_patch_count)), tool_patch_count)
    print('bug的数量(value为patch数): '  + str(len(bugs)), bug_patch_count)
    print('Total patches:', len(patches))