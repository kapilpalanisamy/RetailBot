import streamlit as st
from langchain_helper import get_few_shot_db_chain

st.title("T Shirts : Database Q&A 👕")

# Add some styling and information
st.markdown("""
Welcome to the T-Shirt Inventory Q&A System! 

Ask questions about our t-shirt inventory in natural language and get intelligent answers.

**Example questions you can ask:**
- How many white Nike t-shirts do we have in size XS?
- What's the total value of all Levi's t-shirts?
- How much revenue would we generate selling all Adidas t-shirts with discounts?
""")

# Create a text input for questions
question = st.text_input("Question: ", placeholder="Type your question about t-shirt inventory...")

if question:
    with st.spinner('Searching the database...'):
        try:
            # Get the database chain
            chain = get_few_shot_db_chain()
            
            # Get the answer
            answer = chain.run(question)
            
            # Display the answer
            st.header("Answer:")
            st.write(answer)
            
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            st.write("Please check your database connection and try again.")

# Add some additional information in the sidebar
with st.sidebar:
    st.header("About")
    st.write("""
    This application uses:
    - **LangChain** for natural language processing
    - **Google Gemini AI** for intelligent query understanding  
    - **MySQL Database** for t-shirt inventory data
    - **Few-shot Learning** for improved accuracy
    """)
    
    st.header("Database Schema")
    st.write("""
    **t_shirts table:**
    - t_shirt_id, brand, color, size, price, stock_quantity
    
    **discounts table:**
    - t_shirt_id, pct_discount
    """)
     
