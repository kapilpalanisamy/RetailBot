# AI-Powered Natural Language to SQL Query System for Retail Inventory Management

This project demonstrates how to use LangChain with Google's Gemini AI to create an intelligent SQL query assistant for a t-shirt retail database with a user-friendly Streamlit web interface.

## Features

- **Natural Language to SQL**: Ask questions in plain English about your t-shirt inventory
- **Few-Shot Learning**: Improved accuracy using example queries and responses
- **Semantic Similarity**: Uses embeddings to select the most relevant examples
- **Database Integration**: Direct connection to MySQL database with t-shirt inventory data
- **Streamlit Web Interface**: Beautiful, interactive web application
- **Real-time Responses**: Get instant answers to your inventory questions

## Setup

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Environment Setup**:
   ```bash
   # Copy the example environment file
   cp .env.example .env
   
   # Edit .env file and add your credentials
   # NEVER commit .env file to version control
   ```
   
   Add your actual credentials to the `.env` file:
   ```
   GOOGLE_API_KEY=your_actual_google_api_key_here
   DB_PASSWORD=your_actual_database_password_here
   ```

3. **Quick Setup** (Alternative):
   ```bash
   python setup.py
   ```

4. **Database Setup**:
   - Ensure MySQL is running on localhost:3306
   - Create the `atliq_tshirts` database
   - Make sure the database contains the following tables:
     - `t_shirts` (with columns: t_shirt_id, brand, color, size, price, stock_quantity)
     - `discounts` (with columns: t_shirt_id, pct_discount)

## 🔒 Security

This project follows security best practices:

- ✅ **No hardcoded credentials** - All sensitive data is stored in environment variables
- ✅ **`.env` file in `.gitignore`** - Prevents accidental credential commits
- ✅ **Environment variable validation** - Checks for required credentials
- ✅ **Example configuration** - `.env.example` shows required variables without exposing real values

**Important**: Never commit your `.env` file or any files containing real API keys or passwords!

## Usage

### Option 1: Run the Streamlit Web Application (Recommended)
```bash
# Using the run script
python run_app.py

# Or directly with Streamlit
streamlit run main.py
```

The web application will open in your browser at `http://localhost:8501`

### Option 2: Run the Complete Demo Script
```bash
python langchain_helper.py
```

### Example Questions You Can Ask:

- "How many white Nike t-shirts do we have in size XS?"
- "What's the total value of all Levi's t-shirts in inventory?"
- "How much revenue would we generate selling all Adidas t-shirts with discounts?"
- "How many medium-sized t-shirts do we have in total?"
- "If we sell all Van Heusen t-shirts today with discounts, how much revenue will we generate?"

## File Structure

- `main.py` - Streamlit web application
- `langchain_helper.py` - Core LangChain functionality with few-shot learning
- `few_shots.py` - Example queries for few-shot learning
- `run_app.py` - Helper script to run the Streamlit app
- `requirements.txt` - Python dependencies
- `.env.example` - Environment variables template
- `README.md` - This documentation

## Key Components

### LangChain Helper (`langchain_helper.py`)
- **Google Gemini Integration**: Uses the latest Gemini 1.5 Flash model
- **Semantic Similarity**: Automatically selects the best examples for each query
- **Vector Embeddings**: Uses Sentence Transformers for semantic understanding
- **Few-Shot Learning**: Learns from example queries to improve accuracy

### Streamlit Interface (`main.py`)
- **User-Friendly UI**: Clean, intuitive web interface
- **Real-Time Processing**: Instant responses to user questions
- **Error Handling**: Graceful handling of database and API errors
- **Helpful Information**: Examples and database schema in sidebar

## Database Schema

### t_shirts table:
- `t_shirt_id` - Unique identifier
- `brand` - T-shirt brand (Nike, Adidas, Levi, etc.)
- `color` - Color of the t-shirt
- `size` - Size (XS, S, M, L, XL, etc.)
- `price` - Price per unit
- `stock_quantity` - Number of items in stock

### discounts table:
- `t_shirt_id` - Foreign key to t_shirts table
- `pct_discount` - Percentage discount (0-100)

## Technical Details

- **LLM Model**: Google Gemini 1.5 Flash (cost-effective and fast)
- **Embeddings**: Sentence Transformers all-MiniLM-L6-v2
- **Vector Store**: ChromaDB for similarity search
- **Database**: MySQL with PyMySQL connector
- **Web Framework**: Streamlit for the user interface

## Troubleshooting

1. **Database Connection Issues**: 
   - Ensure MySQL is running
   - Check database credentials in `langchain_helper.py`
   - Verify database and tables exist

2. **API Key Issues**:
   - Make sure your Google API key is valid
   - Check the `.env` file is properly configured

3. **Package Installation Issues**:
   - Try upgrading pip: `pip install --upgrade pip`
   - Install packages one by one if bulk install fails

## Notes

- The application uses semantic similarity to automatically select the most relevant examples
- Few-shot learning examples help the AI understand your specific database schema
- The system is optimized for the t-shirt retail domain but can be adapted for other databases
