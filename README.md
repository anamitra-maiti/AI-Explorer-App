# 🌍 AI World Explorer

**AI World Explorer** is an interactive travel assistant built with **LangChain**, **OpenAI**, and **Streamlit**.

Just enter the name of any country, and the app will:

- 🏙️ Tell you the **capital city**
- 📸 Suggest **places to visit**
- 🧠 Share a **fun cultural fact**
- 🍜 Recommend a **local dish**
- ✍️ Generate a **3-line poetic teaser**

This is powered by LangChain’s `SequentialChain`, where each step’s output is used as input for the next — creating a natural flow of rich, AI-generated travel information.

---

## 🛠 How to Run the Project

### 1. 🔐 Create a `.env` File

In the root directory, create a file named `.env` and add your OpenAI API key:

> ⚠️ **Note:** Never share your `.env` file publicly. It contains your private OpenAI API key.

---

## 2. 📦 Install Dependencies

Install the required Python libraries using the `requirements.txt` file:

```bash
pip install -r requirements.txt


---
## 3. ▶️ Run the App

Start the Streamlit application with:

```bash
streamlit run app.py


## 🧠 Tech Stack

- **Python**
- **Streamlit** – for the interactive UI
- **LangChain** – for chaining multiple LLM prompts
- **OpenAI GPT-3.5-Turbo-Instruct**
- **python-dotenv** – for environment variable management

---

## 🧪 Sample Output

**Input:** `Italy`

**Output:**

- **Capital:** Rome  
- **Places:** Colosseum, Vatican City, Amalfi Coast  
- **Fun Fact:** Home to the world’s oldest active university  
- **Food Recommendation:** Try an authentic wood-fired Margherita pizza  
- **Teaser:**

  > In cobbled streets where ruins dream,  
  > You’ll sip on art and sun-kissed cream,  
  > Italy whispers through each scene.

---

## 📌 Notes

The app is modular and easy to extend.

You can enhance it by:

- 🎨 Adding image generation with DALL·E  
- 🗺️ Integrating an interactive map  
- 🎤 Enabling voice-based queries  
- 🧳 Saving user travel history and preferences  

---

## 📄 License

This project is open source and licensed under the **MIT License**.

