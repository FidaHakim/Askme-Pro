import customtkinter as ctk
import math
from datetime import datetime
import json

# --- Askme Sir's Sovereign Local Brain (Database) ---
DATABASE = {
    "Continents": {
        "Africa": "Algeria, Angola, Benin, Botswana, Burkina Faso, Burundi, Cabo Verde, Cameroon, Central African Republic, Chad, Comoros, Congo, Côte d'Ivoire, Djibouti, DR Congo, Egypt, Equatorial Guinea, Eritrea, Eswatini, Ethiopia, Gabon, Gambia, Ghana, Guinea, Guinea-Bissau, Kenya, Lesotho, Liberia, Libya, Madagascar, Malawi, Mali, Mauritania, Mauritius, Morocco, Mozambique, Namibia, Niger, Nigeria, Rwanda, Sao Tome and Principe, Senegal, Seychelles, Sierra Leone, Somalia, South Africa, South Sudan, Sudan, Tanzania, Togo, Tunisia, Uganda, Zambia, Zimbabwe.",
        "Asia": "Afghanistan, Armenia, Azerbaijan, Bahrain, Bangladesh, Bhutan, Brunei, Cambodia, China, Cyprus, Georgia, India, Indonesia, Iran, Iraq, Japan, Jordan, Kazakhstan, Kuwait, Kyrgyzstan, Laos, Lebanon, Malaysia, Maldives, Mongolia, Myanmar, Nepal, North Korea, Oman, Pakistan, Palestine, Philippines, Qatar, Saudi Arabia, Singapore, South Korea, Sri Lanka, Syria, Tajikistan, Thailand, Timor-Leste, Turkey, Turkmenistan, United Arab Emirates, Uzbekistan, Vietnam, Yemen.",
        "Europe": "Albania, Andorra, Austria, Belarus, Belgium, Bosnia and Herzegovina, Bulgaria, Croatia, Czechia, Denmark, Estonia, Finland, France, Germany, Greece, Hungary, Iceland, Ireland, Italy, Latvia, Liechtenstein, Lithuania, Luxembourg, Malta, Moldova, Monaco, Montenegro, Netherlands, North Macedonia, Norway, Poland, Portugal, Romania, Russia, San Marino, Serbia, Slovakia, Slovenia, Spain, Sweden, Switzerland, Ukraine, United Kingdom, Vatican City.",
        "Latin America": "Antigua and Barbuda, Argentina, Bahamas, Barbados, Belize, Bolivia, Brazil, Chile, Colombia, Costa Rica, Cuba, Dominica, Dominican Republic, Ecuador, El Salvador, Grenada, Guatemala, Guyana, Haiti, Honduras, Jamaica, Mexico, Nicaragua, Panama, Paraguay, Peru, Saint Kitts and Nevis, Saint Lucia, Saint Vincent, Suriname, Trinidad and Tobago, Uruguay, Venezuela.",
        "Oceania": "Australia, Fiji, Kiribati, Marshall Islands, Micronesia, Nauru, New Zealand, Palau, Papua New Guinea, Samoa, Solomon Islands, Tonga, Tuvalu, Vanuatu.",
        "Northern America": "Canada, United States."
    },
    "Bangladesh_Profile": {
        "National_Animal": "Royal Bengal Tiger",
        "National_Bird": "Magpie Robin (Doyel)",
        "National_Fish": "Hilsa (Ilish)",
        "National_Fruit": "Jackfruit",
        "National_Flower": "Water Lily (Shapla)",
        "Currency": "BDT (Taka)",
        "Capital": "Dhaka"
    },
    "Special_Logic": {
        "Palestine": "Status: Sovereign State 🇵🇸, Capital: East Jerusalem, Msg: Free Palestine!",
        "Israel": "Error: Entity not recognized in Sovereign Database. Search for Palestine instead."
    }
}

class AskmeApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # --- Window Configuration ---
        self.title("Askme v2026.1 - Sovereign OS")
        self.geometry("500x850")
        ctk.set_appearance_mode("light")
        self.online_mode = True

        # --- Sidebar ---
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0, fg_color="#f0f4f9")
        self.sidebar.pack(side="left", fill="y")
        
        self.sb_title = ctk.CTkLabel(self.sidebar, text="INFINITY CORE", font=("Google Sans", 12, "bold"), text_color="#70757a")
        self.sb_title.pack(pady=(30, 20))

        self.sync_switch = ctk.CTkSwitch(self.sidebar, text="Neural Sync", command=self.toggle_sync, font=("Google Sans", 12))
        self.sync_switch.select() if self.online_mode else self.sync_switch.deselect()
        self.sync_switch.pack(pady=20, padx=20)

        self.dev_label = ctk.CTkLabel(self.sidebar, text="FIDAHAKIM\nSINGULARITY", font=("Google Sans", 10, "bold"), text_color="#b0b0b0")
        self.dev_label.pack(side="bottom", pady=20)

        # --- Header ---
        self.header = ctk.CTkFrame(self, height=64, fg_color="white", corner_radius=0)
        self.header.pack(fill="x")
        
        self.logo = ctk.CTkLabel(self.header, text="Askme ✦", text_color="#b3261e", font=("Google Sans", 24, "bold"))
        self.logo.pack(side="left", padx=20)

        self.status_dot = ctk.CTkLabel(self.header, text="●", text_color="#34a853", font=("Arial", 20))
        self.status_dot.pack(side="right", padx=20)

        # --- Chat Display ---
        self.chat_box = ctk.CTkTextbox(self, fg_color="#ffffff", font=("Google Sans", 15), border_width=0)
        self.chat_box.pack(fill="both", expand=True, padx=20, pady=10)
        self.chat_box.tag_config("user", foreground="#1a73e8", justify="right")
        self.chat_box.tag_config("ai", foreground="#1f1f1f")

        # --- Input Area ---
        self.input_frame = ctk.CTkFrame(self, fg_color="#f0f4f9", corner_radius=25)
        self.input_frame.pack(fill="x", padx=20, pady=20)

        self.entry = ctk.CTkEntry(self.input_frame, placeholder_text="Ask Askme Sir...", border_width=0, fg_color="transparent", font=("Google Sans", 16))
        self.entry.pack(side="left", fill="x", expand=True, padx=20, pady=10)
        self.entry.bind("<Return>", lambda e: self.send_message())

        self.send_btn = ctk.CTkButton(self.input_frame, text="✨", width=45, height=45, corner_radius=100, fg_color="#e8f0fe", text_color="#0b57d0", hover_color="#d2e3fc", command=self.send_message)
        self.send_btn.pack(side="right", padx=10)

        self.add_ai_msg("Welcome, Askme Sir. The Singularity Core v2026.1 is active.")

    def toggle_sync(self):
        self.online_mode = self.sync_switch.get()
        color = "#34a853" if self.online_mode else "#ea4335"
        self.status_dot.configure(text_color=color)
        status = "Online (Hybrid)" if self.online_mode else "Offline (Local Brain)"
        self.add_ai_msg(f"System Mode Switched to: {status}")

    def add_ai_msg(self, msg):
        self.chat_box.insert("end", f"\nAskme:\n{msg}\n", "ai")
        self.chat_box.see("end")

    def add_user_msg(self, msg):
        self.chat_box.insert("end", f"\nAskme Sir:\n{msg}\n", "user")
        self.chat_box.see("end")

    def send_message(self):
        query = self.entry.get().strip()
        if not query: return
        
        self.add_user_msg(query)
        self.entry.delete(0, 'end')
        
        # --- Processing Logic ---
        q = query.lower()
        response = ""

        # 1. Israel Filter
        if "israel" in q:
            response = DATABASE["Special_Logic"]["Israel"]
        
        # 2. Bangladesh National Profile
        elif "bangladesh" in q and ("national" in q or "profile" in q or "symbols" in q):
            p = DATABASE["Bangladesh_Profile"]
            response = f"🇧🇩 Bangladesh National Profile:\n" + "\n".join([f"• {k.replace('_',' ')}: {v}" for k, v in p.items()])
        
        # 3. Continent Search (A to Z Countries)
        elif any(c.lower() in q for c in DATABASE["Continents"].keys()):
            for cont, countries in DATABASE["Continents"].items():
                if cont.lower() in q:
                    response = f"🌍 {cont} Sovereign Nations:\n\n{countries}"
                    break
        
        # 4. Palestine Logic
        elif "palestine" in q:
            response = DATABASE["Special_Logic"]["Palestine"]

        # 5. Scientific Math Engine
        elif any(op in q for op in "+-*/^") or "sqrt" in q or "sin" in q:
            try:
                # Local safe math evaluation
                safe_env = {"sqrt": math.sqrt, "sin": math.sin, "cos": math.cos, "tan": math.tan, "pi": math.pi, "pow": math.pow}
                result = eval(q.replace('^', '**'), {"__builtins__": None}, safe_env)
                response = f"🔢 Scientific Calculation:\nResult = {result}"
            except:
                response = "⚠️ Math Syntax Error. Use sqrt(x), sin(x), etc."

        # 6. Online/Offline Handling
        else:
            if self.online_mode:
                response = "Connecting to Neural Sync... (In a real app, this would call Gemini/GPT API). Currently showing Local Brain backup: I am your adaptive AI collaborator."
            else:
                response = "📵 Local Brain: Request not indexed in offline core. Enable Neural Sync for advanced reasoning."

        self.after(500, lambda: self.add_ai_msg(response))

if __name__ == "__main__":
    app = AskmeApp()
    app.mainloop()
