import markdown
import argparse

class Converter():
    def __init__(self, folder = "."):
        self.folder = folder

    @staticmethod
    def getBasename(name):
        return name.removesuffix(".md")
    
    def addOverhead(self, htmlInner):
        cssName = "theme.css"
        html = f"<head> <link rel=\"stylesheet\" href=\"{cssName}\"> </head>" + "<body>" + htmlInner + "</body>"
        return html
    
    def convertFile(self, filenameRaw):
        filename = self.getBasename(filenameRaw)
        with open(filename + ".md", "r") as mdF:
            contentMD = mdF.read()
            html = markdown.markdown(contentMD)
            with open(filename + ".html", "w") as htmlF:
                htmlF.write(self.addOverhead(html))
    def convertAll(self):
        self.convertFile("README.md")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MD to html")
    #parser.add_argument("-i", "--input", type=str, help="Input md file")
    parser.add_argument("filename", help="Input md file")
    args = parser.parse_args()
    #print(f"{args.filename}")

    converter = Converter()
    converter.convertAll()

    