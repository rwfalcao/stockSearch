from django.utils.translation import activate

def main_context_processor(request):
    ctx = dict(
        super_template='base.html'
    )

    language_code = request.GET.get('language') if request.GET.get('language') else 'en'
    if language_code:
        activate(language_code)
        
    return ctx