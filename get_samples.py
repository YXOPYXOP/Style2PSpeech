import os
import glob
import json


dir_root = '/apdcephfs_cq8/share_303090499/users/rayrniu/cosyvoice-style/Demo/static/data'
ref_root = '/apdcephfs_cq8/share_303090499/users/rayrniu/cosyvoice-style/Demo/static/ref_wavs'

dic = {}
# for task in os.listdir(dir_root):
#     task_name = task.split('-')[1]
#     data = []
#     with open(os.path.join(dir_root, task, 'transcript.txt'), 'r') as f:
#         lines = f.readlines()
#     for line in lines:
#         line = line.strip().split('|')
#         wav_path = line[0]
#         line = line[1].split('</p>')
#         text = line[0].replace('<p>合成文本:', '')
#         line = line[1].split('</audio>')
#         ref_timbre = line[0].split('src="')[1].replace('">', '')
#         ref_style = line[1].split('src="')[1].replace('">', '')
#         data.append({
#             "text": text,
#             "voice_ref": ref_timbre,
#             "style_ref": ref_style,
#             "result1": os.path.join('static/data', task, 'nosty', wav_path),
#             "result2": os.path.join('static/data', task, 'sty', wav_path)
#         })
#     dic[task_name] = data
# with open('/apdcephfs_cq8/share_303090499/users/rayrniu/cosyvoice-style/Demo/static/samples.json', 'wt', encoding='utf8') as f:
#     json.dump(dic, f, ensure_ascii=False, indent=4)

with open('/apdcephfs_cq8/share_303090499/users/rayrniu/cosyvoice-style/Demo/static/samples.json', 'rt', encoding='utf8') as f:
    dic = json.load(f)

for task in dic.keys():
    for i in range(len(dic[task])):
        domain = dic[task][i]['style_ref'].split('Domain_')[1].split('_')[0]
        dic[task][i]['domain'] = domain

with open('/apdcephfs_cq8/share_303090499/users/rayrniu/cosyvoice-style/Demo/static/samples.json', 'wt', encoding='utf8') as f:
    json.dump(dic, f, ensure_ascii=False, indent=4)
