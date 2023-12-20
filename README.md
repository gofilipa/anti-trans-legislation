# trans bias project overview
This project studies gender bias in language, using current anti-trans
legislation as a test case. The goal is to fine tune a text
classification model to sentences on a scale from non-affirmative to
affirmative.

## data
All data originates from the `www.congress.gov` website, and inclues
bills, amendments, and resolutions from the House of Representatives
and and the Senate over sessions 117 (2022-2023) and 118 (2023-2024).

## methodology
First, I scraped, cleaned, and processed the bill text to prepare it
for text extraction. See the [data gathering](./gathering.ipynb)
notebook for this code. This section uses the `bs4`, `requests`, and
`pandas` library in python. 

Then, I wrote a custom Named Entity Ruler and token matcher to capture
gender terms as they are being defined in the bill text. The matcher
is flexible enough to include definitions for related terms (like
"sexuality," "biological sex"). See the [data
processing](./processing.ipynb). This section uses the `spaCy` and `pandas`

The results are currently being labeled by hand with a "gender
affirming" score, which can be viewd
[here](./out/defs_labels.csv). The next step is to use this dataset to
fine-tune a machine learning model with the Transformers library.
