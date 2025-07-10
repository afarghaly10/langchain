# Intro to vectors db

## Objectives

Create/ Mimic the RAG (Retrieval-Augmented Generation). RAG is the process of optimizing the output of LLM, so if refrences an authoritative knowledge outside of its training data source before generating a response.

<!-- In this project we will use a Medium Article to be authritative knowledge
Take a Medium Article, Load it, split it up to chunks, embed everything and store in the vector store. Based on the user's question the supporting data can be retrieved 

get relevant vecotors that are near this question vector, get back those documents. After that Documentation  -->

## Steps

### Step-1: Ingestion

1. Take a blog from Medium articles, create a `txt` file, and then copy and past the article into the file
1. Laod it to the Langchain document object
2. Split this object with text splitter into smaller chunks
3. Embed those chunks and turn them into vectors
4. Store vectors in Pinecone vector store


### Step-2: Revtieval

1. Take the user input
2. Embed it so we generate a vector representation of the user's request
3. Ask the Vector store (Pinecone) to get relevant vectors that are near this request's vector
4. Return the documents corresponding to those Vectors

### Step-3: Documentation

1. Take the original prompt
2. Augement it with the relevant document chunks
3. Send all the data to the LLM to the generation part
4. Return a well-grounded answer