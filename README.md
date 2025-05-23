# Gemini-Zsh: Consultas a Gemini AI desde tu Terminal Zsh

Este proyecto te permite realizar consultas a la API de Gemini de Google directamente desde tu terminal Zsh. Cualquier comando que no sea reconocido por Zsh será interpretado como un prompt para Gemini.

v2.0: Pequeña integración para agregar relajante música a tu terminal. Va dentro del script, tan solo tendrás que escribrir "music" en tu terminal y disfrutar. 

**¡Atención! Gestión de API Keys:** Recuerda que tu API Key de Gemini es información sensible. **NUNCA subas API Keys reales directamente a repositorios públicos.** Este README y las instrucciones asumen que gestionarás tu API Key de forma segura como una variable de entorno, que es la práctica recomendada.

## Características

* Integración fluida con Zsh usando `command_not_found_handler`.
* Envía comandos no encontrados como prompts a la API de Gemini.
* Muestra las respuestas de Gemini directamente en la terminal.
* Utiliza `glow` para renderizar la respuesta en Markdown (si está instalado).
* Verificaciones básicas de configuración y errores.

## Prerrequisitos

Antes de empezar, asegúrate de tener instalado lo siguiente:

1.  **Zsh:** Como intérprete de comandos.
2.  **Python 3:** El script de consulta a Gemini está escrito en Python.
    * Puedes verificarlo con `python3 --version`.
3.  **Pip:** El gestor de paquetes de Python, para instalar librerías.
    * Suele venir con Python 3. Puedes verificarlo con `pip3 --version`.
4.  **Librería `google-generativeai` para Python:**
    * Se instalará en los pasos siguientes.
5.  **`glow` (Opcional, pero recomendado para la visualización):** Para renderizar la salida Markdown de Gemini.
    * En Debian/Ubuntu: `sudo apt install glow`
    * En macOS (con Homebrew): `brew install glow`
    * Otras distribuciones: Consulta la [documentación de glow](https://github.com/charmbracelet/glow).
6.  **Una API Key de Gemini:**
    * Obtén tu API Key desde [Google AI Studio](https://aistudio.google.com/app/apikey).
  
7.  **En caso de querer usar integración para música lofi:**
     * cli-visualizer (yay -S cli-visualizer)
     * mpv (sudo pacman -S mpv)
     * yt-dlp (sudo pacman -S yt-dlp)

## Instalación

1.  **Clona este repositorio o descarga los archivos:**:
    ```bash
    git clone https://github.com/J27REPO/integracion-gemini-terminal.git
    cd integracion-gemini-terminal
    ```
    Si solo tienes los archivos (`gemini_query.py` y el script con `command_not_found_handler`), asegúrate de tenerlos en tu máquina local. Necesitarás:
    * El script de Zsh que contiene `command_not_found_handler` (ej. podrías guardarlo como `~/.config/zsh/gemini_zsh_integration.zsh`).
    * El script de Python `gemini_query.py`.

2.  **Coloca el script de Python en la ubicación deseada:**
    El script de Zsh espera encontrar `gemini_query.py` en `$HOME/.config/zsh/gemini_query.py` por defecto.
    ```bash
    mkdir -p $HOME/.config/zsh
    cp gemini_query.py $HOME/.config/zsh/gemini_query.py
    ```
    Si usas una ruta diferente para `gemini_query.py`, asegúrate de actualizar la variable `python_script_path` en el script de Zsh.

3.  **Haz ejecutable el script de Python:**
    ```bash
    chmod +x $HOME/.config/zsh/gemini_query.py
    ```

4.  **Instala las dependencias de Python:**
    ```bash
    pip3 install google-generativeai
    ```
    Es recomendable usar un entorno virtual de Python para gestionar las dependencias del proyecto, pero para un script simple como este, la instalación global también funciona.

## Configuración

1.  **Configura tu API Key de Gemini (¡IMPORTANTE Y SEGURO!):**
    La forma más segura y recomendada es establecer tu `GEMINI_API_KEY` como una variable de entorno en tu archivo de configuración de Zsh (`~/.zshrc`):

    ```bash
    echo 'export GEMINI_API_KEY="TU_CLAVE_API_REAL_AQUI"' >> ~/.zshrc
    ```
    **Reemplaza `"TU_CLAVE_API_REAL_AQUI"` con tu API Key real.**
    Después de añadirla, recarga la configuración de tu shell:
    ```bash
    source ~/.zshrc
    ```
    O abre una nueva terminal. El script Zsh (`command_not_found_handler`) ya está preparado para usar esta variable de entorno.

2.  **Integra la función `command_not_found_handler` en tu Zsh:**
    Copia el contenido de tu script Zsh (el que contiene la función `command_not_found_handler`) y pégalo al final de tu archivo `~/.zshrc`.

    Alternativamente, si guardaste el código Zsh en un archivo separado (por ejemplo, `~/.config/zsh/gemini_zsh_integration.zsh`), puedes añadir la siguiente línea a tu `~/.zshrc` para cargarlo:
    ```bash
    echo 'source $HOME/.config/zsh/gemini_zsh_integration.zsh' >> ~/.zshrc
    ```

3.  **Recarga la configuración de tu Zsh:**
    ```bash
    source ~/.zshrc
    ```
    O simplemente abre una nueva ventana de terminal.

## Uso

Una vez configurado (asegurándote de que la `GEMINI_API_KEY` se exporta correctamente desde tu `.zshrc`), cualquier comando que escribas en la terminal Zsh y que no sea un comando conocido, un alias o una función, será enviado a Gemini AI.

**Ejemplo:**

Abre tu terminal y escribe:
```zsh
¿Cuál es la comida típica de Asturias?
```
Verás primero un mensaje:
```zsh
Analizando prompt 🤔
```

Y luego, la respuesta de Gemini (renderizada por glow si está instalado):
```zsh
*****************************************
La comida típica de Asturias es rica y variada, destacando por sus productos de mar y montaña. Algunos platos emblemáticos son:

* **Fabada Asturiana:** El plato más internacional, un potente guiso de fabes (alubias blancas grandes) con compango (morcilla, chorizo, lacón, tocino).
* **Cachopo:** Dos grandes filetes de ternera empanados, rellenos de jamón serrano y queso.
* **Pote Asturiano:** Un guiso contundente con berzas, patatas, fabes y productos del cerdo.
* **Pescados y Mariscos del Cantábrico:** Merluza a la sidra, pixín (rape), oricios (erizos de mar), centollos, nécoras, etc.
* **Quesos Asturianos:** Existe una gran variedad, más de 40 tipos artesanos. Algunos famosos son el Cabrales, Gamonéu, Afuega'l Pitu, y La Peral.
* **Sidra Natural:** La bebida asturiana por excelencia, escanciada para oxigenarla y potenciar su sabor.
* **Postres:** Arroz con leche (requemado), frixuelos (parecidos a los crepes), casadielles (empanadillas dulces rellenas de nuez).
*****************************************
```
Personalización

    Modelo de Gemini: Puedes cambiar el modelo de Gemini utilizado editando la variable model_name en el script gemini_query.py. Actualmente, tu script usa "gemini-2.5-flash-preview-04-17".
    Python

    # En gemini_query.py
    model_name = "gemini-2.5-flash-preview-04-17" # Cambia a otro modelo compatible si lo deseas

    Consulta la documentación de Gemini para ver los modelos disponibles.

    Ruta del script de Python: Si colocaste gemini_query.py en una ubicación diferente a la predeterminada ($HOME/.config/zsh/gemini_query.py), actualiza la variable python_script_path en tu función command_not_found_handler (en tu .zshrc o en el archivo gemini_zsh_integration.zsh).

Solución de Problemas

    "Error: GEMINI_API_KEY no configurada.":
        Asegúrate de haber exportado la variable GEMINI_API_KEY con tu clave real en tu ~/.zshrc.
        Verifica que has recargado la configuración (source ~/.zshrc) o abierto una nueva terminal.
    "Error: Script de Python no encontrado o no ejecutable...": Verifica que la ruta en python_script_path (en el script Zsh) sea correcta y que el script gemini_query.py tenga permisos de ejecución (chmod +x ruta/al/script.py).
    "Error: Comando 'python3' no encontrado...": Asegúrate de que Python 3 esté instalado y accesible en tu PATH.
    Errores del script de Python: Los errores específicos del script Python (ej. problemas con la API, modelo incorrecto, API key inválida) se imprimirán en stderr y deberían ser visibles en la terminal.

Importante: Costos y Límites de la API

Ten en cuenta que el uso de la API de Gemini puede incurrir en costos dependiendo de tu volumen de uso y el modelo seleccionado. Revisa los términos de precios de Google Cloud para la API de Gemini.
Por defecto, se seleccinó el modelo flash 2.5; obtendrás 500 prompts gratuitos al día. Para un uso normal será más que suficiente
Dado que cualquier comando no reconocido se envía a la API, podrías generar muchas solicitudes accidentalmente. ¡Usa con precaución!
Contribuir

Si tienes ideas para mejorar este proyecto, no dudes en abrir un Issue o un Pull Request.
