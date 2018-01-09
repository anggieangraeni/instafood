def bsains(request):
    berita = Bsains.objects.all()
    konten = {'all_berita':berita}
