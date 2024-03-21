# anti-trans legislation project
This project uses AI models to study and detect bias and
discrimination in [anti-trans legislation](). 

I am curating various datasets based off [current anti-trans
legislation in the
US](https://www.erininthemorning.com/p/anti-trans-legislative-risk-assessment-96f),
which I am using to train a text generation and text classification
models. 

## federal legislation dataset
The federal legislation dataset originates from the
`www.congress.gov` website, and includes bills, amendments, and
resolutions from the House of Representatives and and the Senate over
sessions 117 (2022-2023) and 118 (2023-2024).

To get this data, I scraped the bill text (see the [data
gathering](./gathering.ipynb) notebook for this code. Then,
I processed the text to prepare it for analysis. Here, I wrote a
custom Named Entity Ruler and token matcher to capture gender terms
being defined in the bill text. The matcher is flexible enough to
include definitions for related terms (like "sexuality," "biological
sex"). See the [data processing](./processing.ipynb). This
section uses the `spaCy` and `pandas`

The results are currently being labeled by hand with a "gender
affirming" score, which can be viewed
[here](./out/defs_labels.csv). The goal is to amass
hundreds of gender definitions and their scores.

Below is an example of the scoring for gender bias, on a scale from
"affirming" (1) and "non-affirming" (0).

| Definition  |Score |
|:----------- |:------------ |
| It must be the policy of every public K-12 educational institution that is provided in this State that the sex of a person is an immutable biological trait and that it is false to ascribe to a person a pronoun that does not correspond to such person's sex.       | 0      |
| An employee or contractor of a public K-12 educational institution may not provide to a student his or her preferred personal title or pronouns if such preferred personal title or pronouns do not correspond to his or her sex.Paragraph   | 0        |
| The term gender identity means the gender-related identity, appearance, mannerisms, or other gender-related characteristics of an individual, regardless of the individual's designated sex at birth. | 1 | 

The next step is to use this dataset to fine-tune a machine learning
model with the Transformers library.

## state legislation dataset

Thanks to the excellent resource prepared by journalist and
transgender rights activist [Erin
Reed](https://www.erininthemorning.com/) excellent work tracking the
bills at a state level, I have been able to download the bills. 

Next step will be to process them into a format for analysis and
pattern extraction. Then, I will use the gender definitions from these
bills to train an AI text generation model. Stay tuned for more info.
