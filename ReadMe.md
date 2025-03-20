# 补丁总数统计
- Manual2023(之前的仓库)的全部补丁数：584 工具数：41
```
{'': 287, 'capgen': 7, 'sequencer': 5, 'fixminer': 4, 'jgenprog': 2, 'kali': 10, 'coming': 1, 'unknown1': 11, 'avatar': 1, 'benchmark': 3, 'knod': 9, 'arja': 7, 'tbar': 70, 'jkali': 1, 'rsrepair': 7, 'acs': 9, 'cardumen': 1, 'purify': 1, 'arjae': 2, 'simfix': 7, 'sharpfix': 1, 'bugbuilder': 4, 'kpar': 15, 'jmutrepair': 2, 'jaid': 9, 'rapidcapr': 1, 'hdrepair': 7, 'repairingredients': 1, 'deptest': 1, 'tenure': 1, 'sofix': 6, 'transplantfix': 4, 'coconut': 8, 'genprog': 5, 'aprconfig': 3, 'nopol': 5, 'capr': 15, 'sketchfix': 3, 'buggy': 42, 'ssfix': 3, 'cure': 3}
```
- ASE2020的全部补丁数：953 工具数：21
```
 {'capgen': 66, 'fixminer': 33, 'jgenprog': 20, 'kali': 88, 'avatar': 57, 'tbar': 72, 'jkali': 25, 'rsrepair': 41, 'sequencer': 73, 'acs': 22, 'cardumen': 12, 'arja': 57, 'kpar': 63, 'jaid': 81, 'jmutrepair': 22, 'dynamoth': 22, 'simfix': 69, 'sofix': 24, 'genprog': 50, 'nopol': 31, 'sketchfix': 25}
```
- ISSTA2024的全部补丁数：134297 工具数：11
```
{'alpharepair': 13439, 'coconut': 12900, 'cure': 13900, 'edits': 13300, 'recoder': 8768, 'rewardrepair': 14000, 'selfapr': 14000, 'sequencer': 10181, 'simfix': 10117, 'tbar': 10392, 'tufano': 13300}
```
# 和历史数据集的交集统计
- 之前仓库中overlap的bug的数量:101
```
{'math': 31, 'closure': 32, 'time': 4, 'jacksoncore': 2, 'lang': 23, 'codec': 3, 'jsoup': 2, 'mockito': 3, 'gson': 1}
Total patches: 329
```
- ASE2020中overlap的bug的数量:67
```
{'Closure': 26, 'Lang': 16, 'Math': 23, 'Time': 2}
Total patches: 372
```
- ISSTA2024中overlap的bug的数量:38
```
{'math': 8, 'closure': 10, 'time': 2, 'jacksoncore': 2, 'codec': 4, 'lang': 5, 'jsoup': 4, 'mockito': 2, 'gson': 1}
Total patches: 40423
```
# 可编译补丁
## ISSTA2024
- 全部可编译补丁: 1346 工具数：8
- 工具对应的补丁数:  {'alpharepair': 95, 'coconut': 768, 'cure': 109, 'edits': 2, 'recoder': 106, 'rewardrepair': 164, 'selfapr': 34, 'simfix': 68}
- ISSTA2024中可编译的overlap的bug的数量:23 {'jsoup': 3, 'closure': 9, 'gson': 1, 'codec': 2, 'jacksoncore': 2, 'time': 1, 'lang': 5}
- Total compilable patches: 386

# 全部补丁集合
- 见各个目录下

> 所有补丁暂未去重完成