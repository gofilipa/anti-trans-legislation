# project overview
This project studies gender bias in language. It trainsn AI models to detect bias in the way
that gender is defined, and its relationship to related terms like sex and sexuality.

So far, one text generation model has been trained off the data in the [Homosaurus vocabulary](https://homosaurus.org/). 

I am also curating another, more complex dataset to train a classification model that will score gender bias in langauge.
This dataset consists of labeled gender definitions from the anti-trans legislation currently 
proliferating across the US. The goal is to amass hundreds of gender definitions and their scores.
Below is an example of the scoring for gender bias, on a scale from "affirming" (1) and "non-affirming" (0). 

| Definition  |Score |
|:----------- |:------------ |
| It must be the policy of every public K-12 educational institution that is provided in this State that the sex of a person is an immutable biological trait and that it is false to ascribe to a person a pronoun that does not correspond to such person's sex.       | 0      |
| An employee or contractor of a public K-12 educational institution may not provide to a student his or her preferred personal title or pronouns if such preferred personal title or pronouns do not correspond to his or her sex.Paragraph   | 0        |
| The term gender identity means the gender-related identity, appearance, mannerisms, or other gender-related characteristics of an individual, regardless of the individual's designated sex at birth. | 1 | 

## homo-generator
The data for the text generation model ("homo-generator") comes from the [Homosaurus vocabulary](https://homosaurus.org/). 
I used the definitions from this dataset to train the EleutherAI's [gpt-neo-125m](https://huggingface.co/EleutherAI/gpt-neo-125m) model.
You can see [the code](./homo/homo_prep.ipynb) that I used to fine-tune the model, and the [model outputs](homo/homo-model).

So far, I only trained the model on couple hundred lines of the Homosaurus dataset. 
Next step will be to train on the entire dataset, using a supercomputer.

## anti-trans legislation
The data for the classification model (in progress) originates from the `www.congress.gov` website, and includes
bills, amendments, and resolutions from the House of Representatives
and and the Senate over sessions 117 (2022-2023) and 118 (2023-2024).

First, I scraped the bill text. See the [data
gathering](./anti-trans/gathering.ipynb) notebook for this code, which uses the
`bs4`, `requests`, and `pandas` library in python.

Then, I cleaned and processed the text to prepare it for
extraction. Here, I wrote a custom Named Entity Ruler and token
matcher to capture gender terms being defined in the bill
text. The matcher is flexible enough to include definitions for
related terms (like "sexuality," "biological sex"). See the [data
processing](./anti-trans/processing.ipynb). This section uses the `spaCy` and
`pandas`

The results are currently being labeled by hand with a "gender
affirming" score, which can be viewd
[here](./anti-trans/out/defs_labels.csv). The next step is to use this dataset to
fine-tune a machine learning model with the Transformers library.
