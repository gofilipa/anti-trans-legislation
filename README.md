# anti-trans legislation project

This project uses AI models to study and detect bias and
discrimination in anti-trans discourse. It curates datasets from
legislation about transgender people, legislation which for the large
part works to [limit transgender
rights](https://translegislation.com/) relating to healthcare, access
to bathrooms, sports and more, at the federal and state level. The
goal is to use language about sex, gender, sexuality, and related
terms from the legislation to train text generation and text
classification Large Language Models (llms).

## datasets

The federal legislation dataset originates from the `www.congress.gov`
website, and includes bills, amendments, and resolutions from the
House of Representatives and and the Senate over sessions 117
(2022-2023) and 118 (2023-2024) that contain the keyword
"transgender." The state bills dataset originates from Erin Reed's
"[LGBTQ+ Legislative Tracking
2023](https://docs.google.com/spreadsheets/d/1fTxHLjBa86GA7WCT-V6AbEMGRFPMJndnaVGoZZX4PMw/edit?usp=sharing)"
document, which gathers legislation that are explicitly anti-trans.

All of the code for gathering and processing the federal data is
available in this repository. To get this data, I scraped the bill
text from `congress.gov` servers (see the [data
gathering](./gathering.ipynb) and [data
processing](./processing/processing.ipynb) notebooks). The processing
notebook contains a matcher that extracts definitions of gender and
related terms (like "sexuality," "biological sex", etc). You can see
the final dataset on my Huggingface [datasets
page](https://huggingface.co/datasets/gofilipa/gender_congress_117-118).

<!--
The results are currently being labeled by hand with a "gender
affirming" score, which can be viewed [here](./out/defs_labels.csv).
The goal is to amass hundreds of gender definitions and their scores.

Below is an example of the scoring for gender bias, on a scale from
"affirming" (1) and "non-affirming" (0).

| Definition  |Score |
|:----------- |:------------ |
| It must be the policy of every public K-12 educational institution that is provided in this State that the sex of a person is an immutable biological trait and that it is false to ascribe to a person a pronoun that does not correspond to such person's sex.       | 0      |
| An employee or contractor of a public K-12 educational institution may not provide to a student his or her preferred personal title or pronouns if such preferred personal title or pronouns do not correspond to his or her sex.Paragraph   | 0        |
| The term gender identity means the gender-related identity, appearance, mannerisms, or other gender-related characteristics of an individual, regardless of the individual's designated sex at birth. | 1 | 

The next step is to use this dataset to fine-tune a machine learning
model with the Transformers library. --> 

## training

I am currently in the process of using the data to train models which
you can see on my HuggingFace profile page,
[gofilipa](https://huggingface.co/gofilipa).
