import tkinter as tk
from tkinter import scrolledtext, ttk
import datetime

class IndianLawChatbot:
    def __init__(self):
        # Knowledge base of Indian laws
        self.knowledge_base = {
            "ipc": {
                "name": "Indian Penal Code, 1860",
                "description": "The Indian Penal Code (IPC) is the official criminal code of India which covers all substantive aspects of criminal law.",
                "sections": {
                    "302": "Punishment for murder - Death penalty or life imprisonment",
                    "376": "Punishment for rape - Minimum 10 years imprisonment which may extend to life imprisonment",
                    "420": "Cheating and dishonestly inducing delivery of property - Punishment up to 7 years imprisonment",
                    "498A": "Husband or relative of husband subjecting woman to cruelty - Punishment up to 3 years imprisonment and fine"
                }
            },
            "cpc": {
                "name": "Code of Civil Procedure, 1908",
                "description": "The Code of Civil Procedure regulates the procedure to be followed by civil courts in India.",
                "key_points": [
                    "Governs the procedure for civil lawsuits",
                    "Contains provisions for appeals, references, reviews, and revisions",
                    "Provides rules for execution of decrees and orders"
                ]
            },
            "crpc": {
                "name": "Code of Criminal Procedure, 1973",
                "description": "The Code of Criminal Procedure is the main legislation on procedure for administration of substantive criminal law in India.",
                "key_points": [
                    "Defines the procedure for arrest, investigation, and trial",
                    "Contains provisions for bail and anticipatory bail",
                    "Establishes hierarchy of criminal courts"
                ]
            },
            "constitution": {
                "name": "Constitution of India",
                "description": "The supreme law of India that lays down the framework defining fundamental political principles, establishes the structure, procedures, powers and duties of government institutions.",
                "fundamental_rights": [
                    "Right to Equality (Articles 14-18)",
                    "Right to Freedom (Articles 19-22)",
                    "Right against Exploitation (Articles 23-24)",
                    "Right to Freedom of Religion (Articles 25-28)",
                    "Cultural and Educational Rights (Articles 29-30)",
                    "Right to Constitutional Remedies (Article 32)"
                ]
            },
            "consumer": {
                "name": "Consumer Protection Act, 2019",
                "description": "An Act to provide for protection of the interests of consumers and for the establishment of Consumer Protection Councils and other authorities.",
                "key_features": [
                    "Establishes Central Consumer Protection Authority",
                    "Provides for product liability action",
                    "Introduces mediation as an Alternate Dispute Resolution mechanism"
                ]
            },
            "divorce": {
                "name": "Laws related to Divorce",
                "description": "Different laws govern divorce in India based on religion:",
                "laws": {
                    "Hindu Marriage Act, 1955": "Applies to Hindus, Buddhists, Jains, and Sikhs",
                    "Muslim Personal Law": "Governed by the Dissolution of Muslim Marriages Act, 1939",
                    "Indian Divorce Act, 1869": "Applies to Christians",
                    "Special Marriage Act, 1954": "Applies to inter-religion marriages"
                }
            },
            "property": {
                "name": "Property Laws in India",
                "description": "Various laws govern property rights and transactions in India:",
                "key_acts": [
                    "Transfer of Property Act, 1882",
                    "Indian Succession Act, 1925",
                    "Hindu Succession Act, 1956",
                    "Registration Act, 1908"
                ]
            },
            "labor": {
                "name": "Labor Laws in India",
                "description": "Laws governing employer-employee relationships and working conditions:",
                "key_acts": [
                    "Industrial Disputes Act, 1947",
                    "Factories Act, 1948",
                    "Minimum Wages Act, 1948",
                    "Employees' Provident Funds and Miscellaneous Provisions Act, 1952"
                ]
            }
        }
        
        # Greeting messages
        self.greetings = [
            "hello", "hi", "hey", "good morning", "good afternoon", "good evening"
        ]
        
        # Farewell messages
        self.farewells = [
            "bye", "goodbye", "see you", "exit", "quit"
        ]
        
        self.setup_gui()
    
    def setup_gui(self):
        # Create main window
        self.root = tk.Tk()
        self.root.title("AI Legal Assistant - Indian Laws")
        self.root.geometry("700x600")
        self.root.configure(bg="#f0f0f0")
        
        # Create header
        header_frame = tk.Frame(self.root, bg="#2c3e50", height=80)
        header_frame.pack(fill=tk.X, padx=10, pady=10)
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(
            header_frame, 
            text="AI Legal Assistant for Indian Laws", 
            font=("Arial", 16, "bold"), 
            fg="white", 
            bg="#2c3e50"
        )
        title_label.pack(expand=True)
        
        subtitle_label = tk.Label(
            header_frame, 
            text="Ask me about Indian laws and legal procedures", 
            font=("Arial", 10), 
            fg="#ecf0f1", 
            bg="#2c3e50"
        )
        subtitle_label.pack(expand=True)
        
        # Create chat display area
        self.chat_display = scrolledtext.ScrolledText(
            self.root, 
            wrap=tk.WORD, 
            width=80, 
            height=20, 
            font=("Arial", 10),
            state=tk.DISABLED
        )
        self.chat_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Create input area
        input_frame = tk.Frame(self.root, bg="#f0f0f0")
        input_frame.pack(fill=tk.X, padx=10, pady=10)
        
        self.user_input = tk.Entry(
            input_frame, 
            font=("Arial", 12), 
            width=60
        )
        self.user_input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        self.user_input.bind("<Return>", self.send_message)
        
        send_button = tk.Button(
            input_frame, 
            text="Send", 
            font=("Arial", 10, "bold"), 
            bg="#3498db", 
            fg="white",
            command=self.send_message
        )
        send_button.pack(side=tk.RIGHT)
        
        # Create quick action buttons
        quick_actions_frame = tk.Frame(self.root, bg="#f0f0f0")
        quick_actions_frame.pack(fill=tk.X, padx=10, pady=5)
        
        action_buttons = [
            ("IPC", "Ask about Indian Penal Code"),
            ("Constitution", "Ask about Constitution"),
            ("Divorce", "Ask about Divorce Laws"),
            ("Property", "Ask about Property Laws"),
            ("Consumer", "Ask about Consumer Laws")
        ]
        
        for text, tooltip in action_buttons:
            btn = tk.Button(
                quick_actions_frame,
                text=text,
                font=("Arial", 9),
                bg="#ecf0f1",
                command=lambda t=text: self.quick_action(t)
            )
            btn.pack(side=tk.LEFT, padx=5)
            
            # Simple tooltip implementation
            self.create_tooltip(btn, tooltip)
        
        # Display welcome message
        self.display_message("Bot", "Welcome to the AI Legal Assistant for Indian Laws! How can I help you today?\n\nYou can ask me about:\n- Indian Penal Code (IPC)\n- Constitution of India\n- Civil and Criminal Procedures\n- Property Laws\n- Consumer Protection\n- Labor Laws\n- Divorce Laws\n\nTry asking: 'Tell me about IPC section 302' or 'What are fundamental rights?'")
        
        # Set focus to input field
        self.user_input.focus()
    
    def create_tooltip(self, widget, text):
        def on_enter(event):
            tooltip = tk.Toplevel()
            tooltip.wm_overrideredirect(True)
            tooltip.wm_geometry(f"+{event.x_root+10}+{event.y_root+10}")
            label = tk.Label(tooltip, text=text, background="yellow", relief='solid', borderwidth=1)
            label.pack()
            widget.tooltip = tooltip
        
        def on_leave(event):
            if hasattr(widget, 'tooltip'):
                widget.tooltip.destroy()
        
        widget.bind("<Enter>", on_enter)
        widget.bind("<Leave>", on_leave)
    
    def display_message(self, sender, message):
        self.chat_display.config(state=tk.NORMAL)
        
        # Add timestamp
        timestamp = datetime.datetime.now().strftime("%H:%M")
        
        # Format message based on sender
        if sender == "User":
            self.chat_display.insert(tk.END, f"\n[{timestamp}] You: {message}\n", "user")
        else:
            self.chat_display.insert(tk.END, f"\n[{timestamp}] Legal Assistant: {message}\n", "bot")
        
        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.see(tk.END)
        
        # Configure tags for different message styles
        self.chat_display.tag_config("user", foreground="#2c3e50", font=("Arial", 10, "bold"))
        self.chat_display.tag_config("bot", foreground="#2980b9", font=("Arial", 10))
    
    def send_message(self, event=None):
        user_message = self.user_input.get().strip()
        if user_message:
            self.display_message("User", user_message)
            self.user_input.delete(0, tk.END)
            self.process_message(user_message)
    
    def quick_action(self, topic):
        self.display_message("User", f"Tell me about {topic}")
        self.process_message(f"Tell me about {topic}")
    
    def process_message(self, message):
        # Convert to lowercase for easier processing
        message_lower = message.lower()
        
        # Check for greetings
        if any(greet in message_lower for greet in self.greetings):
            self.display_message("Bot", "Hello! I'm your AI Legal Assistant. How can I help you with Indian laws today?")
            return
        
        # Check for farewells
        if any(farewell in message_lower for farewell in self.farewells):
            self.display_message("Bot", "Thank you for using the AI Legal Assistant. Have a great day!")
            return
        
        # Process legal queries
        response = self.generate_response(message_lower)
        self.display_message("Bot", response)
    
    def generate_response(self, message):
        # Check for IPC section queries
        if "ipc" in message and "section" in message:
            for section_num in self.knowledge_base["ipc"]["sections"]:
                if section_num in message:
                    section_info = self.knowledge_base["ipc"]["sections"][section_num]
                    return f"IPC Section {section_num}: {section_info}"
        
        # Check for specific law queries
        if "ipc" in message or "indian penal code" in message:
            ipc_info = self.knowledge_base["ipc"]
            response = f"{ipc_info['name']}\n\n{ipc_info['description']}\n\nImportant Sections:\n"
            for section, desc in ipc_info["sections"].items():
                response += f"• Section {section}: {desc}\n"
            return response
        
        if "constitution" in message or "fundamental rights" in message:
            constitution_info = self.knowledge_base["constitution"]
            response = f"{constitution_info['name']}\n\n{constitution_info['description']}\n\nFundamental Rights:\n"
            for right in constitution_info["fundamental_rights"]:
                response += f"• {right}\n"
            return response
        
        if "divorce" in message:
            divorce_info = self.knowledge_base["divorce"]
            response = f"{divorce_info['name']}\n\n{divorce_info['description']}\n\n"
            for law, desc in divorce_info["laws"].items():
                response += f"• {law}: {desc}\n"
            return response
        
        if "property" in message:
            property_info = self.knowledge_base["property"]
            response = f"{property_info['name']}\n\n{property_info['description']}\n\nKey Acts:\n"
            for act in property_info["key_acts"]:
                response += f"• {act}\n"
            return response
        
        if "consumer" in message:
            consumer_info = self.knowledge_base["consumer"]
            response = f"{consumer_info['name']}\n\n{consumer_info['description']}\n\nKey Features:\n"
            for feature in consumer_info["key_features"]:
                response += f"• {feature}\n"
            return response
        
        if "labor" in message or "employment" in message:
            labor_info = self.knowledge_base["labor"]
            response = f"{labor_info['name']}\n\n{labor_info['description']}\n\nKey Acts:\n"
            for act in labor_info["key_acts"]:
                response += f"• {act}\n"
            return response
        
        if "cpc" in message or "civil procedure" in message:
            cpc_info = self.knowledge_base["cpc"]
            response = f"{cpc_info['name']}\n\n{cpc_info['description']}\n\nKey Points:\n"
            for point in cpc_info["key_points"]:
                response += f"• {point}\n"
            return response
        
        if "crpc" in message or "criminal procedure" in message:
            crpc_info = self.knowledge_base["crpc"]
            response = f"{crpc_info['name']}\n\n{crpc_info['description']}\n\nKey Points:\n"
            for point in crpc_info["key_points"]:
                response += f"• {point}\n"
            return response
        
        # Default response for unrecognized queries
        return "I'm sorry, I don't have specific information about that topic in my knowledge base. I can help you with:\n\n• Indian Penal Code (IPC)\n• Constitution of India\n• Civil and Criminal Procedures\n• Property Laws\n• Consumer Protection\n• Labor Laws\n• Divorce Laws\n\nPlease try asking about one of these topics or be more specific in your query."
    
    def run(self):
        self.root.mainloop()

# Create and run the chatbot
if __name__ == "__main__":
    chatbot = IndianLawChatbot()
    chatbot.run()