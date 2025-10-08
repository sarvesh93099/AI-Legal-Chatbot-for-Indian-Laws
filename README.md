AI Legal Chatbot for Indian Laws 🇮🇳
A simple, interactive GUI-based AI chatbot that provides information about Indian laws without using external APIs. Built with Python and Tkinter for educational purposes.

https://img.shields.io/badge/Python-3.6%252B-blue
https://img.shields.io/badge/GUI-Tkinter-green
https://img.shields.io/badge/No-APIs-orange
https://img.shields.io/badge/License-MIT-lightgrey

✨ Features
🖥️ Interactive GUI - User-friendly interface built with Tkinter

🇮🇳 Indian Law Focus - Covers major Indian legal codes and acts

🔒 No APIs Required - Completely self-contained with pre-loaded knowledge base

🚀 Easy Implementation - Single Python file with no external dependencies

⚡ Quick Actions - One-click buttons for common legal topics

💬 Natural Interaction - Basic conversational capabilities

📱 Responsive Design - Clean and modern interface

📸 Screenshot
https://via.placeholder.com/800x500/2c3e50/ffffff?text=AI+Legal+Chatbot+Interface+Preview

🛠️ Installation
Prerequisites
Python 3.6 or higher

Tkinter (usually comes pre-installed with Python)

Quick Start
Clone the repository:

bash
Copy
Download
git clone https://github.com/yourusername/indian-law-chatbot.git
cd indian-law-chatbot
Run the chatbot:

bash
Copy
Download
python law_chatbot.py
That's it! No additional packages or installations required.

🎯 Usage
Launch the Application:

Run the script and the GUI window will open automatically

You'll see a welcome message with available topics

Ask Legal Questions:

Type your questions in the input field at the bottom

Press Enter or click the "Send" button

Examples:

"Tell me about IPC section 302"

"What are fundamental rights?"

"Explain consumer protection laws"

Use Quick Actions:

Click buttons for instant access to common topics:

IPC, Constitution, Divorce, Property, Consumer laws

📚 Supported Legal Topics
Category	Key Acts/Codes	Features
Constitution	Constitution of India	Fundamental Rights, Basic Structure
Criminal Law	Indian Penal Code, 1860	Sections 302, 376, 420, 498A
Civil Procedures	Code of Civil Procedure, 1908	Court procedures, Appeals
Criminal Procedures	Code of Criminal Procedure, 1973	Arrest, Investigation, Bail
Property Laws	Transfer of Property Act, 1882	Property transfer, Succession
Consumer Protection	Consumer Protection Act, 2019	Consumer rights, Dispute resolution
Labor Laws	Various Labor Acts	Employment rights, Working conditions
Divorce Laws	Personal Laws	Hindu, Muslim, Christian divorce laws
🏗️ Project Structure
text
Copy
Download
indian-law-chatbot/
│
├── law_chatbot.py          # Main application file
├── README.md               # Project documentation
└── assets/                 # Screenshots and resources
    └── demo-screenshot.png
Code Architecture
python
Copy
Download
IndianLawChatbot()
├── __init__()              # Initializes knowledge base and GUI
├── setup_gui()            # Creates user interface components
├── process_message()      # Handles user input processing
├── generate_response()    # Generates legal information responses
└── run()                  # Starts the application
🔧 Customization
Adding New Legal Information
Expand the knowledge base by modifying the knowledge_base dictionary:

python
Copy
Download
"new_act": {
    "name": "Your Act Name",
    "description": "Brief description",
    "sections": {
        "Section1": "Description",
        "Section2": "Description"
    }
}
Modifying UI
Customize colors and layout in the setup_gui() method:

python
Copy
Download
# Change theme colors
header_frame = tk.Frame(self.root, bg="#your_color")
🚀 Quick Deployment
For Educational Institutions
Download the law_chatbot.py file

Distribute to students

Run with: python law_chatbot.py

For Developers
Fork the repository

Extend the knowledge base

Customize the UI

Run and test

📊 Sample Interactions
text
Copy
Download
User: What is IPC section 302?
Bot: IPC Section 302: Punishment for murder - Death penalty or life imprisonment

User: Tell me about fundamental rights
Bot: Constitution of India - Fundamental Rights include Right to Equality, Right to Freedom, Right against Exploitation...
🤝 Contributing
We welcome contributions to improve this educational tool!

How to Contribute
Fork the repository

Create a feature branch: git checkout -b feature/new-feature

Commit changes: git commit -am 'Add new feature'

Push to branch: git push origin feature/new-feature

Submit a pull request

Areas for Improvement
Expand legal knowledge base

Add more interactive features

Improve UI/UX design

Add case studies and examples

Implement better NLP capabilities

⚠️ Limitations & Disclaimer
Technical Limitations
Contains pre-defined information only

Basic keyword matching (no advanced AI)

Cannot learn from interactions

No real-time updates

⚖️ Legal Disclaimer
Important: This is an educational tool only and does not constitute legal advice. The information provided:

May not be complete or up-to-date

Should not be relied upon for legal decisions

Is not a substitute for professional legal consultation

May not reflect recent legal amendments

Always consult qualified legal professionals for actual legal matters.

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

📞 Support
If you encounter issues:

Check existing Issues

Create a new issue with:

Python version

Operating System

Error details

🙏 Acknowledgments
Built with Python and Tkinter

Legal information compiled from public domain sources

Inspired by the need for accessible legal education tools

<div align="center">
⭐ Star this repo if you find it helpful!

Made with ❤️ for educational purposes

</div>
