# to run the code type python main.py in the terminal
#https://www.youtube.com/watch?v=d0o89z134CQ&ab_channel=TechWithTim


from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = '''
Answer the question below.

Here is the conversation history: {context}

Question {question}

Answer:
'''

model = OllamaLLM(model = "llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handel_conversation():
    context =""
    print("Welcome to the chatbo! Type 'exit to quit.'")
    while True:
        user_input = input("You:")
        if user_input.lower() == "exit":
            break
        result = chain.invoke({"context":context,"question":user_input})
        print("Bot:",result)
        context += f"\nUser: {user_input}\nAI:{result}"

if __name__=="__main__":
    handel_conversation()