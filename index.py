import cgi

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
        <form action="result.py" method="post">
          <div id="content" style="display: flex; flex-direction: column; text-align: center;">

            <div class="card border-dark mb-3" style="width: 50rem; margin: 20px; margin-left: auto; margin-right: auto;">
              <div class="card-header">Configuration</div>
              <div class="card-body">
                <h4 class="card-title">Entrez le message que vous souhaitez diffuser en cas de non respect des gestes barrières.</h4>
                <div id="double" style="display: flex; flex-direction:row;">
                  <div id="simple1" style="display: flex; flex-direction:column;margin-left:70px">
                    <input type="text" id="message" name="message" placeholder="Entrez votre message..." style="padding:10px; margin:5px; margin-top:10px; width:300px;">
                    <small class="form-text text-muted">Ce message sera également traduit en anglais.</small>
                  </div>
                  <div id="simple2" style="display: flex; flex-direction:column; ">
                    <input type="number" id="number" name="number" placeholder="Entrez le nombre maximum..." style="padding:10px; margin:5px; margin-top:10px; width:300px">
                    <small class="form-text text-muted">Ce nombre servira de limite au nombre de personne.</small>
                  </div>
                </div>
              </div>
              <div class="card-footer">
                <button class="btn btn-dark" type="submit" style="padding:10px; margin:5px; width:300px">Valider</button>
              </div>
            </div>
          </div>
        </form>
      </div>
    </div>

    <script> // Javascript
      function apercu() {
        document.getElementById("old").style.visibility = "hidden";
        
      }
    </script>

  </body>
</html>"""

print(html)