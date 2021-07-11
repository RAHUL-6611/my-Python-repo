#-------------------------------
this = "                     hoiii                      "

print(this)
print(this.strip())

#-----------------------------


def replace_and_strip(string ,word):

    r_n_s = string.replace(word," binod")
    return r_n_s.strip()

this = "         i am Rahul        "

f= replace_and_strip(this, "Rahul")
print(f)

#-------------------------------

