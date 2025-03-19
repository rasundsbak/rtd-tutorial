.. _08_summarization:

Oppsummeringer
---------------

I denne delen av kurset, skal vi forsøke å bruke språkmidellen på noen artikler. Oppsummeringer av dokumenter har betegnes ogte med sommarizing eller summarization, i koden. Det fins dedikert programvare for å lage oppsummeringer. Imidlertid har store språkmideller også begynt å beherske oppgaven ganske bra.

Nok en gang, skal vi bruke LangChain. Dette er et bibliotek som har åpen kildekode, og som brukes til å lage applikasjoner med store språkmodeller.

.. admonition:: Oppgave: Lage en ny notebook
   :collapsible: closed
  
  Lag en ny Jupyter Notebook som du kaller "summarizing" ved å klikke i JupyterLabs filmeny, deretter "New" og "Notebook". Hvis du blir spurt om å velge en kjerne, velg “Python 3”. Gi den nye notebooken et navn ved å klikke JupyterLabs filmeny og så "Rename Notebook". Bruk navnet "summarizing".

.. admonition:: Oppgave: Stoppe gamle kjerner
   :collapsible: closed



JupyterLab uses a Python kernel to execute the code in each notebook. To free up GPU memory used in the previous chapter, you should stop the kernel for that notebook. In the menu on the left side of JupyterLab, click the dark circle with a white square in it. Then click KERNELS and Shut Down All.
Document location

We have collected some papers licensed with a Creative Commons license. We will try to load all the documents in the folder defined below. If you prefer, you can change this to a different folder name.

document_folder = '/fp/projects01/ec443/documents/terrorism'

The Language Model

We’ll use models from HuggingFace, a website that has tools and models for machine learning. We’ll use the open-weights LLM meta-llama/Llama-3.2-3B-Instruct. This model has a large context window, which means that we can use it to process quite large documents. Yet it is small enough that we can use it with the smallest GPUs on Fox. However, for better results you might want to use one of the somewhat larger models with around 7B or 8B parameters, for example mistralai/Ministral-8B-Instruct-2410.

Tokens versus Words

Short words can be a single token, but longer words usually consist of multiple tokens. Therefore, the maximum document size with this model is less than 128k words. Exactly how words are converted to tokens depends on the tokenizer. LLMs usually come with tokenizers. We will use the default tokenizer that ship with the LLM we use.

import os
os.environ['HF_HOME'] = '/fp/projects01/ec443/huggingface/cache/'

To use the model, we create a pipeline. A pipeline can consist of several processing steps, but in this case, we only need one step. We can use the method HuggingFacePipeline.from_model_id(), which automatically downloads the specified model from HuggingFace.

from langchain_community.llms import HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id='meta-llama/Llama-3.2-3B-Instruct',
    task='text-generation',
    device=0,
    pipeline_kwargs={
        'max_new_tokens': 1000,
        #'do_sample': True,
        #'temperature': 0.3,
        #'num_beams': 4,
    }
)

We can give some arguments to the pipeline:

    model_id: the name of the model on HuggingFace

    task: the task you want to use the model for

    device: the GPU hardware device to use. If we don’t specify a device, no GPU will be used.

    pipeline_kwargs: additional parameters that are passed to the model.

        max_new_tokens: maximum length of the generated text

        do_sample: by default, the most likely next word is chosen. This makes the output deterministic. We can introduce some randomness by sampling among the most likely words instead.

        temperature: the temperature controls the statistical distribution of the next word and is usually between 0 and 1. A low temperature increases the probability of common words. A high temperature increases the probability of outputting a rare word. Model makers often recommend a temperature setting, which we can use as a starting point.

        num_beams: by default the model works with a single sequence of tokens/words. With beam search, the program builds multiple sequences at the same time, and then selects the best one in the end.

Making a Prompt

We can use a prompt to tell the language model how to answer. The prompt should contain a few short, helpful instructions. In addition, we provide placeholders for the input, called context. LangChain replaces the placeholder with the input document when we execute a query.

from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate

separator = '\nYour Summary:\n'
prompt_template = '''Write a summary of the following:

{context}
''' + separator
prompt = PromptTemplate(template=prompt_template,
                        input_variables=['context'])

Separating the Summary from the Input

LangChain returns both the input prompt and the generated response in one long text. To get only the summary, we must split the summary from the document that we sent as input. We can use the LangChain output parser RegexParser for this.

from langchain.output_parsers import RegexParser
import re

output_parser = RegexParser(
    regex=rf'{separator}(.*)',
    output_keys=['summary'],
    flags=re.DOTALL)

Create chain

The document loader loads each PDF page as a separate ‘document’. This is partly for technical reasons because that is the way PDFs are structured. Therefore, we use the chain called create_stuff_documents_chain which joins multiple documents into a single large document.

chain = create_stuff_documents_chain(
        llm, prompt, output_parser=output_parser)

Loading the Documents

We use LangChain’s DirectoryLoader to load all in files in document_folder. document_folder is defined at the start of this Notebook.

from langchain_community.document_loaders import DirectoryLoader

loader = DirectoryLoader(document_folder)
documents = loader.load()
print('number of documents:', len(documents))

Creating the Summaries

Now, we can iterate over these documents with a for-loop.

summaries = {}

for document in documents:
    filename = document.metadata['source']
    print('Summarizing document:', filename)
    result = chain.invoke({"context": [document]})
    summary = result['summary']
    summaries[filename] = summary
    print('Summary of file', filename)
    print(summary)

Saving the Summaries to Text Files

Finally, we save the summaries for later use. We save all the summaries in the file summaries.txt. If you like, you can store each summary in a separate file.

with open('summaries.txt', 'w') as outfile:
    for filename in summaries:
        print('Summary of ', filename, file = outfile)
        print(summaries[filename], file=outfile)
        print(file=outfile)

Bonus Material

Make an Overall Summary

Exercises

Exercise: Summarize your own document

Make a summary of a document that you upload to your own documents folder. Read the summary carefully, and evaluate it with these questions in mind:

    Is the summary useful?

    Is there anything missing from the summary?

    Is the length of the summary suitable?

Exercise: Adjust the summary

Try to make some adjustments to the prompt to modify the summary you got in exercise 1. For example, you can ask for a longer or more concise summary. Or you can tell the model to emphasize certain aspects of the text.

Exercise: Make a summary in a different language

We can use the model to get a summary in a different language from the original document. For example, if the prompt is in Norwegian the response will usually also be Norwegian. You can also specify on the prompt which language you want the summary to be in. Use the model to make a summary of your document from exercise 1 in a different language.

Bonus Exercise: Slurm Jobs
