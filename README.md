# Gemini-Zsh: Consultas a Gemini AI desde tu Terminal Zsh

Este proyecto te permite realizar consultas a la API de Gemini de Google directamente desde tu terminal Zsh. Cualquier comando que no sea reconocido por Zsh será interpretado como un prompt para Gemini.

**¡Atención! Riesgo de seguridad:** El script de Zsh proporcionado en el ejemplo original contiene un placeholder para una API Key (`"TU_CLAVE_API"`) dentro de la función `command_not_found_handler`. **NUNCA subas API Keys reales directamente a repositorios públicos.** Este README y las instrucciones asumen que gestionarás tu API Key de forma segura como una variable de entorno, que es la práctica recomendada para el uso real.

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

## Instalación

1.  **Clona este repositorio o descarga los archivos:**
    Si es un repositorio:
    ```bash
    git clone [https://github.com/TU_USUARIO/TU_REPOSITORIO.git](https://github.com/TU_USUARIO/TU_REPOSITORIO.git)
    cd TU_REPOSITORIO
    ```
    Si solo tienes los archivos, créalos manualmente. Necesitarás:
    * Un archivo para el script de Zsh (ej. `gemini_zsh_integration.zsh`)
    * Un archivo para el script de Python (ej. `gemini_query.py`)

2.  **Coloca el script de Python en la ubicación deseada:**
    El script de Zsh espera encontrar `gemini_query.py` en `$HOME/.config/zsh/gemini_query.py` por defecto.
    ```bash
    mkdir -p $HOME/.config/zsh
    cp gemini_query.py $HOME/.config/zsh/gemini_query.py
    ```
    Si usas una ruta diferente, asegúrate de actualizar la variable `python_script_path` en el script de Zsh.

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
    **NO hardcodees tu API Key real directamente en los scripts que compartes o versionas.**
    La forma más segura y recomendada es establecerla como una variable de entorno en tu archivo de configuración de Zsh (`~/.zshrc`):

    ```bash
    echo 'export GEMINI_API_KEY="TU_CLAVE_API_REAL_AQUI"' >> ~/.zshrc
    ```
    **Reemplaza `"TU_CLAVE_API_REAL_AQUI"` con tu API Key real.**
    Después de añadirla, recarga la configuración de tu shell:
    ```bash
    source ~/.zshrc
    ```
    O abre una nueva terminal.

    **Nota sobre el código Zsh proporcionado:**
    Tu script Zsh actual define la `GEMINI_API_KEY` con un placeholder *dentro* de la función `command_not_found_handler`:
    ```zsh
    command_not_found_handler() {
        export GEMINI_API_KEY="TU_CLAVE_API" # ESTA LÍNEA DENTRO DE LA FUNCIÓN
        local user_input="$*"
    # ...
    }
    ```
    Si dejas esta línea `export GEMINI_API_KEY="TU_CLAVE_API"` en la función, **esta anulará cualquier `GEMINI_API_KEY` que hayas configurado en tu `.zshrc`** cuando la función se ejecute. Esto significa que el script Python intentará usar `"TU_CLAVE_API"` literalmente, lo cual fallará.

    Para una configuración segura y funcional donde usas tu clave real, **DEBES eliminar o comentar esta línea que asigna `GEMINI_API_KEY` dentro de la función del script de Zsh.** Configura tu API Key real *únicamente* a través de `~/.zshrc` como se recomienda arriba. El script Python (`gemini_query.py`) está diseñado para leer la variable de entorno `GEMINI_API_KEY` que establezcas en tu `.zshrc`.

    **Recomendación:** Modifica tu función `command_not_found_handler` en el script Zsh así:
    ```diff
    command_not_found_handler() {
    -   export GEMINI_API_KEY="TU_CLAVE_API" # ¡ELIMINAR O COMENTAR ESTA LÍNEA!
        local user_input="$*"
    ```
    De esta manera, la función usará la `GEMINI_API_KEY` que hayas exportado desde tu `.zshrc`.

2.  **Integra la función `command_not_found_handler` en tu Zsh:**
    Copia el contenido del script de Zsh (el que contiene la función `command_not_found_handler`, **ya modificado según la recomendación anterior para no establecer la API key dentro de la función**) y pégalo al final de tu archivo `~/.zshrc`.

    Alternativamente, si guardaste el código Zsh en un archivo (por ejemplo, `~/.config/zsh/gemini_integration.zsh`), puedes añadir la siguiente línea a tu `~/.zshrc` para cargarlo:
    ```bash
    echo 'source $HOME/.config/zsh/gemini_integration.zsh' >> ~/.zshrc
    ```

3.  **Recarga la configuración de tu Zsh:**
    ```bash
    source ~/.zshrc
    ```
    O simplemente abre una nueva ventana de terminal.

## Uso

Una vez configurado (y asegurándote de que la `GEMINI_API_KEY` se exporta correctamente desde tu `.zshrc` y no desde dentro de la función), cualquier comando que escribas en la terminal Zsh y que no sea un comando conocido, un alias o una función, será enviado a Gemini AI.

**Ejemplo:**

Abre tu terminal y escribe:
```zsh
¿Cuál es la comida típica de Asturias?

Verás primero un mensaje:

Analizando prompt 🤔

Y luego, la respuesta de Gemini (renderizada por glow si está instalado):

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

Personalización

    Modelo de Gemini: Puedes cambiar el modelo de Gemini utilizado editando la variable model_name en el script gemini_query.py.
    Python

    # En gemini_query.py
    model_name = "gemini-1.5-flash-latest" # Cambia a otro modelo compatible si lo deseas

    Consulta la documentación de Gemini para ver los modelos disponibles.

    Ruta del script de Python: Si colocaste gemini_query.py en una ubicación diferente a la predeterminada ($HOME/.config/zsh/gemini_query.py), actualiza la variable python_script_path en tu función command_not_found_handler dentro de ~/.zshrc (o el archivo donde la hayas guardado).

Solución de Problemas

    "Error: GEMINI_API_KEY no configurada.":
        Asegúrate de haber exportado la variable GEMINI_API_KEY con tu clave real en tu ~/.zshrc.
        Verifica que has recargado la configuración (source ~/.zshrc) o abierto una nueva terminal.
        Muy importante: Asegúrate de haber eliminado o comentado la línea export GEMINI_API_KEY="TU_CLAVE_API" de dentro de la función command_not_found_handler en tu script Zsh, ya que esta anularía la clave de tu .zshrc.
    "Error: Script de Python no encontrado o no ejecutable...": Verifica que la ruta en python_script_path (en el script Zsh) sea correcta y que el script gemini_query.py tenga permisos de ejecución (chmod +x ruta/al/script.py).
    "Error: Comando 'python3' no encontrado...": Asegúrate de que Python 3 esté instalado y accesible en tu PATH.
    Errores del script de Python: Los errores específicos del script Python (ej. problemas con la API, modelo incorrecto) se imprimirán en stderr y deberían ser visibles en la terminal. Si la API Key es incorrecta (por ejemplo, si se usa el placeholder "TU_CLAVE_API"), el script Python fallará.

Importante: Costos y Límites de la API

Ten en cuenta que el uso de la API de Gemini puede incurrir en costos dependiendo de tu volumen de uso y el modelo seleccionado. Revisa los términos de precios de Google Cloud para la API de Gemini.

Dado que cualquier comando no reconocido se envía a la API, podrías generar muchas solicitudes accidentalmente. ¡Usa con precaución!
Contribuir

Si tienes ideas para mejorar este proyecto, no dudes en abrir un Issue o un Pull Request.
