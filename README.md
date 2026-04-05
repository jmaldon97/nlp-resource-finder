# 🔎 NLP Resource Finder

A lightweight natural language search application that allows users to query structured data using plain English.

## 🚀 Live App

👉 https://nlp-resource-finder-z5ydpaf6qqgscxpo5yyzvy.streamlit.app/

---

## 🧠 Overview

This project demonstrates how unstructured user input can be translated into structured database queries.

Users can type requests like:

- "housing in kc"
- "legal help in springfield"
- "mental health in stl"

The system:
1. Parses the input
2. Extracts key entities (city + service)
3. Translates them into SQL filters
4. Queries a relational database
5. Returns matching results in a web interface

---

## 🏗️ Tech Stack

- Python
- SQLite
- Streamlit
- difflib (for fuzzy matching)

---

## ⚙️ How It Works

### 1. User Input
Users enter natural language requests via a Streamlit UI.

### 2. Parsing Layer
The system uses:
- Alias mapping (e.g., "kc" → "Kansas City")
- Fuzzy matching (handles typos like "housng")

### 3. Query Builder
Parsed values are injected into a parameterized SQL query:

```sql
WHERE city = ?
AND service = ?
4. Database

A relational SQLite database stores:

Cities
Organizations
Services
5. Output

Results are displayed in a clean, user-friendly format.

📊 Example

Input:

housng in kc

Output:

Organization: KC Youth Shelter  
City: Kansas City  
Service: Housing
📁 Project Structure
nlp-resource-finder/
│
├── app.py             # Streamlit app
├── resources.db       # SQLite database
├── requirements.txt   # Dependencies
├── README.md          # Project documentation
🎯 Key Concepts Demonstrated
Natural language parsing (rule-based)
Translation layer: human input → structured data
SQL query construction
Relational database design
Python + SQL integration
Rapid UI development with Streamlit
Deployment via Streamlit Community Cloud
⚠️ Limitations
Rule-based parsing (not AI-driven)
Limited vocabulary (relies on alias maps)
Fuzzy matching works best on short words
🔮 Future Improvements
Integrate AI/NLP models for better understanding
Expand dataset and resource coverage
Add filtering UI (dropdowns, categories)
Improve fuzzy matching for multi-word phrases
Add user authentication and saving queries
💡 Author

Built as part of a hands-on learning project focused on:

Python development
SQL integration
Natural language interfaces
End-to-end system design
