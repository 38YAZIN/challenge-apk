from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class ClickerGame(App):
    def build(self):
        # تعريف متغير العداد
        self.count = 0
        
        # تصميم الواجهة
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        
        # نص العداد (كبير وواضح)
        self.label = Label(text="Score: 0", font_size='50sp', color=(1, 1, 0, 1))
        
        # زر الضغط
        btn = Button(
            text="CLICK ME!", 
            size_hint=(1, 0.3), 
            background_color=(1, 0, 0, 1), # أحمر
            font_size='30sp'
        )
        btn.bind(on_press=self.increment)
        
        layout.add_widget(self.label)
        layout.add_widget(btn)
        return layout

    def increment(self, instance):
        # زيادة العداد وتحديث النص
        self.count += 1
        self.label.text = f"Score: {self.count}"

if __name__ == '__main__':
    ClickerGame().run()
