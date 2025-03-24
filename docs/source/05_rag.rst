.. _05 rag:

Retrieval-Augmented Generation (RAG)
======================================

.. index:: RAG, dokumenter, retrieval augmented generation, gjenfinningsforsterket tekstgenerering

På norsk: Gjenfinningsforsterket tekstgenerering
-------------------------------------------------

Gjenfinningsforsterket tekstgenerering eller RAG er en måte å inkludere dokumenter for å gi kontekst til spørsmål som man stiller en språkmodell. Dette kan redusere tendensen til hallusinering eller andre feil i svarene. Et system for gjenfinningsutvidet tekstgenerering har to hoveddeler. For det første en dokumentdatabase med søkeindeks og for det andre en stor språkmodell. Tegningen under viser RAG programmets struktur.

.. image:: rag_2025.png

Bilde fra `Retrieval-Augmented Generation <https://uio-library.github.io/LLM-course/4_RAG.html>`_ .
Når brukeren stiller et spørsmål, vil det bli håndtert i to steg. Først blir det brukt til et søk i dokumentdatabasen. Søkeresultatene blir sendt sammen med spørsmålet til språkmodellen. Språkmodellen blir bedt om å svare på spørsmålene basert på konteksten i søkeresultatene.

Vi vil bruke `LangChain <https://www.langchain.com/>`_, et bibliotek med åpen kildekode, som brukes til å lage programmer med store språkmodeller. Dette kapittelet er inspirert av artikkelen `Retrieval-Augmented Generation (RAG) with open-source Hugging Face LLMs using LangChain <https://medium.com/@jiangan0808/retrieval-augmented-generation-rag-with-open-source-hugging-face-llms-using-langchain-bd618371be9d>`.


.. admonition:: Oppgave: Lage en ny notebook
   :collapsible: closed

    Lag en ny Jupyter Notebook som du kaller RAG ved å velge Filmenyen i JupyterLab, deretter "New" og "Notebook". Hvis du blir spurt om å velge en kjerne, velg “Python 3”. Gi den nye notebooken et navn ved å velge Filmenyen i JupyterLab og deretter "Rename Notebook". Bruk navnet RAG.

.. admonition:: Oppgave: Stopp gamle kjerner
   :collapsible: closed

    JupyterLab bruker en Python kjerne til å kjøre koden i hver notebook. For å frigjøre GPU minne som ble brukt i forrige kapittel, bør du stoppe kjernen for den notebooken. I menyen på venstre side av JupyterLab, velg den mørke sirkelen med en hvit firkant i. Deretter velger du KERNELS og "Shut Down All".

Dokumentets plassering
------------------------

Vi har samlet noen artikler som har Creative Commons lisens. Vi skal forsøke å laste opp alle dokumentene fra mappen som det vises til under. Hvis du vil, kan du endre stien til din egen mappe på hjemmeområdet::

   document_folder = '/fp/projects01/ec443/documents'

Språkmodellen
---------------

Vi skal bruke modeller fra HuggingFace, en nettside som har verktøy og modeller til maskinlæring. Vi kommer til å bruke språkmodellen meta-llama/Llama-3.2-3B-Instruct, fordi den er liten nok til at vi kan bruke den med de minste GPUene på Fox. Hvis du kjører på en GPU med mer minne, kan du få bedre resultater med en større modell, som for eksempel mistralai/Ministral-8B-Instruct-2410.

Modellens plassering
---------------------

Vi må laste ned modellen som vi skal bruke. Vi kjører programmet på tungregningsklyngen Fox ved UiO. Vi må peke på stedet der vårt program skal lagre modellene som vi laster ned fra HuggingFace::

   import os
   os.environ['HF_HOME'] = '/fp/projects01/ec443/huggingface/cache/'

.. note::

   Hvis du kjører programmene lokalt på din egen datamaskin, trenger du kanskje ikke sette HF_HOME.

Modellen
---------

Now, we are ready to download and use the model. To use the model, we create a pipeline. A pipeline can consist of several processing steps, but in this case, we only need one step. We can use the method HuggingFacePipeline.from_model_id(), which automatically downloads the specified model from HuggingFace.

from langchain_community.llms import HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id='meta-llama/Llama-3.2-3B-Instruct',
    task='text-generation',
    device=0,
    pipeline_kwargs={
        'max_new_tokens': 500,
        'do_sample': True,
        'temperature': 0.3,
        'num_beams': 4
    }
)

Pipeline Arguments

We give some arguments to the pipeline:

    model_id: the name of the model on HuggingFace

    task: the task you want to use the model for, other alternatives are translation and summarization

    device: the GPU hardware device to use. If we don’t specify a device, no GPU will be used.

    pipeline_kwargs: additional parameters that are passed to the model.

        max_new_tokens: maximum length of the generated text

        do_sample: by default, the most likely next word is chosen. This makes the output deterministic. We can introduce some randomness by sampling among the most likely words instead.

        temperature: the temperature controls the statistical distribution of the next word and is usually between 0 and 1. A low temperature increases the probability of common words. A high temperature increases the probability of outputting a rare word. Model makers often recommend a temperature setting, which we can use as a starting point.

        num_beams: by default the model works with a single sequence of tokens/words. With beam search, the program builds multiple sequences at the same time, and then selects the best one in the end.

Tip

If you’re working on a computer with less memory, you might need to try a smaller model. You can try for example mistralai/Mistral-7B-Instruct-v0.3 or meta-llama/Llama-3.2-1B-Instruct. The latter has only 1 billion parameters, and might be possible to use on a laptop, depending on how much memory it has.
Using the Language Model

Now, the language model is ready to use. Let’s try to use only the language model without RAG. We can send it a query:

query = 'What are the major contributions of the Trivandrum Observatory?'
output = llm.invoke(query)
print(output)

This answer was generated based only on the information contained in the language model. To improve the accuracy of the answer, we can provide the language model with additional context for our query. To do that, we must load our document collection.
The Vectorizer

Text must be vectorized before it can be processed. Our HuggingFace pipeline will do that automatically for the large language model. But we must make a vectorizer for the search index for our documents database. We use a vectorizer called a word embedding model from HuggingFace. Again, the HuggingFace library will automatically download the model.

from langchain_huggingface import HuggingFaceEmbeddings

huggingface_embeddings = HuggingFaceEmbeddings(
    model_name='BAAI/bge-m3',
    model_kwargs = {'device': 'cuda:0'},
    #or: model_kwargs={'device':'cpu'},
    encode_kwargs={'normalize_embeddings': True}
)

Embeddings Arguments

These are the arguments to the embedding model:

    ‘model_name’: the name of the model on HuggingFace

    ‘device’: the hardware device to use, either a GPU or CPU

    ‘normalize_embeddings’: embeddings can have different magnitudes. Normalizing the embeddings makes their magnitudes equal.

Loading the Documents

We use DirectoryLoader from LangChain to load all in files in document_folder. documents_folder is defined above.

from langchain_community.document_loaders import DirectoryLoader

loader = DirectoryLoader(document_folder)
documents = loader.load()

The document loader loads each file as a separate document. We can check how long our documents are. For example, we can use the function max() to find the length of the longest document.

print(f'Number of documents:', len(documents))
print('Maximum document length: ', max([len(doc.page_content) for doc in documents]))

We can examine one of the documents:

print(documents[0])

Splitting the Documents

Since we are only using PDFs with quite short pages, we can use them as they are. Other, longer documents, for example the documents or webpages, we might need to split into chunks. We can use a text splitter from LangChain to split documents.

from langchain.text_splitter import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 700, #  Could be more, for larger models like mistralai/Ministral-8B-Instruct-2410
    chunk_overlap  = 200,
)
documents = text_splitter.split_documents(documents)

Text Splitter Arguments

These are the arguments to the text splitter:

    ‘chunk_size’: the number of tokens in each chunk. Not necessarily the same as the number of words.

    ‘chunk_overlap’: the number of tokens that are included in both chunks where the text is split.

We can check if the maximum document length has changed:

print(f'Number of documents:', len(documents))
print('Maximum document length: ', max([len(doc.page_content) for doc in documents]))

The Document Index

Next, we make a search index for our documents. We will use this index for the retrieval part of ‘Retrieval-Augmented Generation’. We use the open-source library FAISS (Facebook AI Similarity Search) through LangChain.

from langchain_community.vectorstores import FAISS
vectorstore = FAISS.from_documents(documents, huggingface_embeddings)

FAISS can find documents that match a search query:

relevant_documents = vectorstore.similarity_search(query)
print(f'Number of documents found: {len(relevant_documents)}')

We can display the first document:

print(relevant_documents[0].page_content)

For our RAG application we need to access the search engine through an interface called a retriever:

retriever = vectorstore.as_retriever(search_kwargs={'k': 3})

Retriever Arguments

These are the arguments to the retriever:

    ‘k’: the number of documents to return (kNN search)

Making a Prompt

We can use a prompt to tell the language model how to answer. The prompt should contain a few short, helpful instructions. In addition, we provide placeholders for the context and the question. LangChain replaces these with the actual context and question when we execute a query.

from langchain.prompts import PromptTemplate

prompt_template = '''You are an assistant for question-answering tasks.
Use the following pieces of retrieved context to answer the question.
Context: {context}

Question: {input}

Answer:
'''

prompt = PromptTemplate(template=prompt_template,
                        input_variables=['context', 'input'])

Making the «Chatbot»

Now we can use the module create_retrieval_chain from LangChain to make an agent for answering questions, a «chatbot».

from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain

combine_documents_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, combine_documents_chain)

Asking the «Chatbot»

Now, we can send our query to the chatbot.

result = rag_chain.invoke({'input': query})

print(result['answer'])

Hopefully, this answer contains information from the context that wasn’t in the previous answer, when we queried only the language model without RAG.
Exercises

Exercise: Use your own documents

Change the document location to your own documents folder. You can also upload more documents that you want to try with RAG. Change the query to a question that can be answered based on your documents. Try to the run the query and evaluate the answer.

Exercise: Saving the document index

The document index that we created with FAISS is only stored in memory. To avoid having to reindex the documents every time we load the notebook, we can save the index. Try to use the function vectorstore.save_local() to save the index. Then, you can load the index from file using the function FAISS.load_local(). See the documentation of the FAISS module in LangChain for further details.

Exercise: Slurm Jobs

When you have made a program that works, it’s more efficient to run the program as a batch job than in JupyterLab. This is because a JupyterLab session reserves a GPU all the time, also when you’re not running computations. Therefore, you should save your finished program as a regular Python program that you can schedule as a job.

You can save your code by clicking the “File”-menu in JupyterLab, click on “Save and Export Notebook As…” and then click “Executable Script”. The result is the Python file RAG.py that is downloaded to your local computer. You will also need to download the slurm script LLM.slurm.

Upload both the Python file RAG.py and the slurm script LLM.slurm to Fox. Then, start the job with this command:

sbatch LLM.slurm RAG.py

Slurm creates a log file for each job which is stored with a name like slurm-1358473.out. By default, these log files are stored in the current working directory where you run the sbatch command. If you want to store the log files somewhere else, you can add a line like below to your slurm script. Remember to change the username.

#SBATCH --output=/fp/projects01/ec443/<username>/logs/slurm-%j.out
