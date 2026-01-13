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
        if type(name) == str:
            name = Path(name)
        return name.stem
    @staticmethod
    def addOverhead(htmlInner):
        cssName = "theme.css"
        html = f"<head> <link rel=\"stylesheet\" href=\"{cssName}\"> </head>" + "<body>" + htmlInner + "</body>"
        return html
    #def generateMenu(self):
    def getFileStruct(self, directoryPath):
        files = [f.relative_to(directoryPath) for f in Path(directoryPath).rglob(self.fileType) if f.is_file()]
        fileByFolder = {}
        for file in files:
            if not file.parent in fileByFolder:
                fileByFolder[file.parent] = []
            fileByFolder[file.parent].append({"path" : directoryPath / file, "name" : file.stem})        
        return fileByFolder
    def convertFile(self, filenameRaw, outputFilenameRaw):
        print(filenameRaw)
        print(outputFilenameRaw)
        filename = self.getBasename(filenameRaw)
        #outputFilenameRaw += ".html"
        if type(filenameRaw) == str:
            filenameRaw = Path(filenameRaw)
        with filenameRaw.open("r", encoding='utf-8') as mdF:
            contentMD = mdF.read()
            # Add filename as header
            contentMD = f"# {filename} \n\n {contentMD}"
            html = markdown.markdown(contentMD, extensions=["wikilinks"],
            extension_configs={
                "wikilinks": {
                    "base_url": "/docs/",
                    "end_url": ".html",
                }
                }
            )
            with open(outputFilenameRaw, "w", encoding='utf-8') as htmlF:
                htmlF.write(self.addOverhead(html))
    def convertAll(self, dirPath, outPath):
        files = self.getFileStruct(dirPath)
        for folder in files:
            for file in files[folder]:
                self.convertFile(file["path"], outPath + file["name"] + ".html")
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

    