#!/usr/bin/env bash
# Ajustes para el proyecto Android generado por "npx cap add android":
# horizontal fijo, pantalla inmersiva, pantalla siempre encendida durante el juego e icono propio.
set -e
cd "$(dirname "$0")/.."
A=android/app/src/main
MAN=$A/AndroidManifest.xml
JAVADIR=$A/java/com/renato/chickenwar
test -f "$MAN" || { echo "No existe $MAN. Ejecuta antes: npx cap add android"; exit 1; }

# 1) Orientación horizontal (ambos sentidos)
grep -q 'screenOrientation' "$MAN" || sed -i 's/<activity /<activity android:screenOrientation="sensorLandscape" /' "$MAN"

# 2) Actividad principal: modo inmersivo + pantalla encendida
cat > "$JAVADIR/MainActivity.java" <<'JAVA'
package com.renato.chickenwar;

import android.os.Bundle;
import android.view.WindowManager;
import androidx.core.view.WindowCompat;
import androidx.core.view.WindowInsetsCompat;
import androidx.core.view.WindowInsetsControllerCompat;
import com.getcapacitor.BridgeActivity;

public class MainActivity extends BridgeActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        getWindow().addFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON);
        hideSystemBars();
    }

    @Override
    public void onWindowFocusChanged(boolean hasFocus) {
        super.onWindowFocusChanged(hasFocus);
        if (hasFocus) hideSystemBars();
    }

    private void hideSystemBars() {
        WindowInsetsControllerCompat c = WindowCompat.getInsetsController(getWindow(), getWindow().getDecorView());
        c.hide(WindowInsetsCompat.Type.systemBars());
        c.setSystemBarsBehavior(WindowInsetsControllerCompat.BEHAVIOR_SHOW_TRANSIENT_BARS_BY_SWIPE);
    }
}
JAVA

# 3) Icono
python3 scripts/make_icons.py $A/res || echo "(aviso) no se generaron iconos; se usará el icono por defecto"
echo "Parche Android aplicado."
