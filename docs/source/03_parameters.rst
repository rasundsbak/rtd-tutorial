.. _03_parameters:
03 Parameters
==========

.. index:: parameters, num_beams, max_length, tokens, n_grams, early_stoppings, length_penalty

Parameters is a way to control the creativity of the model. If it is creative to the extent that it shows a pattern nobody have thought of, the creativity may be beneficial for your project. However, too much creativity may lead to hallucinations. 

In these lessons, the cell in Jupyter lab will be marked with comments, so that the user will be able to vary the parameters. Below, we show an example of parameters set with Pegasus XSum. Different AI models may use slightly different parameters. The documentation for every AI model, is where you find how to use the parameters. If you find definitions of parameters on this page, that is not set in the code below, it is because it is not relevant for the example, Pegasus XSum.

**Max_length** 
the total number of tokens the AI is allowed to generate in that output. For example if it is set to 10 tokens, it can produce: "The weather today is nice and sunny." But with no constraints it might be long like this: "The weather today is quite pleasant with clear skies and warm temperatures. It is a perfect day for outdoor activities such as hiking, biking, or simply taking a walk in the park. The forecast predicts that the good weather will continue throughout the day, making it an excellent opportunity to enjoy the great outdoors with family and friends."


.. todo:: 
   Todo 3.1: **RS gjør i julen:** Endre været til mørkere, i tråd med det kommende pirateksempelet.

**Num_beams** 
Increasing num_beams lets the model explore multiple potential paths or 'beams' for the next word. Consequences: More beams mean the model can generate higher quality and varied text, but in order to increase the num_beams you need more computational resources and time. For example with low num_beams you just get: "The weather today is sunny and warm." because that is the most probable "next" words. But with higher beam, it can result in: "The weather today is sunny and warm, making it a perfect day for a picnic. However, there is a slight chance of light rain in the evening."

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


**length_penalty** 
With higher penalty you get "The weather today is sunny and warm." while with low penalty you can get something like: "The weather today is quite pleasant with clear skies and a gentle breeze."

**min_length** 
Without min_length you can get an output like: "The weather today is nice." and with min_length on 10 tokens, you can get "The weather today is expected to be sunny with a high of 75 degrees Fahrenheit and a light breeze in the afternoon."

**no_repeat_ngram_size** 
Without it you can get: "The weather today is nice and sunny. The weather today is warm and pleasant. The weather today is perfect for a picnic." but with the size to 3 you can get: "The weather today is nice and sunny with a gentle breeze. It's a perfect day for a picnic or a walk in the park." 

**top_k** 
means that you limit what the model should consider as the next word (Santos 2023). Top_k=3 would only consider the three most probable words for the next step, so it can result in " The weather today is sunny and warm.", but with top_k=50, it consides many probable words, like: "The weather today is pleasantly warm with a chance of mild breezes and partly cloudy skies, making it an ideal day for outdoor activities."

**top_p** 
is a method to balance randomness and predictability. Top_p=0.9 can give: "The weather today is sunny and warm, perfect for a day at the beach." while top_p=0.5 can give "The weather today is sunny and warm." If top_p is set to 0.5, the model will be even more selective, considering only the few tokens with the highest probabilities that together cover 50% of the cumulative distribution.

Referneces and further reading
--------------
Google Brain team (2025): `Project Tensorflow <https://projector.tensorflow.org/>`_ 

Num_beams is related to `beam search <https://en.wikipedia.org/wiki/Beam_search>`_,

Santos, O (2023): `Understanding Key AI Language Model Parameters: top_p, Temperature, num_beams, and do_sample <https://becomingahacker.org/understanding-key-ai-language-model-parameters-top-p-temperature-num-beams-and-do-sample-9874bf3c89ae>`_
