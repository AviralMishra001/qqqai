### The Idea Behind the Application

**QQQAI** is a **multimodal AI agent** designed to provide comprehensive, intelligent answers to a wide range of user queries. The core idea is to create a versatile assistant that can not only answer questions based on its knowledge but also perform real-time web searches, analyze uploaded files, and even provide up-to-date financial information. This makes it a powerful and flexible tool for research, learning, and general inquiry.

---

### How It Works (Architecture/Approach)

The application uses an **AI agent-based approach** built on the **Phidata** framework.

1.  **User Input:** The user enters a question or query into the Streamlit interface. They can also optionally upload a file (like a PDF, image, or video) to provide additional context.

2.  **Agent Initialization:** The app initializes an **AI agent** powered by a **Groq LLM** (specifically, the `openai/gpt-oss-20b` model). This agent is configured with multiple tools, including:
    * **DuckDuckGo:** For real-time web searches to access the latest information.
    * **YFinanceTools:** For fetching financial data.
    * **PythonTools:** For executing Python code to perform specific tasks.

3.  **Query Analysis:** When the user clicks "Analyze Query," the agent receives the question and any uploaded file. It then determines the best course of action. For example:
    * If the query is about a stock price, it uses the **YFinanceTools**.
    * If it requires recent information, it uses **DuckDuckGo** to search the web.
    * If a file is uploaded, the agent incorporates its content into the analysis.

4.  **Response Generation:** The agent uses the information from these tools and its internal knowledge to generate a detailed, user-friendly, and actionable response, which is then displayed back to the user via the Streamlit interface.

---

### Tools and Frameworks Used

* **Streamlit:** The primary **web framework** used to build the interactive, user-friendly front end.
* **Phidata:** A **lightweight AI agent framework** that simplifies the creation and management of AI agents and their tools. The core logic of the agent is built using this library.
* **Groq:** The **Large Language Model (LLM)** provider. The agent uses a model hosted on Groq to power its intelligence and text generation.
* **DuckDuckGo-Search:** Used for performing real-time, anonymous web searches.
* **Yfinance:** A library that provides an interface to Yahoo Finance, used by the agent to get financial data.
* **Python:** The core programming language used for the entire application.
