# ImageExtractor-Gemini-1.5

Sample invoice or image extractor using gemini model

# END to END AIMediBot using LLAMA2

# How to run?

### STEPS:

Clone the repository

```bash
Project repo: https://github.com/codeakki/ImageExtractor-Gemini-1.5.git
```

### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n venv python=3.9 -y
```

```bash
conda activate venv
```

### STEP 02- install the requirements

```bash
pip install -r requirements.txt
```

### Create a `.env` file in the root directory and add your Pinecone credentials as follows:

```ini
GOOGLE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

```bash
# Finally run the following command
python app.py
```

Now,

```bash
open up localhost:
```

### Techstack Used:

- Python
- Streamlit
- google-generativeai
