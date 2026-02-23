<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>V8 GOD MODE — SUPREMACIA DIGITAL</title>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Space+Mono:wght@400;700&family=Syne:wght@400;700;800&display=swap" rel="stylesheet">
<style>
  :root {
    --gold: #d4af37;
    --gold-dim: #8a6d1d;
    --gold-glow: rgba(212,175,55,0.3);
    --bg: #050505;
    --surface: #0a0a0a;
    --border: #1a1a1a;
    --text: #e8e8e8;
    --muted: #555;
  }

  * { margin: 0; padding: 0; box-sizing: border-box; }

  body {
    background: var(--bg);
    color: var(--text);
    font-family: 'Space Mono', monospace;
    overflow-x: hidden;
  }

  /* SCANLINE OVERLAY */
  body::before {
    content: '';
    position: fixed; top: 0; left: 0; right: 0; bottom: 0;
    background: repeating-linear-gradient(0deg, transparent, transparent 2px, rgba(0,0,0,0.15) 2px, rgba(0,0,0,0.15) 4px);
    pointer-events: none; z-index: 9999;
  }

  /* HEADER */
  .header {
    text-align: center;
    padding: 60px 20px 40px;
    position: relative;
    border-bottom: 1px solid #1a1a1a;
  }
  .header::after {
    content: '';
    position: absolute; bottom: -1px; left: 50%; transform: translateX(-50%);
    width: 200px; height: 1px;
    background: var(--gold);
    box-shadow: 0 0 20px var(--gold);
  }
  .header h1 {
    font-family: 'Orbitron', sans-serif;
    font-size: clamp(1.8rem, 5vw, 3.5rem);
    font-weight: 900;
    color: var(--gold);
    letter-spacing: 6px;
    text-shadow: 0 0 40px rgba(212,175,55,0.5);
    animation: pulse 3s ease-in-out infinite;
  }
  @keyframes pulse {
    0%, 100% { text-shadow: 0 0 30px rgba(212,175,55,0.4); }
    50% { text-shadow: 0 0 60px rgba(212,175,55,0.8), 0 0 100px rgba(212,175,55,0.3); }
  }
  .header p {
    margin-top: 12px;
    color: var(--muted);
    font-size: 0.75rem;
    letter-spacing: 3px;
    text-transform: uppercase;
  }

  /* NAV TABS */
  .nav-tabs {
    display: flex;
    justify-content: center;
    gap: 4px;
    padding: 30px 20px 0;
    flex-wrap: wrap;
  }
  .tab-btn {
    background: transparent;
    border: 1px solid #222;
    color: #555;
    font-family: 'Orbitron', sans-serif;
    font-size: 0.65rem;
    font-weight: 700;
    letter-spacing: 2px;
    padding: 12px 20px;
    cursor: pointer;
    transition: all 0.3s;
    text-transform: uppercase;
    position: relative;
  }
  .tab-btn:hover, .tab-btn.active {
    border-color: var(--gold);
    color: var(--gold);
    background: rgba(212,175,55,0.05);
    box-shadow: 0 0 20px rgba(212,175,55,0.15), inset 0 0 20px rgba(212,175,55,0.05);
  }
  .tab-btn.active::after {
    content: '';
    position: absolute; bottom: -1px; left: 0; right: 0; height: 2px;
    background: var(--gold);
    box-shadow: 0 0 10px var(--gold);
  }

  /* CONTENT */
  .content {
    max-width: 1300px;
    margin: 0 auto;
    padding: 40px 20px 80px;
  }

  .tab-panel { display: none; animation: fadeIn 0.4s ease; }
  .tab-panel.active { display: block; }
  @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }

  /* SECTION TITLE */
  .section-title {
    font-family: 'Orbitron', sans-serif;
    font-size: 0.7rem;
    letter-spacing: 4px;
    color: var(--gold);
    text-transform: uppercase;
    margin-bottom: 30px;
    display: flex;
    align-items: center;
    gap: 15px;
  }
  .section-title::before, .section-title::after {
    content: ''; flex: 1; height: 1px;
    background: linear-gradient(90deg, transparent, #333);
  }
  .section-title::before { background: linear-gradient(90deg, #333, transparent); }

  /* RESOURCE GRID */
  .resource-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 2px;
    margin-bottom: 50px;
  }

  .resource-card {
    background: var(--surface);
    border: 1px solid #111;
    padding: 28px;
    position: relative;
    overflow: hidden;
    transition: all 0.3s;
    cursor: pointer;
  }
  .resource-card::before {
    content: '';
    position: absolute; top: 0; left: 0; right: 0; height: 2px;
    background: linear-gradient(90deg, transparent, var(--gold), transparent);
    opacity: 0;
    transition: opacity 0.3s;
  }
  .resource-card:hover {
    border-color: #2a2a2a;
    background: #0d0d0d;
    transform: translateY(-2px);
  }
  .resource-card:hover::before { opacity: 1; }

  .card-tag {
    font-size: 0.6rem;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: var(--gold-dim);
    margin-bottom: 10px;
    font-family: 'Orbitron', sans-serif;
  }
  .card-name {
    font-family: 'Syne', sans-serif;
    font-size: 1.1rem;
    font-weight: 800;
    color: #fff;
    margin-bottom: 8px;
  }
  .card-desc {
    font-size: 0.75rem;
    color: #666;
    line-height: 1.6;
    margin-bottom: 16px;
  }
  .card-link {
    display: inline-block;
    font-size: 0.65rem;
    letter-spacing: 2px;
    color: var(--gold);
    text-decoration: none;
    border: 1px solid var(--gold-dim);
    padding: 6px 14px;
    font-family: 'Orbitron', sans-serif;
    transition: all 0.3s;
    text-transform: uppercase;
  }
  .card-link:hover {
    background: var(--gold);
    color: #000;
    box-shadow: 0 0 20px var(--gold-glow);
  }
  .badge {
    position: absolute; top: 14px; right: 14px;
    font-size: 0.55rem;
    letter-spacing: 1px;
    padding: 3px 8px;
    border-radius: 2px;
    font-family: 'Orbitron', sans-serif;
    text-transform: uppercase;
    font-weight: 700;
  }
  .badge-free { background: #003a1a; color: #00ff88; border: 1px solid #00ff88; }
  .badge-pdf { background: #1a0a00; color: #ff6b00; border: 1px solid #ff6b00; }
  .badge-video { background: #0a001a; color: #a855f7; border: 1px solid #a855f7; }
  .badge-ai { background: #001a1a; color: #00d4ff; border: 1px solid #00d4ff; }

  /* HIGHLIGHT BOX */
  .highlight-box {
    border: 1px solid #222;
    border-left: 3px solid var(--gold);
    background: linear-gradient(135deg, #0a0800, #050505);
    padding: 24px 28px;
    margin-bottom: 40px;
    font-size: 0.8rem;
    color: #888;
    line-height: 1.8;
  }
  .highlight-box strong { color: var(--gold); }

  /* GENERATOR SECTION */
  .gen-form {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 20px;
    margin-bottom: 30px;
  }
  .field-group { display: flex; flex-direction: column; gap: 8px; }
  .field-label {
    font-size: 0.6rem;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: var(--gold-dim);
    font-family: 'Orbitron', sans-serif;
  }
  .field-input {
    background: #0a0a0a;
    border: 1px solid #1a1a1a;
    border-radius: 0;
    color: #fff;
    font-family: 'Space Mono', monospace;
    font-size: 0.8rem;
    padding: 12px 16px;
    transition: all 0.3s;
    outline: none;
    width: 100%;
  }
  .field-input:focus {
    border-color: var(--gold);
    box-shadow: 0 0 15px rgba(212,175,55,0.1);
  }
  .gen-btn {
    background: linear-gradient(135deg, #8a6d1d, #d4af37);
    border: none;
    color: #000;
    font-family: 'Orbitron', sans-serif;
    font-weight: 900;
    font-size: 0.75rem;
    letter-spacing: 3px;
    padding: 18px 40px;
    cursor: pointer;
    text-transform: uppercase;
    transition: all 0.3s;
    display: block;
    width: 100%;
    margin-top: 10px;
  }
  .gen-btn:hover {
    box-shadow: 0 0 50px rgba(212,175,55,0.4);
    transform: translateY(-1px);
  }
  .output-block {
    background: #050505;
    border: 1px solid #1a1a1a;
    border-left: 2px solid var(--gold);
    padding: 30px;
    margin-top: 30px;
    display: none;
  }
  .output-block.visible { display: block; animation: fadeIn 0.5s ease; }
  .post-card {
    background: #0a0a0a;
    border: 1px solid #111;
    border-top: 3px solid var(--gold);
    padding: 24px;
    margin-bottom: 16px;
  }
  .post-title {
    font-family: 'Orbitron', sans-serif;
    font-size: 0.65rem;
    letter-spacing: 3px;
    color: var(--gold);
    margin-bottom: 14px;
  }
  .post-text { font-size: 0.8rem; color: #aaa; line-height: 1.8; }
  .post-tip { font-size: 0.7rem; color: #555; margin-top: 12px; font-style: italic; }

  /* COPY BUTTON */
  .copy-btn {
    background: transparent;
    border: 1px solid #222;
    color: #555;
    font-family: 'Space Mono', monospace;
    font-size: 0.65rem;
    padding: 6px 14px;
    cursor: pointer;
    margin-top: 10px;
    transition: all 0.3s;
  }
  .copy-btn:hover { border-color: var(--gold); color: var(--gold); }

  /* FOOTER */
  .footer {
    text-align: center;
    padding: 40px 20px;
    border-top: 1px solid #111;
    font-size: 0.6rem;
    letter-spacing: 3px;
    color: #333;
    font-family: 'Orbitron', sans-serif;
  }

  /* SCROLLBAR */
  ::-webkit-scrollbar { width: 4px; }
  ::-webkit-scrollbar-track { background: #000; }
  ::-webkit-scrollbar-thumb { background: var(--gold-dim); }

  .divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, #222, transparent);
    margin: 40px 0;
  }
</style>
</head>
<body>

<div class="header">
  <h1>🔱 V8 GOD MODE</h1>
  <p>Supremacia Digital — Material Premium Curado</p>
</div>

<div class="nav-tabs">
  <button class="tab-btn active" onclick="switchTab('recursos')">📚 Arsenal Premium</button>
  <button class="tab-btn" onclick="switchTab('ias')">🤖 IAs Gratuitas</button>
  <button class="tab-btn" onclick="switchTab('video')">🎬 Criação de Vídeo</button>
  <button class="tab-btn" onclick="switchTab('gerador')">⚡ Gerador de Posts</button>
  <button class="tab-btn" onclick="switchTab('curriculo')">🏆 Currículo Elite</button>
</div>

<div class="content">

  <!-- TAB: RECURSOS -->
  <div id="tab-recursos" class="tab-panel active">
    <div class="highlight-box">
      <strong>📌 CURADORIA PREMIUM:</strong> Todos os recursos abaixo são verificados, gratuitos ou freemium, e representam o que há de mais avançado em design visual, branding e criação de conteúdo para posicionamento de alta autoridade.
    </div>

    <div class="section-title">PDFs & Guias de Design Visual</div>
    <div class="resource-grid">

      <div class="resource-card">
        <span class="badge badge-pdf">PDF GRÁTIS</span>
        <div class="card-tag">Design Thinking</div>
        <div class="card-name">Interaction Design Foundation</div>
        <div class="card-desc">Biblioteca com +100 cursos e guias PDF sobre UX, branding e design visual. O maior acervo de design do mundo, parcialmente gratuito.</div>
        <a class="card-link" href="https://www.interaction-design.org/literature" target="_blank">▶ Acessar</a>
      </div>

      <div class="resource-card">
        <span class="badge badge-pdf">PDF GRÁTIS</span>
        <div class="card-tag">Tipografia & Layout</div>
        <div class="card-name">Google Fonts Knowledge</div>
        <div class="card-desc">Guia completo de tipografia: como escolher fontes, hierarquia visual, pares de fontes para branding de alto valor. Conteúdo de nível profissional.</div>
        <a class="card-link" href="https://fonts.google.com/knowledge" target="_blank">▶ Acessar</a>
      </div>

      <div class="resource-card">
        <span class="badge badge-pdf">PDF GRÁTIS</span>
        <div class="card-tag">Branding</div>
        <div class="card-name">Canva Design School</div>
        <div class="card-desc">Guias gratuitos de design para redes sociais, criação de identidade visual, paletas de cores e composição. Ideal para criadores de conteúdo.</div>
        <a class="card-link" href="https://www.canva.com/learn/design" target="_blank">▶ Acessar</a>
      </div>

      <div class="resource-card">
        <span class="badge badge-pdf">ACERVO GRÁTIS</span>
        <div class="card-tag">Visual & Cores</div>
        <div class="card-name">Adobe Color</div>
        <div class="card-desc">Ferramenta gratuita de teoria de cores da Adobe. Gere paletas harmônicas, extraia cores de imagens e crie identidade visual consistente.</div>
        <a class="card-link" href="https://color.adobe.com" target="_blank">▶ Acessar</a>
      </div>

      <div class="resource-card">
        <span class="badge badge-pdf">PDF GRÁTIS</span>
        <div class="card-tag">Design Avançado</div>
        <div class="card-name">Smashing Magazine</div>
        <div class="card-desc">Publicação técnica de design com artigos aprofundados, e-books e guias sobre fotografia, edição de imagem e design para conteúdo digital.</div>
        <a class="card-link" href="https://www.smashingmagazine.com/articles" target="_blank">▶ Acessar</a>
      </div>

      <div class="resource-card">
        <span class="badge badge-pdf">GRÁTIS</span>
        <div class="card-tag">Composição Visual</div>
        <div class="card-name">Unsplash & Pexels Editorial</div>
        <div class="card-desc">Bancos de imagens de altíssima qualidade com guias de composição fotográfica. Imagens gratuitas para uso comercial e educação visual.</div>
        <a class="card-link" href="https://unsplash.com/learn" target="_blank">▶ Unsplash</a>
      </div>

    </div>

    <div class="section-title">Canais YouTube Premium — Design & Branding</div>
    <div class="resource-grid">

      <div class="resource-card">
        <span class="badge badge-video">YOUTUBE</span>
        <div class="card-tag">Identidade Visual</div>
        <div class="card-name">The Futur</div>
        <div class="card-desc">Canal de Chris Do — maior referência em branding e precificação de design. Conteúdo de nível MBA sobre posicionamento e identidade de marca pessoal.</div>
        <a class="card-link" href="https://www.youtube.com/@thefutur" target="_blank">▶ Assistir</a>
      </div>

      <div class="resource-card">
        <span class="badge badge-video">YOUTUBE</span>
        <div class="card-tag">Design & Motion</div>
        <div class="card-name">Flux Academy</div>
        <div class="card-desc">Ran Segall ensina web design, composição visual e estratégia de posicionamento para profissionais e criadores de conteúdo premium.</div>
        <a class="card-link" href="https://www.youtube.com/@FluxAcademy" target="_blank">▶ Assistir</a>
      </div>

      <div class="resource-card">
        <span class="badge badge-video">YOUTUBE</span>
        <div class="card-tag">Fotografia & Vídeo</div>
        <div class="card-name">Peter McKinnon</div>
        <div class="card-desc">Referência mundial em criação de conteúdo visual, fotografia e edição de vídeo. Técnicas profissionais ensinadas de forma acessível.</div>
        <a class="card-link" href="https://www.youtube.com/@PeterMcKinnon" target="_blank">▶ Assistir</a>
      </div>

      <div class="resource-card">
        <span class="badge badge-video">YOUTUBE</span>
        <div class="card-tag">Edição & Produção</div>
        <div class="card-name">Justin Odisho</div>
        <div class="card-desc">Tutoriais de Premiere Pro, After Effects e Photoshop. Foco em efeitos cinematográficos e tratamento de imagem para conteúdo de alto padrão.</div>
        <a class="card-link" href="https://www.youtube.com/@JustinOdisho" target="_blank">▶ Assistir</a>
      </div>

      <div class="resource-card">
        <span class="badge badge-video">YOUTUBE PT-BR</span>
        <div class="card-tag">Design Brasil</div>
        <div class="card-name">Irmãos Coragem</div>
        <div class="card-desc">Um dos melhores canais brasileiros de design e identidade visual. Conteúdo prático sobre branding, tipografia e criação para redes sociais.</div>
        <a class="card-link" href="https://www.youtube.com/@IrmaosCoragem" target="_blank">▶ Assistir</a>
      </div>

      <div class="resource-card">
        <span class="badge badge-video">YOUTUBE PT-BR</span>
        <div class="card-tag">Canva Pro Tips</div>
        <div class="card-name">Canva Brasil Oficial</div>
        <div class="card-desc">Tutoriais oficiais em português para dominar Canva em alto nível — templates premium, animações, Brand Kit e criação de conteúdo profissional.</div>
        <a class="card-link" href="https://www.youtube.com/@CanvaBrasil" target="_blank">▶ Assistir</a>
      </div>

    </div>
  </div>

  <!-- TAB: IAs GRATUITAS -->
  <div id="tab-ias" class="tab-panel">
    <div class="highlight-box">
      <strong>🤖 ARSENAL DE INTELIGÊNCIA ARTIFICIAL GRATUITA:</strong> As ferramentas abaixo são as mais avançadas do mercado com planos gratuitos reais. Especial destaque para IAs que <strong>dão vida a objetos inanimados</strong> com animação generativa.
    </div>

    <div class="section-title">🌟 IAs que Animam Objetos Inanimados (Top Prioridade)</div>
    <div class="resource-grid">

      <div class="resource-card">
        <span class="badge badge-ai">GRÁTIS</span>
        <div class="card-tag">Animação de Imagem</div>
        <div class="card-name">Kling AI</div>
        <div class="card-desc">IA da Kuaishou que transforma qualquer imagem em vídeo animado. Dá vida a fotos paradas, produtos e retratos com movimentos realistas. Plano gratuito com créditos diários.</div>
        <a class="card-link" href="https://klingai.com" target="_blank">▶ Usar Grátis</a>
      </div>

      <div class="resource-card">
        <span class="badge badge-ai">FREEMIUM</span>
        <div class="card-tag">Animação de Imagem</div>
        <div class="card-name">Runway ML (Gen-3)</div>
        <div class="card-desc">Plataforma líder em IA de vídeo. Anima objetos inanimados, transforma imagens em vídeos cinemáticos e aplica efeitos de IA em tempo real. 125 créditos grátis.</div>
        <a class="card-link" href="https://runwayml.com" target="_blank">▶ Usar Grátis</a>
      </div>

      <div class="resource-card">
        <span class="badge badge-ai">GRÁTIS</span>
        <div class="card-tag">Imagem para Vídeo</div>
        <div class="card-name">Luma AI (Dream Machine)</div>
        <div class="card-desc">Gera vídeos a partir de imagens ou texto com qualidade cinematográfica. Ótimo para dar movimento a logos, produtos e personagens. Versão gratuita disponível.</div>
        <a class="card-link" href="https://lumalabs.ai/dream-machine" target="_blank">▶ Usar Grátis</a>
      </div>

      <div class="resource-card">
        <span class="badge badge-ai">GRÁTIS</span>
        <div class="card-tag">Animação de Personagem</div>
        <div class="card-name">D-ID</div>
        <div class="card-desc">Especialista em animar rostos em fotos paradas. Crie avatares que falam, animações de retratos e vídeos de apresentação com IA. Trial gratuito robusto.</div>
        <a class="card-link" href="https://www.d-id.com" target="_blank">▶ Usar Grátis</a>
      </div>

      <div class="resource-card">
        <span class="badge badge-ai">GRÁTIS</span>
        <div class="card-tag">Motion IA</div>
        <div class="card-name">Hailuo AI (MiniMax)</div>
        <div class="card-desc">IA chinesa que anima imagens com movimentos fluidos e naturais. Excelente para dar vida a produtos, cenários e elementos de marca. Créditos gratuitos diários.</div>
        <a class="card-link" href="https://hailuoai.video" target="_blank">▶ Usar Grátis</a>
      </div>

      <div class="resource-card">
        <span class="badge badge-ai">GRÁTIS</span>
        <div class="card-tag">Imagem Animada</div>
        <div class="card-name">Pika Labs</div>
        <div class="card-desc">Transforme qualquer imagem ou descrição em vídeo animado. Ideal para conteúdo de redes sociais, reels e animações de branding pessoal.</div>
        <a class="card-link" href="https://pika.art" target="_blank">▶ Usar Grátis</a>
      </div>

    </div>

    <div class="section-title">🎨 IAs de Criação de Imagem (Gratuitas)</div>
    <div class="resource-grid">

      <div class="resource-card">
        <span class="badge badge-ai">100% GRÁTIS</span>
        <div class="card-tag">Geração de Imagem</div>
        <div class="card-name">Adobe Firefly</div>
        <div class="card-desc">IA da Adobe para criação de imagens. Sem problemas de copyright, ideal para uso comercial. Recursos de expandir imagem, remover fundos e retoques avançados.</div>
        <a class="card-link" href="https://firefly.adobe.com" target="_blank">▶ Usar Grátis</a>
      </div>

      <div class="resource-card">
        <span class="badge badge-ai">GRÁTIS</span>
        <div class="card-tag">Criação de Imagem</div>
        <div class="card-name">Leonardo AI</div>
        <div class="card-desc">150 tokens gratuitos por dia para criação de imagens profissionais. Excelente para criar elementos visuais de marca, texturas e composições de alta qualidade.</div>
        <a class="card-link" href="https://leonardo.ai" target="_blank">▶ Usar Grátis</a>
      </div>

      <div class="resource-card">
        <span class="badge badge-ai">GRÁTIS</span>
        <div class="card-tag">Remoção de Fundo</div>
        <div class="card-name">Remove.bg</div>
        <div class="card-desc">Remove fundo de qualquer imagem em segundos com IA. Essencial para criação de thumbnails, posts e identidade visual profissional.</div>
        <a class="card-link" href="https://www.remove.bg" target="_blank">▶ Usar Grátis</a>
      </div>

      <div class="resource-card">
        <span class="badge badge-ai">GRÁTIS</span>
        <div class="card-tag">Upscale IA</div>
        <div class="card-name">Upscayl</div>
        <div class="card-desc">Aumenta resolução de imagens com IA sem perder qualidade. Open source e gratuito. Ideal para ampliar fotos para uso profissional em alta resolução.</div>
        <a class="card-link" href="https://upscayl.org" target="_blank">▶ Baixar Grátis</a>
      </div>

      <div class="resource-card">
        <span class="badge badge-ai">GRÁTIS</span>
        <div class="card-tag">Design IA</div>
        <div class="card-name">Ideogram AI</div>
        <div class="card-desc">Especialista em gerar imagens com texto integrado de alta qualidade — thumbnails, logos, capas e materiais de branding com tipografia gerada por IA.</div>
        <a class="card-link" href="https://ideogram.ai" target="_blank">▶ Usar Grátis</a>
      </div>

      <div class="resource-card">
        <span class="badge badge-ai">GRÁTIS</span>
        <div class="card-tag">Retoque IA</div>
        <div class="card-name">Luminar Neo (Trial)</div>
        <div class="card-desc">Editor de foto com IA avançada: troca de fundos automática, retoque de pele, relight de foto e edição de céu. Trial gratuito de 30 dias.</div>
        <a class="card-link" href="https://skylum.com/luminar-neo" target="_blank">▶ Testar Grátis</a>
      </div>

    </div>
  </div>

  <!-- TAB: VÍDEO -->
  <div id="tab-video" class="tab-panel">
    <div class="highlight-box">
      <strong>🎬 ARSENAL DE CRIAÇÃO DE VÍDEO:</strong> Ferramentas e recursos para produção de conteúdo audiovisual de alto impacto, desde edição básica até produção cinematográfica com IA.
    </div>

    <div class="section-title">Editores de Vídeo Gratuitos (Nível Profissional)</div>
    <div class="resource-grid">

      <div class="resource-card">
        <span class="badge badge-free">100% GRÁTIS</span>
        <div class="card-tag">Edição Profissional</div>
        <div class="card-name">DaVinci Resolve</div>
        <div class="card-desc">O editor de vídeo mais poderoso do mercado — gratuito para sempre. Usado em Hollywood. Color grading profissional, fusão, áudio Fairlight. Nenhuma limitação real.</div>
        <a class="card-link" href="https://www.blackmagicdesign.com/products/davinciresolve" target="_blank">▶ Baixar Grátis</a>
      </div>

      <div class="resource-card">
        <span class="badge badge-free">GRÁTIS</span>
        <div class="card-tag">Edição Online</div>
        <div class="card-name">CapCut (Desktop + App)</div>
        <div class="card-desc">Editor gratuito com recursos de IA: remoção de fundo, legendas automáticas, templates virais e efeitos de tendência. Perfeito para Reels, TikTok e YouTube Shorts.</div>
        <a class="card-link" href="https://www.capcut.com" target="_blank">▶ Usar Grátis</a>
      </div>

      <div class="resource-card">
        <span class="badge badge-ai">FREEMIUM</span>
        <div class="card-tag">Vídeo com IA</div>
        <div class="card-name">Descript</div>
        <div class="card-desc">Edite vídeo como se fosse um documento de texto. IA que remove "éhs" e pausas, cria clones de voz e gera captions automáticas. Referência em podcast e vídeos de autoridade.</div>
        <a class="card-link" href="https://www.descript.com" target="_blank">▶ Testar Grátis</a>
      </div>

      <div class="resource-card">
        <span class="badge badge-ai">FREEMIUM</span>
        <div class="card-tag">Vídeo IA</div>
        <div class="card-name">InVideo AI</div>
        <div class="card-desc">Cria vídeos completos a partir de texto com IA. Ideal para conteúdo de autoridade, apresentações e vídeos de oferta. Templates profissionais e narração por IA.</div>
        <a class="card-link" href="https://invideo.io" target="_blank">▶ Usar Grátis</a>
      </div>

      <div class="resource-card">
        <span class="badge badge-free">GRÁTIS</span>
        <div class="card-tag">Motion Graphics</div>
        <div class="card-name">Canva (Animações)</div>
        <div class="card-desc">Crie vídeos, animações e apresentações animadas diretamente no browser. Biblioteca de templates para Reels, Stories e vídeos de autoridade. Plano gratuito robusto.</div>
        <a class="card-link" href="https://www.canva.com/video-editor" target="_blank">▶ Usar Grátis</a>
      </div>

      <div class="resource-card">
        <span class="badge badge-ai">FREEMIUM</span>
        <div class="card-tag">Avatar IA</div>
        <div class="card-name">HeyGen</div>
        <div class="card-desc">Crie vídeos com avatares de IA que falam por você. Clone sua voz, gere apresentações com IA e crie conteúdo em múltiplos idiomas sem aparecer na câmera.</div>
        <a class="card-link" href="https://www.heygen.com" target="_blank">▶ Testar Grátis</a>
      </div>

    </div>

    <div class="section-title">Recursos de Áudio & Música para Vídeo</div>
    <div class="resource-grid">

      <div class="resource-card">
        <span class="badge badge-free">GRÁTIS</span>
        <div class="card-tag">Música Livre</div>
        <div class="card-name">YouTube Audio Library</div>
        <div class="card-desc">Biblioteca oficial do YouTube com milhares de músicas e efeitos sonoros totalmente gratuitos para uso comercial. Indispensável para criadores de conteúdo.</div>
        <a class="card-link" href="https://studio.youtube.com/channel/music" target="_blank">▶ Acessar</a>
      </div>

      <div class="resource-card">
        <span class="badge badge-ai">FREEMIUM</span>
        <div class="card-tag">Música com IA</div>
        <div class="card-name">Suno AI</div>
        <div class="card-desc">Crie trilhas sonoras originais com IA a partir de uma descrição. Gere jingles, músicas de abertura e trilhas personalizadas para seus vídeos e marca.</div>
        <a class="card-link" href="https://suno.com" target="_blank">▶ Usar Grátis</a>
      </div>

      <div class="resource-card">
        <span class="badge badge-ai">GRÁTIS</span>
        <div class="card-tag">Narração IA</div>
        <div class="card-name">ElevenLabs (Free)</div>
        <div class="card-desc">As vozes de IA mais realistas do mercado. Clone sua voz ou use vozes premium para narração de vídeos, podcasts e conteúdo de autoridade. 10.000 chars/mês grátis.</div>
        <a class="card-link" href="https://elevenlabs.io" target="_blank">▶ Usar Grátis</a>
      </div>

    </div>
  </div>

  <!-- TAB: GERADOR DE POSTS -->
  <div id="tab-gerador" class="tab-panel">
    <div class="highlight-box">
      <strong>⚡ PROTOCOLO SUPREMACIA — GERADOR DE POSTS:</strong> Preencha seus dados e gere os 3 posts fixados do seu perfil de autoridade máxima.
    </div>

    <div class="gen-form">
      <div class="field-group">
        <label class="field-label">💎 Seu Nome</label>
        <input class="field-input" id="nome" placeholder="Ex: Cássia Kelly" value="Cássia Kelly">
      </div>
      <div class="field-group">
        <label class="field-label">🎯 Seu Nicho / Domínio</label>
        <input class="field-input" id="nicho" placeholder="Ex: Estrategista de Elite">
      </div>
      <div class="field-group">
        <label class="field-label">🔥 Sua Metodologia / Método</label>
        <input class="field-input" id="poder" placeholder="Ex: Protocolo V8">
      </div>
      <div class="field-group">
        <label class="field-label">📢 Sua Grande Promessa</label>
        <input class="field-input" id="promessa" placeholder="Ex: Escala High-Ticket em 30 dias">
      </div>
      <div class="field-group">
        <label class="field-label">🚀 Seu Público-Alvo</label>
        <input class="field-input" id="target" placeholder="Ex: Empresários e Mentores">
      </div>
      <div class="field-group">
        <label class="field-label">🧨 Maior Dor do Público</label>
        <input class="field-input" id="dor" placeholder="Ex: Falta de autoridade visual">
      </div>
    </div>

    <button class="gen-btn" onclick="gerarPosts()">🔥 ATIVAR PROTOCOLO SUPREMACIA</button>

    <div id="output" class="output-block">
      <div style="font-family:'Orbitron',sans-serif; font-size:0.7rem; letter-spacing:3px; color:var(--gold); margin-bottom:25px;">📌 A TRINDADE DO FEED — POSTS FIXADOS</div>
      <div id="post1" class="post-card"></div>
      <div id="post2" class="post-card"></div>
      <div id="post3" class="post-card"></div>

      <div class="divider"></div>
      <div style="font-family:'Orbitron',sans-serif; font-size:0.7rem; letter-spacing:3px; color:var(--gold); margin-bottom:20px;">🌐 BIOS MULTI-PLATAFORMA</div>
      <div id="bios" class="post-card"></div>
    </div>
  </div>

  <!-- TAB: CURRÍCULO -->
  <div id="tab-curriculo" class="tab-panel">
    <div class="highlight-box">
      <strong>🏆 CURRÍCULO ELITE V8:</strong> Preencha os campos na aba "Gerador de Posts" e clique em ativar para gerar seu dossiê completo, ou preencha abaixo para gerar apenas o currículo.
    </div>

    <div class="gen-form">
      <div class="field-group">
        <label class="field-label">💎 Seu Nome</label>
        <input class="field-input" id="cv-nome" placeholder="Ex: Cássia Kelly">
      </div>
      <div class="field-group">
        <label class="field-label">🎯 Nicho</label>
        <input class="field-input" id="cv-nicho" placeholder="Ex: Estrategista de Elite">
      </div>
      <div class="field-group">
        <label class="field-label">🔥 Metodologia</label>
        <input class="field-input" id="cv-poder" placeholder="Ex: Protocolo V8">
      </div>
      <div class="field-group">
        <label class="field-label">📢 Promessa</label>
        <input class="field-input" id="cv-promessa" placeholder="Ex: Escala High-Ticket em 30 dias">
      </div>
      <div class="field-group">
        <label class="field-label">🚀 Público-Alvo</label>
        <input class="field-input" id="cv-target" placeholder="Ex: Empresários e Mentores">
      </div>
      <div class="field-group">
        <label class="field-label">🧨 Dor do Público</label>
        <input class="field-input" id="cv-dor" placeholder="Ex: Falta de autoridade visual">
      </div>
    </div>

    <button class="gen-btn" onclick="gerarCV()">🏆 GERAR CURRÍCULO ELITE</button>

    <div id="cv-output" class="output-block">
      <div style="font-family:'Orbitron',sans-serif; font-size:0.7rem; letter-spacing:3px; color:var(--gold); margin-bottom:20px;">📄 CURRICULUM VITAE V8 — ELITE EDITION</div>
      <pre id="cv-text" style="font-family:'Space Mono',monospace; font-size:0.75rem; color:#aaa; line-height:1.8; white-space:pre-wrap; background:#050505; padding:24px; border:1px solid #111;"></pre>
      <button class="copy-btn" onclick="copiarCV()">📋 COPIAR CURRÍCULO</button>
    </div>
  </div>

</div>

<div class="footer">
  🔱 V8 GOD MODE — SUPREMACIA DIGITAL &nbsp;|&nbsp; MATERIAL PREMIUM CURADO &nbsp;|&nbsp; 2025
</div>

<script>
  function switchTab(name) {
    document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
    document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
    document.getElementById('tab-' + name).classList.add('active');
    event.target.classList.add('active');
  }

  function gerarPosts() {
    const nome = document.getElementById('nome').value || 'Você';
    const nicho = document.getElementById('nicho').value || 'seu nicho';
    const poder = document.getElementById('poder').value || 'seu método';
    const promessa = document.getElementById('promessa').value || 'resultados extraordinários';
    const target = document.getElementById('target').value || 'seu público';
    const dor = document.getElementById('dor').value || 'seu maior problema';

    document.getElementById('post1').innerHTML = `
      <div class="post-title">POST 01 — O MANIFESTO (QUEM SOU EU)</div>
      <div class="post-text">Eu não cheguei aqui por sorte. No mercado de ${nicho}, muitos jogam o jogo — mas poucos dominam as regras. Meu nome é ${nome} e sou a mente por trás do ${poder}. Minha missão é tirar ${target} da invisibilidade e colocá-los no topo. Se você está aqui, é porque cansou de ser esquecido. Seja bem-vindo ao nível seguinte. 🔱</div>
      <div class="post-tip">📸 Visual: Foto profissional em ambiente de poder (escritório, estúdio, ou local de autoridade). Luz dramática, fundo dark.</div>
      <button class="copy-btn" onclick="copiar(this)">📋 Copiar Legenda</button>`;

    document.getElementById('post2').innerHTML = `
      <div class="post-title">POST 02 — O MECANISMO (COMO O ${poder.toUpperCase()} FUNCIONA)</div>
      <div class="post-text">Por que ${promessa} parece impossível para você? Porque você ainda não conhece o ${poder}. Este não é mais um método. É uma engenharia testada. → Fase 1: Scanner de Status (onde você está vs. onde deveria estar) → Fase 2: Blindagem de Autoridade (construção de percepção de elite) → Fase 3: Ativação de Escala (conversão e crescimento) Sem atalhos. Com sistema. 📊</div>
      <div class="post-tip">📸 Visual: Carrossel técnico com gráficos minimalistas, fundo preto e dourado. Cada slide = uma fase do método.</div>
      <button class="copy-btn" onclick="copiar(this)">📋 Copiar Legenda</button>`;

    document.getElementById('post3').innerHTML = `
      <div class="post-title">POST 03 — A PROVA (DOMÍNIO DE MERCADO)</div>
      <div class="post-text">Resultados falam mais alto que promessas. Quando apliquei o ${poder} para resolver ${dor} de ${target}, o resultado foi inevitável. Não foi sorte. Foi sistema. Não foi inspiração. Foi execução. Hoje ${target} que usam o ${poder} estão experimentando ${promessa} — e você pode ser o próximo. Qual é o seu próximo movimento? 🎯</div>
      <div class="post-tip">📸 Visual: Print de resultado, depoimento com foto, ou sua imagem em palco/evento de autoridade. Adicione texto em overlay dourado.</div>
      <button class="copy-btn" onclick="copiar(this)">📋 Copiar Legenda</button>`;

    document.getElementById('bios').innerHTML = `
      <div class="post-title">BIOS MULTI-PLATAFORMA</div>
      <div class="post-text">
      <strong style="color:var(--gold)">INSTAGRAM/TIKTOK:</strong><br>
      ${nicho} | Criador(a) do ${poder} 🔱<br>
      Especialista em: ${promessa}<br>
      Para: ${target}<br>
      ↓ Acesse o protocolo gratuito<br><br>
      <strong style="color:var(--gold)">LINKEDIN (TÍTULO):</strong><br>
      Especialista em ${poder} | ${nicho} | Gerando ${promessa} para ${target}<br><br>
      <strong style="color:var(--gold)">WHATSAPP BIO:</strong><br>
      ${nicho} | ${poder} 🔱 | ${promessa}
      </div>
      <button class="copy-btn" onclick="copiar(this)">📋 Copiar Bios</button>`;

    document.getElementById('output').classList.add('visible');
    document.getElementById('output').scrollIntoView({ behavior: 'smooth', block: 'start' });
  }

  function gerarCV() {
    const nome = document.getElementById('cv-nome').value || 'OPERADOR';
    const nicho = document.getElementById('cv-nicho').value || 'Estrategista';
    const poder = document.getElementById('cv-poder').value || 'Protocolo V8';
    const promessa = document.getElementById('cv-promessa').value || 'Resultados Extraordinários';
    const target = document.getElementById('cv-target').value || 'Empresários';
    const dor = document.getElementById('cv-dor').value || 'Invisibilidade Digital';

    const cv = `━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  OPERADOR: ${nome.toUpperCase()}
  STATUS: ESPECIALISTA ELITE | NICHO: ${nicho.toUpperCase()}
  METODOLOGIA: ${poder.toUpperCase()}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RESUMO EXECUTIVO:
Estrategista de alta performance focado em ${nicho}.
Especialista em converter "${dor}" em autoridade inabalável
para ${target}. Criador(a) do sistema ${poder}, com foco
em entregar: ${promessa}.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
COMPETÊNCIAS CHAVE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ◆ Blindagem de Perfil Omnichannel
  ◆ Engenharia de Conteúdo de Conversão
  ◆ Posicionamento Visual High-Ticket
  ◆ Autoridade Digital e Gestão de Reputação
  ◆ Estratégia de Escala para ${target}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROJETOS E RESULTADOS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ◆ Criação e implementação do ${poder}
  ◆ Consultoria Estratégica para ${target}
  ◆ Resolução da dor crítica: "${dor}"
  ◆ Entrega comprovada de: ${promessa}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CONTATO ESTRATÉGICO:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  [INSIRA SEU LINK/WHATSAPP/CALENDLY AQUI]
  
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  V8 GOD MODE — SUPREMACIA DIGITAL 🔱
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━`;

    document.getElementById('cv-text').textContent = cv;
    document.getElementById('cv-output').classList.add('visible');
    document.getElementById('cv-output').scrollIntoView({ behavior: 'smooth', block: 'start' });
  }

  function copiar(btn) {
    const text = btn.previousElementSibling.innerText;
    navigator.clipboard.writeText(text).then(() => {
      btn.textContent = '✅ Copiado!';
      setTimeout(() => btn.textContent = '📋 Copiar', 2000);
    });
  }

  function copiarCV() {
    const text = document.getElementById('cv-text').textContent;
    navigator.clipboard.writeText(text).then(() => {
      const btn = event.target;
      btn.textContent = '✅ Currículo Copiado!';
      setTimeout(() => btn.textContent = '📋 COPIAR CURRÍCULO', 2000);
    });
  }
</script>
</body>
</html>
