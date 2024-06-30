from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

#region Load entities texts
from load_entities import load_entities
entity_data_folder = './Steps/3_From_Entities_to_Actions/src/Entities'
system_to_entities_dict = load_entities(entity_data_folder)

# Print the loaded texts dictionary
# for key, text in system_to_entities_dict.items():
#     print(f"{key}: {text}\n")

#endregion

#region Load prompts
from load_prompts import read_prompts

prompt_folder = './Steps/3_From_Entities_to_Actions/Findings_Influence_of_Prompts/Prompts'

variation_to_prompts_dict = read_prompts(prompt_folder)

# for key, text in variation_to_prompts_dict.items():
#     print(f"{key}: {text}\n")

#endregion

# Pick just one system and prompt.
entities = system_to_entities_dict["E_Commerce"]

# region Create a chain to execute the breakdown from entities to actions.
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt = ChatPromptTemplate.from_template("{prompt_text}")

model = ChatOpenAI(model="gpt-4o", max_tokens=4096)

parser = StrOutputParser()

chain = prompt | model | parser
# endregion

#region Perform requirement decomposition process using different prompts
prompt_variation_to_actions_dict = {}
for prompt_variation, prompt_text in variation_to_prompts_dict.items():

    input = prompt_text.format(entity_names_split_by_comma = entities)
    print(f"Input: \n{input}")

    raw_result = chain.invoke(input)
    print(f"Raw result: \n{raw_result}")

    from extract_last_result import find_last_text_in_backticks
    final_result = find_last_text_in_backticks(raw_result)
    # print(f"Final result: \n{final_result}")

    if final_result is None:
        print(f"{prompt_variation} : Final_result is None, set to raw result.")
        final_result = raw_result

    variation_to_final_results_text = prompt_variation + "\n" + final_result + "\n"
    # print(variation_to_final_results_text)

    prompt_variation_to_actions_dict[prompt_variation] = final_result

    # print(prompt_variation)
    # print(final_result)
    # print("-"*40)

#endregion

#region Define the loss function
from load_loss_function import load_loss_function
loss_function_file_path = './Steps/3_From_Entities_to_Actions/src/prompts_loss_function.md'
prompt_loss_function = load_loss_function(loss_function_file_path)
# print(prompt_loss_function)

#endregion

#region Evaluate all the variation prompts with the loss function
prompt_loss_function_and_results = prompt_loss_function + "\n" + str(prompt_variation_to_actions_dict)
# print(prompt_loss_function_and_results)

response = model.invoke(prompt_loss_function_and_results)
print(response.content)

#endregion