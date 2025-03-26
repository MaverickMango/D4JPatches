import pandas as pd

bugs_inputs = '/mnt/D4JPatches/bugs_inputs.csv'
compilable_patches_file = '/mnt/D4JPatches/ISSTA2024/plausible_patch_list.txt'

compilable_patches_df_output = '/mnt/D4JPatches/ISSTA2024/plausible_patches.csv'
overlap_compilable_patches_output = '/mnt/D4JPatches/ISSTA2024/overlap_plausible_patches_ISSTA2024.txt'
overlap_compilable_df_output = '/mnt/D4JPatches/ISSTA2024/overlap_plausible_patches.csv'

def split_str(value):
    return pd.Series(str(value).split('_'))


def pivot_proj_tool(df):
    tool_project_patch_count = df.groupby(['tool', 'proj']).size().unstack(fill_value=0)
    tool_proj_bug_count = df.groupby(['tool', 'proj'])['bid'].nunique().unstack(fill_value=0)
    result = pd.DataFrame()
    for tool in df['tool'].unique():
        result[f'{tool}_patch_count'] = tool_project_patch_count.loc[tool]
        result[f'{tool}_bug_count'] = tool_proj_bug_count.loc[tool]
    final_df = result.reset_index().rename(columns={'index': 'proj'})
    return final_df

def compute_overlap(captive=False):
    bugs_names = pd.read_csv(bugs_inputs)
    # print('历史版本数据集中的bug数量: ' + str(len(bugs_names)), split_name_by_project(bugs_names, '_'))
    # bugs_names[['proj', 'bid']] = bugs_names['bug_name'].apply(split_str) # capitial
    bugs_names['bug_name'] = bugs_names['bug_name'].str.lower()

    compilable = []
    with open(compilable_patches_file, 'r') as f:
        lines = f.read().splitlines()
        compilable.extend(lines)
    compilable = [p.lower() for p in compilable]
    df = pd.DataFrame([p.split('-') for p in compilable], columns=['tool', 'proj', 'bid', 'patch'])
    final_df = pivot_proj_tool(df)
    final_df.to_csv(compilable_patches_df_output)

    df['bug_name'] = df['proj'] + '_' + df['bid']
    # overlap_df = df[df['proj', 'bid'].apply(tuple, axis=1).isin(bugs_names[['proj', 'bid']].apply(tuple, axis=1))]
    overlap_df = df[df['bug_name'].isin(bugs_names['bug_name'])].copy()

    overlap_df['bug_name'].apply(split_str)
    overlap_df.drop(columns=['bug_name'], inplace=True)
    overlap_df.insert(3, 'patch', overlap_df.pop('patch'))
    with open(overlap_compilable_patches_output, 'w', encoding='utf-8') as file:
        for _, row in overlap_df.iterrows():
            line = '-'.join(row.astype(str))
            file.write(line+'\n')
    final_overlap = pivot_proj_tool(overlap_df)
    final_overlap.to_csv(overlap_compilable_df_output)


compute_overlap()