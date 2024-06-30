def load_loss_function(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return f"File {file_path} not found."
    except Exception as e:
        return f"An error occurred: {e}"

# # 指定Markdown文件的路径
# file_path = 'prompts_loss_function.md'

# # 读取并打印文件内容
# content = load_loss_function(file_path)
# print(content)
