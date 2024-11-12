.. _02 parameters:
Parameters
==========

.. index:: parameters, num_beams, max_length, tokens, n_grams, early_stoppings, length_penalty

In these lessons, i try to let the cell in Jupyter lab be tagges with #-signs so that the user after some time, will learn how to vary the parameters. Below, you may see an example og parameters set with Pegasus XSum

Code view::

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



