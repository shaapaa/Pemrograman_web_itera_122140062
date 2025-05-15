from pyramid.view import view_config
from pyramid.response import Response

@view_config(route_name='home', renderer='json')
def home_view(request):
    # Opsi 1: Kirim pesan singkat
    return {
        "message": "Selamat datang di API Matakuliah. "
                   "Gunakan endpoint /api/matakuliah untuk operasi CRUD."
    }

    # Opsi 2: Redirect otomatis ke /api/matakuliah
    # from pyramid.httpexceptions import HTTPFound
    # raise HTTPFound(location=request.route_url('matakuliah_list'))
