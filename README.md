# 📄 PDF to WebP Converter

A simple Python script that uses **PyMuPDF (`fitz`)** to convert the first page of a PDF document into a high-resolution **WebP image**.

## 🚀 Features

* 📂 Opens a PDF file with PyMuPDF
* 📄 Extracts the first page
* 🖼️ Renders the page at **200 DPI**
* 🌐 Saves the rendered page as a `.webp` image
* ⚡ Lightweight and easy to use

## 🛠️ Technologies

* **Python**
* **PyMuPDF (fitz)**
* **WebP**

## 📦 Installation

Install PyMuPDF with pip:

```bash
pip install PyMuPDF
```

## 💻 Usage

Place your PDF file in the project directory and name it `example.pdf`.

```python
import fitz

pdf = fitz.open("example.pdf")

pix = pdf[0].get_pixmap(dpi=200)

pix.save("page.webp")

print("WebP Image Created!")
```

## 📁 Project Structure

```text
pdf-to-webp/
│
├── example.pdf
├── main.py
├── page.webp
└── README.md
```

## 🔍 How It Works

### 1. Open the PDF

```python
pdf = fitz.open("example.pdf")
```

Loads the PDF document using PyMuPDF.

### 2. Render the First Page

```python
pix = pdf[0].get_pixmap(dpi=200)
```

Converts the first page into a raster image at **200 DPI**.

### 3. Save as WebP

```python
pix.save("page.webp")
```

Exports the rendered page as a WebP image.

## 📊 Example

**Input:**

```text
example.pdf
```

⬇️

**Processing:**

```text
PDF → First Page → 200 DPI Pixmap
```

⬇️

**Output:**

```text
page.webp
```

## 🎯 Use Cases

This project can be useful for:

* 📄 PDF page previews
* 🖼️ Document thumbnails
* 🌐 Web-friendly document images
* 📚 Digital document processing
* 🔄 PDF-to-image conversion pipelines
* 🤖 Document-processing projects

## ⚙️ Customization

You can convert other pages by changing the page index:

```python
pix = pdf[1].get_pixmap(dpi=200)
```

You can also increase or decrease the resolution:

```python
pix = pdf[0].get_pixmap(dpi=300)
```

Higher DPI generally produces a larger, more detailed image.

## 📝 Note

PyMuPDF's pixmap object should be saved using:

```python
pix.save("page.webp")
```

rather than:

```python
plt.save("page.webp")
```

because `plt` refers to Matplotlib and does not provide the appropriate method for saving a PyMuPDF pixmap.

## 📜 License

This project is open-source and available for educational and personal use.
