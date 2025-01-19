.. _09_parameters:
09 Parameters and pipeline keyword arguments (kwargs)
==========

.. index:: parameters, num_beams, max_length, tokens, n_grams, early_stoppings, length_penalty

We want the user to change the parameters in order to experiment with inputs and putputs. Different AI models may use slightly different parameters. The documentation for every AI model, is where you find how to use parameters. If you find definitions of parameters on this page, that is not set in the code of the lesson, it is because it is not relevant for the example.

   ``Max_length`` the total number of tokens the AI is allowed to generate in that output.

.. todo:: 
   Todo 3.1: RS gjør i julen: Endre været til mørkere hav, i tråd med det kommende pirateksempelet.

``Num_beams`` Increasing num_beams lets the model explore multiple potential paths or 'beams' for the next word. Consequences: More beams mean the model can generate higher quality and varied text, but at the cost of computational resources and time.

Code view with parameters::

    # Funksjon for å generere sammendrag
    def generate_summary(text, model, tokenizer, max_length=800, num_beams=15, length_penalty=0.3, min_length=250, no_repeat_ngram_size=2):
        """Generer sammendrag ved bruk av Pegasus-modellen med justerbare parametere."""
        
        # max_length: Den maksimale lengden på det genererte sammendraget.
        # num_beams: Antall "beams" for strålesøk, noe som kan øke kvaliteten på genererte tekstsekvenser.
        # length_penalty: Straff for lange sekvenser, en lav verdi (<1) kan oppmuntre lengre utgang.
        # min_length: Minimum lengde på utgangen.
        # no_repeat_ngram_size: Forhindrer gjentakelse av n-grams i utgangen.
        
        tokens = tokenizer(text, truncation=True, padding="longest", return_tensors="pt")
        summary_ids = model.generate(tokens.input_ids, 
                                     max_length=max_length, 
                                     num_beams=num_beams, 
                                     length_penalty=length_penalty, 
                                     min_length=min_length, 
                                     no_repeat_ngram_size=no_repeat_ngram_size, 
                                     early_stopping=True)
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return summary


**length_penalty** With hight penalty you get "The weather today is sunny and warm." while with low penalty you can get something like: "The weather today is quite pleasant with clear skies and a gentle breeze."

**min_length** Without min_length you can get an output like: "The weather today is nice." and with min_length on 10 tokens, you can get "The weather today is expected to be sunny with a high of 75 degrees Fahrenheit and a light breeze in the afternoon."

**no_repeat_ngram_size** Without it you can get: "The weather today is nice and sunny. The weather today is warm and pleasant. The weather today is perfect for a picnic." but with the size to 3 you can get: "The weather today is nice and sunny with a gentle breeze. It's a perfect day for a picnic or a walk in the park." 

**top_k** means that you limit what the model should consider as the next word. top_k=3 would only consider the three most probable words for the next step. The result may be something like "The weather today is sunny and warm.", but with top_k=50, it will consider a higher number of probable words, like: "The weather today is pleasantly warm with a chance of mild breezes and partly cloudy skies, making it an ideal day for outdoor activities."

**top_p** means top_p=0.9 can give: "The weather today is sunny and warm, perfect for a day at the beach." while top_p=0.5 can give "The weather today is sunny and warm." If top_p is set to 0.5, the model will be even more selective, considering only the few tokens with the highest probabilities that together cover 50% of the cumulative distribution.

.. todo:: 
   Todo 3.2: Definere early stopping.

Further reading
--------------
When it comes to creaticity, Where does the machine take its suggestions from? In order to understand, it can help studying at this three dimensional presentation of a model `Project Tensorflow <https://projector.tensorflow.org/>`_  

Num_beams is related to `beam search <https://en.wikipedia.org/wiki/Beam_search>`_,
