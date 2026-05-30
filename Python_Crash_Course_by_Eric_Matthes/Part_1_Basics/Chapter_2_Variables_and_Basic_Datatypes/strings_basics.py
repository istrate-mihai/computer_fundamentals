import this
print(this)
# 2-3. Personal Message
name = "Eric"
print("Hello " + name + ", would you like to learn some Python today ?")

# 2-4. Name Cases: Store a person’s name in a variable, and then print that
# person’s name in lowercase, uppercase, and titlecase.
name = "Istrate Mihai"
print(name.lower())
print(name.upper())
print(name.title())

# 2-5. Famous Quote: Find a quote from a famous person you admire. Print the
# quote and the name of its author. Your output should look something like the
# following, including the quotation marks:
# Albert Einstein once said, “A person who never made a
# mistake never tried anything new.”
famous_person = "Albert Einstein"
quote         = "A person who never made a mistake never tried anything new."
message       = famous_person + " once said: “" + quote + "”"
print(message)

name = "   Peter\t\n Parker    "
print(name.lstrip())
print(name.rstrip())
print(name.strip())
