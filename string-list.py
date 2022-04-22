import subprocess
name = "This is testing of string"
l_name = [
    "Shailesh",
    "Shivansh",
    "Saatvik",
    "Kamalini"
]
print(name.upper())
for name in l_name:
    print(name.upper())

emails = {
    'david1': 'david@example.com',
    'mary1': 'mary@example.com',
    'roger': 'roger@example.com',
    'david2': 'david@example.com',
    'mary2': 'mary@example.com'
}
#print(emails)

for name,email in emails.items():
    print(f' {name} -> {email}')

#output = subprocess.check_output("dir", "shell=True")
#print(output)