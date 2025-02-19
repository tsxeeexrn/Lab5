import re

def match_1(s):
    return bool(re.fullmatch(r'a*b*', s))

def match_2(s):
    return bool(re.fullmatch(r'a{1}b{2,3}', s))

def find_lowercase(s):
    return re.findall(r'[a-z]+_[a-z]+', s)

def find_uppercase(s):
    return re.findall(r'[A-Z][a-z]+', s)

def match_5_finding_anything(s):
    return bool(re.fullmatch(r'a.*b', s))

def replace(s):
    return re.sub(r'[ ,.]', ':', s)

def snake_vs_camel(s):
    return ''.join(word.capitalize() for word in s.split('_'))

def split_at_uppercase(s):
    return re.split(r'(?=[A-Z])', s)

def insert_spaces_between_capitals(s):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', s)

def camel_to_snake(s):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()
if __name__ == "__main__":
    test_string = "aabb"
    print(match_1(test_string))  
    print(match_2(test_string))
    print(find_lowercase("abc_def ghi_jkl"))
    print(find_uppercase("HelloAlibek TestString"))
    print(match_5_finding_anything("axb"))
    print(replace("Hello_Alibek. This is a test"))
    print(snake_vs_camel("this_is_a_test"))
    print(split_at_uppercase("HelloAlibek"))
    print(insert_spaces_between_capitals("HelloAlibek"))
    print(camel_to_snake("HelloAlibek"))
