.. _01_ai_board:
01 Getting overview with AI on the blackboard
=================

.. index:: artificial, intelligence, cluster, HPC, Transformers, CUDA, .gguf, llama_cpp

.. image:: AI_board.JPG

Hugging face and the AIs
___________________________
"Hugging Face is a machine learning (ML) and data science platform and community that helps users build, deploy and train machine learning models." Ben Lutkevich on `Tech Target <https://www.techtarget.com/whatis/definition/Hugging-Face>`_

`Hugging face <https://huggingface.co/>`_ is a good place to start, when you want to familiarize yourself with the LLMs. However, in this course you do not need to download them, because we, the instructors have already done some of the work for you. If you want to learn, keep reading!


Fox, Cuda and Cluster
---------------------
Wether you like it or not, AI may be your new colleague. When i talk about aspects of the setup on Fox, i say Cuda, Fox or Cluster.

**CUDA** means Compute Unified Device Architecture. According to Wikipedia is a proprietary parallel computing platform and interface, that allows software to use certain types of graphics processing units (GPUs) (Wikipedia Nov. 12th 2024). 

**Cluster**, The Fox is a `High performance computing cluster for Educloud research users <https://www.uio.no/english/services/it/research/hpc/fox/>`_. A Computing Cluster is a set of connected computers that work together so closely that in many respects they function as a single computer.

**HPC**, A High Performance Computing cluster

**Transformers** A transformer is a learning architecture developed by researchers at Google and based on the multi-head attention mechanism, proposed in the 2017 paper "Attention Is All You Need".


**The .gguf format** developed by @ggerganov is a quantified AI file format that that stores both tensors and metadata in a single file.

**llama_cpp** is a C++ library that allows us to run quantized models. The cpp format also developed by developed by @ggerganov interprets the GGML and GGUF formats.

Parameters
----------
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





  ..note:
  Task: Write a list over concepts that you do not understand. Go in pairs, and discuss the concepts you want to elaborate on. Use google, UiO GPT or an encyclopedia from the library.



