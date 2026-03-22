from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

class FlightTracker(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=30, spacing=15)
        
        # عنوان التطبيق
        self.title_label = Label(text="Flight Status Tracker", font_size='35sp', color=(0, 0.7, 1, 1))
        
        # حقل إدخال رقم الرحلة
        self.flight_input = TextInput(text='Enter Flight No (e.g. EK202)', multiline=False, size_hint=(1, 0.2))
        
        # زر البحث
        btn = Button(text="Check Status", size_hint=(1, 0.3), background_color=(0, 0.5, 0.8, 1))
        btn.bind(on_press=self.check_flight)
        
        # شاشة عرض النتائج
        self.result_label = Label(text="Waiting for input...", font_size='20sp')
        
        layout.add_widget(self.title_label)
        layout.add_widget(self.flight_input)
        layout.add_widget(btn)
        layout.add_widget(self.result_label)
        return layout

    def check_flight(self, instance):
        flight_no = self.flight_input.text
        # هنا يمكنك مستقبلاً ربط API حقيقي للطيران
        if "EK" in flight_no.upper():
            self.result_label.text = f"Flight: {flight_no}\nStatus: ON TIME\nGate: B12"
        else:
            self.result_label.text = f"Searching for {flight_no}...\nStatus: Scheduled"

if __name__ == '__main__':
    FlightTracker().run()
