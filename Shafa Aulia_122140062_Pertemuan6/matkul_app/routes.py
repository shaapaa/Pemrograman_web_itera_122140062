def includeme(config):
    config.add_static_view('static', 'matkul_app:static', cache_max_age=3600)

    # JSON-API CRUD endpoints
    config.add_route('home', '/',                      request_method='GET')
    config.add_route('matakuliah_list',   '/api/matakuliah',      request_method='GET')
    config.add_route('add_matakuliah',    '/api/matakuliah',      request_method='POST')
    config.add_route('get_matakuliah',    '/api/matakuliah/{id}', request_method='GET')
    config.add_route('update_matakuliah', '/api/matakuliah/{id}', request_method='PUT')
    config.add_route('delete_matakuliah', '/api/matakuliah/{id}', request_method='DELETE')
    config.add_route('matakuliah_tambah', '/matakuliah/tambah')
    config.add_route('matakuliah_hapus', '/matakuliah/hapus/{id}')

    # HTML page
    config.add_route('matkul_html', '/matakuliah', request_method='GET')
