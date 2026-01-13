import markdown
import argparse
from markdown.extensions.wikilinks import WikiLinkExtension
from pathlib import Path

class Converter():
    fileType = "*.md"
    def __init__(self, folder = "."):
        self.folder = folder

    @staticmethod
    def getBasename(name):
        return name.removesuffix(".md")
    @staticmethod
    def addOverhead(htmlInner):
        cssName = "theme.css"
        html = f"<head> <link rel=\"stylesheet\" href=\"{cssName}\"> </head>" + "<body>" + htmlInner + "</body>"
        return html
    #def generateMenu(self):
    def getFileStruct(self, directoryPath):
        files = [f for f in Path(directoryPath).rglob(self.fileType) if f.is_file()]
        for file in files:
            print(file.relative_to(directoryPath))
        fileByFolder = {}
       
        #for file in files:
            
        return files
    def convertFile(self, filenameRaw, outputFilenameRaw):
        filename = ""
        if outputFilenameRaw is None:
            filename = self.getBasename(filenameRaw)
            outputFilenameRaw = filename + ".html"
        
        print(outputFilenameRaw)
        with open(filenameRaw, "r", encoding='utf-8') as mdF:
            contentMD = mdF.read()
            # Add filename as header
            contentMD = f"# {filename}\n {contentMD}"
            html = markdown.markdown(contentMD, extensions=[
                "fenced_code",   # ```code blocks```
                "tables",        # таблицы
                "toc",           # оглавление
                "codehilite",     # подсветка кода
                "extra",
                WikiLinkExtension(base_url='/docs/', end_url='.html')
            ])
            with open(outputFilenameRaw, "w", encoding='utf-8') as htmlF:
                htmlF.write(self.addOverhead(html))
    def convertAll(self, dirPath, outPath):
        files = self.getFileStruct(dirPath)
        for file in files:
            pass
        pass
    def convertOne(self, filename, outputFilename):
        self.convertFile(filename, outputFilename)
        #print("HEllo")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MD to html")
    #parser.add_argument("-i", "--input", type=str, help="Input md file")
    parser.add_argument("-s", "--single", action='store_true', help="One file pass") # Store bool
    parser.add_argument("-o", "--out", type=str, help="output file or folder")    
    parser.add_argument("filename", help="Input md file or folder")
    args = parser.parse_args()

    #print(args.single)
    #print(args.filename)

    converter = Converter()
    
    if args.single:        
        converter.convertOne(args.filename, args.out)
    else:
        converter.convertAll(args.filename, args.out)

    