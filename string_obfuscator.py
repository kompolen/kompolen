import random
import string

def obf_string(s):
    # Generate variable names
    var_names = []
    for _ in range(len(s)):
        var_name = ''.join(random.choices(string.ascii_lowercase, k=3))
        while var_name in var_names:
            var_name = ''.join(random.choices(string.ascii_lowercase, k=3))
        var_names.append(var_name)
    
    # Splitting a string
    parts = [s[i:i+2] for i in range(0, len(s), 2)]
    
    # Create obf-d code
    obfuscated_code = []
    for i, part in enumerate(parts):
        var_name = var_names[i]
        obfuscated_code.append(f'{var_name}="{part}"')
    
    return obfuscated_code, var_names[:len(parts)]

def gen_variable_name():
    return ''.join(random.choices(string.ascii_lowercase, k=5))

def main():
    user_input = input("Input a string: ")
    var_definitions, var_names = obf_string(user_input)
    final_var_name = gen_variable_name()

    print("\nObf code: \n")
    random.shuffle(var_definitions)
    print('\n'.join(var_definitions))
    
    # Creating a final variable
    concatenated_string = '+'.join(var_names)
    print(f'{final_var_name}={concatenated_string}')
    print()
    print(f"print({final_var_name})")

if __name__ == "__main__":
    main()
