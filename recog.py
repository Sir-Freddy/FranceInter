from functions.numberOfPeople import numberOfPeople
import cgi
import cgitb
import json

cgitb.enable()
formu = cgi.FieldStorage()

_1_ = """<!doctype html>
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
        background-image: url("src/assets/franceinter.jpg");
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
                <a class="navbar-brand" href="#"><img src="src/assets/logo.png" alt="Logo" style="width:80px; left: 10%; top: 10%; position: absolute"></a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarColor02" aria-controls="navbarColor02" aria-expanded="false" aria-label="Toggle navigation">
                  <span class="navbar-toggler-icon"></span>
                </button>
              </div>
            </nav>
      </div style="text-align: center;">
        <form action="/recog.py" method="post">
          <div id="content" style="display: flex; flex-direction: column; text-align: center;">
            
            <div class="card border-dark mb-3" style="width: 50rem; margin: 20px; margin-left: auto; margin-right: auto;">
              <div class="card-header">Résultats</div>
              <div class="card-body">
                <p class="card-text">Les gestes barrières semblent être respéctés.</p>
              </div>
              <div class="card-footer">
                <form action="recog.py" method="post">
                <p class="card-text">Vous souhaitez analyser une autre image ?</p>
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
  </body>
</html>"""

_0_ = """<!doctype html>
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
        background-image: url("src/assets/franceinter.jpg");
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
                <a class="navbar-brand" href="#"><img src="src/assets/logo.png" alt="Logo" style="width:80px; left: 10%; top: 10%; position: absolute"></a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarColor02" aria-controls="navbarColor02" aria-expanded="false" aria-label="Toggle navigation">
                  <span class="navbar-toggler-icon"></span>
                </button>
              </div>
            </nav>
      </div style="text-align: center;">
        <form action="/recog.py" method="post">
          <div id="content" style="display: flex; flex-direction: column; text-align: center;">
            
            <div class="card border-dark mb-3" style="width: 50rem; margin: 20px; margin-left: auto; margin-right: auto;">
              <div class="card-header">Résultats</div>
              <div class="card-body">
                <p class="card-text">Les gestes barrières semblent ne pas être respéctés.</p>
                <table class="table table-hover">
                  <thead>
                    <tr>
                      <th scope="col">Audio en français</th>
                      <th scope="col">Audio en anglais</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <th>    <audio
                        controls
                        src="sounds/french.wav">
                            Your browser does not support the
                            <code>audio</code> element.
                    </audio></th>
                      <td>    <audio
                        controls
                        src="sounds/english.wav">
                            Your browser does not support the
                            <code>audio</code> element.
                    </audio></td>
                    </tr>
                  </tbody>
                </table>
              </div>
              <div class="card-footer">
                <form action="recog.py" method="post">
                  <p class="card-text">Vous souhaitez analyser une autre image ?</p>
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
  </body>
</html>"""

with open("config.json") as json_data:
            data_dict = json.load(json_data)
            maximum = data_dict['maximum']
            
if formu.getvalue("pic") :
    url = formu.getvalue("pic")
    if numberOfPeople(url) == 0 :
        print(_0_)
    else :
        print(_1_)
else :
    raise Exception("Image manquante ou mauvais format d'URL.")