# -*- coding: utf-8 -*-
# @-=================================================================-@
#   
#   BY: Henrique Félix
#   PROJECT MADE WITH: Qt Designer and PySide6
#   V: 1.0.0
#   LICENSE: GNU General Public License v3.0
#   
# @-=================================================================-@
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
# 
#   
#   Discover other projects at github.com/ricksfelix
#   
#   
# @-=================================================================-@


from PySide6.QtWidgets import QApplication, QMainWindow
from ui_untitled import Ui_MainWindow  
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib, sys, yaml, logging



logging.basicConfig (
    filename='log.log', 
    filemode='a', 
    level=logging.DEBUG, 
    format='%(asctime)s | %(levelname)s | %(message)s', 
    datefmt='%d/%m/%Y ( %H:%M:%S )', 
    encoding='utf-8'    
)



class Send_Email():
    def __init__(self, config):
        self.config = {}
        self.config.update(config)
        self.server = None
        self.config_email = None
    

    def start_connection(self):
        self.server = smtplib.SMTP(self.config['smtp'], self.config['port'])
        self.server.ehlo()
        self.server.starttls()
        self.server.login(self.config['email'], self.config['passwd'])


    def mount_email(self):
        self.config_email = MIMEMultipart()
        self.config_email['From'] = self.config['email']
        self.config_email['To'] = self.config['dest']
        self.config_email['Subject'] = self.config['title']
        self.config_email.attach(MIMEText(self.config['message'], 'plain'))


    def send_email(self):
        self.start_connection()
        self.mount_email()
        self.server.sendmail(self.config['email'], self.config['dest'], self.config_email.as_string())
        self.server.quit()
        self.server = None
        self.config_email = None



class Email_Windown(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Prog Envio de e-mail')
        
        self.ui.bt_send.clicked.connect(self.send_email)

        self.config = {}
        self.load_config()
        
        self.show()


    def load_config(self):
        self.config_email = Config_Email()
        self.config_email.read_yaml()
        self.config.update(self.config_email.get_config())
        if not self.config == {}:
            self.ui.le_email.setText(self.config['email'])
            self.ui.le_smtp.setText(self.config['smtp'])
            self.ui.le_passwd.setText(self.config['passwd'])
            self.ui.le_port.setText(self.config['port'])
            self.ui.le_dest.setText(self.config['dest'])
            self.ui.le_title.setText(self.config['title'])
            self.ui.le_text.setText(self.config['message'])
            self.ui.cb_ssl.setChecked(True)

    
    def send(self):
        try:
            self.sender = Send_Email(self.config)
            self.sender.send_email()
            logging.info('Email enviado com sucesso!')
            logging.info(f"""Email de "{self.config['email']}" para "{self.config['dest']}"\n |-> Titulo: {self.config['title']}\n |-> Mensagem: {self.config['message']}""")
            
            self.ui.lb_result.setText('E-mail enviado com sucesso!')

            self.config_email.set_config(self.config)
            self.config_email.save_yaml()
        except Exception as e:
            logging.error(f"Falha ao enviar email, motivo: {e}")
            self.ui.lb_result.setText(f'Falha ao enviar e-mail\nMotivo: {e}')


    def verify(self):
        inputs = [
            (self.ui.le_dest, 'text'),
            (self.ui.le_title, 'text'),
            (self.ui.le_text, 'plaintext'),
            (self.ui.le_email, 'text'),
            (self.ui.le_smtp, 'text'),
            (self.ui.le_passwd, 'text'),
            (self.ui.le_port, 'text'),
        ]

        for line_edit, content_type in inputs:
            content = line_edit.text() if content_type == 'text' else line_edit.toPlainText()
            if content != "":
                line_edit.setStyleSheet('border: 1px solid black;')
            else:
                line_edit.setStyleSheet('border: 1px solid red;')
                return False
        return True


    def send_email(self):
        self.config['email'] = self.ui.le_email.text()
        self.config['smtp'] = self.ui.le_smtp.text()
        self.config['passwd'] = self.ui.le_passwd.text()
        self.config['port'] = self.ui.le_port.text()
        self.config['dest'] = self.ui.le_dest.text()
        self.config['title'] = self.ui.le_title.text()
        self.config['message'] = self.ui.le_text.toPlainText()
        self.config['ssl'] = self.ui.cb_ssl.isChecked()

        if self.verify(): self.send()

        

class Config_Email:
    def __init__(self):
        self.config = {}


    def set_config(self, config):
        self.config.update(config)


    def get_config(self):
        return self.config


    def save_yaml(self):
        data = None
        with open('config.yaml', 'w') as file:
            data = yaml.dump(self.config, file)
        logging.info('Arquivo "config.yaml" Salvo com sucesso!')
        return data


    def read_yaml(self):
        try:
            data = None
            with open('config.yaml', 'r') as file:
                data = yaml.safe_load(file)
            self.config.update(data)
            logging.info('Arquivo "config.yaml" Lido com sucesso!')
        except FileNotFoundError:
            self.config = {}
            logging.warning('Arquivo "config.yaml" Não Encontrado!')
            return self.config
            


if __name__ == '__main__':
    app = QApplication([])
    config_window = Email_Windown()
    sys.exit(app.exec())