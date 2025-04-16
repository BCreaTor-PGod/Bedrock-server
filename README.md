# Bedrock-server
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Chopin's Minecraft Server</title>
  <style>
    body {
      background-color: #1e1e1e;
      color: #fff;
      font-family: 'Courier New', monospace;
      text-align: center;
      padding: 40px;
    }
    h1 {
      font-size: 3rem;
      color: #00ff88;
    }
    .server-info {
      margin-top: 30px;
      font-size: 1.2rem;
      background: #2a2a2a;
      padding: 20px;
      border-radius: 10px;
      display: inline-block;
    }
    .ip {
      color: #00e0ff;
      font-weight: bold;
    }
    .status {
      margin-top: 10px;
      padding: 10px;
      border-radius: 8px;
      display: inline-block;
      font-weight: bold;
      background-color: {{ '#007f00' if status == 'Online' else '#7f0000' }};
      color: white;
    }
    form {
      margin-top: 20px;
    }
    button {
      padding: 10px 20px;
      font-size: 1rem;
      background: #00ff88;
      color: #000;
      border: none;
      border-radius: 5px;
      cursor: pointer;
    }
  </style>
</head>
<body>

  <h1>Welcome to ChopinCraft</h1>

  <div class="server-info">
    <p><strong>Server IP:</strong> <span class="ip">play.chopincraft.net</span></p>
    <p><strong>Port:</strong> 25565</p>
    <p><strong>Version:</strong> Minecraft 1.20.4</p>
    
    <div class="status">
      Server Status: {{ status }}
    </div>

    <form method="post" action="/start">
      <button type="submit">Start Server</button>
    </form>
    <form method="post" action="/stop">
      <button type="submit">Stop Server</button>
    </form>
  </div>

</body>
</html>
