#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import google.generativeai as genai

def main():
    # 1. Leer la API Key de la variable de entorno
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error en script Python: La variable de entorno GEMINI_API_KEY no está configurada.", file=sys.stderr)
        sys.exit(1)

    # 2. Configurar el SDK de Gemini
    try:
        genai.configure(api_key=api_key)
    except Exception as e:
        print(f"Error en script Python configurando el SDK de Gemini: {e}", file=sys.stderr)
        sys.exit(1)

    # 3. Elegir el nombre del modelo
    #    Usa un modelo de la lista que obtuviste que soporte 'generateContent'.
    #    'gemini-1.5-flash-latest' es una buena opción general.
    model_name = "gemini-2.5-flash-preview-04-17"
    # Otros buenos candidatos de tu lista: "gemini-1.5-pro-latest", "gemini-2.5-flash-preview-04-17"

    # 4. Obtener el prompt de los argumentos de la línea de comandos
    if len(sys.argv) < 2:
        print("Error en script Python: No se proporcionó ningún prompt.", file=sys.stderr)
        print("Uso: gemini_query.py <tu pregunta para Gemini>", file=sys.stderr)
        sys.exit(1)
    
    user_prompt = " ".join(sys.argv[1:])

    # 5. Inicializar el modelo generativo
    try:
        model = genai.GenerativeModel(model_name)
    except Exception as e:
        print(f"Error en script Python inicializando el modelo '{model_name}': {e}", file=sys.stderr)
        sys.exit(1)

    # 6. Generar contenido
    try:
        response = model.generate_content(user_prompt)
        
        # Acceder al texto de la respuesta.
        # El SDK puede tener diferentes formas de acceder al texto según la respuesta.
        # response.text es un atajo común.
        # También es bueno verificar si hay 'parts' en la respuesta.
        
        if hasattr(response, 'text') and response.text:
            print(response.text)
        elif response.parts:
            # Concatenar texto de todas las partes si response.text no está disponible
            # o si prefieres ser explícito.
            full_text = "".join(part.text for part in response.parts if hasattr(part, 'text'))
            if full_text:
                print(full_text)
            else:
                # Si no hay texto, verificar si la solicitud fue bloqueada
                if hasattr(response, 'prompt_feedback') and response.prompt_feedback.block_reason:
                    block_reason = response.prompt_feedback.block_reason
                    block_message = getattr(response.prompt_feedback, 'block_reason_message', 'Sin mensaje adicional.')
                    print(f"Error en script Python: La solicitud fue bloqueada. Razón: {block_reason}. Mensaje: {block_message}", file=sys.stderr)
                else:
                    print("Error en script Python: Respuesta de Gemini vacía o sin contenido textual extraíble.", file=sys.stderr)
                sys.exit(1) # Salir con error si no hay texto útil
        else:
             # Si no hay ni .text ni .parts, puede ser un error o un bloqueo no capturado arriba
            if hasattr(response, 'prompt_feedback') and response.prompt_feedback.block_reason:
                block_reason = response.prompt_feedback.block_reason
                block_message = getattr(response.prompt_feedback, 'block_reason_message', 'Sin mensaje adicional.')
                print(f"Error en script Python: La solicitud fue bloqueada (sin partes de texto). Razón: {block_reason}. Mensaje: {block_message}", file=sys.stderr)
            else:
                print("Error en script Python: Respuesta de Gemini inesperada o vacía.", file=sys.stderr)
                # Opcional: imprimir toda la respuesta para depuración
                # print(f"Respuesta completa: {response}", file=sys.stderr)
            sys.exit(1)

    except Exception as e:
        print(f"Error en script Python generando contenido con Gemini: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
