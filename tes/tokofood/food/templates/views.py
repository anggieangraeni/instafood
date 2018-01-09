def bali(request):
    b = Bali.objects.all()
    konten = {'template':b}
