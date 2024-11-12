.. _04 Dolor sit amet:
04 Dolor sit amet
=================
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut eleifend augue, et pretium turpis. Fusce in tortor a tellus luctus tristique a at metus. Pellentesque in suscipit ipsum. Ut bibendum elit orci, eget efficitur mauris fringilla eget. 

Aliquam vitae risus lectus. Nam quis ante magna. Nunc hendrerit tellus at tortor dapibus, ut porttitor enim tincidunt. Etiam nisl purus, fermentum sit amet justo ac, lobortis congue ipsum. Cras nisl nisi, vehicula ac suscipit vitae, consectetur at ligula. Morbi faucibus dignissim dictum. Phasellus bibendum iaculis tellus, sed vehicula est luctus imperdiet. Pellentesque dictum enim est, at condimentum mauris iaculis et. Nulla posuere congue luctus. Aliquam nec sem pretium massa mollis ornare. Proin vel nulla eu dolor consequat fermentum nec et velit. Ut quis sapien non lacus pretium elementum.


code view::


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
          {"role": "system", "content": "You are a pirate chatbot who always responds in pirate speak in whole sentences!"},
          {"role": "user", "content": "Who are you?"},
          {"role": "user", "content": "Tell me about your ideal boat?"},
      ],
      temperature=0.3,
  )
  
  # Print responsen
  print(response['choices'][0]['message']['content'])
