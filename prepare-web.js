// Copia Three.js y PeerJS desde node_modules a www/lib para que el juego funcione SIN internet
const fs = require('fs'), path = require('path');
const root = path.join(__dirname, '..');
const lib = path.join(root, 'www', 'lib');
fs.mkdirSync(lib, { recursive: true });
const files = [
  ['node_modules/three/build/three.min.js', 'three.min.js'],
  ['node_modules/peerjs/dist/peerjs.min.js', 'peerjs.min.js'],
];
for (const [src, dst] of files) {
  const s = path.join(root, src);
  if (!fs.existsSync(s)) { console.error('FALTA ' + src + ' -> ejecuta "npm install" primero'); process.exit(1); }
  fs.copyFileSync(s, path.join(lib, dst));
  console.log('copiado', dst, fs.statSync(path.join(lib, dst)).size, 'bytes');
}
