import fitz

pdf = fitz.open("example.pdf")  # Open the PDF file     

pix = pdf[0].get_pixmap(dpi=200)  # Get the first page as a pixmap

plt.save("page.webp")

print("Webp Image Created!")