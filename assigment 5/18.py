def swap_comma_dot(s):
    return s.replace(",", "_temp").replace(".", ",").replace("temp_", ".")
s = "32.054,23"
print(swap_comma_dot(s))