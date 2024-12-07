import streamlit as st
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# App title and configuration
st.set_page_config(
    page_title="AgriBot: Agriculture Knowledge Assistant",
    page_icon="🌾",
    layout="wide"
)

# Model loading function (cached to improve performance)
@st.cache_resource
def load_model(model_path):
    try:
        tokenizer = GPT2Tokenizer.from_pretrained(model_path)
        model = GPT2LMHeadModel.from_pretrained(model_path)
        return model, tokenizer
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None, None

# Response generation function
def generate_response(model, tokenizer, prompt, max_length=150):
    try:
        # Prepare input
        input_ids = tokenizer.encode(prompt, return_tensors='pt')
        
        # Generate response
        with torch.no_grad():
            output = model.generate(
                input_ids,
                max_length=max_length,
                num_return_sequences=1,
                no_repeat_ngram_size=2,
                top_k=50,
                top_p=0.95,
                temperature=0.7,
                do_sample=True
            )
        
        # Decode response
        response = tokenizer.decode(output[0], skip_special_tokens=True)
        return response.strip()
    
    except Exception as e:
        st.error(f"Error generating response: {e}")
        return "I'm sorry, I couldn't generate a response."

# Predefined responses for casual queries
def get_casual_response(user_query):
    casual_responses = {
        "hello": "Hello! How can I assist you with agricultural information today?",
        "hi": "Hi there! How can I help you with your agriculture-related questions?",
        "hey": "Hey! I'm the Agriculture Knowledge Assistant. How can I be of assistance?",
        "what's up": "Not much, just waiting to help you with your agriculture questions. How can I be of service?",
        "how are you": "I'm doing great, thanks for asking! How can I help you today?"
    }
    
    for key, value in casual_responses.items():
        if key in user_query.lower():
            return value
    
    return None

# Main Streamlit app
def main():
    # Custom CSS for styling
    st.markdown("""
    <style>
    .main-title {
        font-size: 3rem;
        color: #2C3E50;
        text-align: center;
        margin-bottom: 30px;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #34495E;
        text-align: center;
        margin-bottom: 20px;
    }
    .stTextInput > div > div > input {
        font-size: 1.1rem;
        padding: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

    # App title and description
    st.markdown('<h1 class="main-title">🌾 Agriculture Knowledge Assistant</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Your AI-powered agricultural information companion</p>', unsafe_allow_html=True)

    # Model path (update this to your model's path)
    model_path = './agriculture_gpt2_model'

    # Load the model
    model, tokenizer = load_model(model_path)

    if model is None or tokenizer is None:
        st.error("Failed to load the model. Please check the model path and try again.")
        return

    # User input section
    with st.form(key='query_form'):
        user_query = st.text_input(
            "Ask a question about agriculture:", 
            placeholder="E.g., What is Aquaculture?"
        )
        submit_button = st.form_submit_button(label='Get Answer')

    # Response generation
    if submit_button and user_query:
        # Check for casual queries and provide predefined responses
        casual_response = get_casual_response(user_query)
        if casual_response:
            st.markdown(f"""
            <div style="
                background-color: #F0F4F8; 
                border-left: 5px solid #3498DB; 
                padding: 15px; 
                border-radius: 5px;
                margin-top: 20px;
            ">
            <strong>🌱 Response:</strong><br>
            {casual_response}
            </div>
            """, unsafe_allow_html=True)
        else:
            with st.spinner('Generating response...'):
                response = generate_response(model, tokenizer, user_query)
            
            st.markdown(f"""
            <div style="
                background-color: #F0F4F8; 
                border-left: 5px solid #3498DB; 
                padding: 15px; 
                border-radius: 5px;
                margin-top: 20px;
            ">
            <strong>🌱 Response:</strong><br>
            {response}
            </div>
            """, unsafe_allow_html=True)

    # Additional features
    st.sidebar.header("About the Assistant")
    st.sidebar.info(
        "This AI assistant provides agricultural knowledge "
        "based on a trained GPT-2 model. Always verify critical "
        "information with professional agricultural experts."
    )

    # Footer
    st.markdown("""
    <hr>
    <p style='text-align: center; color: gray;'>
    Powered by GPT-2 | Agriculture Knowledge Base
    </p>
    """, unsafe_allow_html=True)

# Run the app
if __name__ == '__main__':
    main()