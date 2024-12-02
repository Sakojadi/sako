import sys
from PyQt5.QtWidgets import QMessageBox, QDialog, QApplication, QWidget, QLabel, QTextEdit, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QComboBox
from PyQt5.QtGui import QFont
from collections import defaultdict
import requests


class Chat:
    def __init__(self):
        self.users = {}
        self.messages = {}

users = []
messages = defaultdict(list)
me = []
result = [False]

   
class Registration(QDialog):
    def __init__(self):
        super().__init__()
        self.msg_dict = defaultdict(list)

        self.label = QLabel("username")
        self.username = QLineEdit()
        self.label2 = QLabel("password")
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        self.register_button = QPushButton("Register")

        font = QFont()
        font.setPointSize(14) 
        
        self.label.setFont(font)
        self.username.setFont(font)
        self.label2.setFont(font)
        self.password.setFont(font)
        self.register_button.setFont(font)

        self.register_button.clicked.connect(self.register)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.username)
        layout.addWidget(self.label2)
        layout.addWidget(self.password)
        layout.addWidget(self.register_button)

        self.setLayout(layout)
        self.setWindowTitle('Registration')
        self.setGeometry(200, 200, 400, 400)
    
    def register(self):
        username = self.username.text()
        password = self.password.text()
        if password == '12345':
            if len(username) > 0:
                me.append(username)
                result[0] = True
                self.close()
        else:
            msg = QMessageBox(self, f"Wrong Password")
            msg.show()
            result[0] = False

    

class NewUser(QDialog):
    def __init__(self):
        super().__init__()
        self.msg_dict = defaultdict(list)

        self.label = QLabel("New User Name")
        self.contact = QLineEdit()
        self.add_button = QPushButton("Add new user")

        font = QFont()
        font.setPointSize(14) 
        
        self.label.setFont(font)
        self.contact.setFont(font)
        self.add_button.setFont(font)

        self.add_button.clicked.connect(self.add)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.contact)
        layout.addWidget(self.add_button)

        self.setLayout(layout)
        self.setWindowTitle('NEW CONTACT')
        self.setGeometry(200, 200, 400, 400)
    
    def add(self):
        user = self.contact.text()
        if len(user) > 0:
            users.append(user)
            self.label.setText(f'Added new user : {user}')
            self.contact.clear()
    

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.register = Registration()
        self.register.exec()

        if result[0] == True:
            self.msg_dict = defaultdict(list)

            self.contacts = QComboBox()
            self.messages = QTextEdit()
            self.add_user_button = QPushButton("Add new user")
            self.see_chats_button = QPushButton("See chats of the user")
            self.see_my_button = QPushButton("See all my chats")
            self.messages.setReadOnly(True)
            self.message = QLineEdit()
            self.send_button = QPushButton("Send")
            
            font = QFont()
            font.setPointSize(14) 
            
            self.contacts.setFont(font)
            self.message.setFont(font)
            self.messages.setFont(font)
            self.send_button.setFont(font)
            self.add_user_button.setFont(font)
            self.see_chats_button.setFont(font)
            self.see_my_button.setFont(font)

            self.send_button.clicked.connect(self.send)
            self.contacts.currentIndexChanged.connect(self.show_messages)
            self.add_user_button.clicked.connect(self.add_new_user)
            self.see_chats_button.clicked.connect(self.show_messages_user)
            self.see_my_button.clicked.connect(self.show_messages_mine)

            layout = QVBoxLayout()
            layout.addWidget(self.contacts)
            layout.addWidget(self.add_user_button)
            layout.addWidget(self.see_chats_button)
            layout.addWidget(self.see_my_button)
            layout.addWidget(self.messages)
            layout.addWidget(self.message)
            layout.addWidget(self.send_button)
            

            self.setLayout(layout)
            self.setWindowTitle('AIT CHAT 2024')
            self.setGeometry(200, 200, 600, 800)
            for user in users:
                self.contacts.addItem(user)

    def send(self):
        sender = me[0]
        receiver = self.contacts.currentText().strip()
        message = self.message.text()
        if len(receiver) > 0 and len(message) > 0:
            url = 'https://ait23.pythonanywhere.com/addChat'
            data = {'sender': sender, 'receiver': receiver, 'message': message}
            requests.get(url, json= data)
            self.show_messages()
            self.message.clear()

    def show_messages(self):
        sender = me[0]
        receiver = self.contacts.currentText()
        if len(receiver) > 0:
            url = 'https://ait23.pythonanywhere.com/getChat'
            response = requests.get(url, json= {'sender': sender})
            r = response.json().get('response', '').split('\n')
            arr = []
            for i in r:
                if sender in i and receiver in i:
                    arr.append(i)
            self.messages.setText('\n'.join(arr))
            
    def show_messages_user(self):
        sender = self.contacts.currentText()
        if len(sender) > 0:
            url = 'https://ait23.pythonanywhere.com/getChat'
            response = requests.get(url, json= {'sender': sender})
            r = response.json().get('response', '').split('\n')
            arr = []
            for i in r:
                if sender in i:
                    arr.append(i)
            self.messages.setText('\n'.join(arr))
            
    def show_messages_mine(self):
        sender = me[0]
        if len(sender) > 0:
            url = 'https://ait23.pythonanywhere.com/getChat'
            response = requests.get(url, json= {'sender': sender})
            r = response.json().get('response', '').split('\n')
            arr = []
            for i in r:
                if sender in i:
                    arr.append(i)
            self.messages.setText('\n'.join(arr))
    
    def add_new_user(self):
        self.new_user = NewUser()
        self.new_user.exec()
        self.contacts.clear()
        for user in users:
            self.contacts.addItem(user)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())