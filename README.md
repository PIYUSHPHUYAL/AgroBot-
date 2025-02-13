# Agro-Bot: AI-Powered Agricultural Chatbot

## Project Overview
Agro-Bot is an AI-driven chatbot designed to assist farmers with instant, reliable agricultural information. Utilizing Natural Language Processing (NLP) and a fine-tuned GPT-2 model, it addresses agricultural queries with precision and context-aware responses.

## Key Features
- **Intelligent Query Resolution**: Delivers accurate answers to agricultural queries.
- **Web Scraping Data Collection**: Gathers data from trustworthy agricultural websites.
- **GPT-2 Model Fine-Tuning**: Trained specifically on agricultural topics.
- **User-Friendly Interface**: Powered by Streamlit for an interactive web experience.

## Project Workflow

### 1. Data Collection
- **Script Used**: `scraper.py`
- **Process**:
  - Scrapes data from agricultural websites.
  - Generates a `data.txt` file containing relevant agricultural information.

### 2. Data Processing
- **Script Used**: `data_collection.py`
- **Process**:
  - Processes the `data.txt` file.
  - Prepares the dataset for GPT-2 model training by cleaning and structuring the data.

### 3. Model Training
- **Environment**: Google Colab with GPU acceleration.
- **Process**:
  - Fine-tunes the GPT-2 model using the processed dataset.
  - Saves the trained model for deployment.

### 4. Application Deployment
- **Script Used**: `app.py`
- **Platform**: Streamlit.
- **Process**:
  - Deploys the chatbot model to a web interface.
  - Provides an interactive platform for user queries.

## Installation and Usage

### Prerequisites
Ensure the following libraries are installed:
- `streamlit`
- `transformers`
- `datasets`
- `torch`
- `requests`
- `beautifulsoup4`

### Steps to Run the Project

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/agro-bot.git
   cd agro-bot
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Data Scraping**:
   ```bash
   python scraper.py
   ```

4. **Process Data**:
   ```bash
   python data_collection.py
   ```

5. **Train the Model**:
   - Open `Google Colab`.
   - Upload the dataset and fine-tune GPT-2.
   - Save the trained model to `./model/` directory.

6. **Launch the Application**:
   ```bash
   streamlit run app.py
   ```

## Project Structure
- `scraper.py`: Collects data from agricultural websites.
- `data_collection.py`: Processes scraped data for training.
- `train_model.ipynb`: Jupyter notebook for fine-tuning GPT-2 in Google Colab.
- `app.py`: Streamlit-based chatbot interface.

## Contributing
Contributions are welcome! You can:
- Expand the dataset.
- Enhance GPT-2 fine-tuning.
- Improve the Streamlit UI.
- Report bugs and suggest features.

## Future Roadmap
- Broaden dataset coverage.
- Increase model accuracy.
- Add multilingual support.
- Incorporate advanced NLP techniques.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact
For questions, suggestions, or collaboration opportunities, please open an issue in the repository or contact us directly.

