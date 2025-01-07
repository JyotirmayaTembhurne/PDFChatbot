import google.generativeai as genai

mykey1 = "AIzaSyAOn62o8655Nt37-nAB0BEC_V7rJAs7drg"

# Configure the Gemini API with your key
genai.configure(api_key=mykey1)
model = genai.GenerativeModel("gemini-1.5-flash")


def content_chunking(text):
    full_query = f"""You are a *contextual chunking model* designed to divide text into contextually coherent chunks. 
        Your role is to break down the provided text into logical and meaningful segments based on the subject matter. 
        Each chunk should consist of related sentences that share a common theme or subject. If a heading is present (words of the heading will be marked with ## before and after it), 
        start the chunk with the heading. If no heading is present, generate a 
        suitable heading that describes the content of the chunk. Add ## before and after the headings. 
        Ensure that every word from the original text is included in a chunk and no part of the text is left out. 
        The output should be as large as needed to preserve the integrity of the text. 
        You should return the same chunks consistently every time you receive this text as input.
        End the chunks with ****.
        \n\nText:\n
        "{text}"""
    response = model.generate_content(full_query).text
    chunks = [chunk.strip() for chunk in response.split("****")]
    return chunks


# Define a function to query the model with PDF context
def query_pdf(
    user_query,
    pdf_chunks,
):
    context = "\n\n".join(pdf_chunks)

    # Create a more detailed prompt for Gemini
    full_query = f"""You are an expert AI assistant trained to provide accurate and relevant answers based solely on the content of the provided document. 
    Answer the following question using only the information contained in the document. 
    If the document does not contain enough information to provide a satisfactory answer, politely mention that the document does not contain relevant information.
    You may suggest the user rephrase their query for a more accurate response or offer the information you are trained on, based on the context available in the document. 

    Document Context:
    {context}

    User Question: {user_query}

    Please provide a detailed, accurate, and clear answer based solely on the document context. Be precise in your response and ensure that no additional information outside the provided document is included. 
    If uncertain or the document lacks sufficient information, kindly inform the user and suggest alternatives if necessary."""

    # Create a Gemini model instance
    # Send the combined query to the model and get the response
    response = model.generate_content(full_query)

    return response.text


# Example: User asks about photosynthesis in a PDF
# pdf_context = "Photosynthesis is the process by which plants convert sunlight into energy, using it to produce food from carbon dioxide and water."
# user_query = "What is photosynthesis?"

# Get the answer from Gemini based on the PDF context
# answer = query_pdf_with_gemini(user_query, pdf_context)
