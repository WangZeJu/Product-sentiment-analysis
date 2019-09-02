# !/usr/bin/python
# coding = utf-8

def open_doc(i):
    filename = '/safevent/' + str(i) + '.txt'
    with open(filename) as f:
        f_data = f.read()
    return f_data


if __name__ == "__main__":
   data = []
   for i in range(1,413):
       data.append(open_doc(i))
   print(len(data))
