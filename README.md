# Chat with PDF Application

This is a Python-based application that allows users to interact with PDF documents through a chat interface. The app extracts text from uploaded PDFs, chunks the content, computes embeddings, and uses semantic similarity to provide relevant answers to user queries.

## Features
- Upload a PDF file and extract its text.
- Chunk the extracted text into meaningful segments.
- Convert text and queries into embeddings using Sentence Transformers.
- Find the most relevant chunks for the query based on cosine similarity.
- Display AI-generated responses based on the selected document context.
  
## Requirements

To run this application, you need to have Python 3.7+ installed. This project relies on the following Python packages:

- `streamlit` - For building the web application interface.
- `sentence-transformers` - For generating text embeddings.
- `sklearn` - For cosine similarity calculation.
- `PyPDF2` or `pdfplumber` (depending on your preference) - For PDF text extraction.
- `numpy` - For numerical operations.
- `gemini-model` (or equivalent for chunking and querying).

## Gemini API Key

This application utilizes the **Gemini API** for chunking and querying document content. To use the Gemini API, you will need an API key. Follow the steps below to obtain your key:

### Steps to Get a Gemini API Key:

1. **Sign Up or Log In**  
   - Go to the official [Gemini website](https://www.gemini.com/) (or the appropriate API provider URL).
   - Create an account or log in to your existing account.

2. **Navigate to the API Section**  
   - Once logged in, go to the API section of your account dashboard.

3. **Generate an API Key**  
   - Follow the instructions to generate a new API key. You may need to specify the permissions or scope of the API key depending on your usage.

4. **Copy the API Key**  
   - Once generated, copy the API key and store it securely. This key will be used to authenticate requests to the Gemini API.

### Setting the API Key in the Application

Once you have your API key, you need to set it in the application:

1. **Create a `.env` file**  
   - In the root directory of the project, create a `.env` file if it does not already exist.

2. **Add the API Key**  
   - Inside the `.env` file, add the following line:
     ```
     GEMINI_API_KEY=your_api_key_here
     ```

3. **Access the API Key in Code**  
   - The application will automatically read the API key from the `.env` file. Ensure that you have a library like `python-dotenv` installed to load environment variables.

   If you do not have `python-dotenv` installed, you can install it by running:
   ```bash
   pip install python-dotenv

## Setting up the Virtual Environment

To set up and run this application, follow these steps:

1. **Install Python 3.7+**  
   Ensure that you have Python 3.7 or above installed. You can check this by running:
   ```bash
   python --version
   ```

2. **Create a Virtual Environment**  
   It’s recommended to use a virtual environment to manage dependencies. You can create one by running:
   ```bash
   python -m venv chat_pdf_env
   ```

3. **Activate the Virtual Environment**  
   To activate the environment:
   - On Windows:
     ```bash
     .\chat_pdf_env\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source chat_pdf_env/bin/activate
     ```

4. **Install the Required Dependencies**  
   Install the required Python modules using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

   Or manually install the following modules:
   ```bash
   pip install streamlit sentence-transformers sklearn numpy PyPDF2 pdfplumber
   ```

5. **Run the Application**  
   Once the environment is set up, you can run the application using Streamlit:
   ```bash
   streamlit run main.py
   ```

6. **Access the Application**  
   After running the above command, the application will be available at `http://localhost:8501/` in your browser.

## Project Structure

```
chat_with_pdf/
│
├── main.py                  # Main Streamlit application
├── embedding.py             # Handles the creation of embeddings for chunks and queries
├── match_embeddings.py      # Finds the most similar chunks based on cosine similarity
├── gemini_model.py          # Contains logic for chunking and querying (adjust as needed)
├── extraction.py            # Extracts text from uploaded PDFs
├── requirements.txt         # List of dependencies
└── README.md                # Project documentation
```

## Example Use Case

1. **Upload a PDF**: Users can upload a PDF file.
2. **Query the PDF**: After extraction, the user can type a query. The app will process the query by finding the most relevant chunks from the document using embeddings.
3. **Response Generation**: An AI response is generated based on the selected document context, which is returned to the user.

## Troubleshooting

- **Missing Dependencies**: Ensure all required libraries are installed using `pip install -r requirements.txt`.
- **PDF Parsing Issues**: If the text extraction doesn't work as expected, try using `pdfplumber` or `PyPDF2` to extract the text.
  
## License

This project is open source and available under the MIT License.

