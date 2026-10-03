import re

content = '''<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Pyradrink</title>

<!-- iOS Home Screen -->
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="Pyradrink">

<!-- Android / PWA -->
<link rel="manifest" href="manifest.json">
<meta name="theme-color" content="#0b1d3a">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Baloo+2:wght@500;600;700;800&family=Titan+One&display=swap" rel="stylesheet">
<style>
:root{
  --bg1:#0c3d2e; --bg2:#0a2e23; --panel:#fbf3e3; --panel-line:#d8c9a3;
  --ink:#20291f; --muted:#6b6152; --accent:#e2445c; --accent-ink:#7a1626;
  --success:#3ba776; --danger:#e2445c; --gold:#e0a63e; --gold-ink:#7a4e12;
  --navy:#1c2c52; --navy-ink:#101a33;
  --card-bg:#fffdf7; --card-text:#20291f;
  --neon-pink:#ff2d78; --neon-blue:#00e5ff; --neon-gold:#ffd700; --neon-purple:#bc13fe;
  box-sizing:border-box;
  padding-top:env(safe-area-inset-top,0px);
  padding-bottom:env(safe-area-inset-bottom,0px);
}
html{scroll-padding-top:env(safe-area-inset-top,0px); height:100%; background:#0b1d3a;}
*{box-sizing:border-box;}
body{
  margin:0; height:100%; color:#fdf6e3;
  font-family:'Baloo 2',-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
  display:flex; flex-direction:column; overflow-x:hidden; position:relative;
  background:#0b1d3a;
}

/* ── BAR ROOM HOME SCENE ── */
.home-bg-scene {
  position: fixed; inset: 0; z-index: 0; pointer-events: none;
  background: url('assets/media__1790988025283.jpg') center center / cover no-repeat;
  transition: transform 1.2s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.8s ease;
  transform-origin: 50% 75%;
}
body.zoom-to-table .home-bg-scene {
  transform: scale(3.8) translateY(-15%);
  opacity: 0;
}

/* ── TOP-DOWN TABLE GAME SCENE ── */
.table-bg-scene {
  position: fixed; inset: 0; z-index: 0; pointer-events: none;
  background: url('assets/media__1790988031694.png') center center / cover no-repeat;
  opacity: 0; transition: opacity 0.8s ease;
}
body.in-table-view .table-bg-scene {
  opacity: 1;
}

/* ── LAMP FLICKER LIGHT CONE ── */
.lamp-glow {
  position: fixed; top: 0; left: 50%; transform: translateX(-50%);
  width: 500px; height: 500px; border-radius: 50%;
  background: radial-gradient(circle at 50% 20%, rgba(255,230,130,0.45) 0%, rgba(255,170,40,0.18) 45%, transparent 70%);
  animation: lampFlicker 2.2s infinite alternate ease-in-out;
  pointer-events: none; z-index: 1;
}
@keyframes lampFlicker {
  0%, 100% { opacity: 0.85; transform: translateX(-50%) scale(1); }
  20% { opacity: 0.6; transform: translateX(-50%) scale(0.96); }
  45% { opacity: 0.95; transform: translateX(-50%) scale(1.04); }
  70% { opacity: 0.7; transform: translateX(-50%) scale(0.98); }
}

/* 2 BUZZING FLIES */
.fly {
  position: fixed; width: 6px; height: 6px; background: #111; border-radius: 50%;
  box-shadow: 0 0 4px rgba(255,255,255,0.8); pointer-events: none; z-index: 10;
}
.fly-1 { top: 22%; left: 47%; animation: flyBuzz1 3.2s infinite ease-in-out; }
.fly-2 { top: 25%; left: 53%; animation: flyBuzz2 4.1s infinite ease-in-out; }
@keyframes flyBuzz1 {
  0% { transform: translate(0, 0); }
  25% { transform: translate(30px, -20px); }
  50% { transform: translate(-35px, 25px); }
  75% { transform: translate(20px, 40px); }
  100% { transform: translate(0, 0); }
}
@keyframes flyBuzz2 {
  0% { transform: translate(0, 0); }
  25% { transform: translate(-40px, 30px); }
  50% { transform: translate(45px, -25px); }
  75% { transform: translate(-20px, -35px); }
  100% { transform: translate(0, 0); }
}

/* ── RETRO RIBBON BUTTONS ── */
.btn-banner-red {
  background: linear-gradient(180deg, #ff415c 0%, #d81b36 60%, #9e0c21 100%);
  color: #fff9e6; text-shadow: 0 2px 4px rgba(0,0,0,0.6);
  border: 3.5px solid #ffe885; border-radius: 999px;
  font-family: 'Titan One', cursive; text-transform: uppercase;
  box-shadow: 0 6px 0 #5c0512, 0 10px 20px rgba(0,0,0,0.5), inset 0 2px 0 rgba(255,255,255,0.4);
  padding: 16px 46px; font-size: 24px; letter-spacing: 2px;
  cursor: pointer; position: relative; transition: all 0.15s ease; touch-action: manipulation;
}
.btn-banner-red:hover {
  transform: translateY(-2px);
  filter: brightness(1.1);
  box-shadow: 0 8px 0 #5c0512, 0 14px 25px rgba(255,215,0,0.5);
}
.btn-banner-red:active {
  transform: translateY(4px);
  box-shadow: 0 2px 0 #5c0512, 0 4px 10px rgba(0,0,0,0.4);
}

.btn-banner-teal {
  background: linear-gradient(180deg, #2fd8d8 0%, #15a5a5 60%, #0a6666 100%);
  color: #ffffff; text-shadow: 0 2px 4px rgba(0,0,0,0.6);
  border: 3.5px solid #a8ffff; border-radius: 999px;
  font-family: 'Titan One', cursive; text-transform: uppercase;
  box-shadow: 0 6px 0 #043d3d, 0 10px 20px rgba(0,0,0,0.5), inset 0 2px 0 rgba(255,255,255,0.4);
  padding: 12px 28px; font-size: 16px; letter-spacing: 1px;
  cursor: pointer; position: relative; transition: all 0.15s ease; touch-action: manipulation;
}

/* ── BALATRO GLOBAL NEON BACKGROUND GRID ── */
.scanlines{position:fixed; inset:0; z-index:200; pointer-events:none;
  background:repeating-linear-gradient(0deg, rgba(0,0,0,0) 0px, rgba(0,0,0,0) 2px, rgba(0,0,0,.08) 2px, rgba(0,0,0,.08) 4px);
  animation:scanMove 8s linear infinite;}
@keyframes scanMove{from{background-position:0 0;} to{background-position:0 100%;}}
.vignette{position:fixed; inset:0; z-index:199; pointer-events:none;
  background:radial-gradient(ellipse at center, transparent 55%, rgba(0,0,0,.55) 100%);}

#app{position:relative; z-index:2; flex:1; display:flex; flex-direction:column; min-height:100%; padding:16px; gap:16px; transition:opacity .4s ease;}
h1,h2,h3,.name{font-family:'Titan One','Baloo 2',inherit;}

/* Screen shake */
@keyframes screenShake{0%,100%{transform:none;} 15%{transform:translate(-4px,-3px) rotate(-.4deg);} 30%{transform:translate(4px,2px) rotate(.3deg);} 45%{transform:translate(-3px,4px) rotate(-.2deg);} 60%{transform:translate(3px,-2px) rotate(.4deg);} 75%{transform:translate(-2px,1px) rotate(-.1deg);} 90%{transform:translate(1px,-1px);}}
body.shake #app{animation:screenShake .45s cubic-bezier(.36,.07,.19,.97)!important;}

.subtitle,.name{text-shadow:0 2px 5px rgba(0,0,0,.65);}
.top-bar{display:flex; justify-content:space-between; align-items:center; gap:8px; flex-wrap:wrap;}
.top-bar .name{color:#fdf6e3; font-size:20px; letter-spacing:.5px; text-shadow:0 2px 0 rgba(0,0,0,.25);}

.hero-title{
  position:relative; display:inline-flex; align-items:center; background:linear-gradient(180deg,#f8d47c,var(--gold) 55%,#c98a25); color:var(--navy-ink);
  border:4px solid var(--navy-ink); font-family:'Titan One',cursive;
  border-radius:999px; padding:16px 40px; font-size:clamp(34px,11vw,56px); letter-spacing:1px;
  text-shadow:0 2px 0 rgba(255,255,255,.55), 0 -1px 0 rgba(0,0,0,.2);
  box-shadow:inset 0 -6px 0 rgba(0,0,0,.12), inset 0 0 0 4px rgba(255,255,255,.28), 0 4px 0 #a9761f, 0 9px 0 var(--navy-ink), 0 16px 22px rgba(0,0,0,.45);
  transform:rotate(-3deg); animation:heroFloat 3.2s ease-in-out infinite;
}
.title-pyramid{width:.62em; height:.56em; margin:0 -.01em; vertical-align:middle; flex-shrink:0;}
@keyframes heroFloat{0%,100%{transform:rotate(-3deg) translateY(0);} 50%{transform:rotate(2deg) translateY(-8px);}}

.btn{
  background:linear-gradient(180deg,#fffdf7,var(--panel)); color:var(--ink); border:3px solid var(--ink);
  padding:12px 22px; border-radius:999px; font-size:15px; font-family:'Titan One','Baloo 2',inherit; letter-spacing:.5px;
  cursor:pointer; touch-action:manipulation; box-shadow:0 5px 0 rgba(0,0,0,.4); transition:transform .12s, box-shadow .12s, filter .15s;
  position:relative; overflow:hidden;
}
.btn.primary{
  background:linear-gradient(180deg,#ef5b72,var(--accent)); color:#fff8ee; border-color:var(--accent-ink);
  box-shadow:0 5px 0 var(--accent-ink), 0 0 18px rgba(226,68,92,.45);
}
.btn.bluff{background:linear-gradient(180deg,#f0bb5c,var(--gold)); color:var(--navy-ink); border-color:var(--gold-ink); box-shadow:0 5px 0 var(--gold-ink), 0 0 14px rgba(224,166,62,.4);}
.btn.ghost{background:transparent; border-color:transparent; color:#fdf6e3; box-shadow:none;}
.btn:disabled{opacity:.4; cursor:default; box-shadow:none; animation:none;}

input[type=text]{
  flex:1; padding:12px 16px; border-radius:999px; border:2.5px solid var(--ink);
  background:var(--panel); color:var(--ink); font-size:16px; font-family:'Baloo 2',inherit;
}
.player-list{display:flex; flex-wrap:wrap; gap:8px;}
.player-chip{
  background:var(--panel); border:2px solid var(--ink); border-radius:20px; padding:6px 12px 6px 14px; font-size:14px; font-weight:600;
  display:inline-flex; gap:8px; align-items:center; color:var(--ink);
}
.player-chip span[data-action]{color:var(--accent-ink); cursor:pointer; font-weight:800;}
.center-flex{flex:1; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:18px; text-align:center; width:100%;}
input[type=range]{
  width:100%; max-width:320px; height:12px; accent-color:var(--gold); cursor:pointer;
}

/* ── DYNAMIC FREE PYRAMID ON TABLE (NO GREEN BOX) ── */
.pyramid-stage{position:relative; width:100%; display:flex; justify-content:center; padding-bottom:12px;}
.pyramid-free{display:flex; flex-direction:column; align-items:center; gap:6px; max-width:100%; overflow-x:auto; padding:10px;}
.pyramid-row{display:flex; gap:6px; justify-content:center;}
.card, .card-back{
  width:32px; height:46px; border-radius:6px; display:flex; align-items:center; justify-content:center;
  border:2px solid var(--ink); flex-shrink:0; box-shadow: 0 4px 8px rgba(0,0,0,0.5);
}
.card-back{background:repeating-linear-gradient(135deg, var(--navy) 0 6px, var(--navy-ink) 6px 12px); border-color:var(--navy-ink);}
.card{background:var(--card-bg); color:var(--card-text); flex-direction:column; font-size:11px; font-weight:800; gap:1px;}
.card.red{color:var(--accent-ink);}

/* ── OVERLAY CARD LIFT UP & TRANSPARENCY ── */
.card-overlay-wrap{
  position:fixed; inset:0; z-index:150; display:flex; flex-direction:column; align-items:center; justify-content:center;
  background:rgba(0,0,0,0.55); backdrop-filter:blur(6px); transition:all 0.3s ease;
}
.card-overlay-wrap.transparent-view{
  background:rgba(0,0,0,0.18); backdrop-filter:none;
}
.card-overlay-wrap.transparent-view .flip-card{
  opacity:0.35; filter:none;
}

.flip-card{width:140px; height:200px; perspective:900px; filter:drop-shadow(0 0 25px rgba(255,215,0,0.8)); animation:liftUp 0.45s cubic-bezier(.2,.9,.3,1.15);}
@keyframes liftUp{from{transform:translateY(80px) scale(0.3); opacity:0;} to{transform:none; opacity:1;}}
.flip-inner{position:relative; width:100%; height:100%; transform-style:preserve-3d; transition:transform .5s cubic-bezier(.25,.8,.3,1);}
.flip-inner.flipped{transform:rotateY(180deg);}
.flip-face{position:absolute; inset:0; backface-visibility:hidden; border-radius:12px; border:2px solid var(--ink);}
.flip-face.flip-front{transform:rotateY(180deg); background:var(--card-bg); display:block; padding:0;}
.flip-face.flip-back{background:repeating-linear-gradient(135deg, var(--navy) 0 6px, var(--navy-ink) 6px 12px); border-color:var(--navy-ink);}

/* CUL SEC BANNER */
.cul-sec-banner{
  position:fixed; top:12%; left:50%; transform:translateX(-50%);
  background:linear-gradient(180deg, #ff2d55, #c80028);
  color:#fff; font-family:'Titan One', cursive; font-size:32px; letter-spacing:2px;
  padding:12px 36px; border-radius:999px; border:4px solid #ffd700;
  box-shadow:0 0 35px rgba(255,45,85,0.9), 0 6px 0 #600010;
  animation:pulseCulSec 0.9s infinite alternate ease-in-out; z-index:160; text-align:center;
}
@keyframes pulseCulSec{0%{transform:translateX(-50%) scale(1);} 100%{transform:translateX(-50%) scale(1.15);}}

.fab-next{position:fixed; right:16px; bottom:calc(16px + env(safe-area-inset-bottom,0px)); z-index:40;}
.screen-pad-fab{padding-bottom:74px;}
.pack-grid{display:flex; flex-wrap:wrap; gap:16px; justify-content:center;}
.pack{display:flex; cursor:pointer; animation:packWiggle 2.6s ease-in-out infinite; filter:drop-shadow(0 4px 12px rgba(0,0,0,.5)); transition:filter .2s;}
.pack:hover{filter:drop-shadow(0 6px 20px rgba(255,215,0,.6));}
.pack .card-back{width:38px; height:56px; margin-left:-16px;}
.pack .card-back:first-child{margin-left:0;}

.hand-row{display:flex; gap:10px; justify-content:center; flex-wrap:wrap;}
.hand-card{width:58px; height:84px; font-size:16px; cursor:pointer; touch-action:none;}
.wide-hand .hand-card{height:auto; aspect-ratio:5/7; max-width:170px;}

.hand-card.dragging-source{opacity:.25; transform:scale(.92)!important;}
.hand-card.drag-over{transform:translateY(-14px) scale(1.08)!important; filter:drop-shadow(0 0 18px var(--neon-gold)); z-index:5;}
.card-drag-ghost{position:fixed; pointer-events:none; z-index:10000; transition:none; filter:drop-shadow(0 18px 28px rgba(0,0,0,.7)); cursor:grabbing;}

.glass{width:100%; max-width:440px; display:flex; flex-direction:column; align-items:center; gap:12px; padding:16px 16px 14px; border-radius:24px; background:linear-gradient(180deg,rgba(10,22,48,.66),rgba(6,14,30,.52)); border:1.5px solid rgba(255,255,255,.16); box-shadow:0 12px 30px rgba(0,0,0,.45); backdrop-filter:blur(8px);}
.name-bar{display:flex; align-items:center; gap:8px; width:100%; max-width:420px; background:linear-gradient(#fffdf7,#f3e7cc); border:3px solid var(--ink); border-radius:999px; padding:6px 6px 6px 18px;}
.name-bar input[type=text]{border:none; background:transparent; font-size:18px; outline:none; color:var(--ink);}

.particle{position:fixed; pointer-events:none; z-index:9999; border-radius:50%; animation:particleFly .7s ease-out forwards;}
@keyframes particleFly{0%{transform:translate(0,0) scale(1); opacity:1;} 100%{transform:translate(var(--px),var(--py)) scale(0); opacity:0;}}

/* Responsive */
@media (min-width: 600px) {
  #app { max-width: 640px; margin-left: auto; margin-right: auto; padding: 28px 24px; }
  .card, .card-back { width: 44px; height: 62px; font-size: 13px; }
  .flip-card { width: 170px; height: 245px; }
  .hand-card { width: 72px; height: 104px; }
}
</style>
</head>
<body>

<div class="home-bg-scene" aria-hidden="true"></div>
<div class="table-bg-scene" aria-hidden="true"></div>
<div class="lamp-glow" aria-hidden="true"></div>
<div class="fly fly-1" aria-hidden="true"></div>
<div class="fly fly-2" aria-hidden="true"></div>

<div class="vignette" aria-hidden="true"></div>
<div class="scanlines" aria-hidden="true"></div>

<div id="app"></div>

<script>
let S = {
  screen: 'home',
  players: [],
  rows: 5,
  dealQueue: [],
  currentDealer: null,
  packs: [],
  hands: {},
  pyramidRows: [],
  flatOrder: [],
  revealPos: -1,
  overlayCard: null,
  bluffTarget: null,
  bluffFlash: null,
  bluffResult: null,
  bluffAwaitingChoice: false,
  swapPick: null,
  justSettled: null,
  showPyramidOverlay: false
};

function freshState(){
  return {
    screen: 'home', players: [], rows: 5, dealQueue: [], currentDealer: null,
    packs: [], hands: {}, pyramidRows: [], flatOrder: [], revealPos: -1,
    overlayCard: null, bluffTarget: null, bluffFlash: null, bluffResult: null,
    bluffAwaitingChoice: false, swapPick: null, justSettled: null, showPyramidOverlay: false
  };
}

function escapeHtml(str){ return str.replace(/[&<>"']/g, m=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[m])); }
function rankLabel(r){ return r==='V'?'Valet':(r==='D'?'Dame':(r==='R'?'Roi':(r==='A'?'As':r))); }

function buildDeck(){
  const suits=['♠','♥','♦','♣'], ranks=['2','3','4','5','6','7','8','9','10','V','D','R','A'];
  const deck=[];
  for(let s of suits) for(let r of ranks) deck.push({suit:s, rank:r, red:s==='♥'||s==='♦'});
  for(let i=deck.length-1; i>0; i--){ const j=Math.floor(Math.random()*(i+1)); [deck[i],deck[j]]=[deck[j],deck[i]]; }
  return deck;
}

function initDealing(){
  S.dealQueue = [...S.players];
  S.currentDealer = S.dealQueue[0];
  S.packs = Array.from({length: S.players.length}, () => ({ cards: [], taken: false }));
  const deck = buildDeck();
  S.packs.forEach(p => { p.cards = deck.splice(0, 4); });
}

function buildPyramid(){
  const total = (S.rows * (S.rows + 1)) / 2;
  const deck = buildDeck();
  const cards = deck.slice(0, total);
  S.pyramidRows = [];
  S.flatOrder = [];
  let idx = 0;
  for(let r=1; r<=S.rows; r++){
    const row = [];
    for(let c=0; c<r; c++){
      const card = { ...cards[idx], faceUp: false };
      row.push(card);
      idx++;
    }
    S.pyramidRows.push(row);
  }
  for(let r=S.rows-1; r>=0; r--){
    for(let c=0; c<=r; c++){
      S.flatOrder.push({ ri: r, ci: c });
    }
  }
  S.revealPos = -1;
  S.overlayCard = null;
}

function nextCard(){
  S.justSettled = null;
  if(S.revealPos >= 0){
    const cur = S.flatOrder[S.revealPos];
    S.pyramidRows[cur.ri][cur.ci].faceUp = true;
    S.justSettled = cur.ri + '-' + cur.ci;
  }
  S.revealPos++;
  if(S.revealPos >= S.flatOrder.length){ S.screen = 'end'; S.overlayCard = null; return; }
  const nxt = S.flatOrder[S.revealPos];
  S.overlayCard = S.pyramidRows[nxt.ri][nxt.ci];
}

const SUIT_INFO={'♠':{id:'p-S',c:'#1b2230'},'♣':{id:'p-C',c:'#1b2230'},'♥':{id:'p-H',c:'#c8283e'},'♦':{id:'p-D',c:'#c8283e'}};
const SIX=[[32,32],[68,32],[32,70],[68,70],[32,108],[68,108]];
const PIPS={'A':[[50,70]],'2':[[50,32],[50,108]],'3':[[50,32],[50,70],[50,108]],'4':[[32,32],[68,32],[32,108],[68,108]],
 '5':[[32,32],[68,32],[32,108],[68,108],[50,70]],'6':SIX,'7':SIX.concat([[50,51]]),'8':SIX.concat([[50,51],[50,89]]),
 '9':[[32,32],[68,32],[32,57],[68,57],[32,83],[68,83],[32,108],[68,108],[50,70]],
 '10':[[32,32],[68,32],[32,56],[68,56],[32,84],[68,84],[32,108],[68,108],[50,44],[50,96]]};
const CF='Titan One, Baloo 2, sans-serif';

function cardFaceSVG(c){
  const si=SUIT_INFO[c.suit];
  const pip=(x,y,k)=>`<use href="#${si.id}" transform="translate(${x} ${y})${y>70?' rotate(180)':''} scale(${k})"/>`;
  let body='';
  if('VDR'.includes(c.rank)){
    body=`<rect x="20" y="20" width="60" height="100" rx="3" fill="#f6ecd0" stroke="currentColor" stroke-width="1.2"/>${pip(50,70,1.2)}`;
  } else if(c.rank==='A'){ body=pip(50,70,2.6); }
  else { const k=c.rank==='10'?.7:.82; body=PIPS[c.rank].map(([x,y])=>pip(x,y,k)).join(''); }
  const idx=`<text x="12" y="23" text-anchor="middle" font-size="${c.rank==='10'?15:19}" font-weight="800" fill="currentColor" font-family="${CF}">${c.rank}</text><use href="#${si.id}" transform="translate(12 35) scale(.5)"/>`;
  return `<svg class="cface" viewBox="0 0 100 140" fill="currentColor" style="color:${si.c}"><rect x="1.5" y="1.5" width="97" height="137" rx="9" fill="#fffdf7" stroke="#20291f" stroke-width="3"/>${body}${idx}<g transform="rotate(180 50 70)">${idx}</g></svg>`;
}
function cardMiniSVG(c){
  const si=SUIT_INFO[c.suit];
  return `<svg class="cface" viewBox="0 0 100 140" fill="currentColor" style="color:${si.c}"><rect x="2" y="2" width="96" height="136" rx="10" fill="#fffdf7" stroke="#20291f" stroke-width="4"/><text x="50" y="68" text-anchor="middle" font-size="${c.rank==='10'?56:66}" font-weight="800" fill="currentColor" font-family="${CF}">${c.rank}</text><use href="#${si.id}" transform="translate(50 103) scale(1.5)"/></svg>`;
}

const appEl=document.getElementById('app');

function renderHome(){
  return `
  <div class="center-flex" style="justify-content:space-between; padding:40px 0;">
    <div class="title-wrap" style="text-align:center; margin-top:20px;">
      <span class="hero-title">PYRADRINK</span>
    </div>
    <div style="position:fixed; bottom:40px; left:50%; transform:translateX(-50%); z-index:30;">
      <button class="btn-banner-red" data-action="startGameZoom">JOUER</button>
    </div>
  </div>`;
}

function renderPlayersBlock(){
  const n=S.players.length, full=n>=12;
  const chips=S.players.map((p,i)=>`<span class="player-chip">${escapeHtml(p)}<span data-action="removePlayer" data-idx="${i}">✕</span></span>`).join('');
  const hint = n<2 ? `Encore ${2-n} joueur${2-n>1?'s':''} minimum` : (full?'Table complète !':'Prêt à jouer !');
  return `<div class="glass">
    <div class="subtitle" style="font-size:20px;">JOUEURS (${n}/12)</div>
    <div class="player-list">${chips}</div>
    <div class="name-bar">
      <input type="text" id="nameInput" placeholder="${full?'Table complète':'Écris un pseudo…'}" maxlength="16" autocomplete="off" ${full?'disabled':''}>
      <button class="btn primary" data-action="addPlayer" ${full?'disabled':''}>+</button>
    </div>
    <div class="name-hint" id="nameHint">${hint}</div>
  </div>`;
}

function renderSetup(){
  const canNext=S.players.length>=2;
  return `
  <div class="top-bar"><div class="name">Inscription des joueurs</div></div>
  <div class="center-flex screen-pad-fab">${renderPlayersBlock()}</div>
  <button class="btn-banner-red fab-next" data-action="toStep2" ${canNext?'':'disabled'}>SUIVANT</button>`;
}

function renderPreviewPyramid(rows){
  let out='<div class="pyramid-free">';
  for(let i=1; i<=rows; i++){
    out += `<div class="pyramid-row">${'<div class="card-back" style="width:20px;height:28px;"></div>'.repeat(i)}</div>`;
  }
  return out+'</div>';
}

function renderPyramidSize(){
  const totalCards = (S.rows * (S.rows + 1)) / 2;
  return `
  <div class="top-bar">
    <button class="btn ghost" data-action="back">←</button>
    <div class="name">Taille de la pyramide</div>
    <div style="width:44px;"></div>
  </div>
  <div class="center-flex screen-pad-fab">
    ${renderPreviewPyramid(S.rows)}
    <div style="margin:16px 0; width:100%; display:flex; flex-direction:column; align-items:center; gap:8px;">
      <input type="range" min="2" max="12" value="${S.rows}" data-action="sliderRows" id="pyramidSlider">
      <div class="subtitle" style="font-size:22px; color:#ffd700;">${S.rows} rangées (${totalCards} cartes)</div>
    </div>
  </div>
  <button class="btn-banner-red fab-next" data-action="toDealing">DISTRIBUER</button>`;
}

function renderDealing(){
  if(S.packs.length===0) initDealing();
  const packsHtml=S.packs.map((p,i)=> p.taken?'':`<div class="pack" data-action="choosePack" data-idx="${i}">${'<div class="card-back"></div>'.repeat(4)}</div>`).join('');
  return `
  <div class="top-bar"><div class="name">${escapeHtml(S.currentDealer)}, choisis ton jeu de cartes</div></div>
  <div class="center-flex"><div class="pack-grid">${packsHtml}</div></div>`;
}

function renderDealReveal(){
  const hand=S.hands[S.currentDealer];
  const cardsHtml=hand.map((c,i)=>`<div class="card face hand-card ${S.swapPick===i?'selected':''}" data-action="pickSwap" data-idx="${i}">${cardFaceSVG(c)}</div>`).join('');
  return `<div class="center-flex screen-pad-fab">
    <div class="subtitle">Vos cartes (Glissez-déposez pour réorganiser)</div>
    <div class="hand-row wide-hand">${cardsHtml}</div>
  </div>
  <button class="btn-banner-red fab-next" data-action="validateHand">VALIDER</button>`;
}

function renderGame(){
  const rowsHtml=S.pyramidRows.map((row,ri)=>{
    const cardsHtml=row.map((c,ci)=>{
      const active=S.overlayCard && S.flatOrder[S.revealPos] && S.flatOrder[S.revealPos].ri===ri && S.flatOrder[S.revealPos].ci===ci;
      if(active) return '<div class="card-slot" style="width:32px;height:46px;border:2px dashed #00e5ff;"></div>';
      if(c.faceUp){
        return `<div class="card face">${cardMiniSVG(c)}</div>`;
      }
      return '<div class="card-back"></div>';
    }).join('');
    return `<div class="pyramid-row">${cardsHtml}</div>`;
  }).join('');

  const rowNum = S.overlayCard ? (S.rows - S.flatOrder[S.revealPos].ri) : '';
  const isCulSec = S.revealPos === S.flatOrder.length - 1;

  const transparentCls = S.showPyramidOverlay ? ' transparent-view' : '';

  const overlayHtml = S.overlayCard ? `<div class="card-overlay-wrap${transparentCls}">
    ${isCulSec ? '<div class="cul-sec-banner">🔥 CUL SEC ! 🔥</div>' : ''}
    <div class="flip-card">
      <div class="flip-inner flipped">
        <div class="flip-face flip-front">${cardFaceSVG(S.overlayCard)}</div>
      </div>
    </div>
  </div>` : '';

  return `
  <div class="top-bar">
    <div class="name">Pyradrink</div>
    <button class="btn-banner-teal" data-action="togglePyramidOverlay" style="padding:6px 14px; font-size:14px;">👁 Pyramide</button>
  </div>
  <div class="center-flex">
    <div class="pyramid-stage">
      <div class="pyramid-free">${rowsHtml}</div>
      ${overlayHtml}
    </div>
    ${!S.overlayCard? '<div class="subtitle">Appuie sur SUIVANT pour révéler la première carte</div>' : ''}
  </div>
  <div style="display:flex; justify-content:space-between; align-items:center; gap:12px; margin-top:auto;">
    <button class="btn row-indicator" disabled style="min-width:44px; font-weight:800;">${rowNum}</button>
    <button class="btn-banner-red" data-action="nextCard">SUIVANT</button>
    <button class="btn bluff" data-action="startBluff" ${S.overlayCard? '':'disabled'}>BLUFF</button>
  </div>`;
}

function renderBluffPick(){
  const list=S.players.map(p=>`<button class="btn-banner-teal" data-action="pickBluffTarget" data-name="${escapeHtml(p)}">${escapeHtml(p)}</button>`).join('');
  return `<div class="center-flex"><div class="subtitle" style="font-size:22px;">Qui est désigné bluffeur ?</div><div style="display:flex; flex-direction:column; gap:10px;">${list}</div></div>`;
}

function renderBluffSearch(){
  const hand=S.hands[S.bluffTarget];
  const cardsHtml=hand.map((c,i)=>{
    if(S.bluffFlash && S.bluffFlash.idx===i){
      const cls=S.bluffFlash.ok?'flash-green':'flash-red';
      return `<div class="card face hand-card ${cls}">${cardFaceSVG(c)}</div>`;
    }
    return `<div class="card-back hand-card" data-action="${S.bluffAwaitingChoice?'':'guessCard'}" data-idx="${i}"></div>`;
  }).join('');
  const title = S.bluffAwaitingChoice
    ? (S.bluffResult && S.bluffResult.ok ? 'Trouvé ! Il boit.' : 'Perdu ! Il boit double.')
    : (S.overlayCard? `Où est ${rankLabel(S.overlayCard.rank)} ?` : '');
  const buttons = S.bluffAwaitingChoice? `<button class="btn-banner-red" data-action="bluffNext">SUIVANT</button>` : '';
  return `<div class="center-flex">
    <div class="subtitle" style="font-size:20px;">${title}</div>
    <div class="hand-row wide-hand">${cardsHtml}</div>
    ${buttons}
  </div>`;
}

function renderEnd(){
  return `<div class="center-flex" style="gap:24px;">
    <div class="subtitle" style="font-size:32px; color:#ffd700;">🔥 PYRAMIDE TERMINÉE ! 🔥</div>
    <div style="display:flex; gap:16px;">
      <button class="btn-banner-teal" data-action="terminer">QUITTER</button>
      <button class="btn-banner-red" data-action="confirmReplay">REJOUER</button>
    </div>
  </div>`;
}

function render(){
  const map={
    home: renderHome,
    setup: renderSetup,
    pyramidSize: renderPyramidSize,
    dealing: renderDealing,
    dealReveal: renderDealReveal,
    game: renderGame,
    bluffPick: renderBluffPick,
    bluffSearch: renderBluffSearch,
    end: renderEnd
  };

  appEl.innerHTML = map[S.screen] ? map[S.screen]() : renderHome();
  document.body.dataset.screen = S.screen;

  if(S.screen === 'home'){
    document.body.classList.remove('in-table-view', 'zoom-to-table');
  } else {
    document.body.classList.add('in-table-view');
  }

  const input = document.getElementById('nameInput');
  if(input) input.focus();

  if(S.screen === 'dealReveal'){
    setupCardDrag();
  }
}

function setupCardDrag(){
  const container = appEl.querySelector('.hand-row.wide-hand');
  if(!container) return;
  const cards = Array.from(container.querySelectorAll('.hand-card'));
  cards.forEach(card => {
    card.style.touchAction = 'none';
    card.addEventListener('pointerdown', onCardPointerDown);
  });
}

function onCardPointerDown(e){
  if(e.button !== 0 && e.pointerType === 'mouse') return;
  const card = e.currentTarget;
  const initialIdx = parseInt(card.dataset.idx, 10);
  if(isNaN(initialIdx)) return;

  const rect = card.getBoundingClientRect();
  const startX = e.clientX, startY = e.clientY;
  let isDragging = false, ghost = null, currentTargetIdx = null;

  function onPointerMove(eMove){
    const dx = eMove.clientX - startX, dy = eMove.clientY - startY;
    if(!isDragging && Math.hypot(dx, dy) > 5){
      isDragging = true;
      ghost = card.cloneNode(true);
      ghost.classList.add('card-drag-ghost');
      ghost.style.cssText = `position:fixed; left:${rect.left}px; top:${rect.top}px; width:${rect.width}px; height:${rect.height}px; z-index:10000; pointer-events:none; transform:scale(1.08) rotate(3deg);`;
      document.body.appendChild(ghost);
      card.classList.add('dragging-source');
    }
    if(isDragging && ghost){
      ghost.style.transform = `translate3d(${dx}px, ${dy}px, 0) scale(1.08) rotate(3deg)`;
      const elem = document.elementFromPoint(eMove.clientX, eMove.clientY);
      const targetCard = elem ? elem.closest('.hand-card') : null;
      if(targetCard && targetCard !== card){
        currentTargetIdx = parseInt(targetCard.dataset.idx, 10);
      } else {
        currentTargetIdx = null;
      }
    }
  }

  function onPointerUp(){
    window.removeEventListener('pointermove', onPointerMove);
    window.removeEventListener('pointerup', onPointerUp);
    if(ghost && ghost.parentNode) ghost.parentNode.removeChild(ghost);
    card.classList.remove('dragging-source');
    if(isDragging && currentTargetIdx !== null && currentTargetIdx !== initialIdx){
      const hand = S.hands[S.currentDealer];
      if(hand && hand[initialIdx] !== undefined && hand[currentTargetIdx] !== undefined){
        [hand[initialIdx], hand[currentTargetIdx]] = [hand[currentTargetIdx], hand[initialIdx]];
        render();
      }
    }
  }

  window.addEventListener('pointermove', onPointerMove);
  window.addEventListener('pointerup', onPointerUp);
}

function addPlayer(){
  const input=document.getElementById('nameInput');
  if(!input) return;
  const val=input.value.trim();
  if(!val) return;
  if(S.players.some(p=>p.toLowerCase()===val.toLowerCase())){
    const h=document.getElementById('nameHint');
    if(h){ h.textContent='Ce pseudo existe déjà'; h.classList.add('err'); }
    return;
  }
  if(S.players.length<12) S.players.push(val);
  render();
}

function choosePack(idx){
  const pack=S.packs[idx];
  pack.taken=true;
  S.hands[S.currentDealer]=pack.cards;
  S.screen='dealReveal';
}

function pickSwap(idx){
  if(S.swapPick===null){ S.swapPick=idx; }
  else if(S.swapPick===idx){ S.swapPick=null; }
  else {
    const hand=S.hands[S.currentDealer];
    [hand[S.swapPick],hand[idx]]=[hand[idx],hand[S.swapPick]];
    S.swapPick=null;
  }
}

function validateHand(){
  S.swapPick=null;
  S.dealQueue.shift();
  if(S.dealQueue.length>0){ S.currentDealer=S.dealQueue[0]; S.screen='dealing'; }
  else { buildPyramid(); S.screen='game'; }
}

function guessCard(idx){
  const card=S.hands[S.bluffTarget][idx];
  const ok=card.rank===S.overlayCard.rank;
  S.bluffFlash={idx,ok};
  render();
  setTimeout(()=>{ S.bluffFlash=null; S.bluffAwaitingChoice=true; S.bluffResult={ok}; render(); },900);
}

appEl.addEventListener('input', e=>{
  if(e.target.id === 'pyramidSlider'){
    S.rows = parseInt(e.target.value, 10);
    render();
  }
});

appEl.addEventListener('click', e=>{
  const t=e.target.closest('[data-action]');
  if(!t || !t.dataset.action) return;
  const action=t.dataset.action;
  const idx = t.dataset.idx!==undefined ? parseInt(t.dataset.idx) : null;
  switch(action){
    case 'startGameZoom':
      document.body.classList.add('zoom-to-table');
      setTimeout(()=>{
        document.body.classList.remove('zoom-to-table');
        S.screen = 'setup';
        render();
      }, 1100);
      return;
    case 'addPlayer': addPlayer(); return;
    case 'removePlayer': S.players.splice(idx,1); break;
    case 'toStep2': if(S.players.length>=2) S.screen='pyramidSize'; return;
    case 'back': S.screen='setup'; break;
    case 'toDealing': S.screen='dealing'; S.packs=[]; break;
    case 'choosePack': choosePack(idx); break;
    case 'pickSwap': pickSwap(idx); break;
    case 'validateHand': validateHand(); break;
    case 'nextCard': nextCard(); break;
    case 'togglePyramidOverlay': S.showPyramidOverlay = !S.showPyramidOverlay; break;
    case 'startBluff': S.screen='bluffPick'; break;
    case 'pickBluffTarget': S.bluffTarget=t.dataset.name; S.screen='bluffSearch'; S.bluffAwaitingChoice=false; S.bluffFlash=null; S.bluffResult=null; break;
    case 'guessCard': guessCard(idx); return;
    case 'bluffNext': S.screen='game'; S.bluffTarget=null; S.bluffAwaitingChoice=false; S.bluffResult=null; break;
    case 'terminer': const keep=S.players; S=freshState(); S.players=keep; render(); return;
    case 'confirmReplay': S.hands={}; S.packs=[]; S.pyramidRows=[]; S.flatOrder=[]; S.revealPos=-1; S.overlayCard=null; S.screen='dealing'; break;
    default: return;
  }
  render();
});

appEl.addEventListener('keydown', e=>{ if(e.target.id==='nameInput' && e.key==='Enter') addPlayer(); });

render();
</script>
</body>
</html>
'''

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

with open("Pyradrink.html", "w", encoding="utf-8") as f:
    f.write(content)

print("SUCCESS")
