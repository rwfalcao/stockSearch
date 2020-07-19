def main_context_processor(request):
    ctx = dict(
        super_template='base.html'
    )

    return ctx