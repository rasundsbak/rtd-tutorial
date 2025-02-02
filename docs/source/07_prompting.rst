.. _07 prompting:

07 Prompting
=============
.. index:: prompting

Turning roles around: Who is asking now?
-------------------------------------------
A good promting of the AI whould take into account that the AI might not know your context. For example: "I want to grow vegetables in my garden, but before you answer, make an interview with me so that you can give a best possible answer." The AI may ask how much sunlight there is in your garden, and what kind of soil you have. Background information may be essential for the response the AI gives. The AI and you may not have ended on the same conclusion, if you at first had not asked for the interview.

Tips for future prompting
----------------------------
In this workshop, you will practice deciding the role of the AI. An economist, a gardener or a pirate. The Llama model is known for having a special ability to adapt to a role. This may be good or bad. In order to get a good output with the Llama model, you sometimes have to try to neutralize the ego of the AI. This is done through giving the right formulations of the role in the prompt. In the next chapter, we will experiment with different phrasings to see how the model responds. We will also try limiting the output adjusting the parametres. Many users at UiO have already had a year of experience with prompting the UiO Chat GPT. This is a more advanced AI that can remember the conversation. In your future interactions with various AIs, review outputs critically and refine your prompts iteratively. Use the model's strengths to handle complex tasks by breaking them down into simpler questions, like for instance "what is the best cure of Ibux and Paracetamol, if you have headache?". Use follow up questions. Ask the model to elaborate on something you want to know more about. Context and information is important in order to make use of the AI.

Conversation and the Limits of Computational Architecture
----------------------------------------------------------
When conversations with AI extend too long, the model might begin to seem confused or produce unusual language. Smaller models with fewer parameters may struggle more to maintain coherence, leading to grammatical deterioration in extended dialogues. As interactions with the AI continue, especially without precise prompting, a model might gradually shift its understanding of entities or topics, resulting in a drift in focus or coherence. This issue is partly due to the inherent limitations of the model's context window, which dictates how many tokens the AI can process at once. For models like GPT-3.5, this context window is typically capped at approximately 4096 tokens for text. When this limit is exceeded, older parts of the conversation may be truncated to accommodate new inputs, potentially causing the AI to lose track of earlier components in the conversation. To mitigate these effects and improve coherence, maintain precision in prompting and summarize longer discussions. A practical solution is to ask the model to sum up the conversation, use this as a starting point for a new dialogue, and then delete the old dialogue.
