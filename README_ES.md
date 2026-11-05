# 🐔 CHICKEN WAR – versión móvil (Android / iOS)

> hecho por renato y su duro esfuerzo de la IA

## 1. Análisis del proyecto original
| Aspecto | Resultado |
|---|---|
| Tipo | Un solo archivo `CHICKEN_WAR.html` (~50 KB) |
| Motor gráfico | **Three.js r128** (WebGL), sin texturas externas: todo se genera por código |
| Lenguaje | JavaScript (ES2015+) + HTML/CSS |
| Audio | Web Audio API (sonidos sintetizados, sin archivos) |
| Multijugador | PeerJS (WebRTC P2P) – salas con código |
| Dependencias | three.min.js (CDN) y peerjs (CDN, carga bajo demanda) |
| Controles originales | Teclado + ratón + bloqueo de puntero |

Como es un juego web, la adaptación real es: **HTML5 móvil + empaquetado nativo con Capacitor** (WebView nativo
de Android/iOS), con Three.js y PeerJS **incluidos dentro de la app** para que funcione sin internet (salvo el modo online).

## 2. Qué se adaptó
- **Controles táctiles**: joystick analógico (empujar al borde = correr), arrastrar la pantalla para apuntar,
  botones FUEGO (también permite apuntar mientras se mantiene), SALTO, RECARGAR, E (recoger), arma anterior/siguiente,
  barra de armas y pausa.
- **Botones personalizables**: Configuración → *Editar botones táctiles* (o desde Pausa). Se arrastran, cambian de tamaño
  y de opacidad; se guarda el diseño.
- **Menús**: botones grandes, rejilla de 2 columnas, safe-area (notch), soporte vertical/horizontal, teclado sin zoom.
- **HUD compacto** reubicado para no tapar los controles.
- **Orientación**: horizontal (bloqueada en la APK; en navegador pide girar).
- **Rendimiento / batería**: límite de FPS (30 / 60 / sin límite), resolución dinámica ajustada al límite elegido,
  calidad gráfica automática según el equipo, menos partículas en calidad baja, GPU en modo normal (no "high-performance"),
  render a 30 FPS en menús, pausa automática al salir de la app, pantalla encendida solo mientras se juega.
- **Guardado**: perfil (nombre, gallina, mapa, duración, bots, sensibilidad, volumen, calidad, FPS, botones táctiles),
  estadísticas (partidas, victorias, bajas) y **partida en curso** (botón *Continuar partida*: tiempo, bajas, armas,
  munición, vida y posición). Guardado automático cada 5 s y al cerrar/minimizar.
- **Créditos** dentro del juego (menú principal y pantalla *Créditos*): "hecho por renato y su duro esfuerzo de la IA".
- **Se conserva** todo el contenido: 7 armas, 5 mapas, personalización, bots, power-ups, física, sonidos, animaciones
  y multijugador online. El teclado y ratón siguen funcionando en PC.

## 3. Obtener el APK (la forma más fácil, sin instalar nada)
1. Crea una cuenta gratis en https://github.com y un repositorio nuevo (privado o público).
2. Sube TODO el contenido de esta carpeta (incluida la carpeta oculta `.github`). Si el navegador no sube carpetas ocultas,
   crea el archivo a mano: *Add file → Create new file* → nombre `.github/workflows/build-android.yml` y pega su contenido.
3. Ve a la pestaña **Actions → Compilar APK de Android → Run workflow** (también se lanza solo al subir cambios).
4. A los ~5 minutos entra en la ejecución y descarga **ChickenWar-APK** (contiene `app-debug.apk`).
5. Pasa el APK al teléfono, ábrelo y permite "instalar apps de orígenes desconocidos".

El APK de depuración se instala y juega con normalidad. Para publicar en Google Play hay que firmar una versión *release*.

## 4. Compilar en tu PC (alternativa)
Requisitos: Node 18+, JDK 17, Android Studio (SDK 34).
```bash
npm install
npm run android:init     # copia three/peerjs, crea android/, aplica horizontal + icono + inmersivo
npm run android:apk      # genera android/app/build/outputs/apk/debug/app-debug.apk
```
Para abrir el proyecto en Android Studio: `npx cap open android`.

## 5. iOS
Apple solo permite compilar iOS en un Mac con Xcode (y una cuenta de Apple Developer para instalarlo en un iPhone real).
```bash
npm install
npm run ios:init
npm run ios:open        # abre Xcode: elige tu equipo de firma y pulsa ▶
```
## 6. Probar rápido sin compilar
`www/index.html` (o `ChickenWar_Movil.html`) funciona directamente en el navegador del teléfono si se sirve por
HTTPS/HTTP (por ejemplo, subiéndolo a GitHub Pages). Carga Three.js desde CDN si no encuentra `lib/three.min.js`.

## 7. Estado de las pruebas (sé honesto con esto)
- ✅ Comprobado en Chromium móvil emulado (844×390 y 390×844): menús, joystick, botones, apuntado, pausa, editor de botones,
  guardado/carga, continuar partida, rotación, créditos. Sintaxis JS verificada.
- ⚠️ El motor 3D se simuló en esa prueba (sin internet no se podía descargar Three.js), así que **FPS reales y render en
  dispositivos físicos aún no están medidos**. Prueba en tu teléfono y ajusta *Calidad* y *Límite de FPS* en Configuración.
- ⚠️ El APK y el proyecto iOS no se pudieron compilar en el entorno donde se generó este proyecto (sin Android SDK ni red);
  el flujo de la sección 3 los compila por ti en la nube.

## 8. Cambios v1.1 (cámara táctil e interfaz móvil)
- **Cámara**: los deslizamientos se aplican una vez por fotograma con suavizado y aceleración opcionales; la escala depende de la altura de la pantalla (se siente igual en cualquier móvil/tablet); zona muerta de 4 px al tocar; lectura de todos los puntos intermedios del dedo.
- **Configuración nueva**: sensibilidad táctil, sensibilidad vertical, suavizado (Directo/Bajo/Alto), aceleración (Ninguna/Suave/Fuerte), eje vertical invertido y joystick fijo/flotante. Se guardan en el perfil.
- **Joystick flotante** (por defecto): toca en cualquier punto de la mitad izquierda y el joystick aparece bajo tu dedo.
- **HUD**: respeta el notch/bordes en horizontal (antes los márgenes seguros no se aplicaban), marcador compacto (top 3 + tu posición) y barra de armas más grande.
- **Menús**: Configuración en 2 columnas en horizontal y botón VOLVER siempre visible.
- ⚠️ Cambios verificados solo con comprobación de sintaxis; ajusta la sensibilidad en tu teléfono.
