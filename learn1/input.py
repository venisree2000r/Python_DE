import sys

full_name = ".".join(sys.argv[1:])
email_id = full_name.lower().replace(" ", ".") + "@company.com"

print("Employee FullName: ",full_name)
print("Employee Email ID: ",email_id)