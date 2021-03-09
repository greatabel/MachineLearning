import time
import difflib

# 最小编辑距离  http://www.jianshu.com/p/466cf6624e26

def normal_leven(str1, str2):
    len_str1 = len(str1) + 1
    len_str2 = len(str2) + 1
    #create matrix
    matrix = [0 for n in range(len_str1 * len_str2)]
    #init x 
    for i in range(len_str1):
        matrix[i] = i
    #init y
    for j in range(0, len(matrix), len_str1):
        if j % len_str1 == 0:
            matrix[j] = j // len_str1
    
    for i in range(1, len_str1):
        for j in range(1, len_str2):
            if str1[i-1] == str2[j-1]:
                cost = 0
            else:
                cost = 1
            matrix[j*len_str1+i] = min(matrix[(j-1)*len_str1+i]+1,
                                        matrix[j*len_str1+(i-1)]+1,
                                        matrix[(j-1)*len_str1+(i-1)] + cost)
    
    return matrix[-1]

def difflib_leven(str1, str2):
    leven_cost = 0
    s = difflib.SequenceMatcher(None, str1, str2)
    for tag, i1, i2, j1, j2 in s.get_opcodes():
        #print('{:7} a[{}: {}] --> b[{}: {}] {} --> {}'.format(tag, i1, i2, j1, j2, str1[i1: i2], str2[j1: j2]))
    
        if tag == 'replace':
            leven_cost += max(i2-i1, j2-j1)
        elif tag == 'insert':
            leven_cost += (j2-j1)
        elif tag == 'delete':
            leven_cost += (i2-i1)
    return leven_cost        

if __name__ == '__main__':
    str1 = input('str1:')
    str2 = input('str2:')
    print('normal_leven: {}'.format(normal_leven(str1, str2))) 
    print('python_difflib_leven: {}'.format(difflib_leven(str1, str2)))
