import logging
from sqlalchemy.orm import sessionmaker
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound, HTTPBadRequest
from .models.meta import Base
from .models.matakuliah import Matakuliah
from sqlalchemy.orm import Session

log = logging.getLogger(__name__)

# Configure SQLAlchemy session factory
SessionFactory = sessionmaker(bind=Base.metadata.bind)

def get_session():
    engine = Base.metadata.bind
    return Session(bind=engine)

@view_config(route_name='home', renderer='json', request_method='GET')
def home(request):
    return {'message': 'API Matakuliah berjalan'}

@view_config(route_name='matakuliah_list', renderer='json', request_method='GET')
def list_matakuliah(request):
    session = get_session()
    try:
        results = session.query(Matakuliah).all()
        return [m.to_dict() for m in results]
    finally:
        session.close()

@view_config(route_name='get_matakuliah', renderer='json', request_method='GET')
def get_matakuliah(request):
    mid = request.matchdict.get('id')
    if not mid or not mid.isdigit():
        raise HTTPBadRequest(json_body={'error': 'ID tidak valid'})
    session = get_session()
    try:
        m = session.query(Matakuliah).get(int(mid))
        if not m:
            raise HTTPNotFound(json_body={'error': 'Matakuliah tidak ditemukan'})
        return m.to_dict()
    finally:
        session.close()

@view_config(route_name='add_matakuliah', renderer='json', request_method='POST')
def add_matakuliah(request):
    try:
        data = request.json_body
    except Exception:
        raise HTTPBadRequest(json_body={'error': 'JSON body invalid'})
    for field in ('kode_mk', 'nama_mk', 'sks', 'semester'):
        if field not in data:
            raise HTTPBadRequest(json_body={'error': f'Field {field} wajib diisi'})
    session = get_session()
    try:
        m = Matakuliah(
            kode_mk=data['kode_mk'],
            nama_mk=data['nama_mk'],
            sks=int(data['sks']),
            semester=int(data['semester']),
        )
        session.add(m)
        session.commit()
        return {'success': True, 'matakuliah': m.to_dict()}
    finally:
        session.close()

@view_config(route_name='update_matakuliah', renderer='json', request_method='PUT')
def update_matakuliah(request):
    mid = request.matchdict.get('id')
    if not mid or not mid.isdigit():
        raise HTTPBadRequest(json_body={'error': 'ID tidak valid'})
    session = get_session()
    try:
        m = session.query(Matakuliah).get(int(mid))
        if not m:
            raise HTTPNotFound(json_body={'error': 'Matakuliah tidak ditemukan'})
        data = request.json_body or {}
        if 'kode_mk' in data:
            m.kode_mk = data['kode_mk']
        if 'nama_mk' in data:
            m.nama_mk = data['nama_mk']
        if 'sks' in data:
            m.sks = int(data['sks'])
        if 'semester' in data:
            m.semester = int(data['semester'])
        session.commit()
        return {'success': True, 'matakuliah': m.to_dict()}
    finally:
        session.close()

@view_config(route_name='delete_matakuliah', renderer='json', request_method='DELETE')
def delete_matakuliah(request):
    mid = request.matchdict.get('id')
    if not mid or not mid.isdigit():
        raise HTTPBadRequest(json_body={'error': 'ID tidak valid'})
    session = get_session()
    try:
        m = session.query(Matakuliah).get(int(mid))
        if not m:
            raise HTTPNotFound(json_body={'error': 'Matakuliah tidak ditemukan'})
        session.delete(m)
        session.commit()
        return {'success': True}
    finally:
        session.close()

@view_config(route_name='matkul_html', renderer='templates/matakuliah_list.jinja2', request_method='GET')
def matkul_html_view(request):
    session = get_session()
    try:
        daftar_matkul = session.query(Matakuliah).all()
        return {'daftar_matkul': daftar_matkul}
    finally:
        session.close()
