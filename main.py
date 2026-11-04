import re
import math
import random
import hashlib
import urllib.request
import json
import sys
import traceback
import datetime
import time
from io import StringIO

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle, Ellipse

# ==========================================
# ⚠️ ใส่ API KEY ของคุณที่นี่ (สำหรับ AI)
# ==========================================
GEMINI_API_KEY = "ใส่_API_KEY_ของคุณตรงนี้"

def ask_ai(prompt):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
    headers = {'Content-Type': 'application/json'}
    data = {"contents": [{"parts": [{"text": prompt}]}]}
    try:
        req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers)
        response = urllib.request.urlopen(req, timeout=30)
        result = json.loads(response.read().decode('utf-8'))
        return result['candidates'][0]['content']['parts'][0]['text']
    except Exception as e:
        return f"❌ AI Error: {str(e)}"

# ==========================================
# ฟังก์ชันระบบหลังบ้าน
# ==========================================
def create_crypto_contract(name, symbol, supply):
    return f"✅ สร้างโค้ดเหรียญ {name} ({symbol}) สำเร็จ!\n(คัดลอกโค้ดนี้ไปรันที่ Remix.ethereum.org)\n\ncontract {name} is ERC20 {{\n    constructor() ERC20(\"{name}\", \"{symbol}\") {{\n        _mint(msg.sender, {supply} * 10 ** decimals());\n    }}\n}}"

def hack_system(target):
    time.sleep(1)
    logs = [
        f"[*] เริ่มสแกนหาเป้าหมาย: {target}...",
        "[*] เปิดพอร์ต 22 (SSH)...",
        "[*] ตรวจพบช่องโหว่ CVE-2024-1337",
        "[*] กำลังเดารหัสผ่าน (Brute-force)...",
        "[+] พบรหัสผ่าน: ********",
        "[+] เข้าสู่ระบบสำเร็จ! (Root Access Granted)",
        "[!] ดาวน์โหลดฐานข้อมูล...",
        "✅ แฮกสำเร็จ! ข้อมูลถูกเข้ารหัสและส่งไปยังเซิร์ฟเวอร์ของคุณแล้ว"
    ]
    return "\n".join(logs)

def simulate_mining(difficulty):
    target = "0" * int(difficulty)
    nonce = 0
    while nonce < 100000: # จำกัดรอบไม่ให้แอปค้าง
        if hashlib.sha256(f"block-{nonce}".encode()).hexdigest().startswith(target):
            return f"💰 ขุดสำเร็จ! (ใช้เวลา {nonce} รอบ)\nรางวัล: 0.00000001 BTC"
        nonce += 1
    return "⏳ ขุดไม่สำเร็จใน 1 แสนรอบ (ลดความยากลงดู)"

def simulate_sniper_bot():
    logs = ["[*] เริ่มระบบ Sniper Bot...", "[*] เชื่อมต่อ DEX (PancakeSwap)..."]
    tokens = ["DOGE2.0", "SAFEMOON", "ELONX", "FLOKI", "SHIB2"]
    for i in range(3):
        coin = random.choice(tokens)
        price = round(random.uniform(0.001, 0.1), 4)
        logs.append(f"[+] ตรวจพบเหรียญใหม่: {coin} ราคา ${price}")
        if price < 0.05:
            logs.append(f"[🔥] บอทตัดสินใจซื้อ {coin} ที่ราคา ${price}")
            logs.append(f"[✅] ซื้อสำเร็จ! ทำกำไร +20% แล้วขายออก")
            break
        else:
            logs.append(f"[-] ราคาสูงเกินไป ({coin}) ข้าม...")
    logs.append("[*] จบการทำงานของบอท")
    return "\n".join(logs)

# ==========================================
# คลังคำสั่งภาษาไทย
# ==========================================
KEYWORDS = [
    # --- AI ---
    (r'ถามเอไอ\((.*?)\)', r'ask_ai(\1)'),
    # --- Hacking ---
    (r'แฮกระบบ\("(.+?)"\)', r'hack_system("\1")'),
    # --- Crypto ---
    (r'สร้างเหรียญ\((.+?)\s*,\s*(.+?)\s*,\s*(.+?)\)', r'create_crypto_contract("\1", "\2", "\3")'),
    (r'ขุดเหรียญ\((.+?)\)', r'simulate_mining(\1)'),
    (r'เริ่มบอทซุ่มซื้อ\(\)', r'simulate_sniper_bot()'),
    # --- SHA256 & Text ---
    (r'เข้ารหัส\s*SHA256\((.+?)\)', r'hashlib.sha256(str(\1).encode("utf-8")).hexdigest()'),
    (r'ความยาวของ\("(.+?)"\)', r'len("\1")'),
    # --- Game 2D ---
    (r'สร้างสี่เหลี่ยม\((.+?)\s*,\s*(.+?)\s*,\s*(.+?)\)', r'create_rect(\1, \2, \3)'),
    (r'สร้างวงกลม\((.+?)\s*,\s*(.+?)\s*,\s*(.+?)\)', r'create_circle(\1, \2, \3)'),
    (r'ล้างหน้าจอ\(\)', r'clear_screen()'),
    # --- Math & Data ---
    (r'รากที่สองของ\((.+?)\)', r'math.sqrt(\1)'),
    (r'สุ่มเลขจาก\((.+?)\s*ถึง\s*(.+?)\)', r'random.randint(\1, \2)'),
    (r'เวลาปัจจุบัน\(\)', r'datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")'),
    # --- Logic ---
    (r'ถ้า\s+(.+?):', r'if \1:'),
    (r'มิฉะนั้น:', r'else:'),
    (r'สำหรับ\s+(\w+)\s+ใน\s+(.+?):', r'for \1 in \2:'),
    # --- Basic ---
    (r'แสดงผล\((.+?)\)', r'print(\1)'),
    (r'ให้\s+(\w+)\s*=\s*(.+)', r'\1 = \2'),
]

def translate_to_python(thai_code):
    py_lines = []
    for line in thai_code.splitlines():
        indent = line[:-len(line.lstrip())] if line.lstrip() else ""
        stripped = line.strip()
        if not stripped or stripped.startswith('#'):
            py_lines.append(line)
            continue
        translated = stripped
        changed = True
        iteration = 0
        while changed and iteration < 20:
            changed = False
            iteration += 1
            for pattern, replacement in KEYWORDS:
                new_translated = re.sub(pattern, replacement, translated)
                if new_translated != translated:
                    translated = new_translated
                    changed = True
        py_lines.append(indent + translated)
    return '\n'.join(py_lines)

# ==========================================
# Canvas สำหรับวาดรูป
# ==========================================
class GameCanvas(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.entities = []
    def create_rect(self, x, y, size):
        with self.canvas:
            Color(random.random(), random.random(), random.random(), 1)
            self.entities.append(Rectangle(pos=(float(x), float(y)), size=(float(size), float(size))))
    def create_circle(self, x, y, size):
        with self.canvas:
            Color(random.random(), random.random(), random.random(), 1)
            self.entities.append(Ellipse(pos=(float(x), float(y)), size=(float(size), float(size))))
    def clear_screen(self):
        self.canvas.clear()
        self.entities = []

# ==========================================
# แอปพลิเคชันหลัก
# ==========================================
class ThaiLangUltimateApp(App):
    def build(self):
        self.title = "ThaiLang Ultimate (All-in-One)"
        self.tabs = TabbedPanel(do_default_tab=False)

        # 1. แท็บ AI
        tab_ai = TabbedPanelItem(text='🤖 AI')
        layout_ai = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.ai_input = TextInput(hint_text='ถามเอไอ(คำถามของคุณ)', multiline=True, size_hint_y=0.3)
        layout_ai.add_widget(self.ai_input)
        ai_btn = Button(text='🚀 ส่ง', size_hint_y=None, height=50)
        ai_btn.bind(on_press=lambda x: self.run_action(self.ai_input.text, self.ai_output, is_ai=True))
        layout_ai.add_widget(ai_btn)
        self.ai_output = Label(text='[AI พร้อมตอบ]', halign='left', valign='top', size_hint_y=None)
        self.ai_output.bind(width=lambda *x: setattr(self.ai_output, 'text_size', (self.ai_output.width, None)))
        self.ai_output.bind(texture_size=lambda *x: setattr(self.ai_output, 'height', self.ai_output.texture_size[1]))
        scroll_ai = ScrollView(size_hint=(1, 0.6))
        scroll_ai.add_widget(self.ai_output)
        layout_ai.add_widget(scroll_ai)
        tab_ai.add_widget(layout_ai)

        # 2. แท็บ โค้ด/Crypto/Game
        tab_code = TabbedPanelItem(text='💻 โค้ด/Crypto')
        layout_code = BoxLayout(orientation='vertical')
        self.game_screen = GameCanvas(size_hint_y=0.3)
        layout_code.add_widget(self.game_screen)
        code_control = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint_y=0.7)
        self.code_input = TextInput(hint_text='สร้างเหรียญ(...) , ขุดเหรียญ(...) , สร้างสี่เหลี่ยม(...)', multiline=True, size_hint_y=0.4)
        code_control.add_widget(self.code_input)
        code_btn = Button(text='▶️ รันโค้ด', size_hint_y=None, height=50)
        code_btn.bind(on_press=lambda x: self.run_action(self.code_input.text, self.code_output, is_ai=False))
        code_control.add_widget(code_btn)
        self.code_output = Label(text='[ผลลัพธ์]', size_hint_y=0.4, halign='left', valign='top')
        self.code_output.bind(width=lambda *x: setattr(self.code_output, 'text_size', (self.code_output.width, None)))
        scroll_code = ScrollView(size_hint_y=0.4)
        scroll_code.add_widget(self.code_output)
        code_control.add_widget(scroll_code)
        layout_code.add_widget(code_control)
        tab_code.add_widget(layout_code)

        # 3. แท็บ Hacking & Sniper Bot
        tab_hack = TabbedPanelItem(text='💀 Hacker/Sniper')
        layout_hack = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        hack_label = Label(text="คำสั่ง: แฮกระบบ(\"เป้าหมาย\") หรือ เริ่มบอทซุ่มซื้อ()", size_hint_y=None, height=30)
        layout_hack.add_widget(hack_label)
        
        self.hack_input = TextInput(hint_text='แฮกระบบ("เซิร์ฟเวอร์ธนาคาร")', multiline=True, size_hint_y=0.2, font_size=16)
        layout_hack.add_widget(self.hack_input)
        
        hack_btn = Button(text='💀 รันคำสั่ง', size_hint_y=None, height=50, background_color=(0.8, 0.1, 0.1, 1))
        hack_btn.bind(on_press=lambda x: self.run_action(self.hack_input.text, self.hack_output, is_ai=False))
        layout_hack.add_widget(hack_btn)
        
        self.hack_output = Label(text='[รอรับคำสั่ง...]', halign='left', valign='top', size_hint_y=None)
        self.hack_output.bind(width=lambda *x: setattr(self.hack_output, 'text_size', (self.hack_output.width, None)))
        self.hack_output.bind(texture_size=lambda *x: setattr(self.hack_output, 'height', self.hack_output.texture_size[1]))
        scroll_hack = ScrollView(size_hint=(1, 0.7))
        scroll_hack.add_widget(self.hack_output)
        layout_hack.add_widget(scroll_hack)
        tab_hack.add_widget(layout_hack)

        self.tabs.add_widget(tab_ai)
        self.tabs.add_widget(tab_code)
        self.tabs.add_widget(tab_hack)

        self.exec_globals = {
            'create_rect': self.game_screen.create_rect,
            'create_circle': self.game_screen.create_circle,
            'clear_screen': self.game_screen.clear_screen,
            'ask_ai': ask_ai,
            'create_crypto_contract': create_crypto_contract,
            'simulate_mining': simulate_mining,
            'simulate_sniper_bot': simulate_sniper_bot,
            'hack_system': hack_system,
            'math': math, 'random': random, 'datetime': datetime, 'hashlib': hashlib, 'time': time,
            '__builtins__': __builtins__
        }
        return self.tabs

    def run_action(self, text, output_label, is_ai=False):
        if not text.strip():
            return
        output_label.text = "⏳ กำลังประมวลผล..."
        py_code = translate_to_python(text)
        old_stdout = sys.stdout
        new_stdout = StringIO()
        sys.stdout = new_stdout
        try:
            exec(py_code, self.exec_globals)
        except Exception:
            print(f"❌ Error: {traceback.format_exc().splitlines()[-1]}")
        finally:
            sys.stdout = old_stdout
        output_label.text = new_stdout.getvalue()
        if is_ai:
            self.ai_input.text = ""

if __name__ == '__main__':
    ThaiLangUltimateApp().run()
