from fpdf import FPDF
import os

def main():
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    cwd = os.path.dirname(__file__)
    file = os.path.join(cwd, "assets", "fonts", "Raleway-Light.ttf")
    pdf.add_font('Raleway-Light', '', file, uni=True)
    pdf.set_font('Raleway-Light', '', 10)
    pdf.set_text_color(255, 255, 255)
    pdf.image('assets/img/logo_dev4u.png', x=0, y=0, w=210, h=297)
    pdf.output('output/test1.pdf')

if __name__ == '__main__':
    main()