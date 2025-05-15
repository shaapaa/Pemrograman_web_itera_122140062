from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound, HTTPBadRequest
from matkul_app.models.meta import Base
from matkul_app.models.matakuliah import Matakuliah

from sqlalchemy.orm import Session

# GET all
@view_config(route_name='matakuliah_list', renderer='json')
def list_matkul(request):
    session = Session(bind=Base.metadata.bind)
    return [m.to_dict() for m in session.query(Matakuliah).all()]

# POST create
@view_config(route_name='matakuliah_add', renderer='json')
def add_matkul(request):
    data = request.json_body
    required = {'kode_mk', 'nama_mk', 'sks', 'semester'}
    if not required.issubset(data):
        raise HTTPBadRequest('Field tidak lengkap')

    session = Session(bind=Base.metadata.bind)
    m = Matakuliah(
        kode_mk=data['kode_mk'], nama_mk=data['nama_mk'],
        sks=data['sks'], semester=data['semester']
    )
    session.add(m)
    session.flush()
    return m.to_dict()

# GET one
@view_config(route_name='matakuliah_detail', renderer='json')
def get_matkul(request):
    id = request.matchdict['id']
    session = Session(bind=Base.metadata.bind)
    m = session.query(Matakuliah).get(int(id))
    if not m:
        raise HTTPNotFound()
    return m.to_dict()

# PUT update
@view_config(route_name='matakuliah_update', renderer='json')
def update_matkul(request):
    id = request.matchdict['id']
    data = request.json_body
    session = Session(bind=Base.metadata.bind)
    m = session.query(Matakuliah).get(int(id))
    if not m:
        raise HTTPNotFound()
    for field in ('kode_mk','nama_mk','sks','semester'):
        if field in data:
            setattr(m, field, data[field])
    session.flush()
    return m.to_dict()

# DELETE
@view_config(route_name='matakuliah_delete', renderer='json')
def delete_matkul(request):
    id = request.matchdict['id']
    session = Session(bind=Base.metadata.bind)
    m = session.query(Matakuliah).get(int(id))
    if not m:
        raise HTTPNotFound()
    session.delete(m)
    return {'success': True}