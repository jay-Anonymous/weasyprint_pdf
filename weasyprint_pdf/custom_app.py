from weasyprint import HTML

def get_pdf(html, options=None):
    return HTML(string=html).write_pdf()
