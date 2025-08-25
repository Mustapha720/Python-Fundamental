from tabulate import tabulate

table_header = ["Task id", "Title", "Description", "Status"]

table_body = [
    ["1", "Wash", "Wash all the plates", "pending...."],
    ["2", "Cook", "Cook ogbono", "in progress...."]
]

table = tabulate(table_body, headers = table_header, showindex = "always", tablefmt = "double_outline", ) # showindex: auto-number
print(table)