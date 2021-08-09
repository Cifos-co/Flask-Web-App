from sqlalchemy.sql.expression import false, true
from werkzeug.wrappers import request
from .models import User, Client, Bill
from flask import flash
import docx

def write_document():
    doc = docx.Document("website\static\document_templates\ModeloFactura.docx")

    tables = doc.tables()
    

    doc.save("website\static\document_templates\ModeloFactura.docx")

def read_document():
    pass

def save_document(type):
    pass

def send_document(email):
    pass