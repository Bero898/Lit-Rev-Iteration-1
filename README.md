# Microservice Topic Modelling

This repository contains code and data for performing topic modelling on academic articles related to microservices, using both IEEE and ACM sources. The workflow includes data preprocessing, merging datasets with different structures, and applying multiple topic modelling techniques (LDA, FLSA-W, BERTopic) with evaluation and visualization.

---

## Repository Structure

```
.
├── filtered_output_IEEE/           # Filtered IEEE CSV files (Books, Journals, Conferences)
├── filtered_output/                # Filtered ACM CSV files
├── topics/                         # Output: CSVs of articles per topic
├── requirements.txt                # Python dependencies
├── TopicModelling_Microservice.ipynb  # Main Jupyter notebook for topic modelling
├── ... (other scripts and notebooks)
```

---

## Main Features

- **Data Integration:**  
  Merges IEEE and ACM datasets, standardizing columns for unified analysis.

- **Preprocessing:**  
  Cleans, tokenizes, removes stopwords, and lemmatizes text from article titles and abstracts.

- **Topic Modelling Methods:**  
  - **LDA (Latent Dirichlet Allocation)**  
  - **FLSA-W (Fuzzy Latent Semantic Analysis - Weighted)**
  - **BERTopic (Transformer-based topic modelling)**

- **Evaluation:**  
  Computes coherence, diversity, and interpretability metrics for topics.

- **Visualization:**  
  Plots topic distributions and saves articles per topic to CSV files.

---

## Setup

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd <repo-folder>
   ```

2. **Create and activate a virtual environment (recommended):**
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate   # On Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Download NLTK data (run once in Python):**
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')
   nltk.download('wordnet')
   ```

---

## Usage

1. **Prepare Data:**  
   Place your filtered IEEE and ACM CSV files in the appropriate folders as shown above.

2. **Run the Notebook:**  
   Open `TopicModelling_Microservice.ipynb` in Jupyter or VS Code and run all cells.

3. **Results:**  
   - Topic assignments and visualizations will be displayed in the notebook.
   - Articles grouped by topic will be saved in the `topics/` folder.

---

## Notes

- The code expects specific column names in the CSVs. ACM columns are mapped to IEEE-style names for consistency.
- Only the columns `Document Title`, `Abstract`, `source`, and `bool` are used for topic modelling.
- You can adjust preprocessing and topic modelling parameters in the notebook as needed.

---

## Requirements

See `requirements.txt` for all dependencies, including:
- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn
- nltk
- FuzzyTM
- bertopic

---

## License

This project is for academic/research use. See LICENSE file if present.

---

## Contact

For questions or contributions, please open an issue or contact the repository maintainer.