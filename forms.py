from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, DecimalField
from wtforms.validators import DataRequired, ValidationError


class InvoiceForm(FlaskForm):
    client_name = StringField('Client Name', validators=[DataRequired()])
    client_address = StringField('Client Address', validators=[DataRequired()])
    shipping_address = StringField('Shipping Address', validators=[DataRequired()])
    product_name = StringField('Product/Service Name', validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    def validate_quantity(form, field):
        if field.data <= 0:
            raise ValidationError('Quantity must be greater than 0')
    price = DecimalField('Price', validators=[DataRequired()])
    submit = SubmitField('Generate Invoice')
