# Blog: Analysis of the Structure-Odour-Relationship

**Denis Kealy**

## Acquiring a Supervisor

On 24th October, I approached Martin Crane (of the DCU School of Computing) concerning the ideas I have for my practicum project. I uploaded an initial project proposal document which outlined multiple project directions to my gitlab repository. I met with Martin on the 3rd of November - he shared with me his concerns about the complexity of the project as well as his concerns about his fit for this type of project.  He sent me off to further investigate project ideas and to narrow down my range of project directions. We decided to set up a meeting with Tim Downing in DCU’s School of Science to avail of an expert opinion in the domain of Bioinformatics for the purposes of further investigating the complexity and feasibility of such a project.


## Meeting with School of Science faculty

I met with Tim Downing on 8th November to discuss my project ideas. For this meeting, I had focused on a singular idea which, Martin had expressed the most interest in - Explainable AI and the Structure-Odour-Relationship. I went through two papers (which were most relevant to my idea) with Tim and I showed him the data sources that I was considering using for my experimentation. He outlined his concern that the genomic and proteomic data I wanted to use was incomplete and out of date for the fast-moving field of Bioinformatics. We settled on a configurable Explainable AI system which takes molecular descriptors as it’s input to try and classify molecules based on this information. In our case we are trying to classify the molecules perceived scent but Tim noted that this approach could be used to help solve a broad range of problems such as predicting the effects of a new drug or predicting the toxicity of unknown molecules. This approach to solving the problem allows us to abstract the biological details of human olfaction processing as we are only concerned with how our machine classifies smell molecules - not the underlying biological processes by which we humans arrive at our perception.

## Project Proposal Submission

On November 10th, I replaced my initial Project Proposal document with a final version for my Project Proposal Presentation. Dr. Martin Crane assigned himself to my project in the MCM dashboard and we have scheduled to meet on 17th November. In the meantime, Martin has asked me to make a start on implementing an Explainable AI system. For use in my machine learning/classification system I shall require a heavily processed dataset. Martin suggested to do a bit of early stage modelling on a small, clean olfactory dataset to reassure myself about the project before committing myself further. I plan to use scrapy (python library) to obtain a relevant data set from flavornet (mapping of CAS number to a perceived scent). Using the CAS number we can obtain a set of physical descriptors for each molecule using software such as DRAGON or [E-DRAGON](http://www.vcclab.org/lab/edragon/). I plan to use [Mole.db](http://michem.disat.unimib.it/mole_db/) to extract the molecular descriptors for the relevant molecules in my olfaction dataset for a proof of concept-type application.

## First Official Supervisor Meeting

I met with my supervisor on the 17th of November. We discussed my progress so far. I had prepared a small dataset of 500 molecules mapped to their percieved scent - scraped from [flavornet.org](http://www.flavornet.org/flavornet.html). I ran into difficulties when I attempted to augment this dataset with a set of physical descriptors for each entry. There are inconsistencies and missing data between the different data sources. The second database (Mole.db) is a lot trickier to scrape than flavornet.org (one static page) due to the structure of the PHP pages. We discussed the topics to address in my Literature Review (and how to address them) and Martin gave me a list of deliverables for our next meeting which is scheduled for the 1st of December.

Martin's Deliverables for next Meeting:
- Do Gannt chart of work to be done
- Has to do more data pre-processing (e.g. combine DBs)
- PCA could be useful in reducing the dimensionality of the data
- With so many variables student will have to code up the PCA solver by hand
- Look at noise in the data (Random Matrix Theory)
- Do some toy coding with about 10 known descriptors & 10 random ones to test the PCA code and then scale up the code to do the full 1200
- OpenMP could be useful here


