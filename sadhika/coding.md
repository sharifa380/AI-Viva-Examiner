training day 3 :

&#x20;

COMMANDS (PYTHON PACKAGING GUIDE)



\---> to create the file in AI FULL STACK

\---> py -m venv.venv

\---> .venv\\scripts\\activate

\---> py -m pip --version

\---> pip install ollama

\---> then create a file name chatbot.py

\---> then write the code under chatbot.py  (middle in the code to finding the model thats why write in under the terminal ollama list )



**CODEING**



import ollama

response = ollama.chat(model="llama3.2:latest",messages=\[

&#x20;   {

&#x20;       "role":"user",

&#x20;       "content":"what is the role of AI in 2026? Answer in a sentance of 50 words max."

&#x20;   }

])

print(response.message.content)



\---> then execute in the terminal by giving python chatbot.py



import ollama

SYSTEM = ''' You explain programming error messages to a 2nd year engineering student.Reply in 3 parts.1)what is meansin plain english.2) the likely cause.3)how to fix it.keep it under 100 words.'''

response = ollama.chat(model="ollama3.2:latest",messages=\[

&#x20;   {

&#x20;       "role":"system",

&#x20;       "content":SYSTEM

&#x20;   },

&#x20;   {

&#x20;       "role":"user",

&#x20;       "content":"python error - NameEror: name x is not defined"

&#x20;

&#x20;   }

])

print(response.message.content)



28 09 26



topic: streamlit

coding:

import streamlit as st

st.title("welcome to streamlit!")

st.write("Hello !.... MRECW")

name=st.text\_input("Enter your name:")

if name:

&#x20;   st.write(f"your name is {name}")



coding: for option selected:



import streamlit as st

st.title("my AI bot:synora")

name = "Sharifa"

st.write("welcome,",name)

\#dropdown

\#create a dropdown - select your favourite programming language

\#write the selected language

options=\['py','C','C++','Javascripts','HTML','CSS']

select\_options=st.selectbox('choose an option',options)

st.write("You have selected:",select\_options)

question = st.text\_input("Ask a question")

if st.button("Ask"):

&#x20;   st.write("you asked:",question)



code for asking question and giving aswer in streamlit:



import streamlit as st

from ollama import chat

st.title("my AI bot:synora")

system\_message = "You are a Shakespearean tutor.Answer in a sentence of 50 words max."

if "messages" not in st.session\_state:

&#x20;   st.session\_state.messages=\[

&#x20;       {

&#x20;           "role":"system",

&#x20;           "content":system\_message

&#x20;       }

&#x20;   ]

\#Display previous messages

for message in st.session\_state.messages:

&#x20;   if message\["role"] != "system":

&#x20;       with st.chat\_message(message\['role']):

&#x20;           st.write(message\['content'])

&#x20;





name = "Sharifa"

st.write("welcome,",name)

\#dropdown

\#create a dropdown - select your favourite programming language

\#write the selected language

options=\['py','C','C++','Javascripts','HTML','CSS']

select\_options=st.selectbox('choose an option',options)

st.write("You have selected:",select\_options)

question = st.chat\_input("Ask a question")

if question:

&#x20;   #show user message

&#x20;   with st.chat\_message("user"):

&#x20;       st.write(question)

&#x20;   st.session\_state.messages.append({

&#x20;       "role":"user",

&#x20;       "content":question

&#x20;   })

&#x20;   with st.spinner("Thinking ..."):

&#x20;       response = chat(model = "phi3:latest",messages = st.session\_state.messages)

&#x20;       answer = response.message.content

&#x20;       #show assistant message

&#x20;       with st.chat\_message("assistant"):

&#x20;           st.write(answer)

&#x20;       #save the assistant message

&#x20;       st.session\_state.messages.append({



&#x20;           "content":answer

&#x20;       })



sentences transformers:

coding:

from sentence\_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

vec  = model.encode("Telangana's capital is Hyderabad")

print(len(vec))

print(vec\[:5])

vec\_1 = model.encode("I like reading books")

print(len(vec\_1))



RAG: (RETRIEVAL - AUGMENTED GENERATION)

RAG: rag is a technique where relevant information is retrived from external documents and given to an LLM before it generates an answer.

RETRIEVAL: find the relevant  information

GENERATION:answer using that information

&#x20;

Textbook --> search --> Relevant page ---> AI ----> ANSWER

think of rag as an open - book exam

closed - book exam :uses only memory

open - book exam: finds relevant information reads it uses it to answer

&#x20;LLM:learned knowledge



python -c "import sys;print(sys.exceutable)" ---> Cammand

\-----> **embedding model**: coverts the text into numerical vectors

&#x20;----> embedding model  are stores in database



coding:



from pypdf import PdfReader



\#Function to create chunks from text

def create\_chunks(text,size):

&#x20;   chunks = \[]

&#x20;   for i in range(0,len(text),size):

&#x20;       chunk = text\[i:i+size]

&#x20;       chunks.append(chunk)

&#x20;   return chunks

try:

&#x20;   #Read pdf

&#x20;   reader = PdfReader("sample.pdf")

&#x20;   print("Number of pages:",len(reader.pages))

&#x20;   text = ""

&#x20;   #Extract text

&#x20;   for page in reader.pages:

&#x20;       text+=page.extract\_text()

&#x20;   print(text)



&#x20;   # Create embeddings

&#x20;   from sentence\_transformers import SentenceTransformer

&#x20;   model = SentenceTransformer("all-MiniLM-L6-v2")

&#x20;   embeddings = model.encode(chunks\_list)

&#x20;   print("Number of chunks:",len(chunks\_list))

&#x20;   print("Number of embeddings:",len(embeddings))

&#x20;   print(embeddings)

except FileNotFoundError:

&#x20;   print("File not found")



creating a list in single statement:

ids:starting from 0 to 7

in a chromadb string are the

8 chunks are there in chromadb



coding:

import streamlit as st



st.set\_page\_config(

&#x20;   page\_title = "Documind - HR assistant",

&#x20;   layout = "wide",

&#x20;   page\_icon = "📚"

)



question = st.chat\_input("Ask something about your document..")



from pypdf import PdfReader

import chromadb



\#Function to create chunks from text

def create\_chunks(text,size):

&#x20;   chunks = \[]

&#x20;   for i in range(0,len(text),size):

&#x20;       chunk = text\[i:i+size]

&#x20;       chunks.append(chunk)

&#x20;   return chunks

try:

&#x20;   #Read pdf

&#x20;   reader = PdfReader("sample.pdf")

&#x20;   print("Number of pages:",len(reader.pages))

&#x20;   text= ""

&#x20;   #Extract text

&#x20;   for page in reader.pages:z

&#x20;       text+=page.extract\_text()

&#x20;   print(text)



&#x20;   #create chunks

&#x20;   chunks\_list = create\_chunks(text, 500)

&#x20;   print("Number of chunks:", len(chunks\_list))



&#x20;   #Create embeddings

&#x20;   from sentence\_transformers import SentenceTransformer

&#x20;   model = SentenceTransformer("all-miniLM-L6-v2")

&#x20;   embeddings = model.encode(chunks\_list)

&#x20;   print("Number of chunks:",len(chunks\_list))

&#x20;   print("Number of embeddings:",len(embeddings))

&#x20;   print(embeddings)

&#x20;   #Chroma DB -persistent storage

&#x20;   client = chromadb.PersistentClient(path="./doc.store")

&#x20;   collection = client.get\_or\_create\_collection(name="my\_notes")

&#x20;   #Add to collection

&#x20;   collection.add(ids=\[str(i) for i in range(len(chunks\_list))],

&#x20;                  documents = chunks\_list,

&#x20;                  embeddings = embeddings.tolist()

&#x20;   )

&#x20;   print("Documents stored:",collection.count())

&#x20;



except FileNotFoundError:

&#x20;   print("File not found")

\#Quesion processing - using Streamlit,

\#sentence transformer,chromadb, ollama



if question:

&#x20;   #embed query

&#x20;   question\_embedding = model.encode(question)

&#x20;   # Give the most relevant chunks

&#x20;   results = collection.query(query\_embeddings =

&#x20;   \[question\_embedding.tolist()],n\_results = 2)

&#x20;   documents = result\["documents"]\[0]

&#x20;   context = "\\n\\n".join(documents)

&#x20;   #Ask the model

&#x20;   prompt = f'''

&#x20;   Answer the question using ONLY the information proviede below.

&#x20;   If the answer is not present in the information, say "I don't know based on this document".

&#x20;       Information:

&#x20;   {context}

&#x20;       Question:

&#x20;   {question}

&#x20;

huggingface to go and create a token 

and give a name like streamlit

