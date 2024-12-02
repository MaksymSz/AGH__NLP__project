# Natural Language Processing Projects
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.10+-brightgreen.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-blueviolet.svg)
![spaCy](https://img.shields.io/badge/spaCy-3.5+-yellowgreen.svg)
![SQLite](https://img.shields.io/badge/SQLite-3.x-red.svg)

## Overview
This repository contains implementations of three completed as part of the Natural Language Processing (NLP) course during 5th semester. Projects focused on analyzing and generating text, and studying language patterns. Each project explores a different facet of NLP using Python and popular text analysis libraries. Below is an overview of the projects included in this repository. In all projects, the Italian language was the focus of the research. Each project explores different aspects of NLP, from basic text preprocessing to advanced models like Named Entity Recognition (NER).

### 1. Statistical Analysis of Language
**Objective**: Perform statistical analysis on a text corpus to study word frequency, Zipf's law, and semantic networks

**Key Features**:
* Analyzes word frequency and sentence structure
* Implements Zipf's law to evaluate word frequency distributions
* Constructs semantic networks to identify the "core" words of a language
* Provides percentile-based word analyses
  
**Data Source**: [PAISÀ Corpus](https://www.corpusitaliano.it/en/) (Italian Web Texts)
  
### 2. Sentence Generation Application
**Objective**: Create a web application for generating grammatically correct sentences in English

**Key Features**:
* Enables sentence construction using predefined grammar rules
* Supports 12 verb tenses in indicative, interrogative, and negative forms
* Incorporates parts of speech such as nouns, verbs, adjectives, adverbs, and determiners
* Uses a step-by-step interface for sentence customization

**Technologies**:
* Python (Flask Framework)
* HTML/CSS for user interface
* SQLite for words storage

### 3. Verb-Noun Relationship Analysis and Noun Set Manipulation
**Objective**: Analyze semantic relationships between verbs and nouns and provide tools for operations on noun sets

**Key Features**:
* Extracts verb-noun pairs from a text corpus
* Analyzes verb usage patterns and associated nouns
* Implements set operations (AND, OR, XOR) for advanced linguistic inquiries
* Provides a command-line application for semantic analysis
  
**Data Source**: Processed text from the PAISÀ Corpus
  
**Technologies**:
* Python
* [spaCy](https://spacy.io/) for lemmatization and NLP tasks

## Implementation
All projects were developed using Python, leveraging libraries such as:
* `spaCy` for NLP tasks
* `Flask` for web spplication development
* Additional utility libraries for text processing and data visualization

## Table of Contents
- [Installation](#Installation)
- [Structure](#Structure)
- [Data](#Data)
- [Usage](#Usage)
- [Results](#Results)
- [Citations](#Citations)
- [License](#License)

The project is organized into the following directories and files:
```bash
├── README.md                                   	# Project description and usage instructions
├── LICENSE                                     	# License information
├── project_1_Text_Preprocessing
│   ├── code/
│   ├── data/
│   ├── project_1_Report.pdf
│   └── README.md
│
├── project_2_Text_Classification
│   ├── code/
│   ├── data/
│   ├── project_2_Report.pdf
│   └── README.md
│
├── project_3_NER_Model
│   ├── code/
│   ├── data/
│   ├── project_3_Report.pdf
│   └── README.md
│
├── utils
└── requirements.txt                            	# List of required Python packages
```

## Installation
The code for all projects is available in this repository. Clone the repository and follow the instructions in the respective project directories to set up and run the applications.

### Clone the Repository
```bash
git clone https://github.com/MaksymSz/AGH__NLP__project.git
cd AGH__NLP__project
```
### Dependencies
Install the required packages using pip:
```bash
pip install -r requirements.txt
```

## Data
Data can be obtained from public [repository](https://www.corpusitaliano.it/en/).

## Reports
Each project includes a detailed report that covers:

1. Introduction: Brief description of the problem and its relevance. 
2. Methods: Explanation of techniques used in the project. 
3. Results: Key results and performance metrics. 
4. Conclusion: Insights gained and potential improvements.

> **_NOTE:_** Reports can be achieved by direct message
