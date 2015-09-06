import os


# Copy and paste whatever prefix you want to remove to either di_prefix or fi_prefix. 
#If you want to remove directory prefix, UNCOMMENT THE LAST LINE. Then run the script.

# File prefixes
# 'MIT18_03S10_'
# 'MIT18_02SC_'
# 'MIT18_06SCF11_'

# Directory prefixes
# 'session-'

# Change the variables below to whatever prefix you want to remove
fi_prefix = 'MIT18_03S10_'
di_prefix = "session-"

def remove_prefix(prefix, typ="file"):
    if typ == "file":
        fi_or_dir = 2
    elif typ == "directory":
        fi_or_dir = 1
    else:
        print "invalid file type"
        exit()
    li = [i for i in os.walk(os.getcwd())]
    for di in li:
        root = di[0]
        print root
        for ele in di[fi_or_dir]:
            #print ele
            if ele[:len(prefix)] == prefix:
                new_name = os.path.join(root, ele[len(prefix):])
                old_name = os.path.join(root, ele)
                print old_name
                print new_name
                os.rename(old_name, new_name)


remove_prefix(fi_prefix)
# remove_prefix(di_prefix, "directory")
