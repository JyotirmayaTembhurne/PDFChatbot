import streamlit as st
import gemini_model  # Assuming content_chunking and query_pdf are part of this module
from extraction import extract_text  # Assuming this module extracts text from the PDF
from embedding import process_chunks, process_query  # Import embedding functions
from match_embeddings import (
    find_most_similar_chunks,
)  # Assuming this module handles similarity calculation
import base64

# Streamlit UI setup
st.title("Chat with PDF")

# Step 1: PDF Upload
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    # Display the uploaded PDF using a PDF viewer
    pdf_display = uploaded_file.read()
    pdf_base64 = base64.b64encode(pdf_display).decode("utf-8")
    pdf_html = f"""
    <embed src="data:application/pdf;base64,{pdf_base64}" width="100%" height="600px" type="application/pdf">
    """
    st.markdown(pdf_html, unsafe_allow_html=True)

    # Step 2: Extract Text from PDF
    extracted_text = extract_text(uploaded_file)

    # Step 3: Chunk the text into smaller parts (using gemini_model)
    chunks = gemini_model.content_chunking(extracted_text)
    st.write("Chunks Generated:")
    st.write(chunks)

    # Step 4: Convert chunks to embeddings
    chunk_embeddings = process_chunks(chunks)

    # Step 5: User Query Input
    query = st.text_input("Enter your query:")

    if query:
        # Step 6: Convert the query into an embedding
        query_embedding = process_query(query)

        # Step 7: Find the most similar chunks based on the query embedding
        top_matches = find_most_similar_chunks(
            query_embedding, chunk_embeddings, top_n=4
        )

        # Step 8: Extract and display the most relevant chunks based on the similarity
        most_relevant_chunks = [chunks[idx] for idx, _ in top_matches]
        st.write("Most Relevant Chunks:")
        st.write(most_relevant_chunks)

        # Step 9: Combine the relevant chunks into a context for the AI model
        combined_context = "\n\n".join(most_relevant_chunks)

        # Step 10: Generate the response using the AI model (assumed to be handled in gemini_model.query_pdf)
        response = gemini_model.query_pdf(query, combined_context)

        # Step 11: Display the AI-generated response
        st.subheader("AI-Generated Response:")
        st.write(response)

        # Step 12: Save the previous responses (to avoid duplicates)
        if "previous_answers" not in st.session_state:
            st.session_state.previous_answers = []

        if not any(
            answer["query"] == query for answer in st.session_state.previous_answers
        ):
            st.session_state.previous_answers.append(
                {"query": query, "response": response}
            )

    # Step 13: Display Previous Answers
    if "previous_answers" in st.session_state:
        st.subheader("Previous Answers:")
        for idx, answer in enumerate(st.session_state.previous_answers, 1):
            st.markdown(f"**Query {idx}:** {answer['query']}")
            st.markdown(
                f"<div style='background-color: gray; padding: 10px; border-radius: 5px; margin-top: 10px;'>{answer['response']}</div>",
                unsafe_allow_html=True,
            )
