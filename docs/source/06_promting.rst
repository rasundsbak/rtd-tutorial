.. _06 promting:

06 Promting
=======
.. index:: etwas

Try your first promt now::

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
   


2::

   Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
   Vestibulum quis auctor mi, vel elementum arcu. 
   Donec fermentum luctus rhoncus.

   Selected output console:

   > 
   > 
   > 



It is also necesary to rule out the conflicts between the packages that are in use 
3::

   Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
   Vestibulum quis auctor mi, vel elementum arcu. 
   Donec fermentum luctus rhoncus.

4::

   Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
   Vestibulum quis auctor mi, vel elementum arcu. 
   Donec fermentum luctus rhoncus.


   Selected output:

   > 
   > 
   > 
   >
   >
   > 

We are ready to start the process of getting data.
