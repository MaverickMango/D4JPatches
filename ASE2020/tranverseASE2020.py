import os

# 遍历文件夹，列出数据属性表
def list_attributes():
    directory = os.path.dirname(os.path.abspath(__file__))
    # print(directory)
    patches = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if '.patch' not in file_path:
                continue
            patches.append(file_path)
    return patches


def output_patch_stat():
    directory = os.path.dirname(os.path.abspath(__file__))
    # print(directory)  
    projects = set()
    bugs = set()
    tools = set()
    patches = []

    for path in list_attributes():
        path = path.replace(directory, "") # 去掉前缀
        patches.append(path)
        # print(path)
        base_name = os.path.basename(path) # 获取文件名
        bug_name = '-'.join(base_name.split('-')[1:3]) # 获取bug_name
        bugs.add(bug_name)
        prefix = path.replace(os.sep + base_name, "").split(os.sep) # 获取前缀
        # print(prefix)
        if len(prefix) == 4:
            project_name = prefix[-1] # 获取项目id
            projects.add(project_name)
            tool_name = prefix[-2] # 获取工具名
            tools.add(tool_name)
        else:
            projects.add(base_name.split('-')[1])
            tools.add(base_name.split('-')[3].replace('.patch', ''))
            # print('Special directory(patches counted):', path)
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