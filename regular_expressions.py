# Part 1 (Core problem)

# Write a function that takes a nested dictionary of user data (including name and email) and returns a new set of nested dictionaries that contains only unique users. Users are determined to be unique according to their email address.

# For duplicates, use the most recent name. Assume the number (i.e. user_NUMBER) maps to the time the user was created (i.e. user_1 came before user_3)

# input_example = {"user_1": {"name": "John Smith", "email": "john_smith@gmail.com"}, "user_2": {"name": "Jane Doe", "email": "janedoe@gmail.com"}, "user_3": {"name": "Johnathan Smith", "email": "john_smith@gmail.com"}}
# output_example = {"user_1": {"name": "John Smith", "email": "john_smith@gmail.com"}, "user_2": {"name": "Jane Doe", "email": "janedoe@gmail.com"}}


# Part 2 (Slightly more difficult bonus problem)

# Modify your function so that it is able to identify gmail addresses that have been modified using "+" or "." as the same email address. In other words, make sure that in the dictionary you return that there is only one user for john_smith@gmail.com and john_smith+this_part_is_ignored@gmail.com. More details on how this works
# https://gmail.googleblog.com/2008/03/2-hidden-ways-to-get-more-from-your.html

# For duplicates, use unadorned version the email address.
# input_example = {"user_1": {"name": "John Smith", "email": "john_smith@gmail.com"}, "user_2": {"name": "Jane Doe", "email": "janedoe@gmail.com"}, "user_3": {"name": "Johnathan Smith", "email": "john_smith@gmail.com"}, "user_4": {"name": "Johnny Smith", "email": "john_smith+facebook@gmail.com"}, "user_5": {"name": "Janie Smith", "email": "jane.smith@gmail.com"}}
# output_example = {"user_1": {"name": "John Smith", "email": "john_smith@gmail.com"}, "user_2": {"name": "Jane Doe", "email": "jane_doe@gmail.com"}}

# HINT: You're going to want to use regular expressions (there are a lot of articles online) - they're really common in Python


# **********************************************************************

# Write a function that takes a nested dictionary of user data (including name and email) and returns a new set of nested dictionaries that contains only unique users. Users are determined to be unique according to their email address.

# For duplicates, use the most recent name. Assume the number (i.e. user_NUMBER) maps to the time the user was created (i.e. user_1 came before user_3)

original_user_data = {"user_1": {"name": "John Smith", "email": "john_smith@gmail.com"},
                      "user_2": {"name": "Jane Doe", "email": "janedoe@gmail.com"},
                      "user_3": {"name": "Johnathan Smith", "email": "john_smith@gmail.com"}}

deduped_dict = {}
unique_emails = set()

for user_num, user_info in original_user_data.items():
    if user_info["email"] not in unique_emails:
        unique_emails.add(user_info["email"])  # add is the "set" version of append for lists
        # this gets applied to user_info so, bc we have access to user_info, we're able to apply it to the new dictionary
        deduped_dict[user_num] = user_info

print(deduped_dict)

print("")

# **********************************************************************


# Part 2 (Slightly more difficult bonus problem)

# Modify your function so that it is able to identify gmail addresses that have been modified using "+" or "." as the same email address. In other words, make sure that in the dictionary you return that there is only one user for john_smith@gmail.com and john_smith+this_part_is_ignored@gmail.com. More details on how this works
# https://gmail.googleblog.com/2008/03/2-hidden-ways-to-get-more-from-your.html

# For duplicates, use unadorned version the email address.
# input_example = {"user_1": {"name": "John Smith", "email": "john_smith@gmail.com"}, "user_2": {"name": "Jane Doe", "email": "janedoe@gmail.com"}, "user_3": {"name": "Johnathan Smith", "email": "john_smith@gmail.com"}, "user_4": {"name": "Johnny Smith", "email": "john_smith+facebook@gmail.com"}, "user_5": {"name": "Janie Smith", "email": "jane.smith@gmail.com"}}

# output_example = {"user_1": {"name": "John Smith", "email": "john_smith@gmail.com"}, "user_2": {"name": "Jane Doe", "email": "jane_doe@gmail.com"}}

# HINT: You're going to want to use regular expressions (there are a lot of articles online) - they're really common in Python
# First step in coding problems is to break it down into its various steps (this is common in interviews)


# Function 1: de-dupe emails in dictionary by placing them into a set (input: dictionary key value pairs, output: set consisting of unique emails)
# Function 2: identify any emails in the unique_emails2 set that have a "+" in them and remove anything including/following the "+" (input: unique emails in set, output: unique emails in set sans "+" emails)


# REG EX: (search)   [+].*?@
# we're using . as a wild card in this reg ex to ensure we capture any characters included after the + here (e.g., periods, numbers, letters, special characters, etc.)
# the ? usually says the thing before is optional
# if we use *? it will make the regex less "greedy" and will make the * non-greedy (take the bare min of what the regex finds here so that it doesn't look forever)
# we can use .search here bc gmail should only allow one + in an email address
# there's a python operator (.remove or .sub) that you can use to remove that substring from the input - if you use .sub, you could just replace it with the @ sign


# Function 3: identify any emails in the unique_emails2 set that have a "." in the email address body and remove anything including/following the "." (input: unique emails in set, output: unique emails in set sans "." emails)

# could use split to temporarily split the email address at the @ sign,search for ".", and then remove all periods and replace them with nothing in the first half (either .sub or .remove) .remove(".")


# Function 4: call function 1 to de-dupe emails in dictionary and create unique_emails2 set. call function 2 to remove any instances of "+" emails from the set. call function 3 to remove any instances of "." emails from the set. call function 4 to take the remaining (truly unique) unique_emails2 set and use it to add unique users back into the empty deduped_dict2 (input: orig_user_data2 dictionary, output: deduped_dict2 dictionary consisting of only truly unique (no + or .) users and email addresses)


orig_user_data = {"user_1": {"name": "John Smith", "email": "john_smith@gmail.com"},
                  "user_2": {"name": "Jane Doe", "email": "janedoe@gmail.com"},
                  "user_3": {"name": "Johnathan Smith", "email": "john_smith@gmail.com"},
                  "user_4": {"name": "Johnny Smith", "email": "john_smith+facebook@gmail.com"},
                  "user_5": {"name": "Janie Smith", "email": "jane.smith@gmail.com"}}

deduped_dict2 = {}
unique_emails2 = set()

import re

# Function 1
print("* Function 1 *")

def dedupe_user_emails(orig_user_data):
    """Take a dictionary outlining user names and emails and return a dictionary that has only unique users."""

    for user_num, user_info in orig_user_data.items():
        if user_info["email"] not in unique_emails2:
            unique_emails2.add(user_info["email"])

    return unique_emails2

print(dedupe_user_emails(orig_user_data))
print("")

#Function 2: identify any emails in the unique_emails2 set that have a "+" in them and remove anything including/following the "+" (input: unique emails in set, output: unique emails in set sans "+" emails)

# REG EX: (search)   [+].*?@
# we're using . as a wild card in this reg ex to ensure we capture any characters included after the + here (e.g., periods, numbers, letters, special characters, etc.)
# the ? usually says the thing before is optional
# if we use *? it will make the regex less "greedy" and will make the * non-greedy (take the bare min of what the regex finds here so that it doesn't look forever)
# we can use .search here bc gmail should only allow one + in an email address
# there's a python operator (.remove or .sub) that you can use to remove that substring from the input - if you use .sub, you could just replace it with the @ sign


print("* Function 2 *")

def remove_plus_email_aliases(unique_emails2):
    """Identify  any emails with a + in them and remove anything including/following the +. Return the de-duped set."""

    for email in unique_emails2:
        # re.search("[+].*?@", email) #don't seem to need the search regex here
        print(re.sub("[+].*?@", "@", email)) #accurately substituted the +facebook with @ but didn't save to unique_email2
        # unique_emails2.add(email) #tried adding the emails back into this set bc sub didn't appear to stick out of the for loop, but this didn't work either
    print("")

    return unique_emails2

print(remove_plus_email_aliases(unique_emails2)) #see line 117: accurately substituted the +facebook with @ but didn't save to unique_email2



# for email in unique_emails2:
#     plus_emails = re.search("[+].*?@", email)
#     unique_emails2 = re.sub("[+].*?@", "@", email) #might be able to use .sub here but need to figure out how
#     print(plus_emails)   #found one match (which is good/expected)
#
# print(unique_emails2)


#     for email in unique_emails2:
#         plus_emails = re.findall("[+].*?@", user_info["email"] )
#         print(plus_emails)





