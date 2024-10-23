from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class InvoiceForm(FlaskForm):
    client_name = StringField('Client Name', validators=[DataRequired()])
    client_address = StringField('Client Address', validators=[DataRequired()])
    shipping_address = StringField('Shipping Address', validators=[DataRequired()])
    product_name = StringField('Product/Service Name', validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    submit = SubmitField('Generate Invoice')
