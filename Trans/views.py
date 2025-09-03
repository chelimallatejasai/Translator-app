from django.shortcuts import render
from translate import Translator

def home(request):
    if request.method == "POST":
        text = request.POST["translate"]
        language = request.POST["language"]
        translator = Translator(to_lang=language)
        try:
            translation = translator.translate(text)
        except (RuntimeError, StopIteration, Exception):
            translation = "Sorry, translation failed or is not available."
        return render(request, "Trans/output.html", {"translated_text": translation})
    return render(request, "Trans/index.html")
