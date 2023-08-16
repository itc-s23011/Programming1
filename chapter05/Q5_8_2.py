data = [
    ["01", "0001", "Mala", "Yamada", " Tarou", 25, "Tokyo"],
    ["01", "0002", "Male", "Stou", "Takeshi", 27, "Kanagawa"],
    ["01", "0003", "Female", "Tanaka", "Yuko", 25, "Saitama"],
    ["02", "0001", "Male", "smith", "Mike", 22, "NewJersey"],
    ["02", "0002", "Male", "Turner", "Tom", 27, "kansas"],
    ["02", "0003", "Male", "Jackson", "David", 22, "Florida"],
]
data

member_information = {}

for record in data:
    key = (record[0], record[1])
    info = record[2:]
    member_information[key] = info

print("number", "information", sep="\t")
for key, info in member_information.items():
    print(key, info)
