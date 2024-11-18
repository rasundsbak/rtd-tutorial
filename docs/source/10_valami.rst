.. _10 valami:

10 Valami
=======
.. index:: valami

# Importing the Llama class from the llama_cpp package
from llama_cpp import Llama

# Angi stien til den kvantiserte modellfilen
quantized_modelfile_path = "/fp/projects01/ec367/huggingface/cache/Llama/Meta-Llama-3-8B-Instruct.Q5_K_M.gguf"

# Initialiser modell med riktig filsti
lcpp_model = Llama(
    model_path=quantized_modelfile_path,  # Path to the quantized model file
    chat_format="chatml",  # Using the 'chatml' format for conversations
    n_gpu_layers=-1  # Running on CPU (no GPU layers)
)

# Lage en chat completion
response = lcpp_model.create_chat_completion(
    messages=[
        {"role": "system", "content": "You are a world class economist chatbot who always responds in understandable speak in whole sentences!"},
        {"role": "user", "content": "Who are you?"},
        {"role": "user", "content": "Tell me about income equality and colonial history?"},
    ],
    temperature=0.3,
)

# Print responsen
print(response['choices'][0]['message']['content'])
