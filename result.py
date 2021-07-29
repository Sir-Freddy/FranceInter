from functions.textToSpeech import config_sounds
from functions.translations import translate

import json
import cgi
import cgitb
import time

cgitb.enable()
form = cgi.FieldStorage()

if form.getvalue("message") :
    fr_message = form.getvalue("message")
    en_message = translate(fr_message)
    en_message = json.loads(en_message)
    en_message = en_message[0]["translations"][0]["text"]
    config_sounds(fr_message)
else :
    raise Exception("Message manquant.")

if form.getvalue("number") :
    number = form.getvalue("number")
    fichier = open("config.json", "w")
    jsonFile = "{\n"
    dbq='"maximum"'
    jsonFile+="    "+dbq+":"+number+"\n"
    jsonFile+="}"
    fichier.write(jsonFile)
    fichier.close()
else :
    raise Exception("Nombre manquant.")
  
time.sleep(3)
html = """<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-+0n0xVW2eSR5OomGNYDnhzAbDsOXxcvSN1TPprVMTNDbiYZCxYbOOl7+AMvyTG2x" crossorigin="anonymous">
    <title>FranceInter</title>

    <style> /* CSS */
      .background {
        background-image: url("../src/assets/franceinter.jpg");
        background-position: top;
        background-repeat: no-repeat;
        background-size: cover;
        height: 100vh;
        width: 100%;
      }

    .blur {
      background: rgba(0, 0, 0, 0.2); 
      backdrop-filter: blur(8px); 
      height: 100vh;
      width: 100%;
    }
    </style>

  </head> 
  <body>

    <div class="background">
      <div class="blur">
        <div id="header">
          <nav class="navbar navbar-expand-lg navbar-dark bg-dark" style="height:100px">
              <div class="container-fluid">
                <a class="navbar-brand" href="#"><img src="../src/assets/logo.png" alt="Logo" style="width:80px; left: 10%; top: 10%; position: absolute"></a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarColor02" aria-controls="navbarColor02" aria-expanded="false" aria-label="Toggle navigation">
                  <span class="navbar-toggler-icon"></span>
                </button>
              </div>
            </nav>
      </div style="text-align: center;">
        <form action="/recog.py" method="post">
          <div id="content" style="display: flex; flex-direction: column; text-align: center;">

            <div class="card border-dark mb-3" style="width: 50rem; margin: 20px; margin-left: auto; margin-right: auto;">
              <div class="card-header">Aperçu</div>
              <div class="card-body">
                <table class="table table-hover">
                  <tbody>
                    <thead>
                      <tr>
                        <th scope="col">Paramètres</th>
                        <th scope="col">Valeurs</th>
                      </tr>
                    </thead>
                    <tr>
                      <th scope="row">Message en français :</th>
                      <td>"""
print(html)
print(fr_message)        
html = """                     
                      </td>
                    </tr>
                    <tr>
                      <th scope="row">Message en anglais :</th>
                      <td>"""
print(html)
print(en_message)
html = """                     
                      </td>
                    </tr>
                    <tr>
                      <th scope="row">Nombre maximum :</th>
                      <td>"""
print(html)                      
print(number)
html = """                     
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
              <div class="card-footer">
                <table class="table table-hover">
                  <tbody>
                    <thead>
                      <tr>
                        <th scope="col">
                            Audio en français
                        </th>
                        <th scope="col">Audio en anglais</th>
                      </tr>
                    </thead>
                    <tr>
                      <td><audio
                            controls
                            src='"""
print(html)                          
print("sounds/french.wav")
html = """              
                            '>
                                Your browser does not support the
                                <code>audio</code> element.
                        </audio></th>
                      <td><audio
                            controls
                            src='"""
print(html)                            
print("sounds/english.wav")
html = """                            
                            '>
                                Your browser does not support the
                                <code>audio</code> element.
                        </audio></td>
                    </tr>
                  </tbody>
                </table>
                <form action="recog.py" method="post">
                  <label for="pic">Insérez le lien de l'image à analyser :</label>
                  <input type="text" id="pic" name="pic" placeholder="URL de l'image..." style="padding:10px; margin:5px; margin-top:10px; width:300px;"><br>
                  <button class="btn btn-dark" type="submit" style="padding:10px; margin:5px; width:300px">Analyser</button>
                </form>
              </div>
            </div>
          </div>
        </form>
      </div>
    </div>

    <script> // Javascript

    </script>

  </body>
</html>"""
print(html)
