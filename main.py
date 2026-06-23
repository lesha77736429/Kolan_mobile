from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDButton, MDButtonText
from kivy.clock import Clock
import socket
import json
import hashlib

SERVER_IP = "192.168.0.106"  # <-- Твой IP старого ПК (сервера)
SERVER_PORT = 55555

def hash_password(pw: str) -> str:
    return hashlib.sha256(pw.encode("utf-8")).hexdigest()

class LoginScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = MDBoxLayout(orientation='vertical', padding=30, spacing=20, adaptive_height=True)
        layout.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        
        title = MDLabel(text="Kolan Mobile", halign="center")
        layout.add_widget(title)
        
        self.phone_input = MDTextField(hint_text="Номер телефона", mode="outlined")
        layout.add_widget(self.phone_input)
        
        self.password_input = MDTextField(hint_text="Пароль", password=True, mode="outlined")
        layout.add_widget(self.password_input)
        
        # Обновили кнопку под формат KivyMD 2.0
        login_btn = MDButton(style="filled", pos_hint={"center_x": 0.5})
        login_btn.add_widget(MDButtonText(text="Войти"))
        login_btn.bind(on_release=self.auth_on_server)
        layout.add_widget(login_btn)
        
        self.status_label = MDLabel(text="", halign="center")
        layout.add_widget(self.status_label)
        
        self.add_widget(layout)

    def auth_on_server(self, instance):
        phone = self.phone_input.text.strip()
        password = self.password_input.text.strip()
        
        if not phone or not password:
            self.status_label.text = "Заполните все поля!"
            return
            
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.settimeout(3.0)
            client_socket.connect((SERVER_IP, SERVER_PORT))
            
            request = {
                "action": "login",
                "phone": phone,
                "password_hash": hash_password(password)
            }
            client_socket.sendall(json.dumps(request, ensure_ascii=False).encode('utf-8'))
            
            packet = client_socket.recv(1024)
            if packet:
                res = json.loads(packet.decode('utf-8'))
                if res.get("status") == "success":
                    self.status_label.text = f"Успешный вход! Привет, {res.get('name')}"
                else:
                    self.status_label.text = res.get("message", "Ошибка входа")
            client_socket.close()
        except Exception as e:
            self.status_label.text = "Нет связи с сервером!"

class KolanMobileApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Olive" # В KivyMD 2.0 используются новые цвета
        return LoginScreen()

if __name__ == "__main__":
    KolanMobileApp().run()
