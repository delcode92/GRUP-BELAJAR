import pandas as pd
pd.options.display.max_columns = 50

df_load = pd.read_csv('pandas-challenge.csv')

id = []
uraian = []
kode = []
satuan = []

perkalian = []
pembilang = []
penyebut = []


for ind in df_load.index:
    
    # append to array
    id.append(df_load['identifier'][ind])
    uraian.append(df_load['uraian'][ind])
    kode.append(df_load['kode'][ind])
    satuan.append(df_load['satuan'][ind])
    
    r = df_load['rumus'][ind];

    if(  isinstance( r, str) ):
        
        # if contain / sign
        if("/" in r):
            pp = r.split("/")
            pembilang.append(pp[0])
            penyebut.append(pp[1])

            perkalian.append("")
        else:
            pembilang.append("")
            penyebut.append("")
            perkalian.append(r)
    else:
        perkalian.append("")             
        pembilang.append("")
        penyebut.append("")

# print(len(id))
# print(len(uraian))
# print(len(kode))
# print(len(satuan))

# print(len(perkalian))
# print(len(pembilang))
# print(len(penyebut))

data = {
          'identifier': id, 
            'uraian': uraian,
            'kode': kode,
            'satuan': satuan,

            'perkalian': perkalian,
            'pembilang': pembilang,
            'penyebut': penyebut
}  
  
new_df = pd.DataFrame(data)  

# test_dict = {"key1":"test 234",
#             {"x":"x-data"}
#             }

# l = [[12,0]]

# print( l[0][0] )

# print(new_df)
# print(new_df.loc[new_df['identifier'] == "AC.1"])
# print(df_load.head())
# print(df_load["rumus"])
# print(type(df_load["customerID"]))

# print( df_load.shape )
# print( df_load[["customerID","gender"]].head() )
# print( df_load["customerID"].head(2) )
# print( df_load.customerID.head() )

def evaluate(string):
    # if () in s
    # find most inner ()
    s = string.split()
    while len(s) > 1:
        if ('/' in s or
            '*' in s):
            for i in range(len(s)):
                if s[i] == '/':
                    s[i] = int(s[i-1]) / int(s[i+1])
                    s.pop(i-1)
                    s.pop(i)
                    break
                elif s[i] == '*':
                    s[i] = int(s[i-1]) * int(s[i+1])
                    s.pop(i-1)
                    s.pop(i)
                    break
        else:
            for i in range(len(s)):
                if s[i] == '-':
                    s[i] = int(s[i-1]) - int(s[i+1])
                    s.pop(i-1)
                    s.pop(i)
                    break
                elif s[i] == '+':
                    s[i] = int(s[i-1]) + int(s[i+1])
                    s.pop(i-1)
                    s.pop(i)
                    break
    return s[0]

str = "2 / 2 + 3 * 4 - 6";
# (2 / 2) + (3 * 4) - 6
# 1 + 12 - 6

x = evaluate(str)

print(x)