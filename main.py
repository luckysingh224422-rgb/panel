from flask import Flask, render_template_string, request, redirect, url_for, session
import uuid

app = Flask(_name_)
app.secret_key = "supersecret"

# Admin credentials
ADMIN_USER = "Aman"
ADMIN_PASS = "Inxide"

# Approved & Pending storage
approved_ids = set()
pending_ids = set()

# Background image
bg_image = "https://i.ibb.co/wrC4P96k/23740f20818450daec3818412c7fa1e9.jpg"

# ----------------- Approval Page -----------------
approval_page = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Approval System</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta2/css/all.min.css"/>
<style>
body {
  margin: 0;
  font-family: Arial, sans-serif;
  background: url("{{ bg_image }}") no-repeat center center fixed;
  background-size: cover;
  color: #FFFF99;
  text-align: center;
  padding: 20px;
}
.card {
  max-width: 420px;
  margin: 60px auto;
  padding: 20px;
  border-radius: 15px;
  background: rgba(0,0,0,0.7);
  box-shadow: 0 0 25px rgba(255,255,255,0.2);
}
h1 { font-size: 28px; animation: neon 1.5s infinite alternate; color:#FFFF99; }
@keyframes neon { from { text-shadow:0 0 5px #ff00cc;} to{ text-shadow:0 0 20px #00ffff,0 0 30px #ff00cc;} }
.device-box { background:#222; padding:10px; border-radius:8px; margin:15px 0; font-size:14px; word-wrap: break-word; color:#fff; }
.status { margin:15px 0; padding:8px; border-radius:8px; font-weight:bold; color:#fff; }
.approved { background: green; }
.rejected { background: red; }
.btn { margin:10px; padding:12px 22px; font-size:16px; border-radius:25px; border:none; cursor:pointer; font-weight:bold; }
.start { background: white; color: black; }
.admin { background: none; color: #FFFF99; border: 2px solid #ff0077; box-shadow:0 0 10px #ff0077; }
.icons { margin-top:20px; }
.icons a { font-size:22px; margin:0 10px; transition:0.3s; }
.icons a.whatsapp { color:#25D366; }
.icons a.facebook { color:#1877F2; }
.icons a.github { color:#FFFFFF; }
.icons a.youtube { color:#FF0000; }
.icons a:hover.whatsapp { color:#00ff00; text-shadow:0 0 10px #25D366; }
.icons a:hover.facebook { color:#33a2ff; text-shadow:0 0 10px #1877F2; }
.icons a:hover.github { color:#ffffff; text-shadow:0 0 10px #ffffff; }
.icons a:hover.youtube { color:#ff3333; text-shadow:0 0 10px #FF0000; }
.footer { margin-top:25px; font-size:18px; font-weight:bold; text-align:center; color:#fff; }
.footer span { background: linear-gradient(90deg,#ff00cc,#00ffff); -webkit-background-clip:text; -webkit-text-fill-color:transparent; animation: glow 2s infinite alternate; }
@keyframes glow { from{ text-shadow:0 0 5px #ff00cc;} to{ text-shadow:0 0 20px #00ffff,0 0 30px #ff00cc;} }
.copyright { font-size:12px; margin-top:10px; color:#fff; }
</style>
</head>
<body>
<div class="card">
<h1>🔥 AMAN INXIDE APK.0.1 🔥</h1>
<p>Your Device ID:</p>
<div class="device-box">{{ device_id }}</div>

{% if approved %}
  <div class="status approved">✅ Approved</div>
  <button class="btn start" onclick="window.location.href='/main'">🚀 START</button>
{% else %}
  <div class="status rejected">❌ Not Approved</div>
  <button class="btn start" onclick="alert('⏳ Wait for admin approval!')">🚀 START</button>
{% endif %}

<a href="{{ url_for('admin') }}"><button class="btn admin">👤 Admin Panel</button></a>

<div class="icons">
  <a href=".....🤭....." title="Facebook"><i class="fab fa-facebook"></i></a>
      <a href="https://wa.me/+9779829258991" title="WhatsApp"><i class="fab fa-whatsapp"></i></a>
      <a href="...🤭" title="GitHub"><i class="fab fa-github"></i></a>
      <a href=".....🤭..."><i class="fab fa-youtube"></i></a>
</div>

<div class="footer">
<marquee behavior="scroll" direction="left" scrollamount="6">✨ Made by <span>Mr Hassan Dastagir</span> ✨</marquee>
<p class="copyright">©️ 2025 AMAN INXIDE All RIGHTS RESERVED.</p>
</div>
</div>

<!-- SCREENSHOT/SCREEN RECORD DETER SYSTEM -->
<script>
(function(){
    document.addEventListener('contextmenu', e=>e.preventDefault());
    document.addEventListener('keydown', e=>{if(e.key==='PrintScreen'){alert('Screenshot blocked!'); e.preventDefault();}});
    const overlay=document.createElement('div');
    overlay.style.position='fixed';
    overlay.style.top='0';
    overlay.style.left='0';
    overlay.style.width='100%';
    overlay.style.height='100%';
    overlay.style.pointerEvents='none';
    overlay.style.zIndex='999999';
    overlay.style.backgroundColor='rgba(0,0,0,0.01)';
    document.body.appendChild(overlay);
})();
</script>

</body>
</html>
'''

# ----------------- Main Page -----------------
main_page = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>😚❤️ OFFLINE ALL SERVICES BY AMAN INXIDE ❤️😚</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta2/css/all.min.css"/>
<style>
body { font-family:"Poppins",sans-serif; background:url("{{ bg_image }}") no-repeat center center fixed; background-size:cover; color:#fff; padding:20px; text-align:center;}
h2 { animation: neon 1.5s infinite alternate; color:#fff; }
@keyframes neon { from { text-shadow:0 0 5px #ff00cc; } to { text-shadow:0 0 20px #00ffff,0 0 30px #ff00cc; } }
.image-container { width:330px; height:200px; margin:20px auto; box-shadow:0 0 10px rgba(0,0,0,0.5); border-radius:10px; overflow:hidden; }
.image { width:100%; height:100%; object-fit:cover; }
.button-34 { display:block; margin:12px auto; padding:10px 20px; background:black; color:white; border:none; border-radius:999px; font-weight:bold; cursor:pointer; font-size:16px; }
h3 { color:#fff; }
.footer { margin-top:40px; font-size:14px; color:#fff; }
.footer a { color:#fff; margin:0 5px; }
.footer i { margin:0 8px; }
.icons { margin-top:20px; }
.icons a { font-size:22px; margin:0 10px; transition:0.3s; }
.icons a.whatsapp { color:#25D366; }
.icons a.facebook { color:#1877F2; }
.icons a.github { color:#FFFFFF; }
.icons a.youtube { color:#FF0000; }
.icons a:hover.whatsapp { color:#00ff00; text-shadow:0 0 10px #25D366; }
.icons a:hover.facebook { color:#33a2ff; text-shadow:0 0 10px #1877F2; }
.icons a:hover.github { color:#ffffff; text-shadow:0 0 10px #ffffff; }
.icons a:hover.youtube { color:#ff3333; text-shadow:0 0 10px #FF0000; }
</style>
</head>
<body>
<h2>😍𝐀𝐌𝐀𝐍 𝐈𝐍𝐗𝐈𝐃𝐄 𝐎𝐅𝐅𝐋𝐈𝐍𝐄 𝐖𝐄𝐁😍</h2>

<div class="image-container"><img src="https://i.ibb.co/Pz1Mw5dk/photo-1558214000-63bb8c928be5.jpg" class="image"></div>
<h3>⊲ CONTACT OWNER AMAN INXIDE⊳</h3>
<button class="button-34" onclick="window.location.href='https://wa.me/+9779829258991'">⊲ CONTACT OWNER CLICK HERE ⊳</button>

<div class="image-container"><img src="https://i.ibb.co/7J7wySKz/photo-1509479200622-4503f27f12ef.jpg" class="image"></div>
<button class="button-34" onclick="window.location.href='http://fi6.bot-hosting.net:500/'">⊲ OFFLINE NONSTOP SERVER ⊳</button>

<div class="image-container"><img src="https://i.ibb.co/q3jRdxvw/photo-1639805857704-107720c1c6aa.jpg" class="image"></div>
<button class="button-34" onclick="window.location.href='http://fi2.bot-hosting.net:500/'">⊲ TOKEN CHECKER ⊳</button>

<div class="image-container"><img src="https://i.ibb.co/G4jxHZX9/photo-1666615435088-4865bf5ed3fd.jpg" class="image"></div>
<button class="button-34" onclick="window.location.href='http://fi1.bot-hosting.net:500/'">⊲ CONVO FYT GROUP UID ⊳</button>

<div class="image-container"><img src="https://i.ibb.co/fVBKLVHg/images-36.jpg" class="image"></div>
<button class="button-34" onclick="window.location.href='http://104.168.76.139:2709/'">⊲ GROUP NAME LOCK ⊳</button>

<div class="icons">
  <a href=".....🤭....." title="Facebook"><i class="fab fa-facebook"></i></a>
      <a href="https://wa.me/+9779829258991" title="WhatsApp"><i class="fab fa-whatsapp"></i></a>
      <a href="...... 🤭....." title="GitHub"><i class="fab fa-github"></i></a>
      <a href="....🤭...."><i class="fab fa-youtube"></i></a>
  <p>©️ 2025 AMAN INXIDE All RIGHTS RESERVED.</p>
</div>

<div class="footer">
<marquee behavior="scroll" direction="left" scrollamount="6">✨ Made by <span>AMAN INXIDE</span> ✨</marquee>
</div>

<!-- SCREENSHOT/SREEN RECORD DETER SYSTEM -->
<script>
(function(){
    document.addEventListener('contextmenu', e=>e.preventDefault());
    document.addEventListener('keydown', e=>{if(e.key==='PrintScreen'){alert('Screenshot blocked!'); e.preventDefault();}});
    const overlay=document.createElement('div');
    overlay.style.position='fixed';
    overlay.style.top='0';
    overlay.style.left='0';
    overlay.style.width='100%';
    overlay.style.height='100%';
    overlay.style.pointerEvents='none';
    overlay.style.zIndex='999999';
    overlay.style.backgroundColor='rgba(0,0,0,0.01)';
    document.body.appendChild(overlay);
})();
</script>

</body>
</html>
'''

# ----------------- Routes -----------------
@app.route('/')
def approval():
    if "device_id" not in session:
        session["device_id"] = str(uuid.uuid4())
    device_id = session["device_id"]
    if device_id not in approved_ids and device_id not in pending_ids:
        pending_ids.add(device_id)
    approved = device_id in approved_ids
    return render_template_string(approval_page, device_id=device_id, approved=approved, bg_image=bg_image)

@app.route('/main')
def main():
    device_id = session.get('device_id')
    if device_id in approved_ids:
        return render_template_string(main_page, bg_image=bg_image)
    return redirect(url_for('approval'))

# ----------------- Admin -----------------
@app.route('/admin', methods=['GET','POST'])
def admin():
    if request.method == "POST":
        user = request.form.get("username")
        pw = request.form.get("password")
        if user == ADMIN_USER and pw == ADMIN_PASS:
            session['admin'] = True
            return redirect(url_for('dashboard'))
    return '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Admin Login</title>
<style>
body { font-family:Arial,sans-serif; background:url("{{ bg_image }}") no-repeat center center fixed; background-size:cover; color:#fff; text-align:center; padding:50px;}
.card { max-width:400px; margin:auto; background: rgba(0,0,0,0.7); padding:20px; border-radius:15px; box-shadow:0 0 25px rgba(255,255,255,0.2);}
input { width:80%; padding:10px; margin:10px 0; border-radius:10px; border:none;}
button { padding:10px 20px; border:none; border-radius:10px; background:#ff0077; color:#fff; cursor:pointer; font-weight:bold;}
</style>
</head>
<body>
<div class="card">
<h2>Admin Login</h2>
<form method="post">
<input name="username" placeholder="Enter Username"><br>
<input name="password" type="password" placeholder="Enter Password"><br>
<button type="submit">Login</button>
</form>
</div>
</body>
</html>'''

@app.route('/dashboard', methods=['GET','POST'])
def dashboard():
    if not session.get('admin'):
        return redirect(url_for('admin'))
    search_result = ""
    if request.method == "POST":
        search_id = request.form.get("search_id")
        if search_id:
            if search_id in approved_ids:
                search_result = f"<p>✅ Found in Approved List: {search_id} <a href='/remove/{search_id}'><button class='reject'>Remove</button></a></p>"
            elif search_id in pending_ids:
                search_result = f"<p>⏳ Found in Pending List: {search_id} <a href='/approve/{search_id}'><button class='approve'>Approve</button></a> <a href='/reject/{search_id}'><button class='reject'>Reject</button></a></p>"
            else:
                search_result = f"<p>❌ Device ID not found: {search_id}</p>"
    pending_list = "".join([f"<li>{d} <a href='/approve/{d}'><button class='approve'>Approve</button></a> <a href='/reject/{d}'><button class='reject'>Reject</button></a></li>" for d in pending_ids if d not in approved_ids])
    approved_list = "".join([f"<li>{d} <a href='/remove/{d}'><button class='reject'>Remove</button></a></li>" for d in approved_ids])
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Admin Dashboard</title>
<style>
body {{ font-family:Arial,sans-serif; background:url("{bg_image}") no-repeat center center fixed; background-size:cover; color:#fff; text-align:center; padding:20px;}}
button.approve {{ padding:5px 12px; border:none; border-radius:10px; background:green; color:#fff; cursor:pointer; }}
button.reject {{ padding:5px 12px; border:none; border-radius:10px; background:red; color:#fff; cursor:pointer; }}
ul {{ list-style:none; padding:0; }}
li {{ margin:8px 0; }}
input {{ padding:8px; border-radius:8px; border:none; width:250px; }}
button.search {{ padding:8px 12px; border:none; border-radius:8px; background:#ff0077; color:#fff; cursor:pointer; }}
</style>
</head>
<body>
<h2>Admin Dashboard</h2>
<form method="post">
<input name="search_id" placeholder="Enter Device ID to search">
<button class="search" type="submit">Search</button>
</form>
{search_result}
<h3>Pending Devices</h3><ul>{pending_list}</ul>
<h3>Approved Devices</h3><ul>{approved_list}</ul>
</body>
</html>'''

# ----------------- Admin Actions -----------------
@app.route('/approve/<device_id>')
def approve(device_id):
    approved_ids.add(device_id)
    pending_ids.discard(device_id)
    return redirect(url_for('dashboard'))

@app.route('/reject/<device_id>')
def reject(device_id):
    pending_ids.discard(device_id)
    approved_ids.discard(device_id)
    return redirect(url_for('dashboard'))

@app.route('/remove/<device_id>')
def remove(device_id):
    approved_ids.discard(device_id)
    return redirect(url_for('dashboard'))

# ----------------- Run -----------------
if _name=='main_':
    app.run(host='0.0.0.0', port=20460, debug=True)
