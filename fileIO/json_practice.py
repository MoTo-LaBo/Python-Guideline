import json

with open("example.json") as f:
    data = json.load(f)


print(data['glossary']['GlossDiv'])

new_json = {'key1': 'value1', 'key2': (1, 'value2')}  # json file に dump すると tuple が list に変わる
with open("new.json", 'w') as f:
    json.dump(new_json, f)

with open("new.json", 'r') as f:
    new_json_reload = json.load(f)

print(type(new_json_reload['key2']))  # json.load しても list のまま
print(new_json_reload['key2'])        # こういう挙動をする事を理解しておく
# javascript には, tuple がないのでそれに近い list に変換される


# 実際に json file に保存して、アクセスするというやり方


# ただただ文字列を送る,読み込むというやり方がある
json_str = json.dumps(new_json)
print(json_str)
print(type(json_str))

pytho_data = json.loads(json_str)
print(pytho_data)
print(type(pytho_data))