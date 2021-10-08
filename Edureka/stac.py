

i = ["file1", "file2", "join", "file3", "file4", "join", "file5", "file6"]


o = [["file1", "file2", "join"], ["file3", "file4", "join"], "file5",
     "file6"]
for new in i:
    if i in o:

       new = i.index('file2', 'file1')
       print(new)