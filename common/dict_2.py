from dict_data import female_names

# Remove 2011 and store it: female_names_2011
female_names_2011 = female_names.pop(2011)

# Safely remove 2015 with an empty dictionary as the default: female_names_2015
female_names_2015 = female_names.pop(2015, {})

# Delete 2012
del(female_names[2012])

# Print female_names
print(female_names)
