# Write a program "flatten_dict.py" to flatten a nested dictionary by joining the keys with '.' character.
# For example if given dictionary is {'a':1,'b':{'x':2,'y':3},'c':4} 
# it should return {'a':1,'b.x':2,'b.y':3,'c':4}.

d = {'a':1,'b':{'x':2,'y':3},'c':4}
flat = {}

for key, value in d.items():
    if isinstance(value, dict):
        for sub_key, sub_value in value.items():
            flat[f"{key}.{sub_key}"] = sub_value
    else:
        flat[key] = value

print(flat)
