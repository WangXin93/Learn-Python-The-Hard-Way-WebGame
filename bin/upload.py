from PIL import Image
import os
import web

urls = ('/upload', 'Upload')

uploadapp = web.application(urls, globals())
render = web.template.render('templates/', base='layout')

class Upload:
    def GET(self):
        web.header("Content-Type", "text/html; charset=utf-8")
        return render.upload("")

    def POST(self):
        x = web.input(myfile={})
        filedir = './static'
        if 'myfile' in x:
            filepath = x.myfile.filename.replace('\\','/')
            filename = filepath.split('/')[-1]
            fout = open(filedir + '/' + filename, 'wb')
            fout.write(x.myfile.file.read())
            fout.close()

            infile = filedir + '/' + filename
            outfile = infile + '.thumbnail'
            im = Image.open(infile)
            im.thumbnail((128, 128))
            im.save(outfile, im.format)
        return render.upload(outfile)
        
if __name__ == "__main__":
    uploadapp.run()


