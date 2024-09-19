# Ollama RAG

This is a Retrieval Augmented Generation (RAG) project which can use both the OpenAI API or local computational resources to allow the user to chat with the documents added to the database.

## What makes this different from my other projects?
In this project, new PDF documents can be added to the database without the embedding model having to embed all documents each time documents are added. This is achieved by linking the source PDF and chunk id with each chunk. Each time the embedding model is run, the chunk-ids are stored in a list, preventing the same chunks from being embedded into the chroma vector database.

## In-depth insight on the code
The code is split into 3 files: embeddings.py, query.py, and vector_database.py. Each file handles a unique but very important aspect of the RAG pipeline.

### embeddings.py
This file contains the method to create vector embeddings using the OpenAI API and the local system's computational resources. Using the OpenAI API, the "text-embedding-3-small" model is used to create vector embeddings. If Ollama is used, the "nomic-embed-text" model is used as it provides the best embeddings without taking too long and still providing excellent results.

### query.py
This file uses the embedding function from embeddings.py and uses it to embed the query passed in by the user. Next, the top 5 chunks most similar to the embedded queries are retrieved (using the vector embeddings). The model answers based on a chat prompt template, which takes the retrieved chunks as context and answers the question asked by the user. Here, if Ollama is used, the "mistral" model is used, whereas if the OpenAI API is used, "gpt-4o-mini" is used.

### vector_database.py
This file is used to create the chroma vector database on which the similarity search will take place. When a new document is added to the data folder, the chunking model detects if new chunks have been added. If they have, each chunk is assigned an id with the source name to ensure each chunk can be uniquely identified. Once the text from the documents has been split into chunks, they are embedded into vectors using the embedding funciton from embeddings.py. If the phrase "clear database" is written after typing "python vector_database.py", the vector database will be cleared and all chunk ids will be deleted.
