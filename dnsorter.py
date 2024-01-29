import re

# Take the file path as user input
file_path = input("Enter the path to the text file containing URLs: ")

# Read the content of the file
with open(file_path, 'r') as file:
    urls = file.read()

# Extract domains using an improved regular expression
domains = re.findall(r'(?:https?://)?(?:www\d?\.)?([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})(?:\/|\s|\[|$)', urls)

# Filter out IP addresses and empty strings
domains = [domain for domain in domains if not re.match(r'\d+\.\d+\.\d+\.\d+', domain) and domain]

# Print the list of domains
print("Extracted Domains:")
for domain in domains:
    print(domain)

# Save the domains to a new file
output_file_path = input("Enter the path to save the extracted domains: ")
with open(output_file_path, 'w') as output_file:
    for domain in domains:
        output_file.write(domain + '\n')

print(f"Domains have been saved to {output_file_path}")