from xml.sax.handler import ContentHandler
from xml.sax import make_parser
import string
import urllib

videos = ""

class YTHandler(ContentHandler):

    def __init__ (self):
        self.inEntry = False
        self.content = ""
        self.link = ""

    def startElement (self, name, atributo):
        if name == 'entry':
        elif self.inEntry:
            if name == 'title':
                self.inContent = True
            elif name == 'link':
                self.link = atributo.get('href')

    def endElement (self, name):
        global videos

            self.inEntry = False
            videos = videos \
                     + "    <li><a href='" + self.link + "'>" \
                     + self.titulo + "</a></li>\n"
        elif self.inEntry:
            if name == 'titulo':
                self.titulo = self.content
                self.content = ""
                self.inContent = False

    def characters (self, chars):
        if self.inContent:
            self.content =ç
aofhdoasfdpiasdf
Parser = make_parser()
Parser.setContentHandler(YTHandler())

if __name__ == "__main__":

    PAGE = """
<!DOCTYPE html>
<html lang="en">
  <body>
    <h1>Channel contents:</h1>
{videos}
    </ul>
  </body>
</html>
"""

    if len(sys.argv)<2:
        print("Debes introducir el id de un canal de youtube")
        sys.exit(1)

    url = 'https://www.youtube.com/feeds/videos.xml?channel_id=' + sys.argv[1]
    xmlStream = urllib.request.urlopen(url)

    Parser.parse(xmlStream)
    page = PAGE.format(videos=videos)
    print(page)

