from flask import Flask, render_template, request, make_response
from forms import InvoiceForm
import pdfkit
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'


import os

@app.route('/', methods=['GET', 'POST'])
def index():
    form = InvoiceForm()
    if form.validate_on_submit():
        # Collect form data
        client_name = form.client_name.data
        client_address = form.client_address.data
        shipping_address = form.shipping_address.data
        product_name = form.product_name.data
        quantity = form.quantity.data
        price = form.price.data
        current_date = datetime.now().strftime("%d %B, %Y")

        # Get absolute paths for CSS and image
        css_path = os.path.join(os.getcwd(), 'static', 'styles', 'invoice_styles.css')
        logo_path = os.path.join(os.getcwd(), 'static', 'images', 'logo.jpg')

        # Render template
        rendered = render_template('invoice_template.html',
                                   client_name=client_name,
                                   client_address=client_address,
                                   shipping_address=shipping_address,
                                   product_name=product_name,
                                   quantity=quantity,
                                   current_date=current_date,
                                   price=price,
                                   css_path=css_path,
                                   logo_path=logo_path)

        # Generate PDF
        options = {
            'enable-local-file-access': None,
            'no-stop-slow-scripts': None
        }
        pdf = pdfkit.from_string(rendered, False, options=options)

        # Send PDF as a response
        response = make_response(pdf)
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = 'attachment; filename=invoice.pdf'

        return response

    return render_template('index.html', form=form)
