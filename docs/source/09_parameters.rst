.. _09_parameters:

09 Parameters and pipeline keyword arguments (kwargs)
======================================================

.. index:: parameters, num_beams, max_length, tokens, n_grams, early_stoppings, length_penalty

We want the user to change the parameters in order to experiment with inputs and putputs. Different AI models may use slightly different parameters. The documentation for every AI model, is where you find how to use parameters. If you find definitions of parameters on this page, that is not set in the code of the lesson, it is because it is not relevant for the example.

   ``max_length`` the total number of tokens the AI is allowed to generate in that output.

   ``min_length`` the minimum length of the output

   ``num_beams`` Increasing num_beams lets the model explore multiple potential paths or 'beams' for the next word. Consequences: More beams mean the model can generate higher quality and varied text, but at the cost of computational resources and time. Think of a torch, and the higher the nomber of beams, the further the beam will reach out into the forest.

   ``max_new_tokens`` number of tokens allowed in the output.

   ``do_sample`` may be set to true og false. Enables different strategies of sampling. See also the reference list.
       
   ``temperature`` determines wether the output is more random or creative or on the other end of the scale, more predictable. Higher temperature gives higher creativity.

   ``no_repeat_ngram_size`` counts the number of repetitions the model is allowed to do in an output

   ``top_k`` you limit what the model should consider as the next word, to the k most probable words for the next step.

   ``top_p`` top_p computes the cumulative probability distribution, and cut off as soon as that distribution exceeds the value of top_p. For example, a top_p of 0.3 means that only the tokens comprising the top 30% probability mass are considered.
