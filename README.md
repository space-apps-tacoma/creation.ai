# Shockwave Surfers - team project
> 2022 NASA Space Apps Challenge - Tacoma Location

## Selected challenge

> "Can AI Preserve Our Science Legacy?" [:link:](https://2022.spaceappschallenge.org/challenges/2022-challenges/science-legacy/resources)


The challenge is to develop a technique using Artificial Intelligence (AI)
to improve the accessibility and discoverability of records in the public
NASA Technical Report Server ([NTRS](https://ntrs.nasa.gov/)).

## Proposed solution

Improve the accessibility and discoverability of records in the NTRS
- The Search Algorithm (Librarian Analogy)
  1. Enter query through the api
  2. Receive a list of documents
  3. Drill down into the full text of the document
  4. Run NLP to get some statistics for ranking
  
 - automatically read NTRS documents
    - summarize them (Pre-Trained),
    - generate text analytic data (Word Cloud, Frequency Distribution Visualisation, Question Generation and Answering),
    - produce a list of topic keywords to help researchers find the documents they need. 
 - Delivering PDFs in a binder available for reading (with similar parts highlighted)


## Reference

- Challenge specification pdf [:link:](https://cdn.glitch.global/593a4e3c-ebba-4732-879c-242327c0c3b8/challenge-details.pdf?v=1664482261566)
- An example query [:link:](https://ntrs.nasa.gov/api/citations/search?center=CDMS&sort=%7B%22field%22:%22published%22,%22order%22:%22desc%22%7D&subjectCategory=LUNAR%20AND%20PLANETARY%20EXPLORATION&title=IO)
  that returns json and defaults to the first 25 of 345 items.
- json viewers
  - online [:link:](https://jsoneditoronline.org/)
  - jq tutorials [1](https://www.baeldung.com/linux/jq-command-json), [2](https://tecadmin.net/linux-jq-command/)
    ```bash
    cd /data/infiles
    jq '.' query-result.json | less
    jq 'keys' query-result.json
    jq '.results | .[2]' query-result.json | less
    jq '.results | .[2] | .downloads' query-result.json | less
    jq '.results | .[2] | .downloads | .[0]' query-result.json
    jq '.results | .[2] | .downloads | .[0] | .links' query-result.json
    jq '.results | .[2] | .downloads | .[0] | .links | .fulltext' query-result.json
  
    ```
- python
  - json-module [:link:](https://docs.python.org/3/library/json.html)
    (note there is a difference between load and loads !)