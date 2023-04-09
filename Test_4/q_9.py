# d = {'a':1,'b':{'x':2,'y':3},'c':4}
# flat = {}

# for key, value in d.items():
#     if isinstance(value, dict):
#         for sub_key, sub_value in value.items():
#             flat[f"{key}.{sub_key}"] = sub_value
#     else:
#         flat[key] = value

# print(flat)
