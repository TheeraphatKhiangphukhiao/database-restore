import csv

file_path = 'D:\\Knowledge from internship\\New folder (2)\\bmn66.csv'
folder_write_path = 'D:\\Knowledge from internship\\Database Schemas\\bmn66\\'
file_write_path = set()

data_type = set()

with open(file_path, mode='r', encoding="utf-8") as file:
    csvFile = csv.reader(file)

    i = 1
    for line in csvFile:
        if i > 1:
            data_type.add(line[2])
        i += 1
"""
for name in data_type:
    print(name)

print("-----------------------------------------------------------------")
"""

with open(file_path, mode='r', encoding="utf-8") as file:
    csvFile = csv.reader(file)

    i = 1
    for line in csvFile:
        if i > 1:
            file_write_path.add(line[0])
        i += 1



num = 0
for class_name in file_write_path:
    with open(file_path, mode='r', encoding="utf-8") as file:
        csvFile = csv.reader(file)

        path = folder_write_path + class_name + '.cs'
        print(path)
        attributes = []
        datatypes = []
        isNullable = []
        isPrimaryKey = []

        for line in csvFile:
            if line[0] == class_name:
                attributes.append(line[1])

                if line[2] == "decimal":
                    datatypes.append("decimal")
                elif line[2] == "longtext":
                    datatypes.append("string")
                elif line[2] == "tinyint":
                    datatypes.append("byte")
                elif line[2] == "enum":
                    datatypes.append("char")
                elif line[2] == "varchar":
                    datatypes.append("string")
                elif line[2] == "float":
                    datatypes.append("float")
                elif line[2] == "bigint":
                    datatypes.append("long")
                elif line[2] == "double":
                    datatypes.append("double")
                elif line[2] == "mediumtext":
                    datatypes.append("string")
                elif line[2] == "int":
                    datatypes.append("int")
                elif line[2] == "mediumblob":
                    datatypes.append("byte[]")
                elif line[2] == "longblob":
                    datatypes.append("byte[]")
                elif line[2] == "text":
                    datatypes.append("string")
                elif line[2] == "binary":
                    datatypes.append("byte[]")
                elif line[2] == "char":
                    datatypes.append("char")
                elif line[2] == "blob":
                    datatypes.append("byte[]")


                if line[3] == "YES":
                    if line[2] == "datetime" or line[2] == "date":
                        isNullable.append("")
                        datatypes.append("Nullable<DateTime>")
                    else:
                        isNullable.append("?")
                elif line[3] == "NO":
                    isNullable.append("")
                    if line[2] == "datetime" or line[2] == "date":
                        datatypes.append("DateTime")


                if line[4] == "YES":
                    isPrimaryKey.append("[Key]")
                elif line[4] == "NO":
                    isPrimaryKey.append("")

        
        with open(path, 'w') as file_cs:
            file_cs.write("namespace Digix.Standard.Model.Entity\n{\n")
            file_cs.write("    using System;\n    using System.Collections.Generic;\n\n")

            file_cs.write(f"    public partial class {class_name}\n")
            file_cs.write("    {\n")
            for i in range(len(attributes)):
                if isPrimaryKey[i] == "[Key]":
                    file_cs.write(f"        {isPrimaryKey[i]}\n")
                file_cs.write(f"        public {datatypes[i]}{isNullable[i]} {attributes[i]} {{ get; set; }}\n")

            file_cs.write("    }\n")
            file_cs.write("}\n")



"""
SELECT 
TABLE_NAME
,COLUMN_NAME
,DATA_TYPE
,IS_NULLABLE
FROM INFORMATION_SCHEMA.COLUMNS 
WHERE TABLE_SCHEMA = 'cdddb'
order by TABLE_NAME, ORDINAL_POSITION;
"""


"""
SELECT 
    c.TABLE_NAME,
    c.COLUMN_NAME,
    c.DATA_TYPE,
    c.IS_NULLABLE,
    CASE 
        WHEN k.COLUMN_NAME IS NOT NULL THEN 'YES'
        ELSE 'NO'
    END AS IS_PRIMARY_KEY
FROM INFORMATION_SCHEMA.COLUMNS c
LEFT JOIN INFORMATION_SCHEMA.KEY_COLUMN_USAGE k
    ON c.TABLE_NAME = k.TABLE_NAME
    AND c.COLUMN_NAME = k.COLUMN_NAME
    AND k.CONSTRAINT_SCHEMA = c.TABLE_SCHEMA
    AND k.CONSTRAINT_NAME = 'PRIMARY'
WHERE c.TABLE_SCHEMA = 'bmn66'
ORDER BY c.TABLE_NAME, c.ORDINAL_POSITION;

"""