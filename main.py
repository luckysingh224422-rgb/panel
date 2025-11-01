from flask import Flask, render_template_string, request, redirect, url_for, session
import uuid

app = Flask(__name__)
app.secret_key = "supersecret"

# New Stylish Background Images
bg_image = "https://images.unsplash.com/photo-1550684848-fac1c5b4e853?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80"
main_bg_image = "https://images.unsplash.com/photo-1451187580459-43490279c0fa?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2072&q=80"

# ----------------- Main Page -----------------
main_page = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>🚀 PREMIUM SERVICES | RAHUL H3R3 INXIDE 🚀</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta2/css/all.min.css"/>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Exo+2:wght@300;400;600&display=swap" rel="stylesheet">
<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Exo 2', sans-serif;
  background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
  background-image: url("''' + main_bg_image + '''");
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
  color: #ffffff;
  min-height: 100vh;
  padding: 20px;
  position: relative;
  overflow-x: hidden;
}

body::before {
  content: '';
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(15, 12, 41, 0.9);
  z-index: -1;
}

.glow-effect {
  position: fixed;
  top: 20%;
  left: 10%;
  width: 300px;
  height: 300px;
  background: radial-gradient(circle, rgba(255, 0, 204, 0.4) 0%, transparent 70%);
  border-radius: 50%;
  filter: blur(40px);
  z-index: -1;
  animation: float 8s ease-in-out infinite;
}

.glow-effect-2 {
  position: fixed;
  bottom: 10%;
  right: 10%;
  width: 400px;
  height: 400px;
  background: radial-gradient(circle, rgba(0, 255, 255, 0.3) 0%, transparent 70%);
  border-radius: 50%;
  filter: blur(50px);
  z-index: -1;
  animation: float 10s ease-in-out infinite reverse;
}

@keyframes float {
  0%, 100% { transform: translateY(0px) rotate(0deg); }
  50% { transform: translateY(-20px) rotate(180deg); }
}

.header {
  text-align: center;
  margin-bottom: 40px;
  padding: 30px 20px;
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(15px);
  border-radius: 20px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
}

h2 {
  font-family: 'Orbitron', sans-serif;
  font-size: 42px;
  font-weight: 900;
  background: linear-gradient(45deg, #ff00cc, #00ffff, #ff00cc);
  background-size: 200% 200%;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  animation: gradientShift 3s ease infinite;
  text-shadow: 0 0 40px rgba(255, 0, 204, 0.5);
  margin-bottom: 10px;
}

@keyframes gradientShift {
  0%, 100% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
}

.subtitle {
  font-size: 18px;
  opacity: 0.8;
  margin-bottom: 20px;
}

.services-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: 25px;
  max-width: 1400px;
  margin: 0 auto;
}

.service-card {
  background: rgba(255, 255, 255, 0.08);
  backdrop-filter: blur(15px);
  border-radius: 20px;
  padding: 25px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 15px 35px rgba(0, 0, 0, 0.3);
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.service-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.1), transparent);
  transition: left 0.6s;
}

.service-card:hover::before {
  left: 100%;
}

.service-card:hover {
  transform: translateY(-10px) scale(1.02);
  box-shadow: 0 25px 50px rgba(0, 0, 0, 0.5);
  border-color: rgba(255, 255, 255, 0.2);
}

.image-container {
  width: 100%;
  height: 200px;
  border-radius: 15px;
  overflow: hidden;
  margin-bottom: 20px;
  position: relative;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
}

.image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.service-card:hover .image {
  transform: scale(1.1);
}

.service-title {
  font-size: 20px;
  font-weight: 700;
  margin-bottom: 15px;
  color: #00ffff;
  text-align: center;
}

.button-34 {
  display: block;
  width: 100%;
  padding: 15px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  border-radius: 50px;
  font-weight: 700;
  font-size: 16px;
  cursor: pointer;
  transition: all 0.3s ease;
  text-transform: uppercase;
  letter-spacing: 1px;
  position: relative;
  overflow: hidden;
}

.button-34::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
  transition: left 0.5s;
}

.button-34:hover::before {
  left: 100%;
}

.button-34:hover {
  transform: translateY(-3px);
  box-shadow: 0 15px 30px rgba(102, 126, 234, 0.4);
  background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
}

.icons {
  margin-top: 50px;
  text-align: center;
  padding: 30px;
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(15px);
  border-radius: 20px;
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.icons-grid {
  display: flex;
  justify-content: center;
  gap: 25px;
  margin-bottom: 20px;
}

.icons a {
  font-size: 28px;
  width: 60px;
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.icons a::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: currentColor;
  opacity: 0.1;
  border-radius: 50%;
}

.icons a.whatsapp { color: #25D366; }
.icons a.facebook { color: #1877F2; }
.icons a.github { color: #FFFFFF; }
.icons a.youtube { color: #FF0000; }

.icons a:hover {
  transform: translateY(-5px) scale(1.1);
  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.4);
}

.icons a:hover.whatsapp { 
  color: #00ff00; 
  box-shadow: 0 15px 30px rgba(37, 211, 102, 0.5);
}
.icons a:hover.facebook { 
  color: #33a2ff; 
  box-shadow: 0 15px 30px rgba(24, 119, 242, 0.5);
}
.icons a:hover.github { 
  color: #ffffff; 
  box-shadow: 0 15px 30px rgba(255, 255, 255, 0.5);
}
.icons a:hover.youtube { 
  color: #ff3333; 
  box-shadow: 0 15px 30px rgba(255, 0, 0, 0.5);
}

.footer {
  margin-top: 40px;
  text-align: center;
  padding: 20px;
}

.footer marquee {
  font-size: 18px;
  font-weight: 700;
  padding: 15px 0;
}

.footer span {
  background: linear-gradient(45deg, #ff00cc, #00ffff);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  text-shadow: 0 0 20px rgba(255, 0, 204, 0.5);
}

.copyright {
  font-size: 14px;
  margin-top: 15px;
  opacity: 0.7;
}

/* Responsive Design */
@media (max-width: 768px) {
  .services-grid {
    grid-template-columns: 1fr;
  }
  
  h2 {
    font-size: 32px;
  }
  
  .header {
    padding: 20px 15px;
  }
}

/* Particle animation */
@keyframes particle {
  0% { transform: translateY(0) rotate(0deg); opacity: 0; }
  10% { opacity: 1; }
  90% { opacity: 1; }
  100% { transform: translateY(-100vh) rotate(360deg); opacity: 0; }
}

.particle {
  position: fixed;
  pointer-events: none;
  width: 4px;
  height: 4px;
  background: #00ffff;
  border-radius: 50%;
  animation: particle 5s linear infinite;
  z-index: -1;
}
</style>
</head>
<body>
<div class="glow-effect"></div>
<div class="glow-effect-2"></div>

<!-- Animated particles -->
<script>
for(let i = 0; i < 50; i++) {
  const particle = document.createElement('div');
  particle.className = 'particle';
  particle.style.left = Math.random() * 100 + 'vw';
  particle.style.animationDelay = Math.random() * 5 + 's';
  particle.style.animationDuration = (3 + Math.random() * 4) + 's';
  document.body.appendChild(particle);
}
</script>

<div class="header">
  <h2>🚀 AAHAN H3R3 PREMIUM SERVICES 🚀</h2>
  <p class="subtitle">Exclusive Access to Premium Tools & Utilities</p>
</div>

<div class="services-grid">
  <div class="service-card">
    <div class="image-container">
      <img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80" class="image" alt="Contact">
    </div>
    <div class="service-title">📞 DIRECT SUPPORT</div>
    <button class="button-34" onclick="window.location.href='https://wa.me/+966570347083'">🔗 CONNECT WITH DEVELOPER</button>
  </div>

  <div class="service-card">
    <div class="image-container">
      <img src="https://images.unsplash.com/photo-1451187580459-43490279c0fa?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80" class="image" alt="Server">
    </div>
    <div class="service-title">⚡ PREMIUM SERVER</div>
    <button class="button-34" onclick="window.location.href='http://server-idlw.onrender.com/login/'">🎯 ACCESS HIGH-SPEED SERVER</button>
  </div>

  <div class="service-card">
    <div class="image-container">
      <img src="https://images.unsplash.com/photo-1635070041078-e363dbe005cb?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80" class="image" alt="Token">
    </div>
    <div class="service-title">🔐 TOKEN VALIDATOR</div>
    <button class="button-34" onclick="window.location.href='http://token-checker-1hfb.onrender.com/'">✅ VERIFY TOKEN SECURITY</button>
  </div>
  
<div class="service-card" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);">
    <div class="image-container">
      <img src="https://images.unsplash.com/photo-1550745165-9bc0b252726f?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80" class="image" alt="UID Checker">
    </div>
    <div class="service-title">🌈 UID MASTER</div>
    <button class="button-34" onclick="window.location.href='https://uid-checker-1-mt1k.onrender.com/'">🎨 GET UID</button>
</div>

  <div class="service-card">
    <div class="image-container">
      <img src="https://images.unsplash.com/photo-1611605698335-8b1569810432?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80" class="image" alt="Group">
    </div>
    <div class="service-title">👥 GROUP MANAGER</div>
    <button class="button-34" onclick="window.location.href='http://fi1.bot-hosting.net:500/'">🛡️ MANAGE GROUP UIDS</button>
  </div>

  <div class="service-card">
    <div class="image-container">
      <img src="https://images.unsplash.com/photo-1563089145-599997674d42?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80" class="image" alt="Security">
    </div>
    <div class="service-title">🔒 SECURITY LOCK</div>
    <button class="button-34" onclick="window.location.href='http://104.168.76.139:2709/'">⚙️ CONFIGURE GROUP LOCKS</button>
  </div>
</div>

<div class="icons">
  <div class="icons-grid">
    <a href="#" title="Facebook" class="facebook"><i class="fab fa-facebook-f"></i></a>
    <a href="https://wa.me/+9779829258991" title="WhatsApp" class="whatsapp"><i class="fab fa-whatsapp"></i></a>
    <a href="#" title="GitHub" class="github"><i class="fab fa-github"></i></a>
    <a href="#" title="YouTube" class="youtube"><i class="fab fa-youtube"></i></a>
  </div>
  <p class="copyright">© 2025 AAHAN H3R3 INXIDE | Advanced Security Systems Active</p>
</div>

<div class="footer">
  <marquee behavior="scroll" direction="left" scrollamount="8">
    ✨ ENGINEERED WITH PRECISION BY <span>AAHAN H3R3</span> | NEXT-GEN SECURITY SOLUTIONS ✨
  </marquee>
</div>

<!-- Enhanced Security Script -->
<script>
(function(){
    // Comprehensive security implementation
    document.addEventListener('contextmenu', e => {
        e.preventDefault();
        showSecurityAlert('🔒 Context menu disabled');
    });
    
    document.addEventListener('keydown', e => {
        const blockedKeys = {
            'PrintScreen': '📸 Screenshot protection active',
            'F12': '🛡️ Developer tools restricted',
            'F11': '🛡️ Fullscreen mode blocked'
        };
        
        const blockedCombinations = [
            { keys: ['Control', 'Shift', 'I'], message: '🛡️ Inspector disabled' },
            { keys: ['Control', 'Shift', 'J'], message: '🛡️ Console disabled' },
            { keys: ['Control', 'Shift', 'C'], message: '🛡️ Element inspector blocked' },
            { keys: ['Control', 'U'], message: '🛡️ Source view restricted' },
            { keys: ['Control', 'S'], message: '💾 Save functionality disabled' }
        ];
        
        if(blockedKeys[e.key]) {
            e.preventDefault();
            showSecurityAlert(blockedKeys[e.key]);
        }
        
        blockedCombinations.forEach(combo => {
            const comboPressed = combo.keys.every(key => 
                e[key.toLowerCase() + 'Key'] || e[key]
            );
            if(comboPressed) {
                e.preventDefault();
                showSecurityAlert(combo.message);
            }
        });
    });
    
    // Protective overlay with dynamic pattern
    const overlay = document.createElement('div');
    overlay.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 999999;
        background: 
            radial-gradient(circle at 20% 80%, rgba(255,0,204,0.02) 0%, transparent 50%),
            radial-gradient(circle at 80% 20%, rgba(0,255,255,0.02) 0%, transparent 50%);
        mix-blend-mode: overlay;
    `;
    document.body.appendChild(overlay);
    
    function showSecurityAlert(message) {
        const alert = document.createElement('div');
        alert.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background: linear-gradient(135deg, #ff00cc, #00ffff);
            color: white;
            padding: 15px 25px;
            border-radius: 15px;
            font-weight: bold;
            z-index: 1000000;
            box-shadow: 0 15px 35px rgba(0,0,0,0.4);
            animation: alertSlideIn 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);
            border: 2px solid rgba(255,255,255,0.3);
            backdrop-filter: blur(10px);
        `;
        alert.textContent = message;
        document.body.appendChild(alert);
        
        setTimeout(() => {
            alert.style.animation = 'alertSlideOut 0.4s ease';
            setTimeout(() => alert.remove(), 400);
        }, 2500);
    }
    
    // Add security animations
    const securityStyle = document.createElement('style');
    securityStyle.textContent = `
        @keyframes alertSlideIn {
            from { 
                transform: translateX(100%) rotate(10deg);
                opacity: 0;
            }
            to { 
                transform: translateX(0) rotate(0);
                opacity: 1;
            }
        }
        @keyframes alertSlideOut {
            from { 
                transform: translateX(0) rotate(0);
                opacity: 1;
            }
            to { 
                transform: translateX(100%) rotate(-10deg);
                opacity: 0;
            }
        }
    `;
    document.head.appendChild(securityStyle);
    
    // Add floating particles
    function createParticle() {
        const particle = document.createElement('div');
        particle.style.cssText = `
            position: fixed;
            pointer-events: none;
            width: ${2 + Math.random() * 3}px;
            height: ${2 + Math.random() * 3}px;
            background: ${Math.random() > 0.5 ? '#ff00cc' : '#00ffff'};
            border-radius: 50%;
            animation: particleFloat ${3 + Math.random() * 4}s linear infinite;
            z-index: -1;
            opacity: ${0.3 + Math.random() * 0.4};
        `;
        particle.style.left = Math.random() * 100 + 'vw';
        particle.style.top = '100vh';
        document.body.appendChild(particle);
        
        setTimeout(() => particle.remove(), 7000);
    }
    
    // Create particles periodically
    setInterval(createParticle, 200);
    
    // Add particle animation
    const particleStyle = document.createElement('style');
    particleStyle.textContent = `
        @keyframes particleFloat {
            0% {
                transform: translateY(100vh) rotate(0deg);
                opacity: 0;
            }
            10% {
                opacity: 1;
            }
            90% {
                opacity: 1;
            }
            100% {
                transform: translateY(-100vh) rotate(360deg);
                opacity: 0;
            }
        }
    `;
    document.head.appendChild(particleStyle);
})();
</script>
</body>
</html>
'''

# ----------------- Routes -----------------
@app.route('/')
def main():
    return render_template_string(main_page, bg_image=main_bg_image)

# ----------------- Run -----------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
