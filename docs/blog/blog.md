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

## Literature Review and Project Scheduling

To aid in my Project Approval and to get initial feedback from my supervisor I decided to write up my literature review during Week 10. This gave me time to revise my literature review and to submit the first draft to my supervisor before our meeting on Friday 1st  December.  Through the process of writing the literature review I have refined my project direction and scope. I also made a Gantt chart of the projected tasks to be completed to get a better idea of the scope and duration of this project. The Research Plan section of my Literature Review combined with the following Gantt chart is the basis for my project schedule. I plan to have a complete structure-percept dataset with some initial PCA completed for our next meeting at the end of Week 11. 

A Literature Review Document is due to be submitted for CA640 at the end of the semester. I plan to revise my Literature Review with feedback from my CA685 supervisor before submitting for CA640.

![Gantt](https://gitlab.computing.dcu.ie/kealyd2/2018-mcm-kealyd2/raw/master/docs/blog/images/GanttChartDenisKealy.png)

## Second Supervisor Meeting

I met with Martin Crane on the 24th of November for a brief 30-minute session. We discussed my progress thus far and in particular, we went over my literature review and project scheduling issues. Martin has continually expressed concern as to the scope and finishing point of such an investigation. He gave me advice on securing a minimum viable project while still working towards my ideal goal. It may not be possible to attempt all stages of my research plan and as such I will work to identify key stopping points that would yield sufficient results or new knowledge. I was unable to fully augment the structure-percept dataset with the appropriate chemical descriptor sets. We spoke about contacting researchers in the U.S who have collected an appropriate dataset for this investigation. This data could be used as our training data or it could be combined with freely available data sources to form the largest dataset on which such experimentation has ever been carried out. Differences between data sources remains an immediate challenge. I have decided to do some initial PCA on the dataset and to use this work for my Data Visualisation Assignment (CA682). This allows me to spend more time exploring and visualising this dataset before I begin training models with the data.

## Practicum Approval Panel Presentation

I completed my Practicum Approval Panel Presentation on Mon 4th December. Liam Touhey and Qun Liu were the two lecturers on the Panel for my timeslot. The feedback I received was similar to my supervisor's feedback - I have to be careful with the scope of this project as there are a lot of steps and quite a few potential hiccups which could hinder my progress. The main concern was that the complexity of the problem and the amount of work to be done may be too substantial for a Master's Practicum and more suited to a Ph.D. programme. I presented my idea in the following manner:

- Structure-Odor Relationship - Explanation of Problem
- Explainable AI - Explanation of Proposed Solution
- Previous Machine Learning Experiments in this area
	- 2015 Paper using publically available datasets
	- 2017 Paper using private experimental dataset
- Background of Olfaction Processing
	- Difficulties of Problem
	- How XAI can be used in this regard
- Research Plan (Ideal Scenario)
	- Data Collection & Combination
	- Data Validation - PCA, Co-variance, Co-occurrance
 	- Machine Learning Training
	- Machine Learning Testing
	- Comparing with existing solutions 
	- Integrating Interpretability with successful Model (Realistic Minimum Viable Project)
	- Examination of our models outputs
	- Discussion of Results
	- Packaging Software Release

I am taking the concerns about scope very seriously - as such I have decided re-use as much data and code as I can from previous experiments. I went to contact researchers in Rockafeller University in the U.S. over the weekend of Week 11 after my meeting with Martin. Martin's advice was: "They can only say no... or ignore you" - As neither of these outcomes would negatively affect my investigation I decided to reach out to them about their "unpublished dataset" used in a 2017 Structure-Odor-Relationship study. As it turns out a complete data set was published in a previous paper. I now have access to the full dataset used in this study - barring the chemical descriptors which I have still yet to obtain from DRAGON software or an online database. (The school of science may have a license for DRAGON which would reduce the amount of data collection/processing that I have to complete to obtain a suitable dataset for my machine learning program.)
