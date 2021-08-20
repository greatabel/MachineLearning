import json


with open("data/simplified-nq-train.jsonl", "r") as json_file:
    json_list = list(json_file)

# print('@'*20, len(json_list))

length = len(json_list)

# for json_str in json_list[0:1]:
#     result = json.loads(json_str)
#     print(f"result: {result}")
#     print(isinstance(result, dict))


with open("data/mytrain.jsonl", "w") as outfile:
    for json_str in json_list[0:500]:
        result = json.loads(json_str)
        json.dump(result, outfile)
        outfile.write("\n")


# with open('data/mytest.jsonl', 'w') as outfile:
# 	for json_str in json_list[length//2:]:
# 		result = json.loads(json_str)
# 		json.dump(result, outfile)
# 		outfile.write('\n')
