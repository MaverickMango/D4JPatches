import os

def output_patch_stat():
    directory = os.path.dirname(os.path.abspath(__file__))
    pathes = []
    for root, dirs, files in os.walk(directory):
        # 获取当前层级相对于root_dir的深度
        depth = root[len(directory):].count(os.sep)
        # 仅保留深度在三层的目录路径
        if depth == 4:
            pathes.append(root)
            # print(root)

    projects = set() # 所有的project名字都替换为小写
    bugs = set()
    tools = set()
    patches = []
    for path in pathes:
        base_name = os.path.basename(path) # 获取文件名
        items = base_name.split('_')
        bug_name = '-'.join(items[0:2]).lower() # 获取bug_name
        bugs.add(bug_name)
        projects.add(items[0].lower())
        tool_name = items[2]
        tools.add(tool_name)
        patch_name = '-'.join([bug_name, tool_name, 'manual'])
        if len(items) == 4:
            patch_name += items[3]
        patches.append(patch_name)
    return projects, bugs, tools, patches

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


if __name__ == '__main__':
    projects, bugs, tools, patches = output_patch_stat()
    project_patch_count, tool_patch_count, bug_patch_count = output_bug_patch_count(projects, bugs, tools, patches)
    print('project对应的bug数', project_patch_count)
    print('tool的数量: ' + str(len(tool_patch_count)), tool_patch_count)
    print('bug的数量: '  + str(len(bugs)), bug_patch_count)
    print('Total patches:', len(patches))