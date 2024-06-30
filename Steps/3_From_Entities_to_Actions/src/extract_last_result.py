import re

def find_last_text_in_backticks(text):
    # Use regex to find all occurrences of text within triple backticks
    matches = re.findall(r'```(.*?)```', text, re.DOTALL)
    
    if matches:
        return matches[-1]  # Return the last match
    else:
        return None

# Example usage
# text = 'aaa```foo1```balabala1```foo2```balabala2```foo3```aaa'
# last_text = find_last_text_in_backticks(text)
# print(last_text)
